from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="WorkspaceCreateApiView")


@_attrs_define
class WorkspaceCreateApiView:
    """
    Attributes:
        name (str):
        display_name (str):
    """

    name: str
    display_name: str

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        display_name = self.display_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "Name": name,
                "DisplayName": display_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("Name")

        display_name = d.pop("DisplayName")

        workspace_create_api_view = cls(
            name=name,
            display_name=display_name,
        )

        return workspace_create_api_view
