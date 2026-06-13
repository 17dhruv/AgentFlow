from enum import Enum
from typing import Any, Literal

from pydantic import BaseModel, Field


class AgentRole(str, Enum):
    PLANNER = "planner"
    RETRIEVER = "retriever"
    CODER = "coder"
    DEBUGGER = "debugger"
    VALIDATOR = "validator"


class Task(BaseModel):
    id: str
    title: str
    prompt: str
    task_type: Literal["planning", "debugging", "code_generation", "rag_qa"]
    repository_path: str | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)


class RetrievedContext(BaseModel):
    source_id: str
    text: str
    score: float
    citation: str | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)


class ToolCall(BaseModel):
    name: str
    arguments: dict[str, Any] = Field(default_factory=dict)
    success: bool = False
    latency_ms: int | None = None
    output_summary: str | None = None


class WorkflowState(BaseModel):
    task_id: str
    active_role: AgentRole | None = None
    completed_roles: list[AgentRole] = Field(default_factory=list)
    retrieved_context: list[RetrievedContext] = Field(default_factory=list)
    tool_calls: list[ToolCall] = Field(default_factory=list)
    final_answer: str | None = None
    status: Literal["queued", "running", "completed", "failed"] = "queued"


class EvaluationResult(BaseModel):
    task_id: str
    task_completed: bool
    tool_call_success_rate: float
    retrieval_precision_at_k: float | None = None
    average_latency_ms: float | None = None
    faithfulness_score: float | None = None
    notes: str | None = None
