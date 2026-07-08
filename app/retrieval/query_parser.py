from typing import Dict


def parse_query(query: str) -> Dict[str, str]:
    """
    Extract simple structured filters from a teacher question.
    """

    filters = {}

    query_lower = query.lower()

    # Grade detection
    for grade in ["4", "5", "6"]:
        if f"grade {grade}" in query_lower:
            filters["grade"] = grade

    # Subject detection
    subjects = {
        "math": "Mathematics",
        "mathematics": "Mathematics",
        "ela": "English Language Arts",
        "english": "English Language Arts",
        "science": "Science",
        "social studies": "Social Studies",
    }

    for keyword, subject in subjects.items():
        if keyword in query_lower:
            filters["subject"] = subject

    return filters