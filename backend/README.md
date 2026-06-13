# Backend

FastAPI service scaffold for AgentFlow.

Planned responsibilities:

- Accept workflow tasks
- Call the RAG layer for project context
- Run agent orchestration
- Persist workflow state
- Return evaluation summaries

Intended local command:

```bash
uvicorn backend.app.main:app --reload
```
