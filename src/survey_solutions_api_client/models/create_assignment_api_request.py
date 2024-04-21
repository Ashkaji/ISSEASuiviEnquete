from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.assignment_identifying_data_item import AssignmentIdentifyingDataItem


T = TypeVar("T", bound="CreateAssignmentApiRequest")


@_attrs_define
class CreateAssignmentApiRequest:
    """
    Attributes:
        responsible (str):
        questionnaire_id (str): QuestionnaireId for assignment
        identifying_data (List['AssignmentIdentifyingDataItem']):
        quantity (Union[None, Unset, int]): Maximum number of allowed to create assignments
        email (Union[None, Unset, str]):
        password (Union[None, Unset, str]):
        web_mode (Union[Unset, bool]):
        is_audio_recording_enabled (Union[None, Unset, bool]):
        comments (Union[None, Unset, str]):
        protected_variables (Union[List[str], None, Unset]): List of protected variables
    """

    responsible: str
    questionnaire_id: str
    identifying_data: List["AssignmentIdentifyingDataItem"]
    quantity: Union[None, Unset, int] = UNSET
    email: Union[None, Unset, str] = UNSET
    password: Union[None, Unset, str] = UNSET
    web_mode: Union[Unset, bool] = UNSET
    is_audio_recording_enabled: Union[None, Unset, bool] = UNSET
    comments: Union[None, Unset, str] = UNSET
    protected_variables: Union[List[str], None, Unset] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        responsible = self.responsible

        questionnaire_id = self.questionnaire_id

        identifying_data = []
        for identifying_data_item_data in self.identifying_data:
            identifying_data_item = identifying_data_item_data.to_dict()
            identifying_data.append(identifying_data_item)

        quantity: Union[None, Unset, int]
        if isinstance(self.quantity, Unset):
            quantity = UNSET
        else:
            quantity = self.quantity

        email: Union[None, Unset, str]
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        password: Union[None, Unset, str]
        if isinstance(self.password, Unset):
            password = UNSET
        else:
            password = self.password

        web_mode = self.web_mode

        is_audio_recording_enabled: Union[None, Unset, bool]
        if isinstance(self.is_audio_recording_enabled, Unset):
            is_audio_recording_enabled = UNSET
        else:
            is_audio_recording_enabled = self.is_audio_recording_enabled

        comments: Union[None, Unset, str]
        if isinstance(self.comments, Unset):
            comments = UNSET
        else:
            comments = self.comments

        protected_variables: Union[List[str], None, Unset]
        if isinstance(self.protected_variables, Unset):
            protected_variables = UNSET
        elif isinstance(self.protected_variables, list):
            protected_variables = self.protected_variables

        else:
            protected_variables = self.protected_variables

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "Responsible": responsible,
                "QuestionnaireId": questionnaire_id,
                "IdentifyingData": identifying_data,
            }
        )
        if quantity is not UNSET:
            field_dict["Quantity"] = quantity
        if email is not UNSET:
            field_dict["Email"] = email
        if password is not UNSET:
            field_dict["Password"] = password
        if web_mode is not UNSET:
            field_dict["WebMode"] = web_mode
        if is_audio_recording_enabled is not UNSET:
            field_dict["IsAudioRecordingEnabled"] = is_audio_recording_enabled
        if comments is not UNSET:
            field_dict["Comments"] = comments
        if protected_variables is not UNSET:
            field_dict["ProtectedVariables"] = protected_variables

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.assignment_identifying_data_item import AssignmentIdentifyingDataItem

        d = src_dict.copy()
        responsible = d.pop("Responsible")

        questionnaire_id = d.pop("QuestionnaireId")

        identifying_data = []
        _identifying_data = d.pop("IdentifyingData")
        for identifying_data_item_data in _identifying_data:
            identifying_data_item = AssignmentIdentifyingDataItem.from_dict(identifying_data_item_data)

            identifying_data.append(identifying_data_item)

        def _parse_quantity(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        quantity = _parse_quantity(d.pop("Quantity", UNSET))

        def _parse_email(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        email = _parse_email(d.pop("Email", UNSET))

        def _parse_password(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        password = _parse_password(d.pop("Password", UNSET))

        web_mode = d.pop("WebMode", UNSET)

        def _parse_is_audio_recording_enabled(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_audio_recording_enabled = _parse_is_audio_recording_enabled(d.pop("IsAudioRecordingEnabled", UNSET))

        def _parse_comments(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        comments = _parse_comments(d.pop("Comments", UNSET))

        def _parse_protected_variables(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                protected_variables_type_0 = cast(List[str], data)

                return protected_variables_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        protected_variables = _parse_protected_variables(d.pop("ProtectedVariables", UNSET))

        create_assignment_api_request = cls(
            responsible=responsible,
            questionnaire_id=questionnaire_id,
            identifying_data=identifying_data,
            quantity=quantity,
            email=email,
            password=password,
            web_mode=web_mode,
            is_audio_recording_enabled=is_audio_recording_enabled,
            comments=comments,
            protected_variables=protected_variables,
        )

        return create_assignment_api_request
