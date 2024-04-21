from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.interview_import_reference import InterviewImportReference


T = TypeVar("T", bound="PanelImportVerificationError")


@_attrs_define
class PanelImportVerificationError:
    """
    Attributes:
        code (Union[None, Unset, str]):
        message (Union[None, Unset, str]):
        references (Union[List['InterviewImportReference'], None, Unset]):
    """

    code: Union[None, Unset, str] = UNSET
    message: Union[None, Unset, str] = UNSET
    references: Union[List["InterviewImportReference"], None, Unset] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        code: Union[None, Unset, str]
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        message: Union[None, Unset, str]
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        references: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.references, Unset):
            references = UNSET
        elif isinstance(self.references, list):
            references = []
            for references_type_0_item_data in self.references:
                references_type_0_item = references_type_0_item_data.to_dict()
                references.append(references_type_0_item)

        else:
            references = self.references

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if code is not UNSET:
            field_dict["Code"] = code
        if message is not UNSET:
            field_dict["Message"] = message
        if references is not UNSET:
            field_dict["References"] = references

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.interview_import_reference import InterviewImportReference

        d = src_dict.copy()

        def _parse_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        code = _parse_code(d.pop("Code", UNSET))

        def _parse_message(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        message = _parse_message(d.pop("Message", UNSET))

        def _parse_references(data: object) -> Union[List["InterviewImportReference"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                references_type_0 = []
                _references_type_0 = data
                for references_type_0_item_data in _references_type_0:
                    references_type_0_item = InterviewImportReference.from_dict(references_type_0_item_data)

                    references_type_0.append(references_type_0_item)

                return references_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["InterviewImportReference"], None, Unset], data)

        references = _parse_references(d.pop("References", UNSET))

        panel_import_verification_error = cls(
            code=code,
            message=message,
            references=references,
        )

        return panel_import_verification_error
