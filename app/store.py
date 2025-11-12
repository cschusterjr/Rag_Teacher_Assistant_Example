from typing import Tuple, Iterator, List

class SimpleStore:
    def __init__(self):
        self.docs: List[Tuple[str,str]] = []  # (name, text)

    def add(self, name: str, text: str) -> int:
        self.docs.append((name, text))
        return len(self.docs) - 1

    def get(self, idx: int) -> Tuple[str, str]:
        return self.docs[idx]

    def iter_docs(self) -> Iterator[Tuple[int, str]]:
        for i, (name, text) in enumerate(self.docs):
            yield (i, text)
