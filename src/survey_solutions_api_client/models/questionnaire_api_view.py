from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.questionnaire_api_item import QuestionnaireApiItem


T = TypeVar("T", bound="QuestionnaireApiView")


@_attrs_define
class QuestionnaireApiView:
    """
    Attributes:
        limit (int):
        total_count (int):
        offset (int):
        questionnaires (Union[List['QuestionnaireApiItem'], None, Unset]):
        order (Union[None, Unset, str]):
    """

    limit: int
    total_count: int
    offset: int
    questionnaires: Union[List["QuestionnaireApiItem"], None, Unset] = UNSET
    order: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        limit = self.limit

        total_count = self.total_count

        offset = self.offset

        questionnaires: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.questionnaires, Unset):
            questionnaires = UNSET
        elif isinstance(self.questionnaires, list):
            questionnaires = []
            for questionnaires_type_0_item_data in self.questionnaires:
                questionnaires_type_0_item = questionnaires_type_0_item_data.to_dict()
                questionnaires.append(questionnaires_type_0_item)

        else:
            questionnaires = self.questionnaires

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
        if questionnaires is not UNSET:
            field_dict["Questionnaires"] = questionnaires
        if order is not UNSET:
            field_dict["Order"] = order

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.questionnaire_api_item import QuestionnaireApiItem

        d = src_dict.copy()
        limit = d.pop("Limit")

        total_count = d.pop("TotalCount")

        offset = d.pop("Offset")

        def _parse_questionnaires(data: object) -> Union[List["QuestionnaireApiItem"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                questionnaires_type_0 = []
                _questionnaires_type_0 = data
                for questionnaires_type_0_item_data in _questionnaires_type_0:
                    questionnaires_type_0_item = QuestionnaireApiItem.from_dict(questionnaires_type_0_item_data)

                    questionnaires_type_0.append(questionnaires_type_0_item)

                return questionnaires_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["QuestionnaireApiItem"], None, Unset], data)

        questionnaires = _parse_questionnaires(d.pop("Questionnaires", UNSET))

        def _parse_order(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        order = _parse_order(d.pop("Order", UNSET))

        questionnaire_api_view = cls(
            limit=limit,
            total_count=total_count,
            offset=offset,
            questionnaires=questionnaires,
            order=order,
        )

        return questionnaire_api_view
