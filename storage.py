from database import get_connection
from task import Task
from priority import Priority


def add_task(task: Task) -> None:
    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO tasks(title, completed, due_date, priority)
            VALUES (?, ?, ?, ?)
            """,
            (
                task.title,
                task.completed,
                task.due_date,
                task.priority.value,
            ),
        )


def get_all_tasks() -> list[Task]:
    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT id, title, completed, due_date, priority
            FROM tasks
            """
        )

        rows = cursor.fetchall()

    return [
        Task(
            id=row[0],
            title=row[1],
            completed=bool(row[2]),
            due_date=row[3],
            priority=Priority(row[4]),
        )
        for row in rows
    ]


def update_task(task: Task) -> None:
    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE tasks
            SET title = ?, completed = ?, due_date = ?, priority = ?
            WHERE id = ?
            """,
            (
                task.title,
                task.completed,
                task.due_date,
                task.priority.value,
                task.id,
            ),
        )


def delete_task(task_id: int) -> None:
    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute(
            """
            DELETE FROM tasks
            WHERE id = ?
            """,
            (task_id,),
        )