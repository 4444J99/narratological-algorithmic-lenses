"""Structural Diagnostics: Reorderability, Necessity, Information Economy.

These diagnostics assess the structural integrity of a narrative
beyond causal binding.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel, Field

from narratological.diagnostics.base import BaseDiagnostic
from narratological.diagnostics.models import (
    DiagnosticContext,
    DiagnosticType,
    NecessityAssessment,
    ReorderabilityAssessment,
)
from narratological.models.report import DiagnosticIssue, DiagnosticSeverity

if TYPE_CHECKING:
    pass


# =============================================================================
# LLM Response Models
# =============================================================================

class LLMReorderabilityResponse(BaseModel):
    """LLM response for reorderability analysis."""

    assessments: list[dict] = Field(default_factory=list)
    reorderable_count: int = 0
    recommendations: list[str] = Field(default_factory=list)


class LLMNecessityResponse(BaseModel):
    """LLM response for necessity analysis."""

    assessments: list[dict] = Field(default_factory=list)
    unnecessary_count: int = 0
    recommendations: list[str] = Field(default_factory=list)


class LLMInfoEconomyResponse(BaseModel):
    """LLM response for information economy analysis."""

    redundant_expositions: list[dict] = Field(default_factory=list)
    missing_setups: list[dict] = Field(default_factory=list)
    efficiency_score: float = 1.0
    recommendations: list[str] = Field(default_factory=list)


# =============================================================================
# Reorderability Diagnostic
# =============================================================================

class ReorderabilityDiagnostic(BaseDiagnostic):
    """Diagnostic for scene reorderability.

    Tests whether scenes could be moved without affecting the narrative.
    High reorderability indicates weak structure. Lower is better.
    """

    diagnostic_type = DiagnosticType.REORDERABILITY
    description = "Assesses whether scenes could be reordered without narrative damage"

    def run(self, context: DiagnosticContext) -> list[DiagnosticIssue]:
        """Run the reorderability diagnostic."""
        can_run, error = self.can_run(context)
        if not can_run:
            return [
                self.create_issue(
                    description=error or "Cannot run diagnostic",
                    severity=DiagnosticSeverity.INFO,
                    recommendation="Provide scene data or LLM provider",
                )
            ]

        issues = []

        # Use LLM for analysis
        if self.provider is not None:
            assessments = self._analyze_with_llm(context)
        else:
            # Basic algorithmic check based on dependencies
            assessments = self._analyze_algorithmically(context)

        # Generate issues for reorderable scenes
        reorderable = [a for a in assessments if a.is_reorderable]
        score = 1.0 - (len(reorderable) / len(assessments)) if assessments else 1.0

        for assessment in reorderable:
            issues.append(
                self.create_issue(
                    description=f"Scene {assessment.scene_number} could be reordered without affecting the narrative",
                    severity=DiagnosticSeverity.WARNING,
                    location=f"Scene {assessment.scene_number}",
                    recommendation=assessment.reason or "Consider strengthening dependencies to/from this scene",
                )
            )

        # Overall score
        overall_severity = self._get_severity_for_reorderability(1.0 - score)
        issues.append(
            self.create_issue(
                description=f"Reorderability score: {(1.0 - score):.0%} of scenes are loosely bound (lower is better)",
                severity=overall_severity,
                recommendation="Strengthen causal dependencies between scenes" if score < 0.85 else "Scene ordering is well-justified",
            )
        )

        return issues

    def calculate_score(self, context: DiagnosticContext) -> float:
        """Calculate reorderability score (proportion of reorderable scenes)."""
        if self.provider is not None:
            assessments = self._analyze_with_llm(context)
        else:
            assessments = self._analyze_algorithmically(context)

        if not assessments:
            return 0.0

        reorderable = sum(1 for a in assessments if a.is_reorderable)
        return reorderable / len(assessments)

    def _get_severity_for_reorderability(self, score: float) -> DiagnosticSeverity:
        """Get severity (lower score is better for reorderability)."""
        if score <= self.thresholds.reorderability_excellent:
            return DiagnosticSeverity.INFO
        elif score <= self.thresholds.reorderability_good:
            return DiagnosticSeverity.SUGGESTION
        elif score <= self.thresholds.reorderability_warning:
            return DiagnosticSeverity.WARNING
        else:
            return DiagnosticSeverity.CRITICAL

    def _analyze_algorithmically(
        self,
        context: DiagnosticContext,
    ) -> list[ReorderabilityAssessment]:
        """Basic algorithmic analysis based on scene structure."""
        assessments = []

        for scene in context.scenes:
            scene_num = scene.get("number", 0)

            # Simple heuristic: scenes with no explicit connector
            # and generic functions are more reorderable
            connector = scene.get("connector")
            function = scene.get("function", "").upper()

            # Key structural scenes are not reorderable
            key_functions = {"INCITE", "CLIMAX", "CRISIS", "RESOLVE"}
            is_key = function in key_functions

            # Scenes with causal connectors are less reorderable
            causal_connectors = {"BUT", "THEREFORE"}
            has_causal = connector and connector.upper() in causal_connectors

            is_reorderable = not is_key and not has_causal

            assessments.append(
                ReorderabilityAssessment(
                    scene_number=scene_num,
                    is_reorderable=is_reorderable,
                    reason="Key structural scene" if is_key else (
                        "Has causal connector" if has_causal else "Loosely connected"
                    ),
                )
            )

        return assessments

    def _analyze_with_llm(
        self,
        context: DiagnosticContext,
    ) -> list[ReorderabilityAssessment]:
        """Use LLM for reorderability analysis."""
        if self.provider is None:
            return self._analyze_algorithmically(context)

        prompt = self._build_prompt(context)

        try:
            response = self.provider.complete_structured(
                prompt,
                LLMReorderabilityResponse,
                system="You are analyzing whether scenes could be reordered without narrative damage.",
            )

            assessments = []
            for item in response.assessments:
                assessments.append(
                    ReorderabilityAssessment(
                        scene_number=item.get("scene_number", 0),
                        is_reorderable=item.get("is_reorderable", False),
                        reason=item.get("reason"),
                        alternative_positions=item.get("alternative_positions", []),
                    )
                )
            return assessments

        except Exception:
            return self._analyze_algorithmically(context)

    def _build_prompt(self, context: DiagnosticContext) -> str:
        """Build LLM prompt."""
        scenes_text = "\n".join(
            f"Scene {s.get('number')}: {s.get('summary', 'No summary')}"
            for s in context.scenes[:30]
        )

        return f"""Analyze which scenes in this script could be reordered without damaging the narrative.

TITLE: {context.title}

SCENES:
{scenes_text}

For each scene, determine:
1. Could it be moved to a different position without breaking causality?
2. What constraints keep it in its current position?
3. If reorderable, where else could it go?

Respond with JSON containing:
- assessments: Array with scene_number, is_reorderable, reason, alternative_positions
- reorderable_count: How many scenes could be reordered
- recommendations: Suggestions for tightening scene dependencies"""


# =============================================================================
# Necessity Diagnostic
# =============================================================================

class NecessityDiagnostic(BaseDiagnostic):
    """Diagnostic for scene necessity.

    Tests whether each scene is essential to the narrative.
    Higher necessity score is better.
    """

    diagnostic_type = DiagnosticType.NECESSITY
    description = "Assesses whether each scene is necessary to the narrative"

    def run(self, context: DiagnosticContext) -> list[DiagnosticIssue]:
        """Run the necessity diagnostic."""
        can_run, error = self.can_run(context)
        if not can_run:
            return [
                self.create_issue(
                    description=error or "Cannot run diagnostic",
                    severity=DiagnosticSeverity.INFO,
                    recommendation="Provide scene data or LLM provider",
                )
            ]

        issues = []

        if self.provider is not None:
            assessments = self._analyze_with_llm(context)
        else:
            assessments = self._analyze_algorithmically(context)

        # Generate issues for unnecessary scenes
        unnecessary = [a for a in assessments if not a.is_necessary]
        score = (len(assessments) - len(unnecessary)) / len(assessments) if assessments else 1.0

        for assessment in unnecessary:
            issues.append(
                self.create_issue(
                    description=f"Scene {assessment.scene_number} may not be necessary",
                    severity=DiagnosticSeverity.WARNING,
                    location=f"Scene {assessment.scene_number}",
                    recommendation=assessment.removal_impact or "Consider cutting or consolidating this scene",
                )
            )

        # Overall score
        overall_severity = self._get_severity_for_necessity(score)
        issues.append(
            self.create_issue(
                description=f"Necessity score: {score:.0%} of scenes are essential (higher is better)",
                severity=overall_severity,
                recommendation="Consider consolidating redundant scenes" if score < 0.85 else "All scenes serve clear purposes",
            )
        )

        return issues

    def calculate_score(self, context: DiagnosticContext) -> float:
        """Calculate necessity score (proportion of necessary scenes)."""
        if self.provider is not None:
            assessments = self._analyze_with_llm(context)
        else:
            assessments = self._analyze_algorithmically(context)

        if not assessments:
            return 1.0

        necessary = sum(1 for a in assessments if a.is_necessary)
        return necessary / len(assessments)

    def _get_severity_for_necessity(self, score: float) -> DiagnosticSeverity:
        """Get severity (higher is better for necessity)."""
        if score >= self.thresholds.necessity_excellent:
            return DiagnosticSeverity.INFO
        elif score >= self.thresholds.necessity_good:
            return DiagnosticSeverity.SUGGESTION
        elif score >= self.thresholds.necessity_warning:
            return DiagnosticSeverity.WARNING
        else:
            return DiagnosticSeverity.CRITICAL

    def _analyze_algorithmically(
        self,
        context: DiagnosticContext,
    ) -> list[NecessityAssessment]:
        """Basic algorithmic analysis."""
        assessments = []

        for scene in context.scenes:
            scene_num = scene.get("number", 0)
            function = scene.get("function", "").upper()

            # Key structural scenes are always necessary
            key_functions = {"INCITE", "CLIMAX", "CRISIS", "RESOLVE", "SETUP", "PAYOFF"}
            is_key = function in key_functions

            # Scenes with characters present are usually necessary
            has_characters = len(scene.get("characters", [])) > 0

            is_necessary = is_key or has_characters

            assessments.append(
                NecessityAssessment(
                    scene_number=scene_num,
                    is_necessary=is_necessary,
                    narrative_functions=[function] if function else [],
                )
            )

        return assessments

    def _analyze_with_llm(
        self,
        context: DiagnosticContext,
    ) -> list[NecessityAssessment]:
        """Use LLM for necessity analysis."""
        if self.provider is None:
            return self._analyze_algorithmically(context)

        prompt = self._build_prompt(context)

        try:
            response = self.provider.complete_structured(
                prompt,
                LLMNecessityResponse,
                system="You are analyzing whether each scene is essential to the narrative.",
            )

            assessments = []
            for item in response.assessments:
                assessments.append(
                    NecessityAssessment(
                        scene_number=item.get("scene_number", 0),
                        is_necessary=item.get("is_necessary", True),
                        narrative_functions=item.get("functions", []),
                        removal_impact=item.get("removal_impact"),
                    )
                )
            return assessments

        except Exception:
            return self._analyze_algorithmically(context)

    def _build_prompt(self, context: DiagnosticContext) -> str:
        """Build LLM prompt."""
        scenes_text = "\n".join(
            f"Scene {s.get('number')}: {s.get('summary', 'No summary')}"
            for s in context.scenes[:30]
        )

        return f"""Analyze which scenes in this script are essential to the narrative.

TITLE: {context.title}

SCENES:
{scenes_text}

For each scene, determine:
1. Is this scene necessary? What would be lost if it were cut?
2. What narrative functions does it serve?
3. Could its content be merged with another scene?

Respond with JSON containing:
- assessments: Array with scene_number, is_necessary, functions, removal_impact
- unnecessary_count: How many scenes could potentially be cut
- recommendations: Suggestions for consolidation"""


# =============================================================================
# Information Economy Diagnostic
# =============================================================================

class InformationEconomyDiagnostic(BaseDiagnostic):
    """Diagnostic for information economy.

    Tests the efficiency of information delivery:
    - Redundant exposition (same info repeated)
    - Missing setups (payoffs without plants)
    - Exposition dumps vs. organic reveal
    """

    diagnostic_type = DiagnosticType.INFORMATION_ECONOMY
    description = "Assesses efficiency of information delivery"

    def run(self, context: DiagnosticContext) -> list[DiagnosticIssue]:
        """Run the information economy diagnostic."""
        can_run, error = self.can_run(context)
        if not can_run:
            return [
                self.create_issue(
                    description=error or "Cannot run diagnostic",
                    severity=DiagnosticSeverity.INFO,
                    recommendation="Provide scene data or LLM provider",
                )
            ]

        if self.provider is None:
            # This diagnostic really needs LLM for meaningful analysis
            return [
                self.create_issue(
                    description="Information economy analysis requires LLM provider for detailed assessment",
                    severity=DiagnosticSeverity.INFO,
                    recommendation="Use LLM provider for full information economy analysis",
                )
            ]

        issues = []
        analysis = self._analyze_with_llm(context)

        # Issues for redundant exposition
        for redundancy in analysis.get("redundant_expositions", []):
            issues.append(
                self.create_issue(
                    description=f"Redundant exposition: {redundancy.get('content', 'Unknown')}",
                    severity=DiagnosticSeverity.WARNING,
                    location=f"Scenes {redundancy.get('scenes', [])}",
                    recommendation="Consider consolidating or cutting repeated information",
                    category="information",
                )
            )

        # Issues for missing setups
        for missing in analysis.get("missing_setups", []):
            issues.append(
                self.create_issue(
                    description=f"Missing setup for payoff: {missing.get('payoff', 'Unknown')}",
                    severity=DiagnosticSeverity.WARNING,
                    location=f"Scene {missing.get('scene', '?')}",
                    recommendation="Add earlier setup/plant for this payoff",
                    category="information",
                )
            )

        # Overall score
        score = analysis.get("efficiency_score", 1.0)
        overall_severity = self._get_severity_for_info_economy(score)
        issues.append(
            self.create_issue(
                description=f"Information economy score: {score:.0%} efficiency",
                severity=overall_severity,
                recommendation="Review exposition for efficiency" if score < 0.75 else "Information delivery is efficient",
            )
        )

        return issues

    def calculate_score(self, context: DiagnosticContext) -> float:
        """Calculate information economy score."""
        if self.provider is None:
            return 1.0  # Cannot calculate without LLM

        analysis = self._analyze_with_llm(context)
        return analysis.get("efficiency_score", 1.0)

    def _get_severity_for_info_economy(self, score: float) -> DiagnosticSeverity:
        """Get severity (higher is better)."""
        if score >= self.thresholds.info_economy_excellent:
            return DiagnosticSeverity.INFO
        elif score >= self.thresholds.info_economy_good:
            return DiagnosticSeverity.SUGGESTION
        elif score >= self.thresholds.info_economy_warning:
            return DiagnosticSeverity.WARNING
        else:
            return DiagnosticSeverity.CRITICAL

    def _analyze_with_llm(self, context: DiagnosticContext) -> dict:
        """Use LLM for information economy analysis."""
        if self.provider is None:
            return {"efficiency_score": 1.0}

        prompt = self._build_prompt(context)

        try:
            response = self.provider.complete_structured(
                prompt,
                LLMInfoEconomyResponse,
                system="You are analyzing information delivery efficiency in a script.",
            )

            return {
                "redundant_expositions": response.redundant_expositions,
                "missing_setups": response.missing_setups,
                "efficiency_score": response.efficiency_score,
                "recommendations": response.recommendations,
            }

        except Exception:
            return {"efficiency_score": 1.0}

    def _build_prompt(self, context: DiagnosticContext) -> str:
        """Build LLM prompt."""
        scenes_text = "\n".join(
            f"Scene {s.get('number')}: {s.get('summary', 'No summary')}"
            for s in context.scenes[:30]
        )

        return f"""Analyze the information economy of this script.

TITLE: {context.title}

SCENES:
{scenes_text}

Identify:
1. REDUNDANT EXPOSITION: Information delivered multiple times unnecessarily
2. MISSING SETUPS: Payoffs or reveals without earlier plants
3. EXPOSITION DUMPS: Heavy exposition that could be more organic

Rate overall information efficiency from 0.0 to 1.0.

Respond with JSON containing:
- redundant_expositions: Array with content, scenes
- missing_setups: Array with payoff, scene
- efficiency_score: Float 0.0-1.0
- recommendations: Suggestions for improvement"""
