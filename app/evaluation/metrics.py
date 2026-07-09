from typing import Dict, List


def top_k_lesson_match(results: List[Dict], expected_lesson: str, k: int = 3) -> bool:
    top_results = results[:k]

    for result in top_results:
        metadata = result.get("metadata", {})
        lesson = metadata.get("lesson", "")

        if lesson == expected_lesson:
            return True

    return False


def top_1_lesson_match(results: List[Dict], expected_lesson: str) -> bool:
    return top_k_lesson_match(results, expected_lesson, k=1)