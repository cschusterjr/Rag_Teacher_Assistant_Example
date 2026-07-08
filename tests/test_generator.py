from app.generation.generator import generate_answer


def test_generate_answer_with_results():
    results = [
        {
            "score": 0.75,
            "content": "Students should compare fractions using visual models.",
        }
    ]

    answer = generate_answer("How should students compare fractions?", results)

    assert "Students should compare fractions" in answer


def test_generate_answer_without_results():
    answer = generate_answer("What is the lesson objective?", [])

    assert "could not find enough information" in answer