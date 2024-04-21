from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.identity import Identity


T = TypeVar("T", bound="QuestionApiItem")


@_attrs_define
class QuestionApiItem:
    """
    Attributes:
        variable_name (str):
        question_id (Identity):
        answer (Union[None, Unset, str]):
    """

    variable_name: str
    question_id: "Identity"
    answer: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        variable_name = self.variable_name

        question_id = self.question_id.to_dict()

        answer: Union[None, Unset, str]
        if isinstance(self.answer, Unset):
            answer = UNSET
        else:
            answer = self.answer

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "VariableName": variable_name,
                "QuestionId": question_id,
            }
        )
        if answer is not UNSET:
            field_dict["Answer"] = answer

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.identity import Identity

        d = src_dict.copy()
        variable_name = d.pop("VariableName")

        question_id = Identity.from_dict(d.pop("QuestionId"))

        def _parse_answer(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        answer = _parse_answer(d.pop("Answer", UNSET))

        question_api_item = cls(
            variable_name=variable_name,
            question_id=question_id,
            answer=answer,
        )

        return question_api_item
