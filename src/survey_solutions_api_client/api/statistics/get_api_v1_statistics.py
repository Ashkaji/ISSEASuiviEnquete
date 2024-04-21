from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.column_info import ColumnInfo
from ...models.export_file_type import ExportFileType
from ...models.sort_order import SortOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    questionnaire_id: str,
    version: Union[Unset, int] = UNSET,
    question: str,
    min_: Union[Unset, int] = UNSET,
    max_: Union[Unset, int] = UNSET,
    export_type: Union[Unset, ExportFileType] = UNSET,
    conditional_question: Union[Unset, str] = UNSET,
    condition: Union[Unset, List[int]] = UNSET,
    pivot: Union[Unset, bool] = UNSET,
    expand_teams: Union[Unset, bool] = UNSET,
    statuses: Union[Unset, List[str]] = UNSET,
    draw: Union[Unset, int] = UNSET,
    start: Union[Unset, int] = UNSET,
    length: Union[Unset, int] = UNSET,
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

    params["QuestionnaireId"] = questionnaire_id

    params["Version"] = version

    params["Question"] = question

    params["Min"] = min_

    params["Max"] = max_

    json_export_type: Union[Unset, str] = UNSET
    if not isinstance(export_type, Unset):
        json_export_type = export_type.value

    params["exportType"] = json_export_type

    params["ConditionalQuestion"] = conditional_question

    json_condition: Union[Unset, List[int]] = UNSET
    if not isinstance(condition, Unset):
        json_condition = condition

    params["condition[]"] = json_condition

    params["Pivot"] = pivot

    params["ExpandTeams"] = expand_teams

    json_statuses: Union[Unset, List[str]] = UNSET
    if not isinstance(statuses, Unset):
        json_statuses = statuses

    params["statuses[]"] = json_statuses

    params["Draw"] = draw

    params["Start"] = start

    params["Length"] = length

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
        "url": "/api/v1/statistics",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.OK:
        return None
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        return None
    if response.status_code == HTTPStatus.FORBIDDEN:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    questionnaire_id: str,
    version: Union[Unset, int] = UNSET,
    question: str,
    min_: Union[Unset, int] = UNSET,
    max_: Union[Unset, int] = UNSET,
    export_type: Union[Unset, ExportFileType] = UNSET,
    conditional_question: Union[Unset, str] = UNSET,
    condition: Union[Unset, List[int]] = UNSET,
    pivot: Union[Unset, bool] = UNSET,
    expand_teams: Union[Unset, bool] = UNSET,
    statuses: Union[Unset, List[str]] = UNSET,
    draw: Union[Unset, int] = UNSET,
    start: Union[Unset, int] = UNSET,
    length: Union[Unset, int] = UNSET,
    order: Union[Unset, List["SortOrder"]] = UNSET,
    field_c: Union[Unset, List["ColumnInfo"]] = UNSET,
    columns: Union[Unset, List["ColumnInfo"]] = UNSET,
    colummns_list: Union[Unset, List["ColumnInfo"]] = UNSET,
    search_value: Union[Unset, str] = UNSET,
    search_regex: Union[Unset, bool] = UNSET,
    page_index: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Response[Any]:
    """Generate report report based on provided query paramters.

    Args:
        questionnaire_id (str):
        version (Union[Unset, int]):
        question (str):
        min_ (Union[Unset, int]):
        max_ (Union[Unset, int]):
        export_type (Union[Unset, ExportFileType]):
        conditional_question (Union[Unset, str]):
        condition (Union[Unset, List[int]]):
        pivot (Union[Unset, bool]):
        expand_teams (Union[Unset, bool]):
        statuses (Union[Unset, List[str]]):
        draw (Union[Unset, int]):
        start (Union[Unset, int]):
        length (Union[Unset, int]):
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
        Response[Any]
    """

    kwargs = _get_kwargs(
        questionnaire_id=questionnaire_id,
        version=version,
        question=question,
        min_=min_,
        max_=max_,
        export_type=export_type,
        conditional_question=conditional_question,
        condition=condition,
        pivot=pivot,
        expand_teams=expand_teams,
        statuses=statuses,
        draw=draw,
        start=start,
        length=length,
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


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    questionnaire_id: str,
    version: Union[Unset, int] = UNSET,
    question: str,
    min_: Union[Unset, int] = UNSET,
    max_: Union[Unset, int] = UNSET,
    export_type: Union[Unset, ExportFileType] = UNSET,
    conditional_question: Union[Unset, str] = UNSET,
    condition: Union[Unset, List[int]] = UNSET,
    pivot: Union[Unset, bool] = UNSET,
    expand_teams: Union[Unset, bool] = UNSET,
    statuses: Union[Unset, List[str]] = UNSET,
    draw: Union[Unset, int] = UNSET,
    start: Union[Unset, int] = UNSET,
    length: Union[Unset, int] = UNSET,
    order: Union[Unset, List["SortOrder"]] = UNSET,
    field_c: Union[Unset, List["ColumnInfo"]] = UNSET,
    columns: Union[Unset, List["ColumnInfo"]] = UNSET,
    colummns_list: Union[Unset, List["ColumnInfo"]] = UNSET,
    search_value: Union[Unset, str] = UNSET,
    search_regex: Union[Unset, bool] = UNSET,
    page_index: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Response[Any]:
    """Generate report report based on provided query paramters.

    Args:
        questionnaire_id (str):
        version (Union[Unset, int]):
        question (str):
        min_ (Union[Unset, int]):
        max_ (Union[Unset, int]):
        export_type (Union[Unset, ExportFileType]):
        conditional_question (Union[Unset, str]):
        condition (Union[Unset, List[int]]):
        pivot (Union[Unset, bool]):
        expand_teams (Union[Unset, bool]):
        statuses (Union[Unset, List[str]]):
        draw (Union[Unset, int]):
        start (Union[Unset, int]):
        length (Union[Unset, int]):
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
        Response[Any]
    """

    kwargs = _get_kwargs(
        questionnaire_id=questionnaire_id,
        version=version,
        question=question,
        min_=min_,
        max_=max_,
        export_type=export_type,
        conditional_question=conditional_question,
        condition=condition,
        pivot=pivot,
        expand_teams=expand_teams,
        statuses=statuses,
        draw=draw,
        start=start,
        length=length,
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
