from storage import get_all_tasks

NAME = "list"
DESCRIPTION = "Display all tasks"


def execute(arguments):
    tasks = get_all_tasks()

    if not tasks:
        print("No tasks found.")
        return

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

    