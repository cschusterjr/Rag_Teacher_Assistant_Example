from typing import Dict, Iterator, List, Tuple


class SimpleStore:
    def __init__(self):
        self.chunks: List[Dict] = []

    def add_chunk(self, document_name: str, chunk_text: str, chunk_index: int) -> int:
        record = {
            "document_name": document_name,
            "chunk_text": chunk_text,
            "chunk_index": chunk_index,
        }

        self.chunks.append(record)
        return len(self.chunks) - 1

    def get(self, idx: int) -> Dict:
        return self.chunks[idx]

    def iter_chunks(self) -> Iterator[Tuple[int, str]]:
        for i, record in enumerate(self.chunks):
            yield i, record["chunk_text"]