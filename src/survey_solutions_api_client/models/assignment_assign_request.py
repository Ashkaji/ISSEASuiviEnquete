from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="AssignmentAssignRequest")


@_attrs_define
class AssignmentAssignRequest:
    """
    Attributes:
        responsible (str):
    """

    responsible: str

    def to_dict(self) -> Dict[str, Any]:
        responsible = self.responsible

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "Responsible": responsible,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        responsible = d.pop("Responsible")

        assignment_assign_request = cls(
            responsible=responsible,
        )

        return assignment_assign_request
