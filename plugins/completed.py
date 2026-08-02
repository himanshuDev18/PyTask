from storage import get_all_tasks


NAME = "completed"
DESCRIPTION = "Display all completed tasks"


def execute(arguments):
    tasks = get_all_tasks()

    found = False

    for index, task in enumerate(tasks):
        if task.completed:
            print(f"{index + 1}. {task.title}")
            found = True

    if not found:
        print("No completed tasks.")