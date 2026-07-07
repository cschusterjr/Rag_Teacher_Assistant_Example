from app.chunking import chunk_text


def test_chunk_text_creates_chunks():
    text = "a" * 1500

    chunks = chunk_text(text, chunk_size=700, overlap=100)

    assert len(chunks) == 3


def test_chunk_text_rejects_invalid_overlap():
    try:
        chunk_text("sample text", chunk_size=100, overlap=100)
    except ValueError as error:
        assert "chunk_size must be greater than overlap" in str(error)
    else:
        raise AssertionError("Expected ValueError")