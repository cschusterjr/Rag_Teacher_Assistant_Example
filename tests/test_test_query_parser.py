from app.retrieval.query_parser import parse_query


def test_parse_grade_and_subject():
    filters = parse_query(
        "Show me Grade 4 math lessons."
    )

    assert filters["grade"] == "4"
    assert filters["subject"] == "Mathematics"


def test_parse_science():
    filters = parse_query(
        "Find Grade 6 science lessons."
    )

    assert filters["grade"] == "6"
    assert filters["subject"] == "Science"


def test_parse_without_filters():
    filters = parse_query(
        "How do I teach fractions?"
    )

    assert filters == {}