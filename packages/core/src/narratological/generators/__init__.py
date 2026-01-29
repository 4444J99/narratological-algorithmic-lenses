"""Report generators for narrative analysis.

Provides generators for the five report types:
- Coverage: Executive summary with ratings and recommendations
- Beat Map: Scene-by-scene function and connector analysis
- Structural: Act architecture and key dramatic points
- Character Atlas: Want/Need/Lie/Truth and arc analysis
- Diagnostic: Structural issues and recommendations

Each generator can operate with or without LLM assistance.
"""

from narratological.generators.base import (
    BaseReportGenerator,
    GeneratorConfig,
    GeneratorError,
    ReportType,
)
from narratological.generators.beat_map import BeatMapReportGenerator
from narratological.generators.character_atlas import CharacterAtlasReportGenerator
from narratological.generators.coverage import CoverageReportGenerator
from narratological.generators.structural import StructuralReportGenerator

__all__ = [
    # Base classes
    "BaseReportGenerator",
    "GeneratorConfig",
    "GeneratorError",
    "ReportType",
    # Generators
    "BeatMapReportGenerator",
    "StructuralReportGenerator",
    "CharacterAtlasReportGenerator",
    "CoverageReportGenerator",
]
