# narratological

Core library for narratological analysis using formalized algorithms.

## Installation

```bash
pip install narratological
```

## Usage

```python
from narratological import load_compendium, load_study

# Load all studies
compendium = load_compendium()
print(f"Loaded {len(compendium.studies)} studies")

# Load a specific study
study = load_study("bergman")
print(f"{study.creator}: {len(study.axioms)} axioms, {len(study.core_algorithms)} algorithms")

# Search across studies
results = compendium.search_axioms("transformation")
for study_id, axiom in results:
    print(f"[{study_id}] {axiom.name}")
```

## Features

- Pydantic models for all narratological data structures
- Load 14 studies with ~79 axioms and ~92 algorithms
- Search axioms and algorithms across all studies
- Type-safe analysis workflows
