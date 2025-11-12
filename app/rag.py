from typing import List, Tuple, Dict
from .store import SimpleStore
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class RAGPipeline:
    def __init__(self):
        self.store = SimpleStore()
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self._matrix = None
        self._ids = []

    def ingest(self, docs: List[Tuple[str, str]]):
        for name, text in docs:
            self.store.add(name, text)
        corpus = [t for _, t in self.store.iter_docs()]
        if corpus:
            self._matrix = self.vectorizer.fit_transform(corpus)
            self._ids = [i for i, _ in self.store.iter_docs()]

    def search(self, query: str, k: int = 3):
        if self._matrix is None:
            return []
        qv = self.vectorizer.transform([query])
        sims = cosine_similarity(qv, self._matrix).ravel()
        idx = np.argsort(-sims)[:k]
        results = []
        for i in idx:
            doc_id = self._ids[i]
            name, text = self.store.get(doc_id)
            results.append({"doc_id": doc_id, "name": name, "score": float(sims[i]), "snippet": text[:300]})
        return results
