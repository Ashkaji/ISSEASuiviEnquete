from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.assignment_history_item import AssignmentHistoryItem


T = TypeVar("T", bound="AssignmentHistory")


@_attrs_define
class AssignmentHistory:
    """
    Attributes:
        history (Union[List['AssignmentHistoryItem'], None, Unset]):
        records_filtered (Union[Unset, int]):
    """

    history: Union[List["AssignmentHistoryItem"], None, Unset] = UNSET
    records_filtered: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        history: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.history, Unset):
            history = UNSET
        elif isinstance(self.history, list):
            history = []
            for history_type_0_item_data in self.history:
                history_type_0_item = history_type_0_item_data.to_dict()
                history.append(history_type_0_item)

        else:
            history = self.history

        records_filtered = self.records_filtered

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if history is not UNSET:
            field_dict["History"] = history
        if records_filtered is not UNSET:
            field_dict["RecordsFiltered"] = records_filtered

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.assignment_history_item import AssignmentHistoryItem

        d = src_dict.copy()

        def _parse_history(data: object) -> Union[List["AssignmentHistoryItem"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                history_type_0 = []
                _history_type_0 = data
                for history_type_0_item_data in _history_type_0:
                    history_type_0_item = AssignmentHistoryItem.from_dict(history_type_0_item_data)

                    history_type_0.append(history_type_0_item)

                return history_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["AssignmentHistoryItem"], None, Unset], data)

        history = _parse_history(d.pop("History", UNSET))

        records_filtered = d.pop("RecordsFiltered", UNSET)

        assignment_history = cls(
            history=history,
            records_filtered=records_filtered,
        )

        return assignment_history
