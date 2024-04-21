import datetime
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.export_interview_type import ExportInterviewType
from ..models.export_status import ExportStatus
from ..models.export_type import ExportType
from ..models.external_storage_type import ExternalStorageType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.export_job_links import ExportJobLinks


T = TypeVar("T", bound="ExportProcess")


@_attrs_define
class ExportProcess:
    """
    Attributes:
        export_type (ExportType):
        questionnaire_id (str): Questionnaire id in format [QuestionnaireGuid$Version]
        interview_status (ExportInterviewType):
        job_id (Union[Unset, int]): Export process id
        export_status (Union[Unset, ExportStatus]):
        start_date (Union[None, Unset, datetime.datetime]): Export process stated date
        complete_date (Union[None, Unset, datetime.datetime]): Export process completed date
        create_date (Union[None, Unset, datetime.datetime]): Export process stated date
        progress (Union[Unset, int]): Progress of export in percents
        eta (Union[None, Unset, str]): Estimated time to finish of export
        error (Union[None, Unset, str]):
        links (Union[Unset, ExportJobLinks]):
        has_export_file (Union[Unset, bool]): True, if export process is finished and exported file ready for download,
            otherwise false
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
    job_id: Union[Unset, int] = UNSET
    export_status: Union[Unset, ExportStatus] = UNSET
    start_date: Union[None, Unset, datetime.datetime] = UNSET
    complete_date: Union[None, Unset, datetime.datetime] = UNSET
    create_date: Union[None, Unset, datetime.datetime] = UNSET
    progress: Union[Unset, int] = UNSET
    eta: Union[None, Unset, str] = UNSET
    error: Union[None, Unset, str] = UNSET
    links: Union[Unset, "ExportJobLinks"] = UNSET
    has_export_file: Union[Unset, bool] = UNSET
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

        job_id = self.job_id

        export_status: Union[Unset, str] = UNSET
        if not isinstance(self.export_status, Unset):
            export_status = self.export_status.value

        start_date: Union[None, Unset, str]
        if isinstance(self.start_date, Unset):
            start_date = UNSET
        elif isinstance(self.start_date, datetime.datetime):
            start_date = self.start_date.isoformat()
        else:
            start_date = self.start_date

        complete_date: Union[None, Unset, str]
        if isinstance(self.complete_date, Unset):
            complete_date = UNSET
        elif isinstance(self.complete_date, datetime.datetime):
            complete_date = self.complete_date.isoformat()
        else:
            complete_date = self.complete_date

        create_date: Union[None, Unset, str]
        if isinstance(self.create_date, Unset):
            create_date = UNSET
        elif isinstance(self.create_date, datetime.datetime):
            create_date = self.create_date.isoformat()
        else:
            create_date = self.create_date

        progress = self.progress

        eta: Union[None, Unset, str]
        if isinstance(self.eta, Unset):
            eta = UNSET
        else:
            eta = self.eta

        error: Union[None, Unset, str]
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        has_export_file = self.has_export_file

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
        if job_id is not UNSET:
            field_dict["JobId"] = job_id
        if export_status is not UNSET:
            field_dict["ExportStatus"] = export_status
        if start_date is not UNSET:
            field_dict["StartDate"] = start_date
        if complete_date is not UNSET:
            field_dict["CompleteDate"] = complete_date
        if create_date is not UNSET:
            field_dict["CreateDate"] = create_date
        if progress is not UNSET:
            field_dict["Progress"] = progress
        if eta is not UNSET:
            field_dict["ETA"] = eta
        if error is not UNSET:
            field_dict["Error"] = error
        if links is not UNSET:
            field_dict["Links"] = links
        if has_export_file is not UNSET:
            field_dict["HasExportFile"] = has_export_file
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
        from ..models.export_job_links import ExportJobLinks

        d = src_dict.copy()
        export_type = ExportType(d.pop("ExportType"))

        questionnaire_id = d.pop("QuestionnaireId")

        interview_status = ExportInterviewType(d.pop("InterviewStatus"))

        job_id = d.pop("JobId", UNSET)

        _export_status = d.pop("ExportStatus", UNSET)
        export_status: Union[Unset, ExportStatus]
        if isinstance(_export_status, Unset):
            export_status = UNSET
        else:
            export_status = ExportStatus(_export_status)

        def _parse_start_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_date_type_0 = isoparse(data)

                return start_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        start_date = _parse_start_date(d.pop("StartDate", UNSET))

        def _parse_complete_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                complete_date_type_0 = isoparse(data)

                return complete_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        complete_date = _parse_complete_date(d.pop("CompleteDate", UNSET))

        def _parse_create_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                create_date_type_0 = isoparse(data)

                return create_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        create_date = _parse_create_date(d.pop("CreateDate", UNSET))

        progress = d.pop("Progress", UNSET)

        def _parse_eta(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        eta = _parse_eta(d.pop("ETA", UNSET))

        def _parse_error(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        error = _parse_error(d.pop("Error", UNSET))

        _links = d.pop("Links", UNSET)
        links: Union[Unset, ExportJobLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = ExportJobLinks.from_dict(_links)

        has_export_file = d.pop("HasExportFile", UNSET)

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

        export_process = cls(
            export_type=export_type,
            questionnaire_id=questionnaire_id,
            interview_status=interview_status,
            job_id=job_id,
            export_status=export_status,
            start_date=start_date,
            complete_date=complete_date,
            create_date=create_date,
            progress=progress,
            eta=eta,
            error=error,
            links=links,
            has_export_file=has_export_file,
            from_=from_,
            to=to,
            access_token=access_token,
            refresh_token=refresh_token,
            storage_type=storage_type,
            translation_id=translation_id,
            include_meta=include_meta,
        )

        return export_process
