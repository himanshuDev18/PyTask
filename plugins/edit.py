from storage import load_tasks, save_tasks
from exceptions import TaskError,InvalidTaskNumberError

NAME = "edit"
DESCRIPTION = "Edit a task"


def execute(arguments):
    if len(arguments) < 2:
        raise TaskError("Usage: python main.py edit <task_number> <new_title>")

    try:
        index = int(arguments[0]) - 1
    except ValueError:
        raise ValueError("Task number must be an integer.")

    tasks = load_tasks()

    if index < 0 or index >= len(tasks):
        raise InvalidTaskNumberError("Invalid task number.")

    new_title = " ".join(arguments[1:]).strip()

    if not new_title:
        raise TaskError("Task title cannot be empty.")

    tasks[index].rename(new_title)

    save_tasks(tasks)

    print("Task updated successfully.")