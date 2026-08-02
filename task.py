from dataclasses import dataclass
from priority import Priority


@dataclass
class Task:
    title: str
    completed: bool = False
    due_date: str | None = None
    priority: Priority = Priority.MEDIUM

    def mark_completed(self) -> None:
        self.completed = True

    def mark_pending(self) -> None:
        self.completed = False

    def rename(self, new_title: str) -> None:
        self.title = new_title

    def __str__(self) -> str:
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.title} [{self.priority.value}]"

    def to_dict(self) -> dict[str, str | bool]:
        return {
            "title": self.title,
            "completed": self.completed,
            "due_date": self.due_date,
            "priority": self.priority.value,
        }

    @classmethod
    def from_dict(cls, data: dict[str, str | bool]) -> "Task":
        return cls(
            title=data["title"],
            completed=data["completed"],
            due_date=data.get("due_date"),
            priority=Priority(data.get("priority") or "medium"),
        )