from enum import Enum


class AssignWorkspacesMode(str, Enum):
    ADD = "Add"
    ASSIGN = "Assign"
    REMOVE = "Remove"

    def __str__(self) -> str:
        return str(self.value)
