from dataclasses import dataclass


@dataclass(frozen=True)
class DocumentChunk:
    source_id: str
    text: str
    citation: str
    start_index: int
    end_index: int


def chunk_text(source_id: str, text: str, citation: str, chunk_size: int = 120) -> list[DocumentChunk]:
    words = text.split()
    chunks: list[DocumentChunk] = []

    for start in range(0, len(words), chunk_size):
        end = min(start + chunk_size, len(words))
        chunk_words = words[start:end]
        if not chunk_words:
            continue
        chunks.append(
            DocumentChunk(
                source_id=source_id,
                text=" ".join(chunk_words),
                citation=citation,
                start_index=start,
                end_index=end,
            )
        )

    return chunks
