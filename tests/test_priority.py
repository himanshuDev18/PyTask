from priority import Priority


def test_priority_values():
    assert Priority.LOW.value == "low"
    assert Priority.MEDIUM.value == "medium"
    assert Priority.HIGH.value == "high"


def test_priority_from_string():
    assert Priority("low") == Priority.LOW
    assert Priority("medium") == Priority.MEDIUM
    assert Priority("high") == Priority.HIGH