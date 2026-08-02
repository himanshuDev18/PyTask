import json
from task import Task


FILE_NAME = "tasks.json"


def load_tasks() -> list[Task]:

    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
            return [Task.from_dict(task) for task in data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []



def save_tasks(tasks: list[Task]) -> None:

    with open(FILE_NAME, "w") as file:
        json.dump(
            [task.to_dict() for task in tasks],
            file,
            indent=4
        )