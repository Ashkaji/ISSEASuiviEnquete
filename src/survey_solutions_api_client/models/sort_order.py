from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.order_direction import OrderDirection
from ..types import UNSET, Unset

T = TypeVar("T", bound="SortOrder")


@_attrs_define
class SortOrder:
    """
    Attributes:
        column (Union[Unset, int]):
        dir_ (Union[Unset, OrderDirection]):
        name (Union[None, Unset, str]):
    """

    column: Union[Unset, int] = UNSET
    dir_: Union[Unset, OrderDirection] = UNSET
    name: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        column = self.column

        dir_: Union[Unset, str] = UNSET
        if not isinstance(self.dir_, Unset):
            dir_ = self.dir_.value

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if column is not UNSET:
            field_dict["Column"] = column
        if dir_ is not UNSET:
            field_dict["Dir"] = dir_
        if name is not UNSET:
            field_dict["Name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        column = d.pop("Column", UNSET)

        _dir_ = d.pop("Dir", UNSET)
        dir_: Union[Unset, OrderDirection]
        if isinstance(_dir_, Unset):
            dir_ = UNSET
        else:
            dir_ = OrderDirection(_dir_)

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("Name", UNSET))

        sort_order = cls(
            column=column,
            dir_=dir_,
            name=name,
        )

        return sort_order
