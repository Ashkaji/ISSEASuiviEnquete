from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.assignments_list_view import AssignmentsListView
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    search_by: Union[Unset, str] = UNSET,
    questionnaire_id: Union[Unset, str] = UNSET,
    responsible: Union[Unset, str] = UNSET,
    supervisor_id: Union[Unset, str] = UNSET,
    show_archive: Union[Unset, bool] = UNSET,
    order: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["SearchBy"] = search_by

    params["QuestionnaireId"] = questionnaire_id

    params["Responsible"] = responsible

    params["SupervisorId"] = supervisor_id

    params["ShowArchive"] = show_archive

    params["Order"] = order

    params["Offset"] = offset

    params["Limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/assignments",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, AssignmentsListView]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = AssignmentsListView.from_dict(response.json())

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
) -> Response[Union[Any, AssignmentsListView]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    search_by: Union[Unset, str] = UNSET,
    questionnaire_id: Union[Unset, str] = UNSET,
    responsible: Union[Unset, str] = UNSET,
    supervisor_id: Union[Unset, str] = UNSET,
    show_archive: Union[Unset, bool] = UNSET,
    order: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
) -> Response[Union[Any, AssignmentsListView]]:
    """List all assignments with filtering

    Args:
        search_by (Union[Unset, str]):
        questionnaire_id (Union[Unset, str]):
        responsible (Union[Unset, str]):
        supervisor_id (Union[Unset, str]):
        show_archive (Union[Unset, bool]):
        order (Union[Unset, str]):
        offset (Union[Unset, int]):
        limit (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, AssignmentsListView]]
    """

    kwargs = _get_kwargs(
        search_by=search_by,
        questionnaire_id=questionnaire_id,
        responsible=responsible,
        supervisor_id=supervisor_id,
        show_archive=show_archive,
        order=order,
        offset=offset,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    search_by: Union[Unset, str] = UNSET,
    questionnaire_id: Union[Unset, str] = UNSET,
    responsible: Union[Unset, str] = UNSET,
    supervisor_id: Union[Unset, str] = UNSET,
    show_archive: Union[Unset, bool] = UNSET,
    order: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, AssignmentsListView]]:
    """List all assignments with filtering

    Args:
        search_by (Union[Unset, str]):
        questionnaire_id (Union[Unset, str]):
        responsible (Union[Unset, str]):
        supervisor_id (Union[Unset, str]):
        show_archive (Union[Unset, bool]):
        order (Union[Unset, str]):
        offset (Union[Unset, int]):
        limit (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, AssignmentsListView]
    """

    return sync_detailed(
        client=client,
        search_by=search_by,
        questionnaire_id=questionnaire_id,
        responsible=responsible,
        supervisor_id=supervisor_id,
        show_archive=show_archive,
        order=order,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    search_by: Union[Unset, str] = UNSET,
    questionnaire_id: Union[Unset, str] = UNSET,
    responsible: Union[Unset, str] = UNSET,
    supervisor_id: Union[Unset, str] = UNSET,
    show_archive: Union[Unset, bool] = UNSET,
    order: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
) -> Response[Union[Any, AssignmentsListView]]:
    """List all assignments with filtering

    Args:
        search_by (Union[Unset, str]):
        questionnaire_id (Union[Unset, str]):
        responsible (Union[Unset, str]):
        supervisor_id (Union[Unset, str]):
        show_archive (Union[Unset, bool]):
        order (Union[Unset, str]):
        offset (Union[Unset, int]):
        limit (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, AssignmentsListView]]
    """

    kwargs = _get_kwargs(
        search_by=search_by,
        questionnaire_id=questionnaire_id,
        responsible=responsible,
        supervisor_id=supervisor_id,
        show_archive=show_archive,
        order=order,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    search_by: Union[Unset, str] = UNSET,
    questionnaire_id: Union[Unset, str] = UNSET,
    responsible: Union[Unset, str] = UNSET,
    supervisor_id: Union[Unset, str] = UNSET,
    show_archive: Union[Unset, bool] = UNSET,
    order: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, AssignmentsListView]]:
    """List all assignments with filtering

    Args:
        search_by (Union[Unset, str]):
        questionnaire_id (Union[Unset, str]):
        responsible (Union[Unset, str]):
        supervisor_id (Union[Unset, str]):
        show_archive (Union[Unset, bool]):
        order (Union[Unset, str]):
        offset (Union[Unset, int]):
        limit (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, AssignmentsListView]
    """

    return (
        await asyncio_detailed(
            client=client,
            search_by=search_by,
            questionnaire_id=questionnaire_id,
            responsible=responsible,
            supervisor_id=supervisor_id,
            show_archive=show_archive,
            order=order,
            offset=offset,
            limit=limit,
        )
    ).parsed
