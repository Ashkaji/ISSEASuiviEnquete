from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="Identity")


@_attrs_define
class Identity:
    """
    Attributes:
        id (Union[Unset, str]):
        roster_vector (Union[List[int], None, Unset]):
    """

    id: Union[Unset, str] = UNSET
    roster_vector: Union[List[int], None, Unset] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        roster_vector: Union[List[int], None, Unset]
        if isinstance(self.roster_vector, Unset):
            roster_vector = UNSET
        elif isinstance(self.roster_vector, list):
            roster_vector = self.roster_vector

        else:
            roster_vector = self.roster_vector

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if roster_vector is not UNSET:
            field_dict["RosterVector"] = roster_vector

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        def _parse_roster_vector(data: object) -> Union[List[int], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                roster_vector_type_0 = cast(List[int], data)

                return roster_vector_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[int], None, Unset], data)

        roster_vector = _parse_roster_vector(d.pop("RosterVector", UNSET))

        identity = cls(
            id=id,
            roster_vector=roster_vector,
        )

        return identity
