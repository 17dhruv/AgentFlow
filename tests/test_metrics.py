from backend.app.schemas import RetrievedContext, ToolCall
from evaluation.metrics import retrieval_precision_at_k, tool_call_success_rate


def test_tool_call_success_rate() -> None:
    calls = [
        ToolCall(name="planner_step", success=True),
        ToolCall(name="retriever_step", success=False),
        ToolCall(name="validator_step", success=True),
    ]

    assert tool_call_success_rate(calls) == 2 / 3


def test_retrieval_precision_at_k() -> None:
    results = [
        RetrievedContext(source_id="README.md", text="AgentFlow metrics", score=0.9),
        RetrievedContext(source_id="unrelated.md", text="Other content", score=0.2),
    ]

    assert retrieval_precision_at_k(results, {"README.md"}, 2) == 0.5
