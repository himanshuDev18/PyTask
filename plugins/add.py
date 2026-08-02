from storage import add_task, get_all_tasks
from task import Task
from exceptions import TaskError
from datetime import datetime
from priority import Priority
import argparse
import logging
logger = logging.getLogger(__name__)


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

    try:
        args = parser.parse_args(arguments)
    except SystemExit:
        raise TaskError("Invalid arguments. Use 'python main.py help' for usage.")

    title = " ".join(args.title).strip()

    if args.due:
        try:
            datetime.strptime(args.due, "%Y-%m-%d")
        except ValueError:
            raise TaskError("Invalid date format. Use YYYY-MM-DD")

    tasks = get_all_tasks()

    for saved_task in tasks:
        if saved_task.title.lower() == title.lower():
            raise TaskError("Task already exists.")

    task = Task(
        title=title,
        completed=False,
        due_date=args.due,
        priority=Priority(args.priority),
    )

    add_task(task)

    logger.info("Task Added: %s", task.title)

    print("Task added successfully.")
        


    

   