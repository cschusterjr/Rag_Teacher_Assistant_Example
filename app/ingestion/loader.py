from pathlib import Path
from typing import List, Tuple


def load_curriculum_documents(directory: str) -> List[Tuple[str, str]]:
    path = Path(directory)

    if not path.exists():
        return []

    documents = []

    for file_path in path.glob("*.md"):
        text = file_path.read_text(encoding="utf-8")
        documents.append((file_path.name, text))

    return documents