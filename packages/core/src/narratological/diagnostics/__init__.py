"""Diagnostic test runners for narrative analysis.

Provides structural diagnostics for scripts:
- Causal Binding: BUT/THEREFORE vs AND THEN analysis
- Reorderability: Scene independence assessment
- Necessity: Scene essentiality evaluation
- Information Economy: Exposition efficiency
- Framework: Study-specific diagnostic questions

Each diagnostic can operate with or without LLM assistance.
"""

from narratological.diagnostics.base import BaseDiagnostic
from narratological.diagnostics.causal import CausalBindingDiagnostic
from narratological.diagnostics.framework import FrameworkDiagnostic
from narratological.diagnostics.models import (
    DiagnosticContext,
    DiagnosticMetrics,
    DiagnosticThresholds,
    DiagnosticType,
    InformationUnit,
    NecessityAssessment,
    ReorderabilityAssessment,
    SceneTransition,
)
from narratological.diagnostics.runner import DiagnosticRunner, create_diagnostic_runner
from narratological.diagnostics.structural import (
    InformationEconomyDiagnostic,
    NecessityDiagnostic,
    ReorderabilityDiagnostic,
)

__all__ = [
    # Base
    "BaseDiagnostic",
    # Models
    "DiagnosticContext",
    "DiagnosticMetrics",
    "DiagnosticThresholds",
    "DiagnosticType",
    "SceneTransition",
    "ReorderabilityAssessment",
    "NecessityAssessment",
    "InformationUnit",
    # Diagnostics
    "CausalBindingDiagnostic",
    "ReorderabilityDiagnostic",
    "NecessityDiagnostic",
    "InformationEconomyDiagnostic",
    "FrameworkDiagnostic",
    # Runner
    "DiagnosticRunner",
    "create_diagnostic_runner",
]
