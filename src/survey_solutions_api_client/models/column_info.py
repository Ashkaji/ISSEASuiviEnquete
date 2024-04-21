from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_info import SearchInfo


T = TypeVar("T", bound="ColumnInfo")


@_attrs_define
class ColumnInfo:
    """
    Attributes:
        title (Union[Unset, int]):
        name (Union[None, Unset, str]):
        searchable (Union[Unset, bool]):
        orderable (Union[Unset, bool]):
        search (Union[Unset, SearchInfo]):
    """

    title: Union[Unset, int] = UNSET
    name: Union[None, Unset, str] = UNSET
    searchable: Union[Unset, bool] = UNSET
    orderable: Union[Unset, bool] = UNSET
    search: Union[Unset, "SearchInfo"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        title = self.title

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        searchable = self.searchable

        orderable = self.orderable

        search: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.search, Unset):
            search = self.search.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if title is not UNSET:
            field_dict["Title"] = title
        if name is not UNSET:
            field_dict["Name"] = name
        if searchable is not UNSET:
            field_dict["Searchable"] = searchable
        if orderable is not UNSET:
            field_dict["Orderable"] = orderable
        if search is not UNSET:
            field_dict["Search"] = search

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.search_info import SearchInfo

        d = src_dict.copy()
        title = d.pop("Title", UNSET)

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("Name", UNSET))

        searchable = d.pop("Searchable", UNSET)

        orderable = d.pop("Orderable", UNSET)

        _search = d.pop("Search", UNSET)
        search: Union[Unset, SearchInfo]
        if isinstance(_search, Unset):
            search = UNSET
        else:
            search = SearchInfo.from_dict(_search)

        column_info = cls(
            title=title,
            name=name,
            searchable=searchable,
            orderable=orderable,
            search=search,
        )

        return column_info
