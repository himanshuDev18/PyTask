from task import Task
from priority import Priority


def test_task_creation():
    task = Task("Study")

    assert task.title == "Study"
    assert task.completed is False
    assert task.due_date is None
    assert task.priority == Priority.MEDIUM


def test_mark_completed():
    task = Task("Study")

    task.mark_completed()

    assert task.completed is True


def test_mark_pending():
    task = Task("Study")

    task.mark_completed()
    task.mark_pending()

    assert task.completed is False


def test_rename():
    task = Task("Study")

    task.rename("Learn Python")

    assert task.title == "Learn Python"


def test_to_dict():
    task = Task(
        title="Study",
        completed=True,
        due_date="2026-08-05",
        priority=Priority.HIGH,
    )

    data = task.to_dict()

    assert data == {
        "title": "Study",
        "completed": True,
        "due_date": "2026-08-05",
        "priority": "high",
    }


def test_from_dict():
    data = {
        "title": "Study",
        "completed": False,
        "due_date": "2026-08-05",
        "priority": "high",
    }

    task = Task.from_dict(data)

    assert task.title == "Study"
    assert task.completed is False
    assert task.due_date == "2026-08-05"
    assert task.priority == Priority.HIGH