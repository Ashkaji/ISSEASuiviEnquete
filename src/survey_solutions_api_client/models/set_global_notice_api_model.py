from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SetGlobalNoticeApiModel")


@_attrs_define
class SetGlobalNoticeApiModel:
    """
    Attributes:
        message (str):
    """

    message: str

    def to_dict(self) -> Dict[str, Any]:
        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "Message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        message = d.pop("Message")

        set_global_notice_api_model = cls(
            message=message,
        )

        return set_global_notice_api_model
