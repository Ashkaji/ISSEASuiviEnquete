import datetime
from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkspaceApiView")


@_attrs_define
class WorkspaceApiView:
    """
    Attributes:
        name (Union[None, Unset, str]):
        display_name (Union[None, Unset, str]):
        disabled_at_utc (Union[None, Unset, datetime.datetime]):
        created_at_utc (Union[None, Unset, datetime.datetime]):
    """

    name: Union[None, Unset, str] = UNSET
    display_name: Union[None, Unset, str] = UNSET
    disabled_at_utc: Union[None, Unset, datetime.datetime] = UNSET
    created_at_utc: Union[None, Unset, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        display_name: Union[None, Unset, str]
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        disabled_at_utc: Union[None, Unset, str]
        if isinstance(self.disabled_at_utc, Unset):
            disabled_at_utc = UNSET
        elif isinstance(self.disabled_at_utc, datetime.datetime):
            disabled_at_utc = self.disabled_at_utc.isoformat()
        else:
            disabled_at_utc = self.disabled_at_utc

        created_at_utc: Union[None, Unset, str]
        if isinstance(self.created_at_utc, Unset):
            created_at_utc = UNSET
        elif isinstance(self.created_at_utc, datetime.datetime):
            created_at_utc = self.created_at_utc.isoformat()
        else:
            created_at_utc = self.created_at_utc

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if display_name is not UNSET:
            field_dict["DisplayName"] = display_name
        if disabled_at_utc is not UNSET:
            field_dict["DisabledAtUtc"] = disabled_at_utc
        if created_at_utc is not UNSET:
            field_dict["CreatedAtUtc"] = created_at_utc

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("Name", UNSET))

        def _parse_display_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        display_name = _parse_display_name(d.pop("DisplayName", UNSET))

        def _parse_disabled_at_utc(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                disabled_at_utc_type_0 = isoparse(data)

                return disabled_at_utc_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        disabled_at_utc = _parse_disabled_at_utc(d.pop("DisabledAtUtc", UNSET))

        def _parse_created_at_utc(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_utc_type_0 = isoparse(data)

                return created_at_utc_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        created_at_utc = _parse_created_at_utc(d.pop("CreatedAtUtc", UNSET))

        workspace_api_view = cls(
            name=name,
            display_name=display_name,
            disabled_at_utc=disabled_at_utc,
            created_at_utc=created_at_utc,
        )

        return workspace_api_view
