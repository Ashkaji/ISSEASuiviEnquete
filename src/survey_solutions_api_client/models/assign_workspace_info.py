from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AssignWorkspaceInfo")


@_attrs_define
class AssignWorkspaceInfo:
    """
    Attributes:
        workspace (str):
        supervisor_id (Union[None, Unset, str]):
    """

    workspace: str
    supervisor_id: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        workspace = self.workspace

        supervisor_id: Union[None, Unset, str]
        if isinstance(self.supervisor_id, Unset):
            supervisor_id = UNSET
        else:
            supervisor_id = self.supervisor_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "Workspace": workspace,
            }
        )
        if supervisor_id is not UNSET:
            field_dict["SupervisorId"] = supervisor_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        workspace = d.pop("Workspace")

        def _parse_supervisor_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        supervisor_id = _parse_supervisor_id(d.pop("SupervisorId", UNSET))

        assign_workspace_info = cls(
            workspace=workspace,
            supervisor_id=supervisor_id,
        )

        return assign_workspace_info
