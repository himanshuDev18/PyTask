from storage import get_all_tasks, delete_task
from exceptions import InvalidTaskNumberError, TaskError
import logging
logger = logging.getLogger(__name__)

NAME = "remove"
DESCRIPTION = "Remove a task by its number"


def execute(arguments):
    if not arguments:
        raise TaskError("Usage: python main.py remove <task_number>")

    try:
        index = int(arguments[0]) - 1
    except ValueError:
        raise TaskError("Task number must be an integer.")

    tasks = get_all_tasks()

    if index < 0 or index >= len(tasks):
        raise InvalidTaskNumberError("Invalid task number.")

    removed_task = tasks[index]

    delete_task(removed_task.id)

    logger.info("Task removed: %s", removed_task.title)

    print(f"Task '{removed_task.title}' removed successfully.")