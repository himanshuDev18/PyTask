from storage import load_tasks

NAME = "pending"
DESCRIPTION = "Display all pending tasks"


def execute(arguments):
    tasks = load_tasks()

    found = False

    for index, task in enumerate(tasks):
        if not task.completed:
            print(f"{index + 1}. {task.title}")
            found = True

    if not found:
        print("No pending tasks.")