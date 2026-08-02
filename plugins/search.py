from storage import load_tasks
from exceptions import TaskError

NAME = "search"
DESCRIPTION = "Search tasks"


def execute(arguments):
    if not arguments:
        raise TaskError("Usage: python main.py search <keyword>")

    keyword = " ".join(arguments).strip().lower()

    tasks = load_tasks()

    found = False

    for index, task in enumerate(tasks):
        if keyword in task.title.lower():
            found=True
            print(task)


    if not found:
        print("No matching tasks found.")