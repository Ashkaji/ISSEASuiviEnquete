from enum import Enum


class ExportStatus(str, Enum):
    CANCELED = "Canceled"
    COMPLETED = "Completed"
    CREATED = "Created"
    FAIL = "Fail"
    RUNNING = "Running"

    def __str__(self) -> str:
        return str(self.value)
