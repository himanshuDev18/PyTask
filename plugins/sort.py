from storage import load_tasks,save_tasks
from exceptions import TaskError

NAME = "sort"
DESCRIPTION = "Sort tasks by title or completion status"

USAGE="Usage: python main.py sort <title|completed>"

def execute(arguments):

    if len(arguments) != 1:
        raise TaskError(USAGE)

    key=arguments[0].lower()

    tasks = load_tasks()
    
    if key=="title":
        tasks.sort(key=lambda task: task.title)

    elif key=="completed":
        tasks.sort(key=lambda task: task.completed, reverse=True)

    else:
        raise TaskError("Need key to Sort")

    save_tasks(tasks)
    print("Tasks sorted successfully.")







        


