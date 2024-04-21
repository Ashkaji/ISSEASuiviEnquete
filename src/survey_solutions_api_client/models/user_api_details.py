import datetime
from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.user_roles import UserRoles
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserApiDetails")


@_attrs_define
class UserApiDetails:
    """
    Attributes:
        is_archived (bool):
        user_id (str):
        user_name (str):
        role (UserRoles):
        is_locked (bool):
        creation_date (datetime.datetime):
        email (Union[None, Unset, str]):
        phone_number (Union[None, Unset, str]):
        full_name (Union[None, Unset, str]):
    """

    is_archived: bool
    user_id: str
    user_name: str
    role: UserRoles
    is_locked: bool
    creation_date: datetime.datetime
    email: Union[None, Unset, str] = UNSET
    phone_number: Union[None, Unset, str] = UNSET
    full_name: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        is_archived = self.is_archived

        user_id = self.user_id

        user_name = self.user_name

        role = self.role.value

        is_locked = self.is_locked

        creation_date = self.creation_date.isoformat()

        email: Union[None, Unset, str]
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        phone_number: Union[None, Unset, str]
        if isinstance(self.phone_number, Unset):
            phone_number = UNSET
        else:
            phone_number = self.phone_number

        full_name: Union[None, Unset, str]
        if isinstance(self.full_name, Unset):
            full_name = UNSET
        else:
            full_name = self.full_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "IsArchived": is_archived,
                "UserId": user_id,
                "UserName": user_name,
                "Role": role,
                "IsLocked": is_locked,
                "CreationDate": creation_date,
            }
        )
        if email is not UNSET:
            field_dict["Email"] = email
        if phone_number is not UNSET:
            field_dict["PhoneNumber"] = phone_number
        if full_name is not UNSET:
            field_dict["FullName"] = full_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        is_archived = d.pop("IsArchived")

        user_id = d.pop("UserId")

        user_name = d.pop("UserName")

        role = UserRoles(d.pop("Role"))

        is_locked = d.pop("IsLocked")

        creation_date = isoparse(d.pop("CreationDate"))

        def _parse_email(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        email = _parse_email(d.pop("Email", UNSET))

        def _parse_phone_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        phone_number = _parse_phone_number(d.pop("PhoneNumber", UNSET))

        def _parse_full_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        full_name = _parse_full_name(d.pop("FullName", UNSET))

        user_api_details = cls(
            is_archived=is_archived,
            user_id=user_id,
            user_name=user_name,
            role=role,
            is_locked=is_locked,
            creation_date=creation_date,
            email=email,
            phone_number=phone_number,
            full_name=full_name,
        )

        return user_api_details
