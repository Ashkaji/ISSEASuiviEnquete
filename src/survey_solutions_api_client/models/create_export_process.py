import datetime
from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.export_interview_type import ExportInterviewType
from ..models.export_type import ExportType
from ..models.external_storage_type import ExternalStorageType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateExportProcess")


@_attrs_define
class CreateExportProcess:
    """
    Attributes:
        export_type (ExportType):
        questionnaire_id (str): Questionnaire id in format [QuestionnaireGuid$Version]
        interview_status (ExportInterviewType):
        from_ (Union[None, Unset, datetime.datetime]): Started date for timeframe of exported interviews (when change
            was done to an interview). Should be in UTC date
        to (Union[None, Unset, datetime.datetime]): Finished date for timeframe of exported interviews (when change was
            done to an interview). Should be in UTC date
        access_token (Union[None, Unset, str]): Access token to external storage
        refresh_token (Union[None, Unset, str]): Refresh token to external storage
        storage_type (Union[Unset, ExternalStorageType]):
        translation_id (Union[None, Unset, str]): Translation Id of the questionnaire
        include_meta (Union[None, Unset, bool]):
    """

    export_type: ExportType
    questionnaire_id: str
    interview_status: ExportInterviewType
    from_: Union[None, Unset, datetime.datetime] = UNSET
    to: Union[None, Unset, datetime.datetime] = UNSET
    access_token: Union[None, Unset, str] = UNSET
    refresh_token: Union[None, Unset, str] = UNSET
    storage_type: Union[Unset, ExternalStorageType] = UNSET
    translation_id: Union[None, Unset, str] = UNSET
    include_meta: Union[None, Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        export_type = self.export_type.value

        questionnaire_id = self.questionnaire_id

        interview_status = self.interview_status.value

        from_: Union[None, Unset, str]
        if isinstance(self.from_, Unset):
            from_ = UNSET
        elif isinstance(self.from_, datetime.datetime):
            from_ = self.from_.isoformat()
        else:
            from_ = self.from_

        to: Union[None, Unset, str]
        if isinstance(self.to, Unset):
            to = UNSET
        elif isinstance(self.to, datetime.datetime):
            to = self.to.isoformat()
        else:
            to = self.to

        access_token: Union[None, Unset, str]
        if isinstance(self.access_token, Unset):
            access_token = UNSET
        else:
            access_token = self.access_token

        refresh_token: Union[None, Unset, str]
        if isinstance(self.refresh_token, Unset):
            refresh_token = UNSET
        else:
            refresh_token = self.refresh_token

        storage_type: Union[Unset, str] = UNSET
        if not isinstance(self.storage_type, Unset):
            storage_type = self.storage_type.value

        translation_id: Union[None, Unset, str]
        if isinstance(self.translation_id, Unset):
            translation_id = UNSET
        else:
            translation_id = self.translation_id

        include_meta: Union[None, Unset, bool]
        if isinstance(self.include_meta, Unset):
            include_meta = UNSET
        else:
            include_meta = self.include_meta

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "ExportType": export_type,
                "QuestionnaireId": questionnaire_id,
                "InterviewStatus": interview_status,
            }
        )
        if from_ is not UNSET:
            field_dict["From"] = from_
        if to is not UNSET:
            field_dict["To"] = to
        if access_token is not UNSET:
            field_dict["AccessToken"] = access_token
        if refresh_token is not UNSET:
            field_dict["RefreshToken"] = refresh_token
        if storage_type is not UNSET:
            field_dict["StorageType"] = storage_type
        if translation_id is not UNSET:
            field_dict["TranslationId"] = translation_id
        if include_meta is not UNSET:
            field_dict["IncludeMeta"] = include_meta

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        export_type = ExportType(d.pop("ExportType"))

        questionnaire_id = d.pop("QuestionnaireId")

        interview_status = ExportInterviewType(d.pop("InterviewStatus"))

        def _parse_from_(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                from_type_0 = isoparse(data)

                return from_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        from_ = _parse_from_(d.pop("From", UNSET))

        def _parse_to(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                to_type_0 = isoparse(data)

                return to_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        to = _parse_to(d.pop("To", UNSET))

        def _parse_access_token(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        access_token = _parse_access_token(d.pop("AccessToken", UNSET))

        def _parse_refresh_token(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        refresh_token = _parse_refresh_token(d.pop("RefreshToken", UNSET))

        _storage_type = d.pop("StorageType", UNSET)
        storage_type: Union[Unset, ExternalStorageType]
        if isinstance(_storage_type, Unset):
            storage_type = UNSET
        else:
            storage_type = ExternalStorageType(_storage_type)

        def _parse_translation_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        translation_id = _parse_translation_id(d.pop("TranslationId", UNSET))

        def _parse_include_meta(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        include_meta = _parse_include_meta(d.pop("IncludeMeta", UNSET))

        create_export_process = cls(
            export_type=export_type,
            questionnaire_id=questionnaire_id,
            interview_status=interview_status,
            from_=from_,
            to=to,
            access_token=access_token,
            refresh_token=refresh_token,
            storage_type=storage_type,
            translation_id=translation_id,
            include_meta=include_meta,
        )

        return create_export_process
