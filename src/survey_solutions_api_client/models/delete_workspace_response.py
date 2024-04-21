from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteWorkspaceResponse")


@_attrs_define
class DeleteWorkspaceResponse:
    """
    Attributes:
        success (Union[Unset, bool]):
        error_message (Union[None, Unset, str]):
    """

    success: Union[Unset, bool] = UNSET
    error_message: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        success = self.success

        error_message: Union[None, Unset, str]
        if isinstance(self.error_message, Unset):
            error_message = UNSET
        else:
            error_message = self.error_message

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if success is not UNSET:
            field_dict["Success"] = success
        if error_message is not UNSET:
            field_dict["ErrorMessage"] = error_message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        success = d.pop("Success", UNSET)

        def _parse_error_message(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        error_message = _parse_error_message(d.pop("ErrorMessage", UNSET))

        delete_workspace_response = cls(
            success=success,
            error_message=error_message,
        )

        return delete_workspace_response
