from backend.app.schemas import RetrievedContext
from rag.ingestion import DocumentChunk


def keyword_retrieve(query: str, chunks: list[DocumentChunk], top_k: int = 5) -> list[RetrievedContext]:
    query_terms = {term.lower() for term in query.split()}
    scored: list[tuple[float, DocumentChunk]] = []

    for chunk in chunks:
        chunk_terms = {term.lower().strip(".,:;()[]{}") for term in chunk.text.split()}
        if not query_terms:
            score = 0.0
        else:
            score = len(query_terms & chunk_terms) / len(query_terms)
        scored.append((score, chunk))

    scored.sort(key=lambda item: item[0], reverse=True)
    return [
        RetrievedContext(
            source_id=chunk.source_id,
            text=chunk.text,
            score=score,
            citation=chunk.citation,
            metadata={"retriever": "keyword_baseline"},
        )
        for score, chunk in scored[:top_k]
    ]
