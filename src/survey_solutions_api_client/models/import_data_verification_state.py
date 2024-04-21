from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.panel_import_verification_error import PanelImportVerificationError


T = TypeVar("T", bound="ImportDataVerificationState")


@_attrs_define
class ImportDataVerificationState:
    """
    Attributes:
        errors (Union[List['PanelImportVerificationError'], None, Unset]):
        was_responsible_provided (Union[Unset, bool]):
        entities_count (Union[Unset, int]):
        enumerators_count (Union[Unset, int]):
        supervisors_count (Union[Unset, int]):
        file_name (Union[None, Unset, str]):
    """

    errors: Union[List["PanelImportVerificationError"], None, Unset] = UNSET
    was_responsible_provided: Union[Unset, bool] = UNSET
    entities_count: Union[Unset, int] = UNSET
    enumerators_count: Union[Unset, int] = UNSET
    supervisors_count: Union[Unset, int] = UNSET
    file_name: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        errors: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.errors, Unset):
            errors = UNSET
        elif isinstance(self.errors, list):
            errors = []
            for errors_type_0_item_data in self.errors:
                errors_type_0_item = errors_type_0_item_data.to_dict()
                errors.append(errors_type_0_item)

        else:
            errors = self.errors

        was_responsible_provided = self.was_responsible_provided

        entities_count = self.entities_count

        enumerators_count = self.enumerators_count

        supervisors_count = self.supervisors_count

        file_name: Union[None, Unset, str]
        if isinstance(self.file_name, Unset):
            file_name = UNSET
        else:
            file_name = self.file_name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if errors is not UNSET:
            field_dict["Errors"] = errors
        if was_responsible_provided is not UNSET:
            field_dict["WasResponsibleProvided"] = was_responsible_provided
        if entities_count is not UNSET:
            field_dict["EntitiesCount"] = entities_count
        if enumerators_count is not UNSET:
            field_dict["EnumeratorsCount"] = enumerators_count
        if supervisors_count is not UNSET:
            field_dict["SupervisorsCount"] = supervisors_count
        if file_name is not UNSET:
            field_dict["FileName"] = file_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.panel_import_verification_error import PanelImportVerificationError

        d = src_dict.copy()

        def _parse_errors(data: object) -> Union[List["PanelImportVerificationError"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                errors_type_0 = []
                _errors_type_0 = data
                for errors_type_0_item_data in _errors_type_0:
                    errors_type_0_item = PanelImportVerificationError.from_dict(errors_type_0_item_data)

                    errors_type_0.append(errors_type_0_item)

                return errors_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["PanelImportVerificationError"], None, Unset], data)

        errors = _parse_errors(d.pop("Errors", UNSET))

        was_responsible_provided = d.pop("WasResponsibleProvided", UNSET)

        entities_count = d.pop("EntitiesCount", UNSET)

        enumerators_count = d.pop("EnumeratorsCount", UNSET)

        supervisors_count = d.pop("SupervisorsCount", UNSET)

        def _parse_file_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        file_name = _parse_file_name(d.pop("FileName", UNSET))

        import_data_verification_state = cls(
            errors=errors,
            was_responsible_provided=was_responsible_provided,
            entities_count=entities_count,
            enumerators_count=enumerators_count,
            supervisors_count=supervisors_count,
            file_name=file_name,
        )

        return import_data_verification_state
