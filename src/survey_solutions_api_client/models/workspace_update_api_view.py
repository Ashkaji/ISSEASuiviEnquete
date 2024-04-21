from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="WorkspaceUpdateApiView")


@_attrs_define
class WorkspaceUpdateApiView:
    """
    Attributes:
        display_name (str):
    """

    display_name: str

    def to_dict(self) -> Dict[str, Any]:
        display_name = self.display_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "DisplayName": display_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        display_name = d.pop("DisplayName")

        workspace_update_api_view = cls(
            display_name=display_name,
        )

        return workspace_update_api_view
