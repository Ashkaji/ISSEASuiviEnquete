from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExportJobLinks")


@_attrs_define
class ExportJobLinks:
    """
    Attributes:
        cancel (Union[None, Unset, str]): Link for cancelling export process
        download (Union[None, Unset, str]): Link for downloading file with data
    """

    cancel: Union[None, Unset, str] = UNSET
    download: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        cancel: Union[None, Unset, str]
        if isinstance(self.cancel, Unset):
            cancel = UNSET
        else:
            cancel = self.cancel

        download: Union[None, Unset, str]
        if isinstance(self.download, Unset):
            download = UNSET
        else:
            download = self.download

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if cancel is not UNSET:
            field_dict["Cancel"] = cancel
        if download is not UNSET:
            field_dict["Download"] = download

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_cancel(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cancel = _parse_cancel(d.pop("Cancel", UNSET))

        def _parse_download(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        download = _parse_download(d.pop("Download", UNSET))

        export_job_links = cls(
            cancel=cancel,
            download=download,
        )

        return export_job_links
