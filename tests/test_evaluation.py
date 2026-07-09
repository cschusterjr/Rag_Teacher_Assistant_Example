from app.evaluation.metrics import top_1_lesson_match, top_k_lesson_match


def test_top_1_lesson_match_true():
    results = [
        {
            "metadata": {
                "lesson": "Equivalent Fractions",
            }
        }
    ]

    assert top_1_lesson_match(results, "Equivalent Fractions") is True


def test_top_1_lesson_match_false():
    results = [
        {
            "metadata": {
                "lesson": "Food Webs",
            }
        }
    ]

    assert top_1_lesson_match(results, "Equivalent Fractions") is False


def test_top_k_lesson_match_true():
    results = [
        {
            "metadata": {
                "lesson": "Food Webs",
            }
        },
        {
            "metadata": {
                "lesson": "Equivalent Fractions",
            }
        },
    ]

    assert top_k_lesson_match(results, "Equivalent Fractions", k=3) is True