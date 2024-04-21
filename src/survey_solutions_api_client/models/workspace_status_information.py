from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkspaceStatusInformation")


@_attrs_define
class WorkspaceStatusInformation:
    """
    Attributes:
        can_be_deleted (Union[Unset, bool]):
        workspace_name (Union[None, Unset, str]):
        workspace_display_name (Union[None, Unset, str]):
        existing_questionnaires_count (Union[Unset, int]):
        interviewers_count (Union[Unset, int]):
        supervisors_count (Union[Unset, int]):
        maps_count (Union[Unset, int]):
    """

    can_be_deleted: Union[Unset, bool] = UNSET
    workspace_name: Union[None, Unset, str] = UNSET
    workspace_display_name: Union[None, Unset, str] = UNSET
    existing_questionnaires_count: Union[Unset, int] = UNSET
    interviewers_count: Union[Unset, int] = UNSET
    supervisors_count: Union[Unset, int] = UNSET
    maps_count: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        can_be_deleted = self.can_be_deleted

        workspace_name: Union[None, Unset, str]
        if isinstance(self.workspace_name, Unset):
            workspace_name = UNSET
        else:
            workspace_name = self.workspace_name

        workspace_display_name: Union[None, Unset, str]
        if isinstance(self.workspace_display_name, Unset):
            workspace_display_name = UNSET
        else:
            workspace_display_name = self.workspace_display_name

        existing_questionnaires_count = self.existing_questionnaires_count

        interviewers_count = self.interviewers_count

        supervisors_count = self.supervisors_count

        maps_count = self.maps_count

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if can_be_deleted is not UNSET:
            field_dict["CanBeDeleted"] = can_be_deleted
        if workspace_name is not UNSET:
            field_dict["WorkspaceName"] = workspace_name
        if workspace_display_name is not UNSET:
            field_dict["WorkspaceDisplayName"] = workspace_display_name
        if existing_questionnaires_count is not UNSET:
            field_dict["ExistingQuestionnairesCount"] = existing_questionnaires_count
        if interviewers_count is not UNSET:
            field_dict["InterviewersCount"] = interviewers_count
        if supervisors_count is not UNSET:
            field_dict["SupervisorsCount"] = supervisors_count
        if maps_count is not UNSET:
            field_dict["MapsCount"] = maps_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        can_be_deleted = d.pop("CanBeDeleted", UNSET)

        def _parse_workspace_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        workspace_name = _parse_workspace_name(d.pop("WorkspaceName", UNSET))

        def _parse_workspace_display_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        workspace_display_name = _parse_workspace_display_name(d.pop("WorkspaceDisplayName", UNSET))

        existing_questionnaires_count = d.pop("ExistingQuestionnairesCount", UNSET)

        interviewers_count = d.pop("InterviewersCount", UNSET)

        supervisors_count = d.pop("SupervisorsCount", UNSET)

        maps_count = d.pop("MapsCount", UNSET)

        workspace_status_information = cls(
            can_be_deleted=can_be_deleted,
            workspace_name=workspace_name,
            workspace_display_name=workspace_display_name,
            existing_questionnaires_count=existing_questionnaires_count,
            interviewers_count=interviewers_count,
            supervisors_count=supervisors_count,
            maps_count=maps_count,
        )

        return workspace_status_information
