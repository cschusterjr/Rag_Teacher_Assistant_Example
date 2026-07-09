from app.retrieval.rag import RAGPipeline


def test_ingest_extracts_metadata():
    pipeline = RAGPipeline()

    document = """
Subject: Mathematics
Grade: 4
Unit: Fractions
Lesson: Equivalent Fractions
Estimated Time: 45 minutes

Students compare equivalent fractions using visual models.
"""

    pipeline.ingest(
        [
            (
                "grade4_math_equivalent_fractions.md",
                document,
            )
        ]
    )

    record = pipeline.store.get(0)

    assert record["metadata"]["subject"] == "Mathematics"
    assert record["metadata"]["grade"] == "4"
    assert record["metadata"]["lesson"] == "Equivalent Fractions"

def test_metadata_filtering_returns_correct_subject():
    pipeline = RAGPipeline()

    math_doc = """
Subject: Mathematics
Grade: 4
Unit: Fractions
Lesson: Equivalent Fractions

Students compare equivalent fractions using visual models.
"""

    science_doc = """
Subject: Science
Grade: 6
Unit: Ecosystems
Lesson: Food Webs

Students investigate how energy moves through food webs.
"""

    pipeline.ingest(
        [
            ("math.md", math_doc),
            ("science.md", science_doc),
        ]
    )

    results = pipeline.search(
        "Show me Grade 4 math lessons.",
        k=5,
    )

    assert len(results) > 0

    for result in results:
        assert result["metadata"]["grade"] == "4"
        assert result["metadata"]["subject"] == "Mathematics"