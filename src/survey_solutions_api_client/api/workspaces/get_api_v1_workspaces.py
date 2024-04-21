from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.column_info import ColumnInfo
from ...models.sort_order import SortOrder
from ...models.workspace_api_view import WorkspaceApiView
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    start: Union[Unset, int] = UNSET,
    length: Union[Unset, int] = UNSET,
    user_id: Union[Unset, str] = UNSET,
    include_disabled: Union[Unset, bool] = UNSET,
    draw: Union[Unset, int] = UNSET,
    order: Union[Unset, List["SortOrder"]] = UNSET,
    field_c: Union[Unset, List["ColumnInfo"]] = UNSET,
    columns: Union[Unset, List["ColumnInfo"]] = UNSET,
    colummns_list: Union[Unset, List["ColumnInfo"]] = UNSET,
    search_value: Union[Unset, str] = UNSET,
    search_regex: Union[Unset, bool] = UNSET,
    page_index: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["Start"] = start

    params["Length"] = length

    params["UserId"] = user_id

    params["IncludeDisabled"] = include_disabled

    params["Draw"] = draw

    json_order: Union[Unset, List[Dict[str, Any]]] = UNSET
    if not isinstance(order, Unset):
        json_order = []
        for order_item_data in order:
            order_item = order_item_data.to_dict()
            json_order.append(order_item)

    params["Order"] = json_order

    json_field_c: Union[Unset, List[Dict[str, Any]]] = UNSET
    if not isinstance(field_c, Unset):
        json_field_c = []
        for field_c_item_data in field_c:
            field_c_item = field_c_item_data.to_dict()
            json_field_c.append(field_c_item)

    params["_C"] = json_field_c

    json_columns: Union[Unset, List[Dict[str, Any]]] = UNSET
    if not isinstance(columns, Unset):
        json_columns = []
        for columns_item_data in columns:
            columns_item = columns_item_data.to_dict()
            json_columns.append(columns_item)

    params["Columns"] = json_columns

    json_colummns_list: Union[Unset, List[Dict[str, Any]]] = UNSET
    if not isinstance(colummns_list, Unset):
        json_colummns_list = []
        for colummns_list_item_data in colummns_list:
            colummns_list_item = colummns_list_item_data.to_dict()
            json_colummns_list.append(colummns_list_item)

    params["ColummnsList"] = json_colummns_list

    params["Search.Value"] = search_value

    params["Search.Regex"] = search_regex

    params["PageIndex"] = page_index

    params["PageSize"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/workspaces",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, WorkspaceApiView]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = WorkspaceApiView.from_dict(response.json())

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
) -> Response[Union[Any, WorkspaceApiView]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    start: Union[Unset, int] = UNSET,
    length: Union[Unset, int] = UNSET,
    user_id: Union[Unset, str] = UNSET,
    include_disabled: Union[Unset, bool] = UNSET,
    draw: Union[Unset, int] = UNSET,
    order: Union[Unset, List["SortOrder"]] = UNSET,
    field_c: Union[Unset, List["ColumnInfo"]] = UNSET,
    columns: Union[Unset, List["ColumnInfo"]] = UNSET,
    colummns_list: Union[Unset, List["ColumnInfo"]] = UNSET,
    search_value: Union[Unset, str] = UNSET,
    search_regex: Union[Unset, bool] = UNSET,
    page_index: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Response[Union[Any, WorkspaceApiView]]:
    """List existing workspaces

    Args:
        start (Union[Unset, int]):
        length (Union[Unset, int]):
        user_id (Union[Unset, str]):
        include_disabled (Union[Unset, bool]):
        draw (Union[Unset, int]):
        order (Union[Unset, List['SortOrder']]):
        field_c (Union[Unset, List['ColumnInfo']]):
        columns (Union[Unset, List['ColumnInfo']]):
        colummns_list (Union[Unset, List['ColumnInfo']]):
        search_value (Union[Unset, str]):
        search_regex (Union[Unset, bool]):
        page_index (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, WorkspaceApiView]]
    """

    kwargs = _get_kwargs(
        start=start,
        length=length,
        user_id=user_id,
        include_disabled=include_disabled,
        draw=draw,
        order=order,
        field_c=field_c,
        columns=columns,
        colummns_list=colummns_list,
        search_value=search_value,
        search_regex=search_regex,
        page_index=page_index,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    start: Union[Unset, int] = UNSET,
    length: Union[Unset, int] = UNSET,
    user_id: Union[Unset, str] = UNSET,
    include_disabled: Union[Unset, bool] = UNSET,
    draw: Union[Unset, int] = UNSET,
    order: Union[Unset, List["SortOrder"]] = UNSET,
    field_c: Union[Unset, List["ColumnInfo"]] = UNSET,
    columns: Union[Unset, List["ColumnInfo"]] = UNSET,
    colummns_list: Union[Unset, List["ColumnInfo"]] = UNSET,
    search_value: Union[Unset, str] = UNSET,
    search_regex: Union[Unset, bool] = UNSET,
    page_index: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, WorkspaceApiView]]:
    """List existing workspaces

    Args:
        start (Union[Unset, int]):
        length (Union[Unset, int]):
        user_id (Union[Unset, str]):
        include_disabled (Union[Unset, bool]):
        draw (Union[Unset, int]):
        order (Union[Unset, List['SortOrder']]):
        field_c (Union[Unset, List['ColumnInfo']]):
        columns (Union[Unset, List['ColumnInfo']]):
        colummns_list (Union[Unset, List['ColumnInfo']]):
        search_value (Union[Unset, str]):
        search_regex (Union[Unset, bool]):
        page_index (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, WorkspaceApiView]
    """

    return sync_detailed(
        client=client,
        start=start,
        length=length,
        user_id=user_id,
        include_disabled=include_disabled,
        draw=draw,
        order=order,
        field_c=field_c,
        columns=columns,
        colummns_list=colummns_list,
        search_value=search_value,
        search_regex=search_regex,
        page_index=page_index,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    start: Union[Unset, int] = UNSET,
    length: Union[Unset, int] = UNSET,
    user_id: Union[Unset, str] = UNSET,
    include_disabled: Union[Unset, bool] = UNSET,
    draw: Union[Unset, int] = UNSET,
    order: Union[Unset, List["SortOrder"]] = UNSET,
    field_c: Union[Unset, List["ColumnInfo"]] = UNSET,
    columns: Union[Unset, List["ColumnInfo"]] = UNSET,
    colummns_list: Union[Unset, List["ColumnInfo"]] = UNSET,
    search_value: Union[Unset, str] = UNSET,
    search_regex: Union[Unset, bool] = UNSET,
    page_index: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Response[Union[Any, WorkspaceApiView]]:
    """List existing workspaces

    Args:
        start (Union[Unset, int]):
        length (Union[Unset, int]):
        user_id (Union[Unset, str]):
        include_disabled (Union[Unset, bool]):
        draw (Union[Unset, int]):
        order (Union[Unset, List['SortOrder']]):
        field_c (Union[Unset, List['ColumnInfo']]):
        columns (Union[Unset, List['ColumnInfo']]):
        colummns_list (Union[Unset, List['ColumnInfo']]):
        search_value (Union[Unset, str]):
        search_regex (Union[Unset, bool]):
        page_index (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, WorkspaceApiView]]
    """

    kwargs = _get_kwargs(
        start=start,
        length=length,
        user_id=user_id,
        include_disabled=include_disabled,
        draw=draw,
        order=order,
        field_c=field_c,
        columns=columns,
        colummns_list=colummns_list,
        search_value=search_value,
        search_regex=search_regex,
        page_index=page_index,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    start: Union[Unset, int] = UNSET,
    length: Union[Unset, int] = UNSET,
    user_id: Union[Unset, str] = UNSET,
    include_disabled: Union[Unset, bool] = UNSET,
    draw: Union[Unset, int] = UNSET,
    order: Union[Unset, List["SortOrder"]] = UNSET,
    field_c: Union[Unset, List["ColumnInfo"]] = UNSET,
    columns: Union[Unset, List["ColumnInfo"]] = UNSET,
    colummns_list: Union[Unset, List["ColumnInfo"]] = UNSET,
    search_value: Union[Unset, str] = UNSET,
    search_regex: Union[Unset, bool] = UNSET,
    page_index: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, WorkspaceApiView]]:
    """List existing workspaces

    Args:
        start (Union[Unset, int]):
        length (Union[Unset, int]):
        user_id (Union[Unset, str]):
        include_disabled (Union[Unset, bool]):
        draw (Union[Unset, int]):
        order (Union[Unset, List['SortOrder']]):
        field_c (Union[Unset, List['ColumnInfo']]):
        columns (Union[Unset, List['ColumnInfo']]):
        colummns_list (Union[Unset, List['ColumnInfo']]):
        search_value (Union[Unset, str]):
        search_regex (Union[Unset, bool]):
        page_index (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, WorkspaceApiView]
    """

    return (
        await asyncio_detailed(
            client=client,
            start=start,
            length=length,
            user_id=user_id,
            include_disabled=include_disabled,
            draw=draw,
            order=order,
            field_c=field_c,
            columns=columns,
            colummns_list=colummns_list,
            search_value=search_value,
            search_regex=search_regex,
            page_index=page_index,
            page_size=page_size,
        )
    ).parsed
