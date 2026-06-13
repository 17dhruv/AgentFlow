# AgentFlow Architecture

AgentFlow is organized around four layers: API, orchestration, retrieval, and evaluation.

## API Layer

The FastAPI backend receives developer workflow tasks and returns structured workflow results. Planned API surfaces include:

- Submit task
- Retrieve project context
- Run agent workflow
- Fetch workflow state
- Fetch evaluation results

## Agentic Workflow Layer

The orchestration layer routes tasks through specialized roles:

- `planner` decomposes the request into subtasks
- `retriever` gathers relevant project context
- `coder` proposes implementation steps or code changes
- `debugger` analyzes failures and likely fixes
- `validator` checks whether the output satisfies the task

## RAG Layer

The retrieval layer ingests project docs and code snippets, chunks them, assigns metadata, and returns top-k contextual matches. Vector search is represented by interfaces for now so the repo can later plug in FAISS, Chroma, pgvector, or another vector store.

## Evaluation Layer

The evaluation layer reads benchmark records and computes:

- Task completion rate
- Tool-call success rate
- Retrieval precision@k
- Average latency
- Pass/fail result against expected behavior

Answer faithfulness and human-rated quality are planned as later evaluator modules.
