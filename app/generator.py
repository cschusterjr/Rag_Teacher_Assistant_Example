from typing import Dict, List


def generate_answer(query: str, results: List[Dict]) -> str:
    if not results:
        return "I could not find enough information in the provided curriculum documents to answer that."

    top_result = results[0]

    if top_result["score"] <= 0:
        return "I could not find enough information in the provided curriculum documents to answer that."

    return (
        f"Based on the retrieved curriculum content, here is a grounded response to: "
        f"'{query}'\n\n"
        f"{top_result['content']}"
    )