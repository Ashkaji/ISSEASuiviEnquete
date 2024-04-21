from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="GlobalNoticeApiView")


@_attrs_define
class GlobalNoticeApiView:
    """
    Attributes:
        message (Union[None, Unset, str]): Current global notice
    """

    message: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        message: Union[None, Unset, str]
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if message is not UNSET:
            field_dict["Message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_message(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        message = _parse_message(d.pop("Message", UNSET))

        global_notice_api_view = cls(
            message=message,
        )

        return global_notice_api_view
