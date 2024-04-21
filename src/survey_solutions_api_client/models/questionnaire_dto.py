from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="QuestionnaireDto")


@_attrs_define
class QuestionnaireDto:
    """
    Attributes:
        id (Union[None, Unset, str]):
        title (Union[None, Unset, str]):
        version (Union[Unset, int]):
    """

    id: Union[None, Unset, str] = UNSET
    title: Union[None, Unset, str] = UNSET
    version: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id: Union[None, Unset, str]
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        title: Union[None, Unset, str]
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if title is not UNSET:
            field_dict["Title"] = title
        if version is not UNSET:
            field_dict["Version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        id = _parse_id(d.pop("Id", UNSET))

        def _parse_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        title = _parse_title(d.pop("Title", UNSET))

        version = d.pop("Version", UNSET)

        questionnaire_dto = cls(
            id=id,
            title=title,
            version=version,
        )

        return questionnaire_dto
