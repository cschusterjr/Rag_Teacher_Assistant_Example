from typing import List


def chunk_text(text: str, chunk_size: int = 700, overlap: int = 100) -> List[str]:
    """
    Split text into overlapping chunks for retrieval.

    Args:
        text: Source document text.
        chunk_size: Maximum number of characters per chunk.
        overlap: Number of characters repeated between chunks.

    Returns:
        A list of text chunks.
    """
    if chunk_size <= overlap:
        raise ValueError("chunk_size must be greater than overlap.")

    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        start += chunk_size - overlap

    return chunks