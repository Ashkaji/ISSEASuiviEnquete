import datetime
from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="InterviewApiStatistics")


@_attrs_define
class InterviewApiStatistics:
    """
    Attributes:
        answered (Union[Unset, int]):
        not_answered (Union[Unset, int]):
        flagged (Union[Unset, int]):
        not_flagged (Union[Unset, int]):
        valid (Union[Unset, int]):
        invalid (Union[Unset, int]):
        with_comments (Union[Unset, int]):
        for_interviewer (Union[Unset, int]):
        for_supervisor (Union[Unset, int]):
        interview_id (Union[Unset, str]):
        interview_key (Union[None, Unset, str]):
        status (Union[None, Unset, str]):
        responsible_id (Union[Unset, str]):
        responsible_name (Union[None, Unset, str]):
        number_of_interviewers (Union[Unset, int]):
        number_rejections_by_supervisor (Union[Unset, int]):
        number_rejections_by_hq (Union[Unset, int]):
        interview_duration (Union[None, Unset, str]):
        assignment_id (Union[None, Unset, int]):
        updated_at_utc (Union[Unset, datetime.datetime]):
        web_interview_url (Union[None, Unset, str]):
    """

    answered: Union[Unset, int] = UNSET
    not_answered: Union[Unset, int] = UNSET
    flagged: Union[Unset, int] = UNSET
    not_flagged: Union[Unset, int] = UNSET
    valid: Union[Unset, int] = UNSET
    invalid: Union[Unset, int] = UNSET
    with_comments: Union[Unset, int] = UNSET
    for_interviewer: Union[Unset, int] = UNSET
    for_supervisor: Union[Unset, int] = UNSET
    interview_id: Union[Unset, str] = UNSET
    interview_key: Union[None, Unset, str] = UNSET
    status: Union[None, Unset, str] = UNSET
    responsible_id: Union[Unset, str] = UNSET
    responsible_name: Union[None, Unset, str] = UNSET
    number_of_interviewers: Union[Unset, int] = UNSET
    number_rejections_by_supervisor: Union[Unset, int] = UNSET
    number_rejections_by_hq: Union[Unset, int] = UNSET
    interview_duration: Union[None, Unset, str] = UNSET
    assignment_id: Union[None, Unset, int] = UNSET
    updated_at_utc: Union[Unset, datetime.datetime] = UNSET
    web_interview_url: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        answered = self.answered

        not_answered = self.not_answered

        flagged = self.flagged

        not_flagged = self.not_flagged

        valid = self.valid

        invalid = self.invalid

        with_comments = self.with_comments

        for_interviewer = self.for_interviewer

        for_supervisor = self.for_supervisor

        interview_id = self.interview_id

        interview_key: Union[None, Unset, str]
        if isinstance(self.interview_key, Unset):
            interview_key = UNSET
        else:
            interview_key = self.interview_key

        status: Union[None, Unset, str]
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        responsible_id = self.responsible_id

        responsible_name: Union[None, Unset, str]
        if isinstance(self.responsible_name, Unset):
            responsible_name = UNSET
        else:
            responsible_name = self.responsible_name

        number_of_interviewers = self.number_of_interviewers

        number_rejections_by_supervisor = self.number_rejections_by_supervisor

        number_rejections_by_hq = self.number_rejections_by_hq

        interview_duration: Union[None, Unset, str]
        if isinstance(self.interview_duration, Unset):
            interview_duration = UNSET
        else:
            interview_duration = self.interview_duration

        assignment_id: Union[None, Unset, int]
        if isinstance(self.assignment_id, Unset):
            assignment_id = UNSET
        else:
            assignment_id = self.assignment_id

        updated_at_utc: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at_utc, Unset):
            updated_at_utc = self.updated_at_utc.isoformat()

        web_interview_url: Union[None, Unset, str]
        if isinstance(self.web_interview_url, Unset):
            web_interview_url = UNSET
        else:
            web_interview_url = self.web_interview_url

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if answered is not UNSET:
            field_dict["Answered"] = answered
        if not_answered is not UNSET:
            field_dict["NotAnswered"] = not_answered
        if flagged is not UNSET:
            field_dict["Flagged"] = flagged
        if not_flagged is not UNSET:
            field_dict["NotFlagged"] = not_flagged
        if valid is not UNSET:
            field_dict["Valid"] = valid
        if invalid is not UNSET:
            field_dict["Invalid"] = invalid
        if with_comments is not UNSET:
            field_dict["WithComments"] = with_comments
        if for_interviewer is not UNSET:
            field_dict["ForInterviewer"] = for_interviewer
        if for_supervisor is not UNSET:
            field_dict["ForSupervisor"] = for_supervisor
        if interview_id is not UNSET:
            field_dict["InterviewId"] = interview_id
        if interview_key is not UNSET:
            field_dict["InterviewKey"] = interview_key
        if status is not UNSET:
            field_dict["Status"] = status
        if responsible_id is not UNSET:
            field_dict["ResponsibleId"] = responsible_id
        if responsible_name is not UNSET:
            field_dict["ResponsibleName"] = responsible_name
        if number_of_interviewers is not UNSET:
            field_dict["NumberOfInterviewers"] = number_of_interviewers
        if number_rejections_by_supervisor is not UNSET:
            field_dict["NumberRejectionsBySupervisor"] = number_rejections_by_supervisor
        if number_rejections_by_hq is not UNSET:
            field_dict["NumberRejectionsByHq"] = number_rejections_by_hq
        if interview_duration is not UNSET:
            field_dict["InterviewDuration"] = interview_duration
        if assignment_id is not UNSET:
            field_dict["AssignmentId"] = assignment_id
        if updated_at_utc is not UNSET:
            field_dict["UpdatedAtUtc"] = updated_at_utc
        if web_interview_url is not UNSET:
            field_dict["WebInterviewUrl"] = web_interview_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        answered = d.pop("Answered", UNSET)

        not_answered = d.pop("NotAnswered", UNSET)

        flagged = d.pop("Flagged", UNSET)

        not_flagged = d.pop("NotFlagged", UNSET)

        valid = d.pop("Valid", UNSET)

        invalid = d.pop("Invalid", UNSET)

        with_comments = d.pop("WithComments", UNSET)

        for_interviewer = d.pop("ForInterviewer", UNSET)

        for_supervisor = d.pop("ForSupervisor", UNSET)

        interview_id = d.pop("InterviewId", UNSET)

        def _parse_interview_key(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        interview_key = _parse_interview_key(d.pop("InterviewKey", UNSET))

        def _parse_status(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        status = _parse_status(d.pop("Status", UNSET))

        responsible_id = d.pop("ResponsibleId", UNSET)

        def _parse_responsible_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        responsible_name = _parse_responsible_name(d.pop("ResponsibleName", UNSET))

        number_of_interviewers = d.pop("NumberOfInterviewers", UNSET)

        number_rejections_by_supervisor = d.pop("NumberRejectionsBySupervisor", UNSET)

        number_rejections_by_hq = d.pop("NumberRejectionsByHq", UNSET)

        def _parse_interview_duration(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        interview_duration = _parse_interview_duration(d.pop("InterviewDuration", UNSET))

        def _parse_assignment_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        assignment_id = _parse_assignment_id(d.pop("AssignmentId", UNSET))

        _updated_at_utc = d.pop("UpdatedAtUtc", UNSET)
        updated_at_utc: Union[Unset, datetime.datetime]
        if isinstance(_updated_at_utc, Unset):
            updated_at_utc = UNSET
        else:
            updated_at_utc = isoparse(_updated_at_utc)

        def _parse_web_interview_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        web_interview_url = _parse_web_interview_url(d.pop("WebInterviewUrl", UNSET))

        interview_api_statistics = cls(
            answered=answered,
            not_answered=not_answered,
            flagged=flagged,
            not_flagged=not_flagged,
            valid=valid,
            invalid=invalid,
            with_comments=with_comments,
            for_interviewer=for_interviewer,
            for_supervisor=for_supervisor,
            interview_id=interview_id,
            interview_key=interview_key,
            status=status,
            responsible_id=responsible_id,
            responsible_name=responsible_name,
            number_of_interviewers=number_of_interviewers,
            number_rejections_by_supervisor=number_rejections_by_supervisor,
            number_rejections_by_hq=number_rejections_by_hq,
            interview_duration=interview_duration,
            assignment_id=assignment_id,
            updated_at_utc=updated_at_utc,
            web_interview_url=web_interview_url,
        )

        return interview_api_statistics
