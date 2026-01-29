"""Character Atlas Report Generator.

Generates comprehensive character analysis with Want/Need/Lie/Truth
structure, arc classifications, and relationship mapping.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel, Field

from narratological.generators.base import (
    BaseReportGenerator,
    GeneratorConfig,
    GeneratorError,
    ReportType,
)
from narratological.generators.prompts import (
    CHARACTER_ATLAS_SYSTEM_PROMPT,
    build_character_atlas_prompt,
)
from narratological.generators.utils import (
    calculate_screen_time,
    find_antagonist,
    find_protagonist,
)
from narratological.models.analysis import ArcClassification
from narratological.models.report import (
    CharacterAtlasEntry,
    CharacterAtlasReport,
    CharacterRelationship,
)

if TYPE_CHECKING:
    from narratological.llm.providers import LLMProvider
    from narratological.models.analysis import Script


class LLMCharacterEntry(BaseModel):
    """Intermediate model for LLM character response."""

    name: str
    role: str
    screen_time: float = 0.0
    first_appearance: int = 1
    want: str | None = None
    need: str | None = None
    lie: str | None = None
    truth: str | None = None
    arc_type: str = "flat"
    arc_description: str = ""
    key_scenes: list[int] = Field(default_factory=list)


class LLMRelationship(BaseModel):
    """Intermediate model for LLM relationship response."""

    character_a: str
    character_b: str
    relationship_type: str
    description: str
    evolution: str | None = None


class LLMCharacterAtlasResponse(BaseModel):
    """LLM response model for character atlas generation."""

    total_characters: int
    principal_count: int
    entries: list[LLMCharacterEntry]
    protagonist: str | None = None
    antagonist: str | None = None
    ensemble_balance: str | None = None
    missing_archetypes: list[str] = Field(default_factory=list)
    relationships: list[LLMRelationship] = Field(default_factory=list)


class CharacterAtlasReportGenerator(BaseReportGenerator[CharacterAtlasReport]):
    """Generator for Character Atlas reports.

    Analyzes characters:
    - Want vs Need (conscious goal vs unconscious need)
    - Lie vs Truth (false belief vs lesson learned)
    - Arc classification (positive, negative, flat, corrupted, redeemed)
    - Screen time and key scenes
    - Relationship mapping

    Can use existing character annotations or LLM analysis.
    """

    report_type = ReportType.CHARACTER_ATLAS

    def __init__(
        self,
        provider: LLMProvider | None = None,
        config: GeneratorConfig | None = None,
    ):
        """Initialize the character atlas generator.

        Args:
            provider: LLM provider for analysis.
            config: Generator configuration.
        """
        super().__init__(provider, config)

    def generate(self, script: Script, **kwargs) -> CharacterAtlasReport:
        """Generate a character atlas report.

        Args:
            script: The script to analyze.
            **kwargs: Additional parameters (unused currently).

        Returns:
            Complete CharacterAtlasReport with character entries.

        Raises:
            GeneratorError: If generation fails.
        """
        can_gen, errors = self.can_generate(script)
        if not can_gen:
            raise GeneratorError(
                f"Cannot generate character atlas: {'; '.join(errors)}",
                report_type=self.report_type,
            )

        # Check if we can use existing character annotations
        if self._has_character_annotations(script):
            return self._generate_from_annotations(script)
        elif self.provider is not None:
            return self._generate_with_llm(script)
        else:
            # Generate minimal report from character list
            return self._generate_minimal(script)

    def _requires_llm(self) -> bool:
        """Character atlas can work without LLM if annotated."""
        return False

    def _validate_prerequisites(self, script: Script) -> list[str]:
        """Validate script has character data."""
        errors = super()._validate_prerequisites(script)

        if not script.characters:
            errors.append("Script must have characters for character atlas")

        return errors

    def _has_character_annotations(self, script: Script) -> bool:
        """Check if characters have Want/Need annotations."""
        if not script.characters:
            return False

        # Need at least some Want/Need info
        annotated = sum(
            1 for c in script.characters
            if c.want is not None or c.need is not None
        )
        return annotated >= len(script.characters) * 0.3

    def _generate_from_annotations(self, script: Script) -> CharacterAtlasReport:
        """Generate report from existing character annotations."""
        entries = []

        for char in script.characters:
            # Calculate screen time if scenes available
            screen_time = 0.0
            if script.scenes:
                screen_time = calculate_screen_time(char.name, script.scenes)

            # Skip minor characters if configured
            if not self.config.include_minor_characters:
                if screen_time < self.config.screen_time_threshold:
                    continue

            entry = CharacterAtlasEntry(
                name=char.name,
                role=char.role,
                screen_time=screen_time,
                first_appearance=char.first_appearance or 1,
                want=char.want,
                need=char.need,
                lie=char.lie,
                truth=char.truth,
                arc_type=char.arc_classification or ArcClassification.FLAT,
                arc_description=char.arc_summary or "",
                key_scenes=self._find_key_scenes_for_character(script, char.name),
                relationships=self._extract_relationships(char),
            )
            entries.append(entry)

        return self._build_report(script, entries)

    def _generate_minimal(self, script: Script) -> CharacterAtlasReport:
        """Generate minimal report from character list."""
        entries = []

        for char in script.characters:
            screen_time = 0.0
            if script.scenes:
                screen_time = calculate_screen_time(char.name, script.scenes)

            if not self.config.include_minor_characters:
                if screen_time < self.config.screen_time_threshold:
                    continue

            entry = CharacterAtlasEntry(
                name=char.name,
                role=char.role,
                screen_time=screen_time,
                first_appearance=char.first_appearance or 1,
                arc_type=ArcClassification.FLAT,
                arc_description="Requires analysis",
                key_scenes=[],
                relationships=[],
            )
            entries.append(entry)

        return self._build_report(script, entries)

    def _generate_with_llm(self, script: Script) -> CharacterAtlasReport:
        """Generate report using LLM analysis."""
        if self.provider is None:
            raise GeneratorError(
                "LLM provider required for character analysis",
                report_type=self.report_type,
            )

        system_prompt = self._build_system_prompt()
        analysis_prompt = self._build_analysis_prompt(script)

        try:
            response = self.provider.complete_structured(
                analysis_prompt,
                LLMCharacterAtlasResponse,
                system=system_prompt,
            )
        except Exception as e:
            raise GeneratorError(
                f"LLM analysis failed: {e}",
                report_type=self.report_type,
                cause=e,
            ) from e

        return self._convert_llm_response(script, response)

    def _convert_llm_response(
        self,
        script: Script,
        response: LLMCharacterAtlasResponse,
    ) -> CharacterAtlasReport:
        """Convert LLM response to CharacterAtlasReport."""
        # Build relationship map for character entries
        relationship_map: dict[str, list[CharacterRelationship]] = {}
        for rel in response.relationships:
            # Add relationship to both characters
            for name in [rel.character_a, rel.character_b]:
                if name not in relationship_map:
                    relationship_map[name] = []
                relationship_map[name].append(
                    CharacterRelationship(
                        character_a=rel.character_a,
                        character_b=rel.character_b,
                        relationship_type=rel.relationship_type,
                        description=rel.description,
                        evolution=rel.evolution,
                    )
                )

        entries = []
        for llm_entry in response.entries:
            # Parse arc type
            try:
                arc_type = ArcClassification(llm_entry.arc_type.lower())
            except ValueError:
                arc_type = ArcClassification.FLAT

            entry = CharacterAtlasEntry(
                name=llm_entry.name,
                role=llm_entry.role,
                screen_time=llm_entry.screen_time,
                first_appearance=llm_entry.first_appearance,
                want=llm_entry.want,
                need=llm_entry.need,
                lie=llm_entry.lie,
                truth=llm_entry.truth,
                arc_type=arc_type,
                arc_description=llm_entry.arc_description,
                key_scenes=llm_entry.key_scenes,
                relationships=relationship_map.get(llm_entry.name, []),
            )
            entries.append(entry)

        return CharacterAtlasReport(
            title=script.title,
            total_characters=response.total_characters,
            principal_count=response.principal_count,
            entries=entries,
            protagonist=response.protagonist,
            antagonist=response.antagonist,
            ensemble_balance=response.ensemble_balance,
            missing_archetypes=response.missing_archetypes,
        )

    def _build_report(
        self,
        script: Script,
        entries: list[CharacterAtlasEntry],
    ) -> CharacterAtlasReport:
        """Build the final report from entries."""
        # Identify protagonist/antagonist
        protagonist = find_protagonist(script)
        antagonist = find_antagonist(script)

        # Count principals (significant screen time)
        principal_count = sum(
            1 for e in entries
            if e.screen_time and e.screen_time >= self.config.screen_time_threshold
        )

        return CharacterAtlasReport(
            title=script.title,
            total_characters=len(script.characters),
            principal_count=principal_count,
            entries=entries,
            protagonist=protagonist,
            antagonist=antagonist,
            ensemble_balance=None,  # Would need LLM
            missing_archetypes=[],  # Would need LLM
        )

    def _find_key_scenes_for_character(
        self,
        script: Script,
        character_name: str,
    ) -> list[int]:
        """Find key scenes for a character based on function codes."""
        from narratological.models.analysis import BeatFunction

        key_functions = {
            BeatFunction.INCITE,
            BeatFunction.CRISIS,
            BeatFunction.CLIMAX,
            BeatFunction.REVEAL,
        }

        key_scenes = []
        for scene in script.scenes:
            if character_name not in scene.characters_present:
                continue
            if scene.function in key_functions:
                key_scenes.append(scene.number)

        return key_scenes

    def _extract_relationships(
        self,
        character,
    ) -> list[CharacterRelationship]:
        """Extract relationships from character annotations."""
        relationships = []

        for other_name, rel_type in character.relationships.items():
            relationships.append(
                CharacterRelationship(
                    character_a=character.name,
                    character_b=other_name,
                    relationship_type=rel_type,
                    description=rel_type,  # Minimal description
                    evolution=None,
                )
            )

        return relationships

    def _build_system_prompt(self) -> str:
        """Build system prompt for LLM."""
        return CHARACTER_ATLAS_SYSTEM_PROMPT

    def _build_analysis_prompt(self, script: Script) -> str:
        """Build analysis prompt for LLM."""
        return build_character_atlas_prompt(script)
