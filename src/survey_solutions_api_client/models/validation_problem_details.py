from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.validation_problem_details_errors_type_0 import ValidationProblemDetailsErrorsType0
    from ..models.validation_problem_details_extensions_type_0 import ValidationProblemDetailsExtensionsType0


T = TypeVar("T", bound="ValidationProblemDetails")


@_attrs_define
class ValidationProblemDetails:
    """
    Attributes:
        errors (Union['ValidationProblemDetailsErrorsType0', None, Unset]):
        type (Union[None, Unset, str]):
        title (Union[None, Unset, str]):
        status (Union[None, Unset, int]):
        detail (Union[None, Unset, str]):
        instance (Union[None, Unset, str]):
        extensions (Union['ValidationProblemDetailsExtensionsType0', None, Unset]):
    """

    errors: Union["ValidationProblemDetailsErrorsType0", None, Unset] = UNSET
    type: Union[None, Unset, str] = UNSET
    title: Union[None, Unset, str] = UNSET
    status: Union[None, Unset, int] = UNSET
    detail: Union[None, Unset, str] = UNSET
    instance: Union[None, Unset, str] = UNSET
    extensions: Union["ValidationProblemDetailsExtensionsType0", None, Unset] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from ..models.validation_problem_details_errors_type_0 import ValidationProblemDetailsErrorsType0
        from ..models.validation_problem_details_extensions_type_0 import ValidationProblemDetailsExtensionsType0

        errors: Union[Dict[str, Any], None, Unset]
        if isinstance(self.errors, Unset):
            errors = UNSET
        elif isinstance(self.errors, ValidationProblemDetailsErrorsType0):
            errors = self.errors.to_dict()
        else:
            errors = self.errors

        type: Union[None, Unset, str]
        if isinstance(self.type, Unset):
            type = UNSET
        else:
            type = self.type

        title: Union[None, Unset, str]
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        status: Union[None, Unset, int]
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        detail: Union[None, Unset, str]
        if isinstance(self.detail, Unset):
            detail = UNSET
        else:
            detail = self.detail

        instance: Union[None, Unset, str]
        if isinstance(self.instance, Unset):
            instance = UNSET
        else:
            instance = self.instance

        extensions: Union[Dict[str, Any], None, Unset]
        if isinstance(self.extensions, Unset):
            extensions = UNSET
        elif isinstance(self.extensions, ValidationProblemDetailsExtensionsType0):
            extensions = self.extensions.to_dict()
        else:
            extensions = self.extensions

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if errors is not UNSET:
            field_dict["Errors"] = errors
        if type is not UNSET:
            field_dict["Type"] = type
        if title is not UNSET:
            field_dict["Title"] = title
        if status is not UNSET:
            field_dict["Status"] = status
        if detail is not UNSET:
            field_dict["Detail"] = detail
        if instance is not UNSET:
            field_dict["Instance"] = instance
        if extensions is not UNSET:
            field_dict["Extensions"] = extensions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.validation_problem_details_errors_type_0 import ValidationProblemDetailsErrorsType0
        from ..models.validation_problem_details_extensions_type_0 import ValidationProblemDetailsExtensionsType0

        d = src_dict.copy()

        def _parse_errors(data: object) -> Union["ValidationProblemDetailsErrorsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                errors_type_0 = ValidationProblemDetailsErrorsType0.from_dict(data)

                return errors_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ValidationProblemDetailsErrorsType0", None, Unset], data)

        errors = _parse_errors(d.pop("Errors", UNSET))

        def _parse_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        type = _parse_type(d.pop("Type", UNSET))

        def _parse_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        title = _parse_title(d.pop("Title", UNSET))

        def _parse_status(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        status = _parse_status(d.pop("Status", UNSET))

        def _parse_detail(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        detail = _parse_detail(d.pop("Detail", UNSET))

        def _parse_instance(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        instance = _parse_instance(d.pop("Instance", UNSET))

        def _parse_extensions(data: object) -> Union["ValidationProblemDetailsExtensionsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                extensions_type_0 = ValidationProblemDetailsExtensionsType0.from_dict(data)

                return extensions_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ValidationProblemDetailsExtensionsType0", None, Unset], data)

        extensions = _parse_extensions(d.pop("Extensions", UNSET))

        validation_problem_details = cls(
            errors=errors,
            type=type,
            title=title,
            status=status,
            detail=detail,
            instance=instance,
            extensions=extensions,
        )

        return validation_problem_details
