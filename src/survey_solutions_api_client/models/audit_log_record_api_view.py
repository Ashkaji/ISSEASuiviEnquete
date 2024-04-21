import datetime
from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuditLogRecordApiView")


@_attrs_define
class AuditLogRecordApiView:
    """
    Attributes:
        time (Union[Unset, datetime.datetime]):
        message (Union[None, Unset, str]):
    """

    time: Union[Unset, datetime.datetime] = UNSET
    message: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        time: Union[Unset, str] = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.isoformat()

        message: Union[None, Unset, str]
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if time is not UNSET:
            field_dict["Time"] = time
        if message is not UNSET:
            field_dict["Message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _time = d.pop("Time", UNSET)
        time: Union[Unset, datetime.datetime]
        if isinstance(_time, Unset):
            time = UNSET
        else:
            time = isoparse(_time)

        def _parse_message(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        message = _parse_message(d.pop("Message", UNSET))

        audit_log_record_api_view = cls(
            time=time,
            message=message,
        )

        return audit_log_record_api_view
