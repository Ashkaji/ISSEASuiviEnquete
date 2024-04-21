from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.export_interview_type import ExportInterviewType
from ...models.export_process import ExportProcess
from ...models.export_status import ExportStatus
from ...models.export_type import ExportType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    export_type: Union[Unset, ExportType] = UNSET,
    interview_status: Union[Unset, ExportInterviewType] = UNSET,
    questionnaire_identity: Union[Unset, str] = UNSET,
    export_status: Union[Unset, ExportStatus] = UNSET,
    has_file: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_export_type: Union[Unset, str] = UNSET
    if not isinstance(export_type, Unset):
        json_export_type = export_type.value

    params["exportType"] = json_export_type

    json_interview_status: Union[Unset, str] = UNSET
    if not isinstance(interview_status, Unset):
        json_interview_status = interview_status.value

    params["interviewStatus"] = json_interview_status

    params["questionnaireIdentity"] = questionnaire_identity

    json_export_status: Union[Unset, str] = UNSET
    if not isinstance(export_status, Unset):
        json_export_status = export_status.value

    params["exportStatus"] = json_export_status

    params["hasFile"] = has_file

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/export",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, List["ExportProcess"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ExportProcess.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, List["ExportProcess"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    export_type: Union[Unset, ExportType] = UNSET,
    interview_status: Union[Unset, ExportInterviewType] = UNSET,
    questionnaire_identity: Union[Unset, str] = UNSET,
    export_status: Union[Unset, ExportStatus] = UNSET,
    has_file: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Response[Union[Any, List["ExportProcess"]]]:
    """Get list of export processes

    Args:
        export_type (Union[Unset, ExportType]):
        interview_status (Union[Unset, ExportInterviewType]):
        questionnaire_identity (Union[Unset, str]):
        export_status (Union[Unset, ExportStatus]):
        has_file (Union[Unset, bool]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['ExportProcess']]]
    """

    kwargs = _get_kwargs(
        export_type=export_type,
        interview_status=interview_status,
        questionnaire_identity=questionnaire_identity,
        export_status=export_status,
        has_file=has_file,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    export_type: Union[Unset, ExportType] = UNSET,
    interview_status: Union[Unset, ExportInterviewType] = UNSET,
    questionnaire_identity: Union[Unset, str] = UNSET,
    export_status: Union[Unset, ExportStatus] = UNSET,
    has_file: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, List["ExportProcess"]]]:
    """Get list of export processes

    Args:
        export_type (Union[Unset, ExportType]):
        interview_status (Union[Unset, ExportInterviewType]):
        questionnaire_identity (Union[Unset, str]):
        export_status (Union[Unset, ExportStatus]):
        has_file (Union[Unset, bool]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['ExportProcess']]
    """

    return sync_detailed(
        client=client,
        export_type=export_type,
        interview_status=interview_status,
        questionnaire_identity=questionnaire_identity,
        export_status=export_status,
        has_file=has_file,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    export_type: Union[Unset, ExportType] = UNSET,
    interview_status: Union[Unset, ExportInterviewType] = UNSET,
    questionnaire_identity: Union[Unset, str] = UNSET,
    export_status: Union[Unset, ExportStatus] = UNSET,
    has_file: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Response[Union[Any, List["ExportProcess"]]]:
    """Get list of export processes

    Args:
        export_type (Union[Unset, ExportType]):
        interview_status (Union[Unset, ExportInterviewType]):
        questionnaire_identity (Union[Unset, str]):
        export_status (Union[Unset, ExportStatus]):
        has_file (Union[Unset, bool]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['ExportProcess']]]
    """

    kwargs = _get_kwargs(
        export_type=export_type,
        interview_status=interview_status,
        questionnaire_identity=questionnaire_identity,
        export_status=export_status,
        has_file=has_file,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    export_type: Union[Unset, ExportType] = UNSET,
    interview_status: Union[Unset, ExportInterviewType] = UNSET,
    questionnaire_identity: Union[Unset, str] = UNSET,
    export_status: Union[Unset, ExportStatus] = UNSET,
    has_file: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, List["ExportProcess"]]]:
    """Get list of export processes

    Args:
        export_type (Union[Unset, ExportType]):
        interview_status (Union[Unset, ExportInterviewType]):
        questionnaire_identity (Union[Unset, str]):
        export_status (Union[Unset, ExportStatus]):
        has_file (Union[Unset, bool]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['ExportProcess']]
    """

    return (
        await asyncio_detailed(
            client=client,
            export_type=export_type,
            interview_status=interview_status,
            questionnaire_identity=questionnaire_identity,
            export_status=export_status,
            has_file=has_file,
            limit=limit,
            offset=offset,
        )
    ).parsed
