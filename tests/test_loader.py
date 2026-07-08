from app.ingestion.loader import load_curriculum_documents


def test_load_curriculum_documents(tmp_path):
    curriculum_file = tmp_path / "sample_lesson.md"
    curriculum_file.write_text(
        "Subject: Mathematics\nGrade: 4\nLesson: Equivalent Fractions",
        encoding="utf-8",
    )

    documents = load_curriculum_documents(str(tmp_path))

    assert len(documents) == 1
    assert documents[0][0] == "sample_lesson.md"
    assert "Equivalent Fractions" in documents[0][1]


def test_load_curriculum_documents_missing_folder():
    documents = load_curriculum_documents("missing_folder")

    assert documents == []