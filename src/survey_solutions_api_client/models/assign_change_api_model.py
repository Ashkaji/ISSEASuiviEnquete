from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AssignChangeApiModel")


@_attrs_define
class AssignChangeApiModel:
    """Provide either responsible id or responsible name

    Attributes:
        responsible_id (Union[None, Unset, str]): New responsible id
        responsible_name (Union[None, Unset, str]): New responsible name
    """

    responsible_id: Union[None, Unset, str] = UNSET
    responsible_name: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        responsible_id: Union[None, Unset, str]
        if isinstance(self.responsible_id, Unset):
            responsible_id = UNSET
        else:
            responsible_id = self.responsible_id

        responsible_name: Union[None, Unset, str]
        if isinstance(self.responsible_name, Unset):
            responsible_name = UNSET
        else:
            responsible_name = self.responsible_name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if responsible_id is not UNSET:
            field_dict["ResponsibleId"] = responsible_id
        if responsible_name is not UNSET:
            field_dict["ResponsibleName"] = responsible_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_responsible_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        responsible_id = _parse_responsible_id(d.pop("ResponsibleId", UNSET))

        def _parse_responsible_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        responsible_name = _parse_responsible_name(d.pop("ResponsibleName", UNSET))

        assign_change_api_model = cls(
            responsible_id=responsible_id,
            responsible_name=responsible_name,
        )

        return assign_change_api_model
