# narratological-cli

Command-line interface for narratological analysis.

## Installation

```bash
pip install narratological-cli
```

## Usage

```bash
# List all studies
narratological study list

# Show a specific study
narratological study show bergman

# Search for axioms
narratological study search "transformation"

# Analyze a script (requires LLM integration)
narratological analyze script my-script.txt --framework pixar
```

## Commands

- `study` - Explore narratological studies
- `analyze` - Analyze scripts and stories
- `diagnose` - Run diagnostic tests
- `generate` - Generate narrative structures
