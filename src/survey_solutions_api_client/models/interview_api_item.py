import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.interview_status import InterviewStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.interview_featured_question import InterviewFeaturedQuestion


T = TypeVar("T", bound="InterviewApiItem")


@_attrs_define
class InterviewApiItem:
    """
    Attributes:
        interview_id (str):
        questionnaire_id (str):
        questionnaire_version (int):
        responsible_id (str):
        responsible_name (str):
        errors_count (int):
        status (InterviewStatus):
        last_entry_date (datetime.datetime):
        featured_questions (Union[List['InterviewFeaturedQuestion'], None, Unset]):
        assignment_id (Union[None, Unset, int]):
        received_by_device (Union[Unset, bool]):
        received_by_device_at_utc (Union[None, Unset, datetime.datetime]):
    """

    interview_id: str
    questionnaire_id: str
    questionnaire_version: int
    responsible_id: str
    responsible_name: str
    errors_count: int
    status: InterviewStatus
    last_entry_date: datetime.datetime
    featured_questions: Union[List["InterviewFeaturedQuestion"], None, Unset] = UNSET
    assignment_id: Union[None, Unset, int] = UNSET
    received_by_device: Union[Unset, bool] = UNSET
    received_by_device_at_utc: Union[None, Unset, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        interview_id = self.interview_id

        questionnaire_id = self.questionnaire_id

        questionnaire_version = self.questionnaire_version

        responsible_id = self.responsible_id

        responsible_name = self.responsible_name

        errors_count = self.errors_count

        status = self.status.value

        last_entry_date = self.last_entry_date.isoformat()

        featured_questions: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.featured_questions, Unset):
            featured_questions = UNSET
        elif isinstance(self.featured_questions, list):
            featured_questions = []
            for featured_questions_type_0_item_data in self.featured_questions:
                featured_questions_type_0_item = featured_questions_type_0_item_data.to_dict()
                featured_questions.append(featured_questions_type_0_item)

        else:
            featured_questions = self.featured_questions

        assignment_id: Union[None, Unset, int]
        if isinstance(self.assignment_id, Unset):
            assignment_id = UNSET
        else:
            assignment_id = self.assignment_id

        received_by_device = self.received_by_device

        received_by_device_at_utc: Union[None, Unset, str]
        if isinstance(self.received_by_device_at_utc, Unset):
            received_by_device_at_utc = UNSET
        elif isinstance(self.received_by_device_at_utc, datetime.datetime):
            received_by_device_at_utc = self.received_by_device_at_utc.isoformat()
        else:
            received_by_device_at_utc = self.received_by_device_at_utc

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "InterviewId": interview_id,
                "QuestionnaireId": questionnaire_id,
                "QuestionnaireVersion": questionnaire_version,
                "ResponsibleId": responsible_id,
                "ResponsibleName": responsible_name,
                "ErrorsCount": errors_count,
                "Status": status,
                "LastEntryDate": last_entry_date,
            }
        )
        if featured_questions is not UNSET:
            field_dict["FeaturedQuestions"] = featured_questions
        if assignment_id is not UNSET:
            field_dict["AssignmentId"] = assignment_id
        if received_by_device is not UNSET:
            field_dict["ReceivedByDevice"] = received_by_device
        if received_by_device_at_utc is not UNSET:
            field_dict["ReceivedByDeviceAtUtc"] = received_by_device_at_utc

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.interview_featured_question import InterviewFeaturedQuestion

        d = src_dict.copy()
        interview_id = d.pop("InterviewId")

        questionnaire_id = d.pop("QuestionnaireId")

        questionnaire_version = d.pop("QuestionnaireVersion")

        responsible_id = d.pop("ResponsibleId")

        responsible_name = d.pop("ResponsibleName")

        errors_count = d.pop("ErrorsCount")

        status = InterviewStatus(d.pop("Status"))

        last_entry_date = isoparse(d.pop("LastEntryDate"))

        def _parse_featured_questions(data: object) -> Union[List["InterviewFeaturedQuestion"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                featured_questions_type_0 = []
                _featured_questions_type_0 = data
                for featured_questions_type_0_item_data in _featured_questions_type_0:
                    featured_questions_type_0_item = InterviewFeaturedQuestion.from_dict(
                        featured_questions_type_0_item_data
                    )

                    featured_questions_type_0.append(featured_questions_type_0_item)

                return featured_questions_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["InterviewFeaturedQuestion"], None, Unset], data)

        featured_questions = _parse_featured_questions(d.pop("FeaturedQuestions", UNSET))

        def _parse_assignment_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        assignment_id = _parse_assignment_id(d.pop("AssignmentId", UNSET))

        received_by_device = d.pop("ReceivedByDevice", UNSET)

        def _parse_received_by_device_at_utc(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                received_by_device_at_utc_type_0 = isoparse(data)

                return received_by_device_at_utc_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        received_by_device_at_utc = _parse_received_by_device_at_utc(d.pop("ReceivedByDeviceAtUtc", UNSET))

        interview_api_item = cls(
            interview_id=interview_id,
            questionnaire_id=questionnaire_id,
            questionnaire_version=questionnaire_version,
            responsible_id=responsible_id,
            responsible_name=responsible_name,
            errors_count=errors_count,
            status=status,
            last_entry_date=last_entry_date,
            featured_questions=featured_questions,
            assignment_id=assignment_id,
            received_by_device=received_by_device,
            received_by_device_at_utc=received_by_device_at_utc,
        )

        return interview_api_item
