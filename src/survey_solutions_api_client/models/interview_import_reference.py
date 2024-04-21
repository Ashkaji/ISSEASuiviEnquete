from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.preloaded_data_verification_reference_type import PreloadedDataVerificationReferenceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="InterviewImportReference")


@_attrs_define
class InterviewImportReference:
    """
    Attributes:
        type (Union[Unset, PreloadedDataVerificationReferenceType]):
        column (Union[None, Unset, str]):
        row (Union[None, Unset, int]):
        content (Union[None, Unset, str]):
        data_file (Union[None, Unset, str]):
    """

    type: Union[Unset, PreloadedDataVerificationReferenceType] = UNSET
    column: Union[None, Unset, str] = UNSET
    row: Union[None, Unset, int] = UNSET
    content: Union[None, Unset, str] = UNSET
    data_file: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        column: Union[None, Unset, str]
        if isinstance(self.column, Unset):
            column = UNSET
        else:
            column = self.column

        row: Union[None, Unset, int]
        if isinstance(self.row, Unset):
            row = UNSET
        else:
            row = self.row

        content: Union[None, Unset, str]
        if isinstance(self.content, Unset):
            content = UNSET
        else:
            content = self.content

        data_file: Union[None, Unset, str]
        if isinstance(self.data_file, Unset):
            data_file = UNSET
        else:
            data_file = self.data_file

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if type is not UNSET:
            field_dict["Type"] = type
        if column is not UNSET:
            field_dict["Column"] = column
        if row is not UNSET:
            field_dict["Row"] = row
        if content is not UNSET:
            field_dict["Content"] = content
        if data_file is not UNSET:
            field_dict["DataFile"] = data_file

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _type = d.pop("Type", UNSET)
        type: Union[Unset, PreloadedDataVerificationReferenceType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = PreloadedDataVerificationReferenceType(_type)

        def _parse_column(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        column = _parse_column(d.pop("Column", UNSET))

        def _parse_row(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        row = _parse_row(d.pop("Row", UNSET))

        def _parse_content(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        content = _parse_content(d.pop("Content", UNSET))

        def _parse_data_file(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        data_file = _parse_data_file(d.pop("DataFile", UNSET))

        interview_import_reference = cls(
            type=type,
            column=column,
            row=row,
            content=content,
            data_file=data_file,
        )

        return interview_import_reference
