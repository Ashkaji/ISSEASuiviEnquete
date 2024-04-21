from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.question_api_item import QuestionApiItem


T = TypeVar("T", bound="InterviewApiDetails")


@_attrs_define
class InterviewApiDetails:
    """
    Attributes:
        answers (List['QuestionApiItem']):
    """

    answers: List["QuestionApiItem"]

    def to_dict(self) -> Dict[str, Any]:
        answers = []
        for answers_item_data in self.answers:
            answers_item = answers_item_data.to_dict()
            answers.append(answers_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "Answers": answers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.question_api_item import QuestionApiItem

        d = src_dict.copy()
        answers = []
        _answers = d.pop("Answers")
        for answers_item_data in _answers:
            answers_item = QuestionApiItem.from_dict(answers_item_data)

            answers.append(answers_item)

        interview_api_details = cls(
            answers=answers,
        )

        return interview_api_details
