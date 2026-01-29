"""Diagnostic Runner - orchestrates all diagnostic tests.

Provides a unified interface for running structural diagnostics
and generating comprehensive diagnostic reports.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from narratological.diagnostics.base import BaseDiagnostic
from narratological.diagnostics.causal import CausalBindingDiagnostic
from narratological.diagnostics.framework import FrameworkDiagnostic
from narratological.diagnostics.models import (
    DiagnosticContext,
    DiagnosticMetrics,
    DiagnosticThresholds,
    DiagnosticType,
)
from narratological.diagnostics.structural import (
    InformationEconomyDiagnostic,
    NecessityDiagnostic,
    ReorderabilityDiagnostic,
)
from narratological.models.report import DiagnosticIssue, DiagnosticReport, DiagnosticSeverity

if TYPE_CHECKING:
    from narratological.llm.providers import LLMProvider
    from narratological.models.analysis import Script
    from narratological.models.study import Compendium


class DiagnosticRunner:
    """Orchestrates all diagnostic tests and generates reports.

    Coordinates the execution of:
    - Causal binding analysis
    - Reorderability assessment
    - Necessity evaluation
    - Information economy analysis
    - Framework-specific diagnostics
    """

    def __init__(
        self,
        provider: LLMProvider | None = None,
        compendium: Compendium | None = None,
        thresholds: DiagnosticThresholds | None = None,
    ):
        """Initialize the diagnostic runner.

        Args:
            provider: LLM provider for diagnostics.
            compendium: Compendium for framework diagnostics.
            thresholds: Severity thresholds.
        """
        self.provider = provider
        self.compendium = compendium
        self.thresholds = thresholds or DiagnosticThresholds()

        # Initialize diagnostic instances
        self._diagnostics: dict[DiagnosticType, BaseDiagnostic] = {
            DiagnosticType.CAUSAL_BINDING: CausalBindingDiagnostic(
                provider=provider,
                thresholds=self.thresholds,
            ),
            DiagnosticType.REORDERABILITY: ReorderabilityDiagnostic(
                provider=provider,
                thresholds=self.thresholds,
            ),
            DiagnosticType.NECESSITY: NecessityDiagnostic(
                provider=provider,
                thresholds=self.thresholds,
            ),
            DiagnosticType.INFORMATION_ECONOMY: InformationEconomyDiagnostic(
                provider=provider,
                thresholds=self.thresholds,
            ),
            DiagnosticType.FRAMEWORK: FrameworkDiagnostic(
                provider=provider,
                compendium=compendium,
                thresholds=self.thresholds,
            ),
        }

    def run_all(
        self,
        context: DiagnosticContext,
        include_framework: bool = True,
        framework_studies: list[str] | None = None,
    ) -> DiagnosticReport:
        """Run all diagnostic tests and generate a report.

        Args:
            context: The diagnostic context.
            include_framework: Whether to run framework diagnostics.
            framework_studies: Specific studies for framework diagnostics.

        Returns:
            Complete DiagnosticReport.
        """
        all_issues: list[DiagnosticIssue] = []

        # Run structural diagnostics
        causal_issues = self.run_causal(context)
        all_issues.extend(causal_issues[1])

        reorder_issues = self.run_reorderability(context)
        all_issues.extend(reorder_issues[1])

        necessity_issues = self.run_necessity(context)
        all_issues.extend(necessity_issues[1])

        info_issues = self.run_information_economy(context)
        all_issues.extend(info_issues[1])

        # Run framework diagnostics if requested
        if include_framework:
            framework_issues = self.run_framework(context, framework_studies)
            all_issues.extend(framework_issues)

        # Calculate metrics
        metrics = self._calculate_metrics(context)

        # Count issues by severity
        critical_count = sum(
            1 for i in all_issues if i.severity == DiagnosticSeverity.CRITICAL
        )
        warning_count = sum(
            1 for i in all_issues if i.severity == DiagnosticSeverity.WARNING
        )

        # Generate priority fixes
        priority_fixes = self._generate_priority_fixes(all_issues)

        # Determine frameworks applied
        frameworks_applied = ["causal_binding", "reorderability", "necessity", "information_economy"]
        if include_framework:
            frameworks_applied.append("framework")

        return DiagnosticReport(
            title=context.title,
            frameworks_applied=frameworks_applied,
            issues=all_issues,
            causal_binding_ratio=metrics.causal_binding_ratio,
            reorderability_score=metrics.reorderability_score,
            necessity_score=metrics.necessity_score,
            information_economy_score=metrics.information_economy_score,
            critical_count=critical_count,
            warning_count=warning_count,
            overall_health=metrics.overall_health,
            priority_fixes=priority_fixes,
        )

    def run_causal(
        self,
        context: DiagnosticContext,
    ) -> tuple[float, list[DiagnosticIssue]]:
        """Run causal binding diagnostic.

        Args:
            context: The diagnostic context.

        Returns:
            Tuple of (score, issues).
        """
        diagnostic = self._diagnostics[DiagnosticType.CAUSAL_BINDING]
        issues = diagnostic.run(context)
        score = diagnostic.calculate_score(context)
        return score, issues

    def run_reorderability(
        self,
        context: DiagnosticContext,
    ) -> tuple[float, list[DiagnosticIssue]]:
        """Run reorderability diagnostic.

        Args:
            context: The diagnostic context.

        Returns:
            Tuple of (score, issues).
        """
        diagnostic = self._diagnostics[DiagnosticType.REORDERABILITY]
        issues = diagnostic.run(context)
        score = diagnostic.calculate_score(context)
        return score, issues

    def run_necessity(
        self,
        context: DiagnosticContext,
    ) -> tuple[float, list[DiagnosticIssue]]:
        """Run necessity diagnostic.

        Args:
            context: The diagnostic context.

        Returns:
            Tuple of (score, issues).
        """
        diagnostic = self._diagnostics[DiagnosticType.NECESSITY]
        issues = diagnostic.run(context)
        score = diagnostic.calculate_score(context)
        return score, issues

    def run_information_economy(
        self,
        context: DiagnosticContext,
    ) -> tuple[float, list[DiagnosticIssue]]:
        """Run information economy diagnostic.

        Args:
            context: The diagnostic context.

        Returns:
            Tuple of (score, issues).
        """
        diagnostic = self._diagnostics[DiagnosticType.INFORMATION_ECONOMY]
        issues = diagnostic.run(context)
        score = diagnostic.calculate_score(context)
        return score, issues

    def run_framework(
        self,
        context: DiagnosticContext,
        study_ids: list[str] | None = None,
    ) -> list[DiagnosticIssue]:
        """Run framework diagnostics.

        Args:
            context: The diagnostic context.
            study_ids: Specific studies to evaluate against.

        Returns:
            List of framework diagnostic issues.
        """
        diagnostic = self._diagnostics[DiagnosticType.FRAMEWORK]
        if isinstance(diagnostic, FrameworkDiagnostic):
            return diagnostic.run(context, study_ids)
        return diagnostic.run(context)

    def run_single(
        self,
        diagnostic_type: DiagnosticType | str,
        context: DiagnosticContext,
    ) -> tuple[float, list[DiagnosticIssue]]:
        """Run a single diagnostic by type.

        Args:
            diagnostic_type: The type of diagnostic to run.
            context: The diagnostic context.

        Returns:
            Tuple of (score, issues).
        """
        if isinstance(diagnostic_type, str):
            diagnostic_type = DiagnosticType(diagnostic_type)

        diagnostic = self._diagnostics.get(diagnostic_type)
        if diagnostic is None:
            return 0.0, []

        issues = diagnostic.run(context)
        score = diagnostic.calculate_score(context)
        return score, issues

    def _calculate_metrics(self, context: DiagnosticContext) -> DiagnosticMetrics:
        """Calculate all diagnostic metrics."""
        causal_score = self._diagnostics[DiagnosticType.CAUSAL_BINDING].calculate_score(context)
        reorder_score = self._diagnostics[DiagnosticType.REORDERABILITY].calculate_score(context)
        necessity_score = self._diagnostics[DiagnosticType.NECESSITY].calculate_score(context)
        info_score = self._diagnostics[DiagnosticType.INFORMATION_ECONOMY].calculate_score(context)

        metrics = DiagnosticMetrics(
            causal_binding_ratio=causal_score,
            reorderability_score=reorder_score,
            necessity_score=necessity_score,
            information_economy_score=info_score,
        )

        metrics.compute_health(self.thresholds)
        return metrics

    def _generate_priority_fixes(
        self,
        issues: list[DiagnosticIssue],
    ) -> list[str]:
        """Generate prioritized list of fixes.

        Args:
            issues: All diagnostic issues.

        Returns:
            List of priority fix recommendations.
        """
        # Sort by severity (critical first)
        severity_order = {
            DiagnosticSeverity.CRITICAL: 0,
            DiagnosticSeverity.WARNING: 1,
            DiagnosticSeverity.SUGGESTION: 2,
            DiagnosticSeverity.INFO: 3,
        }

        sorted_issues = sorted(
            issues,
            key=lambda i: severity_order.get(i.severity, 3),
        )

        # Extract unique recommendations
        seen = set()
        priority_fixes = []

        for issue in sorted_issues:
            if issue.recommendation and issue.recommendation not in seen:
                # Skip generic/positive messages
                rec_lower = issue.recommendation.lower()
                if "is strong" in rec_lower or "well-justified" in rec_lower:
                    continue
                if "serves clear purposes" in rec_lower or "is efficient" in rec_lower:
                    continue

                seen.add(issue.recommendation)
                priority_fixes.append(issue.recommendation)

        return priority_fixes[:10]  # Top 10

    def from_script(self, script: Script) -> DiagnosticContext:
        """Create a diagnostic context from a Script model.

        Args:
            script: The script to analyze.

        Returns:
            DiagnosticContext ready for analysis.
        """
        return DiagnosticContext.from_script(script)


def create_diagnostic_runner(
    provider: LLMProvider | None = None,
    compendium: Compendium | None = None,
    thresholds: DiagnosticThresholds | None = None,
) -> DiagnosticRunner:
    """Factory function to create a diagnostic runner.

    Args:
        provider: LLM provider for diagnostics.
        compendium: Compendium for framework diagnostics.
        thresholds: Severity thresholds.

    Returns:
        Configured DiagnosticRunner instance.
    """
    return DiagnosticRunner(
        provider=provider,
        compendium=compendium,
        thresholds=thresholds,
    )
