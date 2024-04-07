# client.ExportApi

All URIs are relative to *https://api.myserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_export_get**](ExportApi.md#api_v2_export_get) | **GET** /api/v2/export | Get list of export processes
[**api_v2_export_id_delete**](ExportApi.md#api_v2_export_id_delete) | **DELETE** /api/v2/export/{id} | Cancel export process
[**api_v2_export_id_file_get**](ExportApi.md#api_v2_export_id_file_get) | **GET** /api/v2/export/{id}/file | Downloads export file. It will return either 200 status code with export file content or 302 redirect to export location.
[**api_v2_export_id_get**](ExportApi.md#api_v2_export_id_get) | **GET** /api/v2/export/{id} | Get detailed information about export process
[**api_v2_export_post**](ExportApi.md#api_v2_export_post) | **POST** /api/v2/export | Start export file creation

# **api_v2_export_get**
> list[ExportProcess] api_v2_export_get(export_type=export_type, interview_status=interview_status, questionnaire_identity=questionnaire_identity, export_status=export_status, has_file=has_file, limit=limit, offset=offset)

Get list of export processes

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
api_instance = client.ExportApi(client.ApiClient(configuration))
export_type = client.ExportType() # ExportType | Format of export data to download (optional)
interview_status = client.ExportInterviewType() # ExportInterviewType | Status of exported interviews (optional)
questionnaire_identity = 'questionnaire_identity_example' # str | Questionnaire id (optional)
export_status = client.ExportStatus() # ExportStatus | Status of export process (optional)
has_file = true # bool | Has export process file to download (optional)
limit = 56 # int | Select a limited number of records (optional)
offset = 56 # int | Skip number of records before beginning to return records (optional)

try:
    # Get list of export processes
    api_response = api_instance.api_v2_export_get(export_type=export_type, interview_status=interview_status, questionnaire_identity=questionnaire_identity, export_status=export_status, has_file=has_file, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExportApi->api_v2_export_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_type** | [**ExportType**](.md)| Format of export data to download | [optional] 
 **interview_status** | [**ExportInterviewType**](.md)| Status of exported interviews | [optional] 
 **questionnaire_identity** | **str**| Questionnaire id | [optional] 
 **export_status** | [**ExportStatus**](.md)| Status of export process | [optional] 
 **has_file** | **bool**| Has export process file to download | [optional] 
 **limit** | **int**| Select a limited number of records | [optional] 
 **offset** | **int**| Skip number of records before beginning to return records | [optional] 

### Return type

[**list[ExportProcess]**](ExportProcess.md)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_export_id_delete**
> ExportProcess api_v2_export_id_delete(id)

Cancel export process

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
api_instance = client.ExportApi(client.ApiClient(configuration))
id = 789 # int | 

try:
    # Cancel export process
    api_response = api_instance.api_v2_export_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExportApi->api_v2_export_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ExportProcess**](ExportProcess.md)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_export_id_file_get**
> api_v2_export_id_file_get(id)

Downloads export file. It will return either 200 status code with export file content or 302 redirect to export location.

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
api_instance = client.ExportApi(client.ApiClient(configuration))
id = 789 # int | Export process id

try:
    # Downloads export file. It will return either 200 status code with export file content or 302 redirect to export location.
    api_instance.api_v2_export_id_file_get(id)
except ApiException as e:
    print("Exception when calling ExportApi->api_v2_export_id_file_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Export process id | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_export_id_get**
> ExportProcess api_v2_export_id_get(id)

Get detailed information about export process

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
api_instance = client.ExportApi(client.ApiClient(configuration))
id = 789 # int | Export process id

try:
    # Get detailed information about export process
    api_response = api_instance.api_v2_export_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExportApi->api_v2_export_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Export process id | 

### Return type

[**ExportProcess**](ExportProcess.md)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_export_post**
> ExportProcess api_v2_export_post(body)

Start export file creation

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
api_instance = client.ExportApi(client.ApiClient(configuration))
body = client.CreateExportProcess() # CreateExportProcess | 

try:
    # Start export file creation
    api_response = api_instance.api_v2_export_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExportApi->api_v2_export_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateExportProcess**](CreateExportProcess.md)|  | 

### Return type

[**ExportProcess**](ExportProcess.md)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

