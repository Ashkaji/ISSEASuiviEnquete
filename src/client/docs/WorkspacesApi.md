# client.WorkspacesApi

All URIs are relative to *https://api.myserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_workspaces_assign_post**](WorkspacesApi.md#api_v1_workspaces_assign_post) | **POST** /api/v1/workspaces/assign | Assigns workspaces to user.
[**api_v1_workspaces_get**](WorkspacesApi.md#api_v1_workspaces_get) | **GET** /api/v1/workspaces | List existing workspaces
[**api_v1_workspaces_name_delete**](WorkspacesApi.md#api_v1_workspaces_name_delete) | **DELETE** /api/v1/workspaces/{name} | Delete workspace
[**api_v1_workspaces_name_disable_post**](WorkspacesApi.md#api_v1_workspaces_name_disable_post) | **POST** /api/v1/workspaces/{name}/disable | Disables specified workspace
[**api_v1_workspaces_name_enable_post**](WorkspacesApi.md#api_v1_workspaces_name_enable_post) | **POST** /api/v1/workspaces/{name}/enable | Enables specified workspace
[**api_v1_workspaces_name_get**](WorkspacesApi.md#api_v1_workspaces_name_get) | **GET** /api/v1/workspaces/{name} | Get single workspace details
[**api_v1_workspaces_name_patch**](WorkspacesApi.md#api_v1_workspaces_name_patch) | **PATCH** /api/v1/workspaces/{name} | Updates workspace
[**api_v1_workspaces_post**](WorkspacesApi.md#api_v1_workspaces_post) | **POST** /api/v1/workspaces | Creates new workspace. Accessible only to administrator
[**api_v1_workspaces_status_name_get**](WorkspacesApi.md#api_v1_workspaces_status_name_get) | **GET** /api/v1/workspaces/status/{name} | Request server for information about workspace status and it&#x27;s ability to delete

# **api_v1_workspaces_assign_post**
> api_v1_workspaces_assign_post(body=body)

Assigns workspaces to user.

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
api_instance = client.WorkspacesApi(client.ApiClient(configuration))
body = client.AssignWorkspacesToUserModel() # AssignWorkspacesToUserModel |  (optional)

try:
    # Assigns workspaces to user.
    api_instance.api_v1_workspaces_assign_post(body=body)
except ApiException as e:
    print("Exception when calling WorkspacesApi->api_v1_workspaces_assign_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AssignWorkspacesToUserModel**](AssignWorkspacesToUserModel.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_workspaces_get**
> WorkspaceApiView api_v1_workspaces_get(start=start, length=length, user_id=user_id, include_disabled=include_disabled, draw=draw, order=order, c=c, columns=columns, colummns_list=colummns_list, search_value=search_value, search_regex=search_regex, page_index=page_index, page_size=page_size)

List existing workspaces

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
api_instance = client.WorkspacesApi(client.ApiClient(configuration))
start = 56 # int |  (optional)
length = 56 # int |  (optional)
user_id = 'user_id_example' # str | Return only workspaces assigned to specified user (optional)
include_disabled = true # bool | Returned list will also include disabled workspaces (optional)
draw = 56 # int | Datatables specific (optional)
order = [client.SortOrder()] # list[SortOrder] | order of output (optional)
c = [client.ColumnInfo()] # list[ColumnInfo] | This is shorthand for `Columns` property. DataTable works via Get requests (optional)
columns = [client.ColumnInfo()] # list[ColumnInfo] | List of columns that need to be outputed. Leave null for default values (optional)
colummns_list = [client.ColumnInfo()] # list[ColumnInfo] |  (optional)
search_value = 'search_value_example' # str |  (optional)
search_regex = true # bool |  (optional)
page_index = 56 # int |  (optional)
page_size = 56 # int |  (optional)

try:
    # List existing workspaces
    api_response = api_instance.api_v1_workspaces_get(start=start, length=length, user_id=user_id, include_disabled=include_disabled, draw=draw, order=order, c=c, columns=columns, colummns_list=colummns_list, search_value=search_value, search_regex=search_regex, page_index=page_index, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->api_v1_workspaces_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**|  | [optional] 
 **length** | **int**|  | [optional] 
 **user_id** | **str**| Return only workspaces assigned to specified user | [optional] 
 **include_disabled** | **bool**| Returned list will also include disabled workspaces | [optional] 
 **draw** | **int**| Datatables specific | [optional] 
 **order** | [**list[SortOrder]**](SortOrder.md)| order of output | [optional] 
 **c** | [**list[ColumnInfo]**](ColumnInfo.md)| This is shorthand for &#x60;Columns&#x60; property. DataTable works via Get requests | [optional] 
 **columns** | [**list[ColumnInfo]**](ColumnInfo.md)| List of columns that need to be outputed. Leave null for default values | [optional] 
 **colummns_list** | [**list[ColumnInfo]**](ColumnInfo.md)|  | [optional] 
 **search_value** | **str**|  | [optional] 
 **search_regex** | **bool**|  | [optional] 
 **page_index** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 

### Return type

[**WorkspaceApiView**](WorkspaceApiView.md)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_workspaces_name_delete**
> DeleteWorkspaceResponse api_v1_workspaces_name_delete(name)

Delete workspace

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
api_instance = client.WorkspacesApi(client.ApiClient(configuration))
name = 'name_example' # str | Workspace name

try:
    # Delete workspace
    api_response = api_instance.api_v1_workspaces_name_delete(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->api_v1_workspaces_name_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Workspace name | 

### Return type

[**DeleteWorkspaceResponse**](DeleteWorkspaceResponse.md)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_workspaces_name_disable_post**
> api_v1_workspaces_name_disable_post(name)

Disables specified workspace

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
api_instance = client.WorkspacesApi(client.ApiClient(configuration))
name = 'name_example' # str | 

try:
    # Disables specified workspace
    api_instance.api_v1_workspaces_name_disable_post(name)
except ApiException as e:
    print("Exception when calling WorkspacesApi->api_v1_workspaces_name_disable_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_workspaces_name_enable_post**
> api_v1_workspaces_name_enable_post(name)

Enables specified workspace

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
api_instance = client.WorkspacesApi(client.ApiClient(configuration))
name = 'name_example' # str | 

try:
    # Enables specified workspace
    api_instance.api_v1_workspaces_name_enable_post(name)
except ApiException as e:
    print("Exception when calling WorkspacesApi->api_v1_workspaces_name_enable_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_workspaces_name_get**
> WorkspaceApiView api_v1_workspaces_name_get(name)

Get single workspace details

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
api_instance = client.WorkspacesApi(client.ApiClient(configuration))
name = 'name_example' # str | 

try:
    # Get single workspace details
    api_response = api_instance.api_v1_workspaces_name_get(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->api_v1_workspaces_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**WorkspaceApiView**](WorkspaceApiView.md)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_workspaces_name_patch**
> api_v1_workspaces_name_patch(name, body=body)

Updates workspace

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
api_instance = client.WorkspacesApi(client.ApiClient(configuration))
name = 'name_example' # str | 
body = client.WorkspaceUpdateApiView() # WorkspaceUpdateApiView |  (optional)

try:
    # Updates workspace
    api_instance.api_v1_workspaces_name_patch(name, body=body)
except ApiException as e:
    print("Exception when calling WorkspacesApi->api_v1_workspaces_name_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **body** | [**WorkspaceUpdateApiView**](WorkspaceUpdateApiView.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_workspaces_post**
> WorkspaceApiView api_v1_workspaces_post(body=body)

Creates new workspace. Accessible only to administrator

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
api_instance = client.WorkspacesApi(client.ApiClient(configuration))
body = client.WorkspaceCreateApiView() # WorkspaceCreateApiView |  (optional)

try:
    # Creates new workspace. Accessible only to administrator
    api_response = api_instance.api_v1_workspaces_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->api_v1_workspaces_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WorkspaceCreateApiView**](WorkspaceCreateApiView.md)|  | [optional] 

### Return type

[**WorkspaceApiView**](WorkspaceApiView.md)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_workspaces_status_name_get**
> WorkspaceStatusInformation api_v1_workspaces_status_name_get(name)

Request server for information about workspace status and it's ability to delete

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
api_instance = client.WorkspacesApi(client.ApiClient(configuration))
name = 'name_example' # str | Workspace name

try:
    # Request server for information about workspace status and it's ability to delete
    api_response = api_instance.api_v1_workspaces_status_name_get(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->api_v1_workspaces_status_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Workspace name | 

### Return type

[**WorkspaceStatusInformation**](WorkspaceStatusInformation.md)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

