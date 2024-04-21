from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.user_api_view import UserApiView
from ...types import UNSET, Response, Unset


def _get_kwargs(
    supervisor_id: str,
    *,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = 1,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/supervisors/{supervisor_id}/interviewers",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, UserApiView]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = UserApiView.from_dict(response.json())

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
) -> Response[Union[Any, UserApiView]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    supervisor_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = 1,
) -> Response[Union[Any, UserApiView]]:
    """Gets list of interviewers in the specific supervisor team

    Args:
        supervisor_id (str):
        limit (Union[Unset, int]):  Default: 10.
        offset (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UserApiView]]
    """

    kwargs = _get_kwargs(
        supervisor_id=supervisor_id,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    supervisor_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = 1,
) -> Optional[Union[Any, UserApiView]]:
    """Gets list of interviewers in the specific supervisor team

    Args:
        supervisor_id (str):
        limit (Union[Unset, int]):  Default: 10.
        offset (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UserApiView]
    """

    return sync_detailed(
        supervisor_id=supervisor_id,
        client=client,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    supervisor_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = 1,
) -> Response[Union[Any, UserApiView]]:
    """Gets list of interviewers in the specific supervisor team

    Args:
        supervisor_id (str):
        limit (Union[Unset, int]):  Default: 10.
        offset (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UserApiView]]
    """

    kwargs = _get_kwargs(
        supervisor_id=supervisor_id,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    supervisor_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = 1,
) -> Optional[Union[Any, UserApiView]]:
    """Gets list of interviewers in the specific supervisor team

    Args:
        supervisor_id (str):
        limit (Union[Unset, int]):  Default: 10.
        offset (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UserApiView]
    """

    return (
        await asyncio_detailed(
            supervisor_id=supervisor_id,
            client=client,
            limit=limit,
            offset=offset,
        )
    ).parsed
