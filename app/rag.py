from typing import Dict, List, Tuple

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from .chunking import chunk_text
from .store import SimpleStore


class RAGPipeline:
    def __init__(self):
        self.store = SimpleStore()
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self._matrix = None
        self._ids = []

    def ingest(self, docs: List[Tuple[str, str]]):
        for name, text in docs:
            chunks = chunk_text(text)

            for chunk_index, chunk in enumerate(chunks):
                self.store.add_chunk(
                    document_name=name,
                    chunk_text=chunk,
                    chunk_index=chunk_index,
                )

        corpus = [text for _, text in self.store.iter_chunks()]

        if corpus:
            self._matrix = self.vectorizer.fit_transform(corpus)
            self._ids = [chunk_id for chunk_id, _ in self.store.iter_chunks()]

    def search(self, query: str, k: int = 3) -> List[Dict]:
        if self._matrix is None:
            return []

        query_vector = self.vectorizer.transform([query])
        similarities = cosine_similarity(query_vector, self._matrix).ravel()
        ranked_indexes = np.argsort(-similarities)[:k]

        results = []

        for index in ranked_indexes:
            chunk_id = self._ids[index]
            record = self.store.get(chunk_id)

            results.append(
        {
            "chunk_id": chunk_id,
            "source": record["document_name"],
            "chunk_index": record["chunk_index"],
            "score": float(similarities[index]),
            "content": record["chunk_text"],
        }
    )

        return results