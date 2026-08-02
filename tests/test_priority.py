import pytest
from priority import Priority


def test_valid_priority():
    priority = Priority("high")

    assert priority == Priority.HIGH


def test_invalid_priority():
    with pytest.raises(ValueError):
        Priority("hiefgh")

@pytest.mark.parametrize(
    "text, expected",
    [
        ("low", Priority.LOW),
        ("medium", Priority.MEDIUM),
        ("high", Priority.HIGH),
    ],
)
def test_priority(text, expected):
    assert Priority(text) == expected