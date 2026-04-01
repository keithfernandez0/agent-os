from enum import Enum, auto

class TaskState(Enum):
    QUEUED = auto()
    RUNNING = auto()
    COMPLETED = auto()
    FAILED = auto()
    CANCELLED = auto()

    def __str__(self):
        return self.name
