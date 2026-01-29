# narratological-api

FastAPI backend for narratological analysis.

## Installation

```bash
pip install narratological-api
```

## Usage

```bash
# Start the server
uvicorn narratological_api.main:app --reload

# API documentation available at http://localhost:8000/docs
```

## Endpoints

- `GET /studies/` - List all studies
- `GET /studies/{study_id}` - Get a specific study
- `GET /studies/{study_id}/axioms` - Get study axioms
- `GET /studies/{study_id}/algorithms` - Get study algorithms
- `GET /studies/search/axioms?q=query` - Search axioms
- `POST /analysis/scene` - Analyze a scene
- `GET /diagnostics/metrics` - Get diagnostic metrics
