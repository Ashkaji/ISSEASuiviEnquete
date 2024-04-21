from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.validation_problem_details import ValidationProblemDetails
from ...models.workspace_api_view import WorkspaceApiView
from ...models.workspace_create_api_view import WorkspaceCreateApiView
from ...types import Response


def _get_kwargs(
    *,
    body: WorkspaceCreateApiView,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/workspaces",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ValidationProblemDetails, WorkspaceApiView]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = WorkspaceApiView.from_dict(response.json())

        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ValidationProblemDetails.from_dict(response.json())

        return response_400
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
) -> Response[Union[Any, ValidationProblemDetails, WorkspaceApiView]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: WorkspaceCreateApiView,
) -> Response[Union[Any, ValidationProblemDetails, WorkspaceApiView]]:
    """Creates new workspace. Accessible only to administrator

    Args:
        body (WorkspaceCreateApiView):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ValidationProblemDetails, WorkspaceApiView]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: WorkspaceCreateApiView,
) -> Optional[Union[Any, ValidationProblemDetails, WorkspaceApiView]]:
    """Creates new workspace. Accessible only to administrator

    Args:
        body (WorkspaceCreateApiView):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ValidationProblemDetails, WorkspaceApiView]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: WorkspaceCreateApiView,
) -> Response[Union[Any, ValidationProblemDetails, WorkspaceApiView]]:
    """Creates new workspace. Accessible only to administrator

    Args:
        body (WorkspaceCreateApiView):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ValidationProblemDetails, WorkspaceApiView]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: WorkspaceCreateApiView,
) -> Optional[Union[Any, ValidationProblemDetails, WorkspaceApiView]]:
    """Creates new workspace. Accessible only to administrator

    Args:
        body (WorkspaceCreateApiView):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ValidationProblemDetails, WorkspaceApiView]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
