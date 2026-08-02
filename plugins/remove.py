from storage import load_tasks,save_tasks
from exceptions import InvalidTaskNumberError,TaskError

NAME = "remove"
DESCRIPTION = "Remove a task by its number"


def execute(arguments):
    if not arguments:
        raise TaskError("Usage: python main.py remove <task_number>")

    try:
        index=int(arguments[0])-1

    except ValueError:
        raise ValueError("index must be int")

    else:
        tasks=load_tasks()

        if (index>= len(tasks) or index< 0):
            raise InvalidTaskNumberError("Invalid Task Number")

        else:
            removed_task=tasks.pop(index)

            save_tasks(tasks)

            print(f"Task '{removed_task.title}' is removed")




    
