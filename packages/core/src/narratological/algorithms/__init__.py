"""Algorithm implementations for narratological analysis.

This module provides the infrastructure for executing narratological algorithms
using LLM providers. All 92 algorithms across 14 studies are accessible through
the AlgorithmRegistry.

Example usage:
    from narratological.algorithms import AlgorithmRegistry, create_executor

    # Get an algorithm
    registry = AlgorithmRegistry()
    algo = registry.get("pixar", "engineer_empathy")

    # Execute with an LLM
    executor = create_executor("anthropic")
    result = executor.analyze(algo, "Once upon a time...")
"""

from narratological.algorithms.base import (
    AnalysisResult,
    ExecutableAlgorithm,
    ExecutionMode,
    GenerationResult,
    ValidationResult,
)
from narratological.algorithms.executor import (
    AlgorithmExecutor,
    ExecutionContext,
    ExecutionLog,
    ExecutorError,
    create_executor,
)
from narratological.algorithms.registry import (
    AlgorithmInfo,
    AlgorithmRegistry,
    get_registry,
    reset_registry,
)

__all__ = [
    # Base classes and results
    "ExecutableAlgorithm",
    "ExecutionMode",
    "AnalysisResult",
    "GenerationResult",
    "ValidationResult",
    # Registry
    "AlgorithmRegistry",
    "AlgorithmInfo",
    "get_registry",
    "reset_registry",
    # Executor
    "AlgorithmExecutor",
    "ExecutionContext",
    "ExecutionLog",
    "ExecutorError",
    "create_executor",
]
