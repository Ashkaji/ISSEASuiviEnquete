from enum import Enum


class AssignmentHistoryAction(str, Enum):
    ARCHIVED = "Archived"
    AUDIORECORDINGCHANGED = "AudioRecordingChanged"
    CREATED = "Created"
    DELETED = "Deleted"
    QUANTITYCHANGED = "QuantityChanged"
    REASSIGNED = "Reassigned"
    RECEIVEDBYTABLET = "ReceivedByTablet"
    UNARCHIVED = "UnArchived"
    UNKNOWN = "Unknown"
    WEBMODECHANGED = "WebModeChanged"

    def __str__(self) -> str:
        return str(self.value)
