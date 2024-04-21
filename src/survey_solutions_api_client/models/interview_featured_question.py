from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="InterviewFeaturedQuestion")


@_attrs_define
class InterviewFeaturedQuestion:
    """
    Attributes:
        id (Union[Unset, int]):
        question (Union[None, Unset, str]):
        answer (Union[None, Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    question: Union[None, Unset, str] = UNSET
    answer: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        question: Union[None, Unset, str]
        if isinstance(self.question, Unset):
            question = UNSET
        else:
            question = self.question

        answer: Union[None, Unset, str]
        if isinstance(self.answer, Unset):
            answer = UNSET
        else:
            answer = self.answer

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if question is not UNSET:
            field_dict["Question"] = question
        if answer is not UNSET:
            field_dict["Answer"] = answer

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        def _parse_question(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        question = _parse_question(d.pop("Question", UNSET))

        def _parse_answer(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        answer = _parse_answer(d.pop("Answer", UNSET))

        interview_featured_question = cls(
            id=id,
            question=question,
            answer=answer,
        )

        return interview_featured_question
