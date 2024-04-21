from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.interview_historical_record_view import InterviewHistoricalRecordView


T = TypeVar("T", bound="InterviewHistoryView")


@_attrs_define
class InterviewHistoryView:
    """
    Attributes:
        interview_id (Union[Unset, str]):
        questionnaire_id (Union[Unset, str]):
        questionnaire_version (Union[Unset, int]):
        records (Union[List['InterviewHistoricalRecordView'], None, Unset]):
    """

    interview_id: Union[Unset, str] = UNSET
    questionnaire_id: Union[Unset, str] = UNSET
    questionnaire_version: Union[Unset, int] = UNSET
    records: Union[List["InterviewHistoricalRecordView"], None, Unset] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        interview_id = self.interview_id

        questionnaire_id = self.questionnaire_id

        questionnaire_version = self.questionnaire_version

        records: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.records, Unset):
            records = UNSET
        elif isinstance(self.records, list):
            records = []
            for records_type_0_item_data in self.records:
                records_type_0_item = records_type_0_item_data.to_dict()
                records.append(records_type_0_item)

        else:
            records = self.records

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if interview_id is not UNSET:
            field_dict["InterviewId"] = interview_id
        if questionnaire_id is not UNSET:
            field_dict["QuestionnaireId"] = questionnaire_id
        if questionnaire_version is not UNSET:
            field_dict["QuestionnaireVersion"] = questionnaire_version
        if records is not UNSET:
            field_dict["Records"] = records

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.interview_historical_record_view import InterviewHistoricalRecordView

        d = src_dict.copy()
        interview_id = d.pop("InterviewId", UNSET)

        questionnaire_id = d.pop("QuestionnaireId", UNSET)

        questionnaire_version = d.pop("QuestionnaireVersion", UNSET)

        def _parse_records(data: object) -> Union[List["InterviewHistoricalRecordView"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                records_type_0 = []
                _records_type_0 = data
                for records_type_0_item_data in _records_type_0:
                    records_type_0_item = InterviewHistoricalRecordView.from_dict(records_type_0_item_data)

                    records_type_0.append(records_type_0_item)

                return records_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["InterviewHistoricalRecordView"], None, Unset], data)

        records = _parse_records(d.pop("Records", UNSET))

        interview_history_view = cls(
            interview_id=interview_id,
            questionnaire_id=questionnaire_id,
            questionnaire_version=questionnaire_version,
            records=records,
        )

        return interview_history_view
