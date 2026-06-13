from agents.roles import DEFAULT_AGENT_SEQUENCE
from backend.app.schemas import Task, ToolCall, WorkflowState


def run_workflow(task: Task) -> WorkflowState:
    """Return a deterministic workflow trace until model-backed agents are added."""
    state = WorkflowState(task_id=task.id, status="running")

    for role in DEFAULT_AGENT_SEQUENCE:
        state.active_role = role
        state.tool_calls.append(
            ToolCall(
                name=f"{role.value}_step",
                arguments={"task_type": task.task_type},
                success=True,
                latency_ms=0,
                output_summary=f"Scaffolded {role.value} action for {task.title}.",
            )
        )
        state.completed_roles.append(role)

    state.active_role = None
    state.status = "completed"
    state.final_answer = (
        "Workflow scaffold completed. Model-backed planning, retrieval, and validation "
        "will be connected in later implementation stages."
    )
    return state
