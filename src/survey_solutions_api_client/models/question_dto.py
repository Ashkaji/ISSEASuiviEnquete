from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.question_answer_view import QuestionAnswerView


T = TypeVar("T", bound="QuestionDto")


@_attrs_define
class QuestionDto:
    """
    Attributes:
        id (Union[Unset, str]):
        variable_name (Union[None, Unset, str]):
        question_text (Union[None, Unset, str]):
        answers (Union[List['QuestionAnswerView'], None, Unset]):
        breadcrumbs (Union[List[str], None, Unset]):
        label (Union[None, Unset, str]):
        type (Union[None, Unset, str]):
        has_total (Union[Unset, bool]):
        support_conditions (Union[Unset, bool]):
    """

    id: Union[Unset, str] = UNSET
    variable_name: Union[None, Unset, str] = UNSET
    question_text: Union[None, Unset, str] = UNSET
    answers: Union[List["QuestionAnswerView"], None, Unset] = UNSET
    breadcrumbs: Union[List[str], None, Unset] = UNSET
    label: Union[None, Unset, str] = UNSET
    type: Union[None, Unset, str] = UNSET
    has_total: Union[Unset, bool] = UNSET
    support_conditions: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        variable_name: Union[None, Unset, str]
        if isinstance(self.variable_name, Unset):
            variable_name = UNSET
        else:
            variable_name = self.variable_name

        question_text: Union[None, Unset, str]
        if isinstance(self.question_text, Unset):
            question_text = UNSET
        else:
            question_text = self.question_text

        answers: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.answers, Unset):
            answers = UNSET
        elif isinstance(self.answers, list):
            answers = []
            for answers_type_0_item_data in self.answers:
                answers_type_0_item = answers_type_0_item_data.to_dict()
                answers.append(answers_type_0_item)

        else:
            answers = self.answers

        breadcrumbs: Union[List[str], None, Unset]
        if isinstance(self.breadcrumbs, Unset):
            breadcrumbs = UNSET
        elif isinstance(self.breadcrumbs, list):
            breadcrumbs = self.breadcrumbs

        else:
            breadcrumbs = self.breadcrumbs

        label: Union[None, Unset, str]
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        type: Union[None, Unset, str]
        if isinstance(self.type, Unset):
            type = UNSET
        else:
            type = self.type

        has_total = self.has_total

        support_conditions = self.support_conditions

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if variable_name is not UNSET:
            field_dict["VariableName"] = variable_name
        if question_text is not UNSET:
            field_dict["QuestionText"] = question_text
        if answers is not UNSET:
            field_dict["Answers"] = answers
        if breadcrumbs is not UNSET:
            field_dict["Breadcrumbs"] = breadcrumbs
        if label is not UNSET:
            field_dict["Label"] = label
        if type is not UNSET:
            field_dict["Type"] = type
        if has_total is not UNSET:
            field_dict["HasTotal"] = has_total
        if support_conditions is not UNSET:
            field_dict["SupportConditions"] = support_conditions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.question_answer_view import QuestionAnswerView

        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        def _parse_variable_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        variable_name = _parse_variable_name(d.pop("VariableName", UNSET))

        def _parse_question_text(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        question_text = _parse_question_text(d.pop("QuestionText", UNSET))

        def _parse_answers(data: object) -> Union[List["QuestionAnswerView"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                answers_type_0 = []
                _answers_type_0 = data
                for answers_type_0_item_data in _answers_type_0:
                    answers_type_0_item = QuestionAnswerView.from_dict(answers_type_0_item_data)

                    answers_type_0.append(answers_type_0_item)

                return answers_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["QuestionAnswerView"], None, Unset], data)

        answers = _parse_answers(d.pop("Answers", UNSET))

        def _parse_breadcrumbs(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                breadcrumbs_type_0 = cast(List[str], data)

                return breadcrumbs_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        breadcrumbs = _parse_breadcrumbs(d.pop("Breadcrumbs", UNSET))

        def _parse_label(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        label = _parse_label(d.pop("Label", UNSET))

        def _parse_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        type = _parse_type(d.pop("Type", UNSET))

        has_total = d.pop("HasTotal", UNSET)

        support_conditions = d.pop("SupportConditions", UNSET)

        question_dto = cls(
            id=id,
            variable_name=variable_name,
            question_text=question_text,
            answers=answers,
            breadcrumbs=breadcrumbs,
            label=label,
            type=type,
            has_total=has_total,
            support_conditions=support_conditions,
        )

        return question_dto
