class TaskError(Exception):
    """Base exception"""
    pass


class TaskNotFoundError(TaskError):
    pass


class InvalidTaskNumberError(TaskError):
    pass