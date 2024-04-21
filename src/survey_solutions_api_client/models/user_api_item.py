import datetime
from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserApiItem")


@_attrs_define
class UserApiItem:
    """
    Attributes:
        is_locked (bool):
        creation_date (datetime.datetime):
        user_id (str):
        user_name (str):
        email (Union[None, Unset, str]):
        device_id (Union[None, Unset, str]):
    """

    is_locked: bool
    creation_date: datetime.datetime
    user_id: str
    user_name: str
    email: Union[None, Unset, str] = UNSET
    device_id: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        is_locked = self.is_locked

        creation_date = self.creation_date.isoformat()

        user_id = self.user_id

        user_name = self.user_name

        email: Union[None, Unset, str]
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        device_id: Union[None, Unset, str]
        if isinstance(self.device_id, Unset):
            device_id = UNSET
        else:
            device_id = self.device_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "IsLocked": is_locked,
                "CreationDate": creation_date,
                "UserId": user_id,
                "UserName": user_name,
            }
        )
        if email is not UNSET:
            field_dict["Email"] = email
        if device_id is not UNSET:
            field_dict["DeviceId"] = device_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        is_locked = d.pop("IsLocked")

        creation_date = isoparse(d.pop("CreationDate"))

        user_id = d.pop("UserId")

        user_name = d.pop("UserName")

        def _parse_email(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        email = _parse_email(d.pop("Email", UNSET))

        def _parse_device_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        device_id = _parse_device_id(d.pop("DeviceId", UNSET))

        user_api_item = cls(
            is_locked=is_locked,
            creation_date=creation_date,
            user_id=user_id,
            user_name=user_name,
            email=email,
            device_id=device_id,
        )

        return user_api_item
