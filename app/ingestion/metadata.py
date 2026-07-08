from typing import Dict


def extract_metadata(text: str) -> Dict[str, str]:
    metadata = {}

    field_map = {
        "Subject": "subject",
        "Grade": "grade",
        "Unit": "unit",
        "Lesson": "lesson",
        "Estimated Time": "estimated_time",
    }

    for line in text.splitlines():
        line = line.strip()

        for label, key in field_map.items():
            prefix = f"{label}:"

            if line.startswith(prefix):
                metadata[key] = line.replace(prefix, "", 1).strip()

    return metadata