import datetime
from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AssignmentViewItem")


@_attrs_define
class AssignmentViewItem:
    """
    Attributes:
        id (Union[Unset, int]):
        responsible_id (Union[Unset, str]):
        responsible_name (Union[None, Unset, str]): Name of the responsible person
            Can be used for ordering
        questionnaire_id (Union[None, Unset, str]): Questionnaire Id
        interviews_count (Union[Unset, int]): Quantity of submitted interviews for this assignment
            Can be used for ordering
        quantity (Union[None, Unset, int]): Maximum allowed quantity of interviews that can be created from this
            assignment
            Can be used for ordering
        archived (Union[Unset, bool]): Archived status to filter by. True or False
        created_at_utc (Union[Unset, datetime.datetime]): Date (UTC) when assignment were created
            Can be used for ordering
        updated_at_utc (Union[Unset, datetime.datetime]): Last Update Date (UTC) of assignment
            Can be used for ordering
        email (Union[None, Unset, str]):
        password (Union[None, Unset, str]):
        web_mode (Union[None, Unset, bool]):
        received_by_tablet_at_utc (Union[None, Unset, datetime.datetime]): Represents date (UTC) when assignment was
            received by tablet
        is_audio_recording_enabled (Union[Unset, bool]): Determines if interview from this assignment must record voice
            during interview (only on tablet)
    """

    id: Union[Unset, int] = UNSET
    responsible_id: Union[Unset, str] = UNSET
    responsible_name: Union[None, Unset, str] = UNSET
    questionnaire_id: Union[None, Unset, str] = UNSET
    interviews_count: Union[Unset, int] = UNSET
    quantity: Union[None, Unset, int] = UNSET
    archived: Union[Unset, bool] = UNSET
    created_at_utc: Union[Unset, datetime.datetime] = UNSET
    updated_at_utc: Union[Unset, datetime.datetime] = UNSET
    email: Union[None, Unset, str] = UNSET
    password: Union[None, Unset, str] = UNSET
    web_mode: Union[None, Unset, bool] = UNSET
    received_by_tablet_at_utc: Union[None, Unset, datetime.datetime] = UNSET
    is_audio_recording_enabled: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        responsible_id = self.responsible_id

        responsible_name: Union[None, Unset, str]
        if isinstance(self.responsible_name, Unset):
            responsible_name = UNSET
        else:
            responsible_name = self.responsible_name

        questionnaire_id: Union[None, Unset, str]
        if isinstance(self.questionnaire_id, Unset):
            questionnaire_id = UNSET
        else:
            questionnaire_id = self.questionnaire_id

        interviews_count = self.interviews_count

        quantity: Union[None, Unset, int]
        if isinstance(self.quantity, Unset):
            quantity = UNSET
        else:
            quantity = self.quantity

        archived = self.archived

        created_at_utc: Union[Unset, str] = UNSET
        if not isinstance(self.created_at_utc, Unset):
            created_at_utc = self.created_at_utc.isoformat()

        updated_at_utc: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at_utc, Unset):
            updated_at_utc = self.updated_at_utc.isoformat()

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

        web_mode: Union[None, Unset, bool]
        if isinstance(self.web_mode, Unset):
            web_mode = UNSET
        else:
            web_mode = self.web_mode

        received_by_tablet_at_utc: Union[None, Unset, str]
        if isinstance(self.received_by_tablet_at_utc, Unset):
            received_by_tablet_at_utc = UNSET
        elif isinstance(self.received_by_tablet_at_utc, datetime.datetime):
            received_by_tablet_at_utc = self.received_by_tablet_at_utc.isoformat()
        else:
            received_by_tablet_at_utc = self.received_by_tablet_at_utc

        is_audio_recording_enabled = self.is_audio_recording_enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if responsible_id is not UNSET:
            field_dict["ResponsibleId"] = responsible_id
        if responsible_name is not UNSET:
            field_dict["ResponsibleName"] = responsible_name
        if questionnaire_id is not UNSET:
            field_dict["QuestionnaireId"] = questionnaire_id
        if interviews_count is not UNSET:
            field_dict["InterviewsCount"] = interviews_count
        if quantity is not UNSET:
            field_dict["Quantity"] = quantity
        if archived is not UNSET:
            field_dict["Archived"] = archived
        if created_at_utc is not UNSET:
            field_dict["CreatedAtUtc"] = created_at_utc
        if updated_at_utc is not UNSET:
            field_dict["UpdatedAtUtc"] = updated_at_utc
        if email is not UNSET:
            field_dict["Email"] = email
        if password is not UNSET:
            field_dict["Password"] = password
        if web_mode is not UNSET:
            field_dict["WebMode"] = web_mode
        if received_by_tablet_at_utc is not UNSET:
            field_dict["ReceivedByTabletAtUtc"] = received_by_tablet_at_utc
        if is_audio_recording_enabled is not UNSET:
            field_dict["IsAudioRecordingEnabled"] = is_audio_recording_enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        responsible_id = d.pop("ResponsibleId", UNSET)

        def _parse_responsible_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        responsible_name = _parse_responsible_name(d.pop("ResponsibleName", UNSET))

        def _parse_questionnaire_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        questionnaire_id = _parse_questionnaire_id(d.pop("QuestionnaireId", UNSET))

        interviews_count = d.pop("InterviewsCount", UNSET)

        def _parse_quantity(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        quantity = _parse_quantity(d.pop("Quantity", UNSET))

        archived = d.pop("Archived", UNSET)

        _created_at_utc = d.pop("CreatedAtUtc", UNSET)
        created_at_utc: Union[Unset, datetime.datetime]
        if isinstance(_created_at_utc, Unset):
            created_at_utc = UNSET
        else:
            created_at_utc = isoparse(_created_at_utc)

        _updated_at_utc = d.pop("UpdatedAtUtc", UNSET)
        updated_at_utc: Union[Unset, datetime.datetime]
        if isinstance(_updated_at_utc, Unset):
            updated_at_utc = UNSET
        else:
            updated_at_utc = isoparse(_updated_at_utc)

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

        def _parse_web_mode(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        web_mode = _parse_web_mode(d.pop("WebMode", UNSET))

        def _parse_received_by_tablet_at_utc(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                received_by_tablet_at_utc_type_0 = isoparse(data)

                return received_by_tablet_at_utc_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        received_by_tablet_at_utc = _parse_received_by_tablet_at_utc(d.pop("ReceivedByTabletAtUtc", UNSET))

        is_audio_recording_enabled = d.pop("IsAudioRecordingEnabled", UNSET)

        assignment_view_item = cls(
            id=id,
            responsible_id=responsible_id,
            responsible_name=responsible_name,
            questionnaire_id=questionnaire_id,
            interviews_count=interviews_count,
            quantity=quantity,
            archived=archived,
            created_at_utc=created_at_utc,
            updated_at_utc=updated_at_utc,
            email=email,
            password=password,
            web_mode=web_mode,
            received_by_tablet_at_utc=received_by_tablet_at_utc,
            is_audio_recording_enabled=is_audio_recording_enabled,
        )

        return assignment_view_item
