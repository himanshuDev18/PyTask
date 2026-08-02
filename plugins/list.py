from storage import load_tasks

NAME = "list"
DESCRIPTION = "Display all tasks"


def execute(arguments):
        
        tasks=load_tasks()

        for index,task in enumerate(tasks):
                print(task)

     


    