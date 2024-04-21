from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="AssignmentQuantitySettings")


@_attrs_define
class AssignmentQuantitySettings:
    """
    Attributes:
        can_change_quantity (bool): Assignment Quantity Settings.
    """

    can_change_quantity: bool

    def to_dict(self) -> Dict[str, Any]:
        can_change_quantity = self.can_change_quantity

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "CanChangeQuantity": can_change_quantity,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        can_change_quantity = d.pop("CanChangeQuantity")

        assignment_quantity_settings = cls(
            can_change_quantity=can_change_quantity,
        )

        return assignment_quantity_settings
