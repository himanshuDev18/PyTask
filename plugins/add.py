from storage import load_tasks,save_tasks
from task import Task
from exceptions import TaskError
from datetime import datetime
from priority import Priority
import argparse
from logger import logger



NAME = "add"
DESCRIPTION = "Add a new task"

def execute(arguments):

    parser = argparse.ArgumentParser()

    parser.add_argument("title", nargs="+")
    parser.add_argument("--due")
    parser.add_argument(
        "--priority",
        choices=["low", "medium", "high"],
        default="medium",
    )

    args = parser.parse_args(arguments)

    title = " ".join(args.title)

    if args.due:
        try:
            datetime.strptime(args.due, "%Y-%m-%d")
        except ValueError:
            raise TaskError("Invalid date format. Use YYYY-MM-DD")
        
    tasks=load_tasks()

    for saved_task in tasks:
        if saved_task.title == title:
            raise TaskError("Task exits Already")

    priority = Priority(args.priority)

    task = Task(
        title=title,
        completed=False,
        due_date=args.due,
        priority=priority,
    )

    tasks.append(task)
    save_tasks(tasks)
    logger.info("Task Added")
            

        


    

   