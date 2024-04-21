from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_api_item import UserApiItem


T = TypeVar("T", bound="UserApiView")


@_attrs_define
class UserApiView:
    """
    Attributes:
        limit (int):
        total_count (int):
        offset (int):
        users (Union[List['UserApiItem'], None, Unset]):
        order (Union[None, Unset, str]):
    """

    limit: int
    total_count: int
    offset: int
    users: Union[List["UserApiItem"], None, Unset] = UNSET
    order: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        limit = self.limit

        total_count = self.total_count

        offset = self.offset

        users: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.users, Unset):
            users = UNSET
        elif isinstance(self.users, list):
            users = []
            for users_type_0_item_data in self.users:
                users_type_0_item = users_type_0_item_data.to_dict()
                users.append(users_type_0_item)

        else:
            users = self.users

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
        if users is not UNSET:
            field_dict["Users"] = users
        if order is not UNSET:
            field_dict["Order"] = order

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_api_item import UserApiItem

        d = src_dict.copy()
        limit = d.pop("Limit")

        total_count = d.pop("TotalCount")

        offset = d.pop("Offset")

        def _parse_users(data: object) -> Union[List["UserApiItem"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                users_type_0 = []
                _users_type_0 = data
                for users_type_0_item_data in _users_type_0:
                    users_type_0_item = UserApiItem.from_dict(users_type_0_item_data)

                    users_type_0.append(users_type_0_item)

                return users_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["UserApiItem"], None, Unset], data)

        users = _parse_users(d.pop("Users", UNSET))

        def _parse_order(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        order = _parse_order(d.pop("Order", UNSET))

        user_api_view = cls(
            limit=limit,
            total_count=total_count,
            offset=offset,
            users=users,
            order=order,
        )

        return user_api_view
