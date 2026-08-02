from storage import add_task, get_all_tasks, update_task, delete_task
from task import Task
from priority import Priority


def test_storage_crud():
    # Create
    task = Task(
        title="pytest_task",
        priority=Priority.HIGH,
    )

    add_task(task)

    tasks = get_all_tasks()

    added = next(t for t in tasks if t.title == "pytest_task")

    assert added.priority == Priority.HIGH
    assert not added.completed

    # Update
    added.mark_completed()
    update_task(added)

    tasks = get_all_tasks()

    updated = next(t for t in tasks if t.id == added.id)

    assert updated.completed

    # Delete
    delete_task(updated.id)

    tasks = get_all_tasks()

    assert all(t.id != updated.id for t in tasks)