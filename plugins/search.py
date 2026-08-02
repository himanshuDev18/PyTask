from storage import get_all_tasks
from exceptions import TaskError
import logging
logger = logging.getLogger(__name__)

NAME = "search"
DESCRIPTION = "Search tasks"


def execute(arguments):
    if not arguments:
        raise TaskError("Usage: python main.py search <keyword>")

    keyword = " ".join(arguments).strip().lower()

    tasks = get_all_tasks()

    found = False

    for index, task in enumerate(tasks, start=1):
        if keyword in task.title.lower():
            print(f"{index}. {task}")
            found = True

    logger.info("Task search performed: '%s'", keyword)

    if not found:
        print("No matching tasks found.")