from backend.app.schemas import AgentRole


ROLE_DESCRIPTIONS: dict[AgentRole, str] = {
    AgentRole.PLANNER: "Breaks developer requests into structured subtasks.",
    AgentRole.RETRIEVER: "Collects project context through RAG.",
    AgentRole.CODER: "Drafts implementation steps or code-oriented actions.",
    AgentRole.DEBUGGER: "Analyzes failures and proposes fixes.",
    AgentRole.VALIDATOR: "Checks output against expected behavior.",
}


DEFAULT_AGENT_SEQUENCE: list[AgentRole] = [
    AgentRole.PLANNER,
    AgentRole.RETRIEVER,
    AgentRole.CODER,
    AgentRole.VALIDATOR,
]
