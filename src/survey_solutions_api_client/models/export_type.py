from enum import Enum


class ExportType(str, Enum):
    BINARY = "Binary"
    DDI = "DDI"
    PARADATA = "Paradata"
    SPSS = "SPSS"
    STATA = "STATA"
    TABULAR = "Tabular"

    def __str__(self) -> str:
        return str(self.value)
