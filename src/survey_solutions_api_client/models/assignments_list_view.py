from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.assignment_view_item import AssignmentViewItem


T = TypeVar("T", bound="AssignmentsListView")


@_attrs_define
class AssignmentsListView:
    """
    Attributes:
        limit (int):
        total_count (int):
        offset (int):
        assignments (Union[List['AssignmentViewItem'], None, Unset]):
        order (Union[None, Unset, str]):
    """

    limit: int
    total_count: int
    offset: int
    assignments: Union[List["AssignmentViewItem"], None, Unset] = UNSET
    order: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        limit = self.limit

        total_count = self.total_count

        offset = self.offset

        assignments: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.assignments, Unset):
            assignments = UNSET
        elif isinstance(self.assignments, list):
            assignments = []
            for assignments_type_0_item_data in self.assignments:
                assignments_type_0_item = assignments_type_0_item_data.to_dict()
                assignments.append(assignments_type_0_item)

        else:
            assignments = self.assignments

        order: Union[None, Unset, str]
        if isinstance(self.order, Unset):
            order = UNSET
        else:
            order = self.order

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "Limit": limit,
                "TotalCount": total_count,
                "Offset": offset,
            }
        )
        if assignments is not UNSET:
            field_dict["Assignments"] = assignments
        if order is not UNSET:
            field_dict["Order"] = order

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.assignment_view_item import AssignmentViewItem

        d = src_dict.copy()
        limit = d.pop("Limit")

        total_count = d.pop("TotalCount")

        offset = d.pop("Offset")

        def _parse_assignments(data: object) -> Union[List["AssignmentViewItem"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                assignments_type_0 = []
                _assignments_type_0 = data
                for assignments_type_0_item_data in _assignments_type_0:
                    assignments_type_0_item = AssignmentViewItem.from_dict(assignments_type_0_item_data)

                    assignments_type_0.append(assignments_type_0_item)

                return assignments_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["AssignmentViewItem"], None, Unset], data)

        assignments = _parse_assignments(d.pop("Assignments", UNSET))

        def _parse_order(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        order = _parse_order(d.pop("Order", UNSET))

        assignments_list_view = cls(
            limit=limit,
            total_count=total_count,
            offset=offset,
            assignments=assignments,
            order=order,
        )

        return assignments_list_view
