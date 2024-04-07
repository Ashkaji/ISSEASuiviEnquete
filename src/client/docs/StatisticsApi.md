# client.StatisticsApi

All URIs are relative to *https://api.myserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_statistics_get**](StatisticsApi.md#api_v1_statistics_get) | **GET** /api/v1/statistics | Generate report report based on provided query paramters.
[**api_v1_statistics_questionnaires_get**](StatisticsApi.md#api_v1_statistics_questionnaires_get) | **GET** /api/v1/statistics/questionnaires | 
[**api_v1_statistics_questions_get**](StatisticsApi.md#api_v1_statistics_questions_get) | **GET** /api/v1/statistics/questions | Get questions list

# **api_v1_statistics_get**
> api_v1_statistics_get(questionnaire_id, question, version=version, min=min, max=max, export_type=export_type, conditional_question=conditional_question, condition=condition, pivot=pivot, expand_teams=expand_teams, statuses=statuses, draw=draw, start=start, length=length, order=order, c=c, columns=columns, colummns_list=colummns_list, search_value=search_value, search_regex=search_regex, page_index=page_index, page_size=page_size)

Generate report report based on provided query paramters.

### Example
```python
from __future__ import print_function
import time
import client
from ..rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basic
configuration = client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = client.StatisticsApi(client.ApiClient(configuration))
questionnaire_id = 'questionnaire_id_example' # str | Questionnaire Id
question = 'question_example' # str | Question variable name or UUID
version = 789 # int | Questionnaire version (optional)
min = 56 # int | Minimum value of answers to count in report (optional)
max = 56 # int | Maximum value of answers to count in report (optional)
export_type = client.ExportFileType() # ExportFileType | Specify report format to ouput (optional)
conditional_question = 'conditional_question_example' # str | Condition question variable name or UUID (optional)
condition = [56] # list[int] | List of condition question answers to filter on (optional)
pivot = true # bool | Specify `true` if Pivot Table output needed. (optional)
expand_teams = true # bool | Show detailed report with team members for each team (optional)
statuses = ['statuses_example'] # list[str] | List of statuses to apply filtering (optional)
draw = 56 # int | Datatables specific (optional)
start = 56 # int | Paging - Start row (optional)
length = 56 # int | How many rows per page (optional)
order = [client.SortOrder()] # list[SortOrder] | order of output (optional)
c = [client.ColumnInfo()] # list[ColumnInfo] | This is shorthand for `Columns` property. DataTable works via Get requests (optional)
columns = [client.ColumnInfo()] # list[ColumnInfo] | List of columns that need to be outputed. Leave null for default values (optional)
colummns_list = [client.ColumnInfo()] # list[ColumnInfo] |  (optional)
search_value = 'search_value_example' # str |  (optional)
search_regex = true # bool |  (optional)
page_index = 56 # int |  (optional)
page_size = 56 # int |  (optional)

try:
    # Generate report report based on provided query paramters.
    api_instance.api_v1_statistics_get(questionnaire_id, question, version=version, min=min, max=max, export_type=export_type, conditional_question=conditional_question, condition=condition, pivot=pivot, expand_teams=expand_teams, statuses=statuses, draw=draw, start=start, length=length, order=order, c=c, columns=columns, colummns_list=colummns_list, search_value=search_value, search_regex=search_regex, page_index=page_index, page_size=page_size)
except ApiException as e:
    print("Exception when calling StatisticsApi->api_v1_statistics_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **questionnaire_id** | **str**| Questionnaire Id | 
 **question** | **str**| Question variable name or UUID | 
 **version** | **int**| Questionnaire version | [optional] 
 **min** | **int**| Minimum value of answers to count in report | [optional] 
 **max** | **int**| Maximum value of answers to count in report | [optional] 
 **export_type** | [**ExportFileType**](.md)| Specify report format to ouput | [optional] 
 **conditional_question** | **str**| Condition question variable name or UUID | [optional] 
 **condition** | [**list[int]**](int.md)| List of condition question answers to filter on | [optional] 
 **pivot** | **bool**| Specify &#x60;true&#x60; if Pivot Table output needed. | [optional] 
 **expand_teams** | **bool**| Show detailed report with team members for each team | [optional] 
 **statuses** | [**list[str]**](str.md)| List of statuses to apply filtering | [optional] 
 **draw** | **int**| Datatables specific | [optional] 
 **start** | **int**| Paging - Start row | [optional] 
 **length** | **int**| How many rows per page | [optional] 
 **order** | [**list[SortOrder]**](SortOrder.md)| order of output | [optional] 
 **c** | [**list[ColumnInfo]**](ColumnInfo.md)| This is shorthand for &#x60;Columns&#x60; property. DataTable works via Get requests | [optional] 
 **columns** | [**list[ColumnInfo]**](ColumnInfo.md)| List of columns that need to be outputed. Leave null for default values | [optional] 
 **colummns_list** | [**list[ColumnInfo]**](ColumnInfo.md)|  | [optional] 
 **search_value** | **str**|  | [optional] 
 **search_regex** | **bool**|  | [optional] 
 **page_index** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_statistics_questionnaires_get**
> list[QuestionnaireDto] api_v1_statistics_questionnaires_get()



### Example
```python
from __future__ import print_function
import time
import client
from ..rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basic
configuration = client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = client.StatisticsApi(client.ApiClient(configuration))

try:
    api_response = api_instance.api_v1_statistics_questionnaires_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->api_v1_statistics_questionnaires_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[QuestionnaireDto]**](QuestionnaireDto.md)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_statistics_questions_get**
> list[QuestionDto] api_v1_statistics_questions_get(questionnaire_id=questionnaire_id, version=version)

Get questions list

Gets a questions list for specified questionnaire identity. Only questions that have data are shown

### Example
```python
from __future__ import print_function
import time
import client
from ..rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basic
configuration = client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = client.StatisticsApi(client.ApiClient(configuration))
questionnaire_id = 'questionnaire_id_example' # str | Questionnaire Id (optional)
version = 789 # int | Questionnaire version (optional)

try:
    # Get questions list
    api_response = api_instance.api_v1_statistics_questions_get(questionnaire_id=questionnaire_id, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->api_v1_statistics_questions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **questionnaire_id** | **str**| Questionnaire Id | [optional] 
 **version** | **int**| Questionnaire version | [optional] 

### Return type

[**list[QuestionDto]**](QuestionDto.md)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

