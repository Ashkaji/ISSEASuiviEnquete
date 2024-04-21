import datetime
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.interview_historical_action import InterviewHistoricalAction
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.interview_historical_record_view_parameters_type_0 import InterviewHistoricalRecordViewParametersType0


T = TypeVar("T", bound="InterviewHistoricalRecordView")


@_attrs_define
class InterviewHistoricalRecordView:
    """
    Attributes:
        index (Union[Unset, int]):
        action (Union[Unset, InterviewHistoricalAction]):
        originator_name (Union[None, Unset, str]):
        originator_role (Union[None, Unset, str]):
        parameters (Union['InterviewHistoricalRecordViewParametersType0', None, Unset]):
        timestamp (Union[None, Unset, datetime.datetime]):
        offset (Union[None, Unset, str]):
    """

    index: Union[Unset, int] = UNSET
    action: Union[Unset, InterviewHistoricalAction] = UNSET
    originator_name: Union[None, Unset, str] = UNSET
    originator_role: Union[None, Unset, str] = UNSET
    parameters: Union["InterviewHistoricalRecordViewParametersType0", None, Unset] = UNSET
    timestamp: Union[None, Unset, datetime.datetime] = UNSET
    offset: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from ..models.interview_historical_record_view_parameters_type_0 import (
            InterviewHistoricalRecordViewParametersType0,
        )

        index = self.index

        action: Union[Unset, str] = UNSET
        if not isinstance(self.action, Unset):
            action = self.action.value

        originator_name: Union[None, Unset, str]
        if isinstance(self.originator_name, Unset):
            originator_name = UNSET
        else:
            originator_name = self.originator_name

        originator_role: Union[None, Unset, str]
        if isinstance(self.originator_role, Unset):
            originator_role = UNSET
        else:
            originator_role = self.originator_role

        parameters: Union[Dict[str, Any], None, Unset]
        if isinstance(self.parameters, Unset):
            parameters = UNSET
        elif isinstance(self.parameters, InterviewHistoricalRecordViewParametersType0):
            parameters = self.parameters.to_dict()
        else:
            parameters = self.parameters

        timestamp: Union[None, Unset, str]
        if isinstance(self.timestamp, Unset):
            timestamp = UNSET
        elif isinstance(self.timestamp, datetime.datetime):
            timestamp = self.timestamp.isoformat()
        else:
            timestamp = self.timestamp

        offset: Union[None, Unset, str]
        if isinstance(self.offset, Unset):
            offset = UNSET
        else:
            offset = self.offset

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if index is not UNSET:
            field_dict["Index"] = index
        if action is not UNSET:
            field_dict["Action"] = action
        if originator_name is not UNSET:
            field_dict["OriginatorName"] = originator_name
        if originator_role is not UNSET:
            field_dict["OriginatorRole"] = originator_role
        if parameters is not UNSET:
            field_dict["Parameters"] = parameters
        if timestamp is not UNSET:
            field_dict["Timestamp"] = timestamp
        if offset is not UNSET:
            field_dict["Offset"] = offset

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.interview_historical_record_view_parameters_type_0 import (
            InterviewHistoricalRecordViewParametersType0,
        )

        d = src_dict.copy()
        index = d.pop("Index", UNSET)

        _action = d.pop("Action", UNSET)
        action: Union[Unset, InterviewHistoricalAction]
        if isinstance(_action, Unset):
            action = UNSET
        else:
            action = InterviewHistoricalAction(_action)

        def _parse_originator_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        originator_name = _parse_originator_name(d.pop("OriginatorName", UNSET))

        def _parse_originator_role(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        originator_role = _parse_originator_role(d.pop("OriginatorRole", UNSET))

        def _parse_parameters(data: object) -> Union["InterviewHistoricalRecordViewParametersType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                parameters_type_0 = InterviewHistoricalRecordViewParametersType0.from_dict(data)

                return parameters_type_0
            except:  # noqa: E722
                pass
            return cast(Union["InterviewHistoricalRecordViewParametersType0", None, Unset], data)

        parameters = _parse_parameters(d.pop("Parameters", UNSET))

        def _parse_timestamp(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                timestamp_type_0 = isoparse(data)

                return timestamp_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        timestamp = _parse_timestamp(d.pop("Timestamp", UNSET))

        def _parse_offset(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        offset = _parse_offset(d.pop("Offset", UNSET))

        interview_historical_record_view = cls(
            index=index,
            action=action,
            originator_name=originator_name,
            originator_role=originator_role,
            parameters=parameters,
            timestamp=timestamp,
            offset=offset,
        )

        return interview_historical_record_view
