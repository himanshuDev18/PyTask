from storage import get_all_tasks, update_task
from storage import get_all_tasks, update_task
from exceptions import TaskError, InvalidTaskNumberError
import logging
logger = logging.getLogger(__name__)

NAME = "complete"
DESCRIPTION = "Mark a task as completed"


def execute(arguments):
    if not arguments:
        raise TaskError("Usage: python main.py complete <task_number>")

    try:
        index = int(arguments[0]) - 1
    except ValueError:
        raise TaskError("Task number must be an integer.")

    tasks = get_all_tasks()

    if index < 0 or index >= len(tasks):
        raise InvalidTaskNumberError("Invalid task number.")

    task = tasks[index]

    if task.completed:
        raise TaskError("Task already completed.")

    task.mark_completed()

    update_task(task)

    logger.info("Task completed: %s", task.title)

    print(f"Task '{task.title}' marked as completed.")