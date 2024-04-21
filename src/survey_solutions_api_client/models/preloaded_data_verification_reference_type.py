from enum import Enum


class PreloadedDataVerificationReferenceType(str, Enum):
    CELL = "Cell"
    COLUMN = "Column"
    FILE = "File"
    ROW = "Row"

    def __str__(self) -> str:
        return str(self.value)
