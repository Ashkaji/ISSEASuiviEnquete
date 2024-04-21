from enum import Enum


class Roles(str, Enum):
    APIUSER = "ApiUser"
    HEADQUARTER = "Headquarter"
    INTERVIEWER = "Interviewer"
    OBSERVER = "Observer"
    SUPERVISOR = "Supervisor"

    def __str__(self) -> str:
        return str(self.value)
