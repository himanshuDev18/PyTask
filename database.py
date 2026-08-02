import sqlite3

DATABASE_NAME = "tasks.db"


def get_connection() -> sqlite3.Connection:
    return sqlite3.connect(DATABASE_NAME)


def initialize_database() -> None:
    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                completed INTEGER NOT NULL,
                due_date TEXT,
                priority TEXT NOT NULL
            )
            """
        )