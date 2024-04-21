import datetime
from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.assignment_history_action import AssignmentHistoryAction
from ..types import UNSET, Unset

T = TypeVar("T", bound="AssignmentHistoryItem")


@_attrs_define
class AssignmentHistoryItem:
    """
    Attributes:
        action (Union[Unset, AssignmentHistoryAction]):
        actor_name (Union[None, Unset, str]):
        utc_date (Union[Unset, datetime.datetime]):
        additional_data (Union[Unset, Any]):
    """

    action: Union[Unset, AssignmentHistoryAction] = UNSET
    actor_name: Union[None, Unset, str] = UNSET
    utc_date: Union[Unset, datetime.datetime] = UNSET
    additional_data: Union[Unset, Any] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        action: Union[Unset, str] = UNSET
        if not isinstance(self.action, Unset):
            action = self.action.value

        actor_name: Union[None, Unset, str]
        if isinstance(self.actor_name, Unset):
            actor_name = UNSET
        else:
            actor_name = self.actor_name

        utc_date: Union[Unset, str] = UNSET
        if not isinstance(self.utc_date, Unset):
            utc_date = self.utc_date.isoformat()

        additional_data = self.additional_data

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if action is not UNSET:
            field_dict["Action"] = action
        if actor_name is not UNSET:
            field_dict["ActorName"] = actor_name
        if utc_date is not UNSET:
            field_dict["UtcDate"] = utc_date
        if additional_data is not UNSET:
            field_dict["AdditionalData"] = additional_data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _action = d.pop("Action", UNSET)
        action: Union[Unset, AssignmentHistoryAction]
        if isinstance(_action, Unset):
            action = UNSET
        else:
            action = AssignmentHistoryAction(_action)

        def _parse_actor_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        actor_name = _parse_actor_name(d.pop("ActorName", UNSET))

        _utc_date = d.pop("UtcDate", UNSET)
        utc_date: Union[Unset, datetime.datetime]
        if isinstance(_utc_date, Unset):
            utc_date = UNSET
        else:
            utc_date = isoparse(_utc_date)

        additional_data = d.pop("AdditionalData", UNSET)

        assignment_history_item = cls(
            action=action,
            actor_name=actor_name,
            utc_date=utc_date,
            additional_data=additional_data,
        )

        return assignment_history_item
