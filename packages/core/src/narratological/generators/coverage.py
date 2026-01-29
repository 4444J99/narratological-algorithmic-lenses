"""Coverage Report Generator.

Generates executive summary coverage reports with ratings,
recommendations, and 8-role analyst notes.
"""

from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from pydantic import BaseModel, Field

from narratological.generators.base import (
    BaseReportGenerator,
    GeneratorConfig,
    GeneratorError,
    ReportType,
)
from narratological.generators.prompts import (
    COVERAGE_SYSTEM_PROMPT,
    build_coverage_prompt,
    build_role_analysis_prompt,
)
from narratological.models.report import CoverageReport, RecommendationType

if TYPE_CHECKING:
    from narratological.llm.providers import LLMProvider
    from narratological.models.analysis import Script


class LLMCoverageResponse(BaseModel):
    """LLM response model for coverage generation."""

    logline: str
    synopsis: str
    recommendation: str

    premise_rating: int = Field(ge=1, le=10)
    structure_rating: int = Field(ge=1, le=10)
    character_rating: int = Field(ge=1, le=10)
    dialogue_rating: int = Field(ge=1, le=10)
    originality_rating: int = Field(ge=1, le=10)
    marketability_rating: int = Field(ge=1, le=10)

    strengths: list[str] = Field(default_factory=list)
    weaknesses: list[str] = Field(default_factory=list)
    opportunities: list[str] = Field(default_factory=list)
    comparables: list[str] = Field(default_factory=list)


class LLMRoleNotes(BaseModel):
    """LLM response model for role-specific analysis."""

    notes: str
    key_observations: list[str] = Field(default_factory=list)


class CoverageReportGenerator(BaseReportGenerator[CoverageReport]):
    """Generator for Coverage reports.

    Creates executive summary coverage with:
    - Ratings across 6 dimensions (premise, structure, character, dialogue, originality, marketability)
    - Overall recommendation (CONSIDER, PASS, DEVELOP, URGENT)
    - Strengths, weaknesses, opportunities
    - 8-role analyst notes (Aesthete through First-Reader)
    - Comparable works

    Requires LLM for meaningful analysis.
    """

    report_type = ReportType.COVERAGE

    # Role mapping for analyst notes
    ANALYST_ROLES = [
        "aesthete",
        "dramaturgist",
        "narratologist",
        "art_historian",
        "cinephile",
        "rhetorician",
        "producer",
        "academic",
        "first_reader",
    ]

    def __init__(
        self,
        provider: LLMProvider | None = None,
        config: GeneratorConfig | None = None,
    ):
        """Initialize the coverage report generator.

        Args:
            provider: LLM provider for analysis.
            config: Generator configuration.
        """
        super().__init__(provider, config)

    def generate(self, script: Script, **kwargs) -> CoverageReport:
        """Generate a coverage report.

        Args:
            script: The script to analyze.
            **kwargs: Additional parameters:
                - include_role_notes: Override config setting

        Returns:
            Complete CoverageReport with ratings and notes.

        Raises:
            GeneratorError: If generation fails.
        """
        can_gen, errors = self.can_generate(script)
        if not can_gen:
            raise GeneratorError(
                f"Cannot generate coverage report: {'; '.join(errors)}",
                report_type=self.report_type,
            )

        include_role_notes = kwargs.get(
            "include_role_notes",
            self.config.include_role_notes,
        )

        # Generate main coverage
        coverage = self._generate_main_coverage(script)

        # Generate role notes if requested
        if include_role_notes and self.provider is not None:
            role_notes = self._generate_role_notes(script)
            coverage = self._add_role_notes(coverage, role_notes)

        return coverage

    def _requires_llm(self) -> bool:
        """Coverage report requires LLM."""
        return True

    def _generate_main_coverage(self, script: Script) -> CoverageReport:
        """Generate the main coverage analysis."""
        if self.provider is None:
            raise GeneratorError(
                "LLM provider required for coverage report",
                report_type=self.report_type,
            )

        system_prompt = self._build_system_prompt()
        analysis_prompt = self._build_analysis_prompt(script)

        try:
            response = self.provider.complete_structured(
                analysis_prompt,
                LLMCoverageResponse,
                system=system_prompt,
            )
        except Exception as e:
            raise GeneratorError(
                f"LLM analysis failed: {e}",
                report_type=self.report_type,
                cause=e,
            ) from e

        return self._convert_llm_response(script, response)

    def _generate_role_notes(self, script: Script) -> dict[str, str]:
        """Generate notes from each analyst role."""
        if self.provider is None:
            return {}

        role_notes = {}

        for role in self.ANALYST_ROLES:
            try:
                prompt = build_role_analysis_prompt(role, script)
                response = self.provider.complete_structured(
                    prompt,
                    LLMRoleNotes,
                    system=f"You are analyzing this script as the {role.upper()}.",
                )
                role_notes[role] = response.notes
            except Exception:
                # Continue with other roles if one fails
                role_notes[role] = None

        return role_notes

    def _convert_llm_response(
        self,
        script: Script,
        response: LLMCoverageResponse,
    ) -> CoverageReport:
        """Convert LLM response to CoverageReport."""
        # Parse recommendation
        recommendation_map = {
            "CONSIDER": RecommendationType.CONSIDER,
            "PASS": RecommendationType.PASS,
            "DEVELOP": RecommendationType.DEVELOP,
            "URGENT": RecommendationType.URGENT,
        }
        recommendation = recommendation_map.get(
            response.recommendation.upper(),
            RecommendationType.DEVELOP,
        )

        # Limit comparables
        comparables = response.comparables
        if self.config.include_comparables:
            comparables = comparables[: self.config.max_comparables]
        else:
            comparables = []

        return CoverageReport(
            title=script.title,
            analyst="Narratological AI",
            date=datetime.now(),
            logline=response.logline,
            synopsis=response.synopsis,
            recommendation=recommendation,
            premise_rating=response.premise_rating,
            structure_rating=response.structure_rating,
            character_rating=response.character_rating,
            dialogue_rating=response.dialogue_rating,
            originality_rating=response.originality_rating,
            marketability_rating=response.marketability_rating,
            strengths=response.strengths,
            weaknesses=response.weaknesses,
            opportunities=response.opportunities,
            comparables=comparables,
        )

    def _add_role_notes(
        self,
        coverage: CoverageReport,
        role_notes: dict[str, str | None],
    ) -> CoverageReport:
        """Add role-specific notes to the coverage report."""
        # Create updated report with role notes
        return CoverageReport(
            title=coverage.title,
            analyst=coverage.analyst,
            date=coverage.date,
            logline=coverage.logline,
            synopsis=coverage.synopsis,
            recommendation=coverage.recommendation,
            premise_rating=coverage.premise_rating,
            structure_rating=coverage.structure_rating,
            character_rating=coverage.character_rating,
            dialogue_rating=coverage.dialogue_rating,
            originality_rating=coverage.originality_rating,
            marketability_rating=coverage.marketability_rating,
            strengths=coverage.strengths,
            weaknesses=coverage.weaknesses,
            opportunities=coverage.opportunities,
            comparables=coverage.comparables,
            # Role notes
            aesthete_notes=role_notes.get("aesthete"),
            dramaturgist_notes=role_notes.get("dramaturgist"),
            narratologist_notes=role_notes.get("narratologist"),
            art_historian_notes=role_notes.get("art_historian"),
            cinephile_notes=role_notes.get("cinephile"),
            rhetorician_notes=role_notes.get("rhetorician"),
            producer_notes=role_notes.get("producer"),
            academic_notes=role_notes.get("academic"),
            first_reader_notes=role_notes.get("first_reader"),
        )

    def _build_system_prompt(self) -> str:
        """Build system prompt for LLM."""
        return COVERAGE_SYSTEM_PROMPT

    def _build_analysis_prompt(self, script: Script) -> str:
        """Build analysis prompt for LLM."""
        return build_coverage_prompt(script)
