from backend.app.schemas import RetrievedContext, ToolCall


def tool_call_success_rate(tool_calls: list[ToolCall]) -> float:
    if not tool_calls:
        return 0.0
    return sum(1 for call in tool_calls if call.success) / len(tool_calls)


def average_latency_ms(tool_calls: list[ToolCall]) -> float | None:
    latencies = [call.latency_ms for call in tool_calls if call.latency_ms is not None]
    if not latencies:
        return None
    return sum(latencies) / len(latencies)


def retrieval_precision_at_k(results: list[RetrievedContext], relevant_source_ids: set[str], k: int) -> float:
    if k <= 0:
        return 0.0
    top_results = results[:k]
    if not top_results:
        return 0.0
    hits = sum(1 for result in top_results if result.source_id in relevant_source_ids)
    return hits / len(top_results)


def summarize_tool_calls(tool_calls: list[ToolCall]) -> dict[str, float | None]:
    return {
        "success_rate": tool_call_success_rate(tool_calls),
        "average_latency_ms": average_latency_ms(tool_calls),
    }
