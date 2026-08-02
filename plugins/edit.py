from storage import get_all_tasks, update_task
from exceptions import TaskError, InvalidTaskNumberError
import logging
logger = logging.getLogger(__name__)

NAME = "edit"
DESCRIPTION = "Edit a task"


def execute(arguments):
    if len(arguments) < 2:
        raise TaskError("Usage: python main.py edit <task_number> <new_title>")

    try:
        index = int(arguments[0]) - 1
    except ValueError:
        raise TaskError("Task number must be an integer.")

    tasks = get_all_tasks()

    if index < 0 or index >= len(tasks):
        raise InvalidTaskNumberError("Invalid task number.")

    task = tasks[index]

    new_title = " ".join(arguments[1:]).strip()

    if not new_title:
        raise TaskError("Task title cannot be empty.")

    for existing_task in tasks:
        if (
            existing_task.id != task.id
            and existing_task.title.lower() == new_title.lower()
        ):
            raise TaskError("Task already exists.")

    old_title = task.title

    task.rename(new_title)

    update_task(task)

    logger.info("Task renamed: '%s' -> '%s'", old_title, new_title)

    print("Task updated successfully.")