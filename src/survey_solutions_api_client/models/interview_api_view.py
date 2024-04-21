from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.interview_api_item import InterviewApiItem


T = TypeVar("T", bound="InterviewApiView")


@_attrs_define
class InterviewApiView:
    """
    Attributes:
        limit (int):
        total_count (int):
        offset (int):
        interviews (Union[List['InterviewApiItem'], None, Unset]):
        order (Union[None, Unset, str]):
    """

    limit: int
    total_count: int
    offset: int
    interviews: Union[List["InterviewApiItem"], None, Unset] = UNSET
    order: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        limit = self.limit

        total_count = self.total_count

        offset = self.offset

        interviews: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.interviews, Unset):
            interviews = UNSET
        elif isinstance(self.interviews, list):
            interviews = []
            for interviews_type_0_item_data in self.interviews:
                interviews_type_0_item = interviews_type_0_item_data.to_dict()
                interviews.append(interviews_type_0_item)

        else:
            interviews = self.interviews

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
        if interviews is not UNSET:
            field_dict["Interviews"] = interviews
        if order is not UNSET:
            field_dict["Order"] = order

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.interview_api_item import InterviewApiItem

        d = src_dict.copy()
        limit = d.pop("Limit")

        total_count = d.pop("TotalCount")

        offset = d.pop("Offset")

        def _parse_interviews(data: object) -> Union[List["InterviewApiItem"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                interviews_type_0 = []
                _interviews_type_0 = data
                for interviews_type_0_item_data in _interviews_type_0:
                    interviews_type_0_item = InterviewApiItem.from_dict(interviews_type_0_item_data)

                    interviews_type_0.append(interviews_type_0_item)

                return interviews_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["InterviewApiItem"], None, Unset], data)

        interviews = _parse_interviews(d.pop("Interviews", UNSET))

        def _parse_order(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        order = _parse_order(d.pop("Order", UNSET))

        interview_api_view = cls(
            limit=limit,
            total_count=total_count,
            offset=offset,
            interviews=interviews,
            order=order,
        )

        return interview_api_view
