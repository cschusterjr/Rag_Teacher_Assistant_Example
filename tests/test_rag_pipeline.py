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