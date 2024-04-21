from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.abstract_answer import AbstractAnswer
    from ..models.identity import Identity


T = TypeVar("T", bound="InterviewAnswer")


@_attrs_define
class InterviewAnswer:
    """
    Attributes:
        identity (Union[Unset, Identity]):
        answer (Union[Unset, AbstractAnswer]):
        variable (Union[None, Unset, str]):
    """

    identity: Union[Unset, "Identity"] = UNSET
    answer: Union[Unset, "AbstractAnswer"] = UNSET
    variable: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        identity: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.identity, Unset):
            identity = self.identity.to_dict()

        answer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.answer, Unset):
            answer = self.answer.to_dict()

        variable: Union[None, Unset, str]
        if isinstance(self.variable, Unset):
            variable = UNSET
        else:
            variable = self.variable

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if identity is not UNSET:
            field_dict["Identity"] = identity
        if answer is not UNSET:
            field_dict["Answer"] = answer
        if variable is not UNSET:
            field_dict["Variable"] = variable

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.abstract_answer import AbstractAnswer
        from ..models.identity import Identity

        d = src_dict.copy()
        _identity = d.pop("Identity", UNSET)
        identity: Union[Unset, Identity]
        if isinstance(_identity, Unset):
            identity = UNSET
        else:
            identity = Identity.from_dict(_identity)

        _answer = d.pop("Answer", UNSET)
        answer: Union[Unset, AbstractAnswer]
        if isinstance(_answer, Unset):
            answer = UNSET
        else:
            answer = AbstractAnswer.from_dict(_answer)

        def _parse_variable(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        variable = _parse_variable(d.pop("Variable", UNSET))

        interview_answer = cls(
            identity=identity,
            answer=answer,
            variable=variable,
        )

        return interview_answer
