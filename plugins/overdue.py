from datetime import datetime
from storage import get_all_tasks

NAME = "overdue"
DESCRIPTION = "List overdue tasks"


def execute(arguments):
    tasks = get_all_tasks()

    today = datetime.today().date()
    found = False

    for index, task in enumerate(tasks, start=1):
        if task.due_date is None:
            continue

        due = datetime.strptime(task.due_date, "%Y-%m-%d").date()

        if not task.completed and due < today:
            print(f"{index}. {task} (Due: {task.due_date})")
            found = True

    if not found:
        print("No overdue tasks.")

