from storage import get_all_tasks

NAME = "pending"
DESCRIPTION = "Display all pending tasks"


def execute(arguments):
    tasks = get_all_tasks()

    found = False

    for index, task in enumerate(tasks, start=1):
        if not task.completed:
            print(f"{index}. {task}")
            found = True

    if not found:
        print("No pending tasks.")