from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchInfo")


@_attrs_define
class SearchInfo:
    """
    Attributes:
        value (Union[None, Unset, str]):
        regex (Union[Unset, bool]):
    """

    value: Union[None, Unset, str] = UNSET
    regex: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        value: Union[None, Unset, str]
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        regex = self.regex

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if value is not UNSET:
            field_dict["Value"] = value
        if regex is not UNSET:
            field_dict["Regex"] = regex

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_value(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        value = _parse_value(d.pop("Value", UNSET))

        regex = d.pop("Regex", UNSET)

        search_info = cls(
            value=value,
            regex=regex,
        )

        return search_info
