from fastapi import FastAPI

from agents.orchestrator import run_workflow
from backend.app.schemas import EvaluationResult, Task, WorkflowState
from evaluation.metrics import summarize_tool_calls

app = FastAPI(
    title="AgentFlow",
    description="Agentic ML workflow orchestration and RAG evaluation platform.",
    version="0.1.0",
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "project": "AgentFlow"}


@app.post("/tasks", response_model=WorkflowState)
def submit_task(task: Task) -> WorkflowState:
    return run_workflow(task)


@app.post("/tasks/{task_id}/evaluate", response_model=EvaluationResult)
def evaluate_task(task_id: str, state: WorkflowState) -> EvaluationResult:
    summary = summarize_tool_calls(state.tool_calls)
    return EvaluationResult(
        task_id=task_id,
        task_completed=state.status == "completed",
        tool_call_success_rate=summary["success_rate"],
        average_latency_ms=summary["average_latency_ms"],
        notes="Initial scaffold evaluator. Retrieval and faithfulness metrics are planned.",
    )
