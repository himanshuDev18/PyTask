from storage import get_all_tasks

NAME = "stats"
DESCRIPTION = "Display task statistics"


def execute(arguments):
    tasks = get_all_tasks()

    total = len(tasks)
    completed = sum(task.completed for task in tasks)
    pending = total - completed

    overdue = sum(
    not task.completed and task.due_date is not None
    for task in tasks
    )

    high_priority = sum(
        task.priority.value == "high"
        for task in tasks
    )

    print(f"Total Tasks     : {total}")
    print(f"Completed Tasks : {completed}")
    print(f"Pending Tasks   : {pending}")
    print(f"Overdue Tasks   : {overdue}")
    print(f"High Priority   : {high_priority}")