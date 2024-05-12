from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.interview_api_view import InterviewApiView
from ...models.interview_status import InterviewStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    questionnaire_id: Union[Unset, str] = UNSET,
    questionnaire_version: Union[Unset, int] = UNSET,
    status: Union[Unset, InterviewStatus] = UNSET,
    responsible_name: Union[Unset, str] = UNSET,
    interview_id: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["questionnaireId"] = questionnaire_id

    params["questionnaireVersion"] = questionnaire_version

    json_status: Union[Unset, str] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["responsibleName"] = responsible_name

    params["interviewId"] = interview_id

    params["pageSize"] = page_size

    params["page"] = page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/interviews",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, InterviewApiView]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = InterviewApiView.from_dict(response.json())
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
) -> Response[Union[Any, InterviewApiView]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    questionnaire_id: Union[Unset, str] = UNSET,
    questionnaire_version: Union[Unset, int] = UNSET,
    status: Union[Unset, InterviewStatus] = UNSET,
    responsible_name: Union[Unset, str] = UNSET,
    interview_id: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = 10,
    page: Union[Unset, int] = 1,
) -> Response[Union[Any, InterviewApiView]]:
    """Gets list of interviews existing in the system

    Args:
        questionnaire_id (Union[Unset, str]):
        questionnaire_version (Union[Unset, int]):
        status (Union[Unset, InterviewStatus]):
        responsible_name (Union[Unset, str]):
        interview_id (Union[Unset, str]):
        page_size (Union[Unset, int]):  Default: 10.
        page (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, InterviewApiView]]
    """

    kwargs = _get_kwargs(
        questionnaire_id=questionnaire_id,
        questionnaire_version=questionnaire_version,
        status=status,
        responsible_name=responsible_name,
        interview_id=interview_id,
        page_size=page_size,
        page=page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    questionnaire_id: Union[Unset, str] = UNSET,
    questionnaire_version: Union[Unset, int] = UNSET,
    status: Union[Unset, InterviewStatus] = UNSET,
    responsible_name: Union[Unset, str] = UNSET,
    interview_id: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = 10,
    page: Union[Unset, int] = 1,
) -> Optional[Union[Any, InterviewApiView]]:
    """Gets list of interviews existing in the system

    Args:
        questionnaire_id (Union[Unset, str]):
        questionnaire_version (Union[Unset, int]):
        status (Union[Unset, InterviewStatus]):
        responsible_name (Union[Unset, str]):
        interview_id (Union[Unset, str]):
        page_size (Union[Unset, int]):  Default: 10.
        page (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, InterviewApiView]
    """

    return sync_detailed(
        client=client,
        questionnaire_id=questionnaire_id,
        questionnaire_version=questionnaire_version,
        status=status,
        responsible_name=responsible_name,
        interview_id=interview_id,
        page_size=page_size,
        page=page,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    questionnaire_id: Union[Unset, str] = UNSET,
    questionnaire_version: Union[Unset, int] = UNSET,
    status: Union[Unset, InterviewStatus] = UNSET,
    responsible_name: Union[Unset, str] = UNSET,
    interview_id: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = 10,
    page: Union[Unset, int] = 1,
) -> Response[Union[Any, InterviewApiView]]:
    """Gets list of interviews existing in the system

    Args:
        questionnaire_id (Union[Unset, str]):
        questionnaire_version (Union[Unset, int]):
        status (Union[Unset, InterviewStatus]):
        responsible_name: Union[Unset, str] = UNSET,
        interview_id (Union[Unset, str]):
        page_size (Union[Unset, int]):  Default: 10.
        page (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, InterviewApiView]]
    """

    kwargs = _get_kwargs(
        questionnaire_id=questionnaire_id,
        questionnaire_version=questionnaire_version,
        status=status,
        responsible_name=responsible_name,
        interview_id=interview_id,
        page_size=page_size,
        page=page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    questionnaire_id: Union[Unset, str] = UNSET,
    questionnaire_version: Union[Unset, int] = UNSET,
    status: Union[Unset, InterviewStatus] = UNSET,
    responsible_name: Union[Unset, str] = UNSET,
    interview_id: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = 10,
    page: Union[Unset, int] = 1,
) -> Optional[Union[Any, InterviewApiView]]:
    """Gets list of interviews existing in the system

    Args:
        questionnaire_id (Union[Unset, str]):
        questionnaire_version (Union[Unset, int]):
        status (Union[Unset, InterviewStatus]):
        responsible_name: Union[Unset, str] = UNSET,
        interview_id (Union[Unset, str]):
        page_size (Union[Unset, int]):  Default: 10.
        page (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, InterviewApiView]
    """

    return (
        await asyncio_detailed(
            client=client,
            questionnaire_id=questionnaire_id,
            questionnaire_version=questionnaire_version,
            status=status,
            responsible_name=responsible_name,
            interview_id=interview_id,
            page_size=page_size,
            page=page,
        )
    ).parsed
