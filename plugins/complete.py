from storage import load_tasks, save_tasks
from exceptions import TaskError,InvalidTaskNumberError

NAME = "complete"
DESCRIPTION = "Mark a task as completed"


def execute(arguments):
    if not arguments:
        raise TaskError("Usage: python main.py complete <task_number>")

    try:
        index = int(arguments[0]) - 1
    except ValueError:
        raise ValueError("Task number must be an integer.")

    tasks = load_tasks()

    if index < 0 or index >= len(tasks):
        raise InvalidTaskNumberError("Invalid task number.")

    if tasks[index].completed:
        raise TaskError("Task Already Completed")

    tasks[index].completed = True

    save_tasks(tasks)

    print(f"Task '{tasks[index].title}' marked as completed.")