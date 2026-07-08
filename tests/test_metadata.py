from app.ingestion.metadata import extract_metadata

def test_extract_metadata():
    text = """
    Subject: Mathematics
    Grade: 4
    Unit: Fractions
    Lesson: Equivalent Fractions
    Estimated Time: 45 minutes
    """

    metadata = extract_metadata(text)

    assert metadata["subject"] == "Mathematics"
    assert metadata["grade"] == "4"
    assert metadata["unit"] == "Fractions"
    assert metadata["lesson"] == "Equivalent Fractions"
    assert metadata["estimated_time"] == "45 minutes"