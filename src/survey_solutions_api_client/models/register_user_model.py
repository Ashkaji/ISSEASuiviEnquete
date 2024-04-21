from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.roles import Roles
from ..types import UNSET, Unset

T = TypeVar("T", bound="RegisterUserModel")


@_attrs_define
class RegisterUserModel:
    """
    Attributes:
        role (Roles): User role
        user_name (str):
        password (str):
        full_name (Union[None, Unset, str]):
        phone_number (Union[None, Unset, str]):
        email (Union[None, Unset, str]):
        supervisor (Union[None, Unset, str]):
    """

    role: Roles
    user_name: str
    password: str
    full_name: Union[None, Unset, str] = UNSET
    phone_number: Union[None, Unset, str] = UNSET
    email: Union[None, Unset, str] = UNSET
    supervisor: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        role = self.role.value

        user_name = self.user_name

        password = self.password

        full_name: Union[None, Unset, str]
        if isinstance(self.full_name, Unset):
            full_name = UNSET
        else:
            full_name = self.full_name

        phone_number: Union[None, Unset, str]
        if isinstance(self.phone_number, Unset):
            phone_number = UNSET
        else:
            phone_number = self.phone_number

        email: Union[None, Unset, str]
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        supervisor: Union[None, Unset, str]
        if isinstance(self.supervisor, Unset):
            supervisor = UNSET
        else:
            supervisor = self.supervisor

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "Role": role,
                "UserName": user_name,
                "Password": password,
            }
        )
        if full_name is not UNSET:
            field_dict["FullName"] = full_name
        if phone_number is not UNSET:
            field_dict["PhoneNumber"] = phone_number
        if email is not UNSET:
            field_dict["Email"] = email
        if supervisor is not UNSET:
            field_dict["Supervisor"] = supervisor

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        role = Roles(d.pop("Role"))

        user_name = d.pop("UserName")

        password = d.pop("Password")

        def _parse_full_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        full_name = _parse_full_name(d.pop("FullName", UNSET))

        def _parse_phone_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        phone_number = _parse_phone_number(d.pop("PhoneNumber", UNSET))

        def _parse_email(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        email = _parse_email(d.pop("Email", UNSET))

        def _parse_supervisor(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        supervisor = _parse_supervisor(d.pop("Supervisor", UNSET))

        register_user_model = cls(
            role=role,
            user_name=user_name,
            password=password,
            full_name=full_name,
            phone_number=phone_number,
            email=email,
            supervisor=supervisor,
        )

        return register_user_model
