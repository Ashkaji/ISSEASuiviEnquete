from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="QuestionAnswerView")


@_attrs_define
class QuestionAnswerView:
    """
    Attributes:
        answer (Union[Unset, int]):
        text (Union[None, Unset, str]):
        column (Union[None, Unset, str]): Column name in API
    """

    answer: Union[Unset, int] = UNSET
    text: Union[None, Unset, str] = UNSET
    column: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        answer = self.answer

        text: Union[None, Unset, str]
        if isinstance(self.text, Unset):
            text = UNSET
        else:
            text = self.text

        column: Union[None, Unset, str]
        if isinstance(self.column, Unset):
            column = UNSET
        else:
            column = self.column

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if answer is not UNSET:
            field_dict["Answer"] = answer
        if text is not UNSET:
            field_dict["Text"] = text
        if column is not UNSET:
            field_dict["Column"] = column

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        answer = d.pop("Answer", UNSET)

        def _parse_text(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        text = _parse_text(d.pop("Text", UNSET))

        def _parse_column(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        column = _parse_column(d.pop("Column", UNSET))

        question_answer_view = cls(
            answer=answer,
            text=text,
            column=column,
        )

        return question_answer_view
