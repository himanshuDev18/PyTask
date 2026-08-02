# PyTask

A Python command-line task manager built to help users organize tasks with priorities, due dates, SQLite storage, logging, and automated testing.

## Features

- Add, edit, and remove tasks
- Mark tasks as completed or pending
- Search tasks
- Sort tasks
- View task statistics
- Support for due dates
- Priority levels (Low, Medium, High)
- SQLite database storage
- Plugin-based architecture
- Logging
- Automated tests using pytest

## Installation

Clone the repository

```bash
git clone https://github.com/himanshuDev18/PyTask.git
```

Navigate to the project directory

```bash
cd PyTask
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the virtual environment

### Windows

```bash
.venv\Scripts\activate
```

Install the required dependencies

```bash
pip install -r requirements.txt
```


## Usage

Display all available commands

```bash
python main.py help
```

Add a task

```bash
python main.py add "Learn Python"
```

Add a task with priority

```bash
python main.py add "Learn SQLite" --priority high
```

Add a task with a due date

```bash
python main.py add "Complete Project" --due 2026-08-15
```

List all tasks

```bash
python main.py list
```

Mark a task as completed

```bash
python main.py complete 1
```

Remove a task

```bash
python main.py remove 1
```

Run the test suite

```bash
pytest
```

## Technologies Used

- Python 3
- SQLite
- argparse
- Dataclasses
- Enum
- Logging
- Pytest
- Git
- GitHub


## Project Structure

```text
PyTask/
│
├── plugins/          # CLI command plugins
├── tests/            # Unit tests
├── database.py       # Database initialization
├── storage.py        # Database CRUD operations
├── task.py           # Task model
├── priority.py       # Priority enum
├── logger.py         # Logging configuration
├── exceptions.py     # Custom exceptions
├── main.py           # Application entry point
├── requirements.txt
└── README.md
```


## Future Improvements

- Add task categories
- Add task tags
- Export tasks to CSV
- Add recurring tasks
- Improve search functionality
- Build a REST API using FastAPI
- Add user authentication

---

## License

This project is licensed under the MIT License.