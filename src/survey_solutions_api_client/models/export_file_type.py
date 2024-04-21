from enum import Enum


class ExportFileType(str, Enum):
    CSV = "Csv"
    EXCEL = "Excel"
    TAB = "Tab"

    def __str__(self) -> str:
        return str(self.value)
