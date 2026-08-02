from storage import get_all_tasks
from exceptions import TaskError
import logging
logger = logging.getLogger(__name__)

NAME = "sort"
DESCRIPTION = "Sort tasks by title or completion status"

USAGE = "Usage: python main.py sort <title|completed>"


def execute(arguments):
    if len(arguments) != 1:
        raise TaskError(USAGE)

    key = arguments[0].lower()

    tasks = get_all_tasks()

    if key == "title":
        tasks.sort(key=lambda task: task.title.lower())

    elif key == "completed":
        tasks.sort(key=lambda task: task.completed, reverse=True)

    else:
        raise TaskError("Sort key must be 'title' or 'completed'.")

    logger.info("Tasks sorted by %s", key)

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")
