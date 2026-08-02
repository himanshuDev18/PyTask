from datetime import datetime
from storage import load_tasks

NAME = "overdue"
DESCRIPTION = "List overdue tasks"


def execute(arguments):

    tasks= load_tasks()

    today=datetime.today()

    found=False
    for task in tasks:
        if task.due_date is None:
            continue

        due=datetime.strptime(task.due_date, "%Y-%m-%d")

        if not task.completed and due<today:
            print(f"{task} due({task.due_date})")
            found =True

    if not found:
        print("No Overdeu") 
        

    


