from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.interview_api_view import InterviewApiView
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    version: int,
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
        "url": f"/api/v1/questionnaires/{id}/{version}/interviews",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, InterviewApiView]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = InterviewApiView.from_dict(response.text)

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
    id: str,
    version: int,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = 1,
) -> Response[Union[Any, InterviewApiView]]:
    """
    Args:
        id (str):
        version (int):
        limit (Union[Unset, int]):  Default: 10.
        offset (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, InterviewApiView]]
    """

    kwargs = _get_kwargs(
        id=id,
        version=version,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    version: int,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = 1,
) -> Optional[Union[Any, InterviewApiView]]:
    """
    Args:
        id (str):
        version (int):
        limit (Union[Unset, int]):  Default: 10.
        offset (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, InterviewApiView]
    """

    return sync_detailed(
        id=id,
        version=version,
        client=client,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    id: str,
    version: int,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = 1,
) -> Response[Union[Any, InterviewApiView]]:
    """
    Args:
        id (str):
        version (int):
        limit (Union[Unset, int]):  Default: 10.
        offset (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, InterviewApiView]]
    """

    kwargs = _get_kwargs(
        id=id,
        version=version,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    version: int,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = 1,
) -> Optional[Union[Any, InterviewApiView]]:
    """
    Args:
        id (str):
        version (int):
        limit (Union[Unset, int]):  Default: 10.
        offset (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, InterviewApiView]
    """

    return (
        await asyncio_detailed(
            id=id,
            version=version,
            client=client,
            limit=limit,
            offset=offset,
        )
    ).parsed
