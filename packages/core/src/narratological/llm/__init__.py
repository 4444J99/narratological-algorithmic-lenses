"""LLM integration for narratological analysis.

This module provides:
- LLM provider implementations (Anthropic, OpenAI, Mock)
- 8-role analyst system for multi-perspective analysis
- Multi-role orchestration and synthesis

Example usage:
    from narratological.llm import get_provider, AnthropicProvider
    from narratological.llm import get_analyst, MultiRoleOrchestrator

    # Using factory function
    provider = get_provider("anthropic")

    # Multi-role analysis
    orchestrator = MultiRoleOrchestrator(provider)
    result = orchestrator.analyze(text, title="My Script")
"""

from narratological.llm.analyst import BaseAnalyst
from narratological.llm.providers import (
    AnthropicProvider,
    CompletionResult,
    LLMProvider,
    MockProvider,
    MockResponse,
    OpenAIProvider,
    get_provider,
)
from narratological.llm.roles import get_all_analysts, get_analyst
from narratological.llm.synthesis import AnalysisOrchestrator, MultiRoleOrchestrator

__all__ = [
    # Providers
    "LLMProvider",
    "AnthropicProvider",
    "OpenAIProvider",
    "MockProvider",
    "MockResponse",
    "CompletionResult",
    "get_provider",
    # Analysts
    "BaseAnalyst",
    "get_analyst",
    "get_all_analysts",
    # Orchestration
    "MultiRoleOrchestrator",
    "AnalysisOrchestrator",
]
