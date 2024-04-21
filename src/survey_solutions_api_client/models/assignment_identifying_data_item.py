from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AssignmentIdentifyingDataItem")


@_attrs_define
class AssignmentIdentifyingDataItem:
    """
    Attributes:
        identity (Union[None, Unset, str]): Question identity
            Expected format: GuidWithoutDashes_Int1-Int2, where _Int1-Int2 - codes of parent rosters (empty if question is
            not inside any roster).
            For example: 11111111111111111111111111111111_0-1 should be used for question on the second level
        variable (Union[None, Unset, str]):
        answer (Union[None, Unset, str]):
    """

    identity: Union[None, Unset, str] = UNSET
    variable: Union[None, Unset, str] = UNSET
    answer: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        identity: Union[None, Unset, str]
        if isinstance(self.identity, Unset):
            identity = UNSET
        else:
            identity = self.identity

        variable: Union[None, Unset, str]
        if isinstance(self.variable, Unset):
            variable = UNSET
        else:
            variable = self.variable

        answer: Union[None, Unset, str]
        if isinstance(self.answer, Unset):
            answer = UNSET
        else:
            answer = self.answer

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if identity is not UNSET:
            field_dict["Identity"] = identity
        if variable is not UNSET:
            field_dict["Variable"] = variable
        if answer is not UNSET:
            field_dict["Answer"] = answer

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_identity(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        identity = _parse_identity(d.pop("Identity", UNSET))

        def _parse_variable(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        variable = _parse_variable(d.pop("Variable", UNSET))

        def _parse_answer(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        answer = _parse_answer(d.pop("Answer", UNSET))

        assignment_identifying_data_item = cls(
            identity=identity,
            variable=variable,
            answer=answer,
        )

        return assignment_identifying_data_item
