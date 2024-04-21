from enum import Enum


class ExternalStorageType(str, Enum):
    DROPBOX = "Dropbox"
    GOOGLEDRIVE = "GoogleDrive"
    ONEDRIVE = "OneDrive"

    def __str__(self) -> str:
        return str(self.value)
