from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.assign_workspaces_mode import AssignWorkspacesMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.assign_workspace_info import AssignWorkspaceInfo


T = TypeVar("T", bound="AssignWorkspacesToUserModel")


@_attrs_define
class AssignWorkspacesToUserModel:
    """
    Attributes:
        user_ids (List[str]):
        workspaces (List['AssignWorkspaceInfo']):
        mode (Union[Unset, AssignWorkspacesMode]): Assignment mode for workspaces
    """

    user_ids: List[str]
    workspaces: List["AssignWorkspaceInfo"]
    mode: Union[Unset, AssignWorkspacesMode] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        user_ids = self.user_ids

        workspaces = []
        for workspaces_item_data in self.workspaces:
            workspaces_item = workspaces_item_data.to_dict()
            workspaces.append(workspaces_item)

        mode: Union[Unset, str] = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "UserIds": user_ids,
                "Workspaces": workspaces,
            }
        )
        if mode is not UNSET:
            field_dict["Mode"] = mode

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.assign_workspace_info import AssignWorkspaceInfo

        d = src_dict.copy()
        user_ids = cast(List[str], d.pop("UserIds"))

        workspaces = []
        _workspaces = d.pop("Workspaces")
        for workspaces_item_data in _workspaces:
            workspaces_item = AssignWorkspaceInfo.from_dict(workspaces_item_data)

            workspaces.append(workspaces_item)

        _mode = d.pop("Mode", UNSET)
        mode: Union[Unset, AssignWorkspacesMode]
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = AssignWorkspacesMode(_mode)

        assign_workspaces_to_user_model = cls(
            user_ids=user_ids,
            workspaces=workspaces,
            mode=mode,
        )

        return assign_workspaces_to_user_model
