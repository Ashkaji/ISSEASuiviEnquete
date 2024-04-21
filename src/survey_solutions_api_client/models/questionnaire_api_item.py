import datetime
from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="QuestionnaireApiItem")


@_attrs_define
class QuestionnaireApiItem:
    """
    Attributes:
        questionnaire_id (str):
        version (int):
        title (str):
        variable (str):
        last_entry_date (datetime.datetime):
        questionnaire_identity (Union[None, Unset, str]):
        is_audio_recording_enabled (Union[Unset, bool]):
        web_mode_enabled (Union[Unset, bool]):
    """

    questionnaire_id: str
    version: int
    title: str
    variable: str
    last_entry_date: datetime.datetime
    questionnaire_identity: Union[None, Unset, str] = UNSET
    is_audio_recording_enabled: Union[Unset, bool] = UNSET
    web_mode_enabled: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        questionnaire_id = self.questionnaire_id

        version = self.version

        title = self.title

        variable = self.variable

        last_entry_date = self.last_entry_date.isoformat()

        questionnaire_identity: Union[None, Unset, str]
        if isinstance(self.questionnaire_identity, Unset):
            questionnaire_identity = UNSET
        else:
            questionnaire_identity = self.questionnaire_identity

        is_audio_recording_enabled = self.is_audio_recording_enabled

        web_mode_enabled = self.web_mode_enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "QuestionnaireId": questionnaire_id,
                "Version": version,
                "Title": title,
                "Variable": variable,
                "LastEntryDate": last_entry_date,
            }
        )
        if questionnaire_identity is not UNSET:
            field_dict["QuestionnaireIdentity"] = questionnaire_identity
        if is_audio_recording_enabled is not UNSET:
            field_dict["IsAudioRecordingEnabled"] = is_audio_recording_enabled
        if web_mode_enabled is not UNSET:
            field_dict["WebModeEnabled"] = web_mode_enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        questionnaire_id = d.pop("QuestionnaireId")

        version = d.pop("Version")

        title = d.pop("Title")

        variable = d.pop("Variable")

        last_entry_date = isoparse(d.pop("LastEntryDate"))

        def _parse_questionnaire_identity(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        questionnaire_identity = _parse_questionnaire_identity(d.pop("QuestionnaireIdentity", UNSET))

        is_audio_recording_enabled = d.pop("IsAudioRecordingEnabled", UNSET)

        web_mode_enabled = d.pop("WebModeEnabled", UNSET)

        questionnaire_api_item = cls(
            questionnaire_id=questionnaire_id,
            version=version,
            title=title,
            variable=variable,
            last_entry_date=last_entry_date,
            questionnaire_identity=questionnaire_identity,
            is_audio_recording_enabled=is_audio_recording_enabled,
            web_mode_enabled=web_mode_enabled,
        )

        return questionnaire_api_item
