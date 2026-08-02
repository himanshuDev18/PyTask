from storage import load_tasks

NAME = "stats"
DESCRIPTION = "Display task statistics"


def execute(arguments):
    tasks = load_tasks()

    total = len(tasks)
    completed = sum(task.completed for task in tasks)
    pending = total - completed

    print(f"Total Tasks     : {total}")
    print(f"Completed Tasks : {completed}")
    print(f"Pending Tasks   : {pending}")