# swagger_client.UsersApi

All URIs are relative to *https://api.myserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_interviewers_id_actions_log_get**](UsersApi.md#api_v1_interviewers_id_actions_log_get) | **GET** /api/v1/interviewers/{id}/actions-log | Returns audit log records for interviewer.  You can specify \&quot;start\&quot; and \&quot;end\&quot; parameters in query string to get range results.
[**api_v1_interviewers_id_get**](UsersApi.md#api_v1_interviewers_id_get) | **GET** /api/v1/interviewers/{id} | Gets detailed info about single interviewer
[**api_v1_supervisors_get**](UsersApi.md#api_v1_supervisors_get) | **GET** /api/v1/supervisors | Gets list of supervisors
[**api_v1_supervisors_id_get**](UsersApi.md#api_v1_supervisors_id_get) | **GET** /api/v1/supervisors/{id} | Gets detailed info about single supervisor
[**api_v1_supervisors_supervisor_id_interviewers_get**](UsersApi.md#api_v1_supervisors_supervisor_id_interviewers_get) | **GET** /api/v1/supervisors/{supervisorId}/interviewers | Gets list of interviewers in the specific supervisor team
[**api_v1_users_id_archive_patch**](UsersApi.md#api_v1_users_id_archive_patch) | **PATCH** /api/v1/users/{id}/archive | Archives interviewer or supervisor with all his interviewers
[**api_v1_users_id_get**](UsersApi.md#api_v1_users_id_get) | **GET** /api/v1/users/{id} | Gets detailed info about single user
[**api_v1_users_id_unarchive_patch**](UsersApi.md#api_v1_users_id_unarchive_patch) | **PATCH** /api/v1/users/{id}/unarchive | Unarchives single user
[**api_v1_users_post**](UsersApi.md#api_v1_users_post) | **POST** /api/v1/users | Creates new user with specified role.

# **api_v1_interviewers_id_actions_log_get**
> list[AuditLogRecordApiView] api_v1_interviewers_id_actions_log_get(id, start=start, end=end)

Returns audit log records for interviewer.  You can specify \"start\" and \"end\" parameters in query string to get range results.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | User id
start = '2013-10-20T19:20:30+01:00' # datetime | Start datetime. If isn't specified then return data for last 7 days. (optional)
end = '2013-10-20T19:20:30+01:00' # datetime | End datetime. If isn't specified then get data for 7 days from start data. (optional)

try:
    # Returns audit log records for interviewer.  You can specify \"start\" and \"end\" parameters in query string to get range results.
    api_response = api_instance.api_v1_interviewers_id_actions_log_get(id, start=start, end=end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->api_v1_interviewers_id_actions_log_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| User id | 
 **start** | **datetime**| Start datetime. If isn&#x27;t specified then return data for last 7 days. | [optional] 
 **end** | **datetime**| End datetime. If isn&#x27;t specified then get data for 7 days from start data. | [optional] 

### Return type

[**list[AuditLogRecordApiView]**](AuditLogRecordApiView.md)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_interviewers_id_get**
> InterviewerUserApiDetails api_v1_interviewers_id_get(id)

Gets detailed info about single interviewer

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | User id

try:
    # Gets detailed info about single interviewer
    api_response = api_instance.api_v1_interviewers_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->api_v1_interviewers_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| User id | 

### Return type

[**InterviewerUserApiDetails**](InterviewerUserApiDetails.md)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_supervisors_get**
> UserApiView api_v1_supervisors_get(limit=limit, offset=offset)

Gets list of supervisors

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
limit = 10 # int |  (optional) (default to 10)
offset = 1 # int |  (optional) (default to 1)

try:
    # Gets list of supervisors
    api_response = api_instance.api_v1_supervisors_get(limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->api_v1_supervisors_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 10]
 **offset** | **int**|  | [optional] [default to 1]

### Return type

[**UserApiView**](UserApiView.md)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_supervisors_id_get**
> UserApiDetails api_v1_supervisors_id_get(id)

Gets detailed info about single supervisor

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | User id or user name or user email

try:
    # Gets detailed info about single supervisor
    api_response = api_instance.api_v1_supervisors_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->api_v1_supervisors_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User id or user name or user email | 

### Return type

[**UserApiDetails**](UserApiDetails.md)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_supervisors_supervisor_id_interviewers_get**
> UserApiView api_v1_supervisors_supervisor_id_interviewers_get(supervisor_id, limit=limit, offset=offset)

Gets list of interviewers in the specific supervisor team

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
supervisor_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Id of supervisor
limit = 10 # int |  (optional) (default to 10)
offset = 1 # int |  (optional) (default to 1)

try:
    # Gets list of interviewers in the specific supervisor team
    api_response = api_instance.api_v1_supervisors_supervisor_id_interviewers_get(supervisor_id, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->api_v1_supervisors_supervisor_id_interviewers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supervisor_id** | [**str**](.md)| Id of supervisor | 
 **limit** | **int**|  | [optional] [default to 10]
 **offset** | **int**|  | [optional] [default to 1]

### Return type

[**UserApiView**](UserApiView.md)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_users_id_archive_patch**
> api_v1_users_id_archive_patch(id)

Archives interviewer or supervisor with all his interviewers

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | User id

try:
    # Archives interviewer or supervisor with all his interviewers
    api_instance.api_v1_users_id_archive_patch(id)
except ApiException as e:
    print("Exception when calling UsersApi->api_v1_users_id_archive_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User id | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_users_id_get**
> UserApiDetails api_v1_users_id_get(id)

Gets detailed info about single user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | User id or user name or user email

try:
    # Gets detailed info about single user
    api_response = api_instance.api_v1_users_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->api_v1_users_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User id or user name or user email | 

### Return type

[**UserApiDetails**](UserApiDetails.md)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_users_id_unarchive_patch**
> api_v1_users_id_unarchive_patch(id)

Unarchives single user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | User id

try:
    # Unarchives single user
    api_instance.api_v1_users_id_unarchive_patch(id)
except ApiException as e:
    print("Exception when calling UsersApi->api_v1_users_id_unarchive_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User id | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_users_post**
> api_v1_users_post(body)

Creates new user with specified role.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.RegisterUserModel() # RegisterUserModel | 

try:
    # Creates new user with specified role.
    api_instance.api_v1_users_post(body)
except ApiException as e:
    print("Exception when calling UsersApi->api_v1_users_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RegisterUserModel**](RegisterUserModel.md)|  | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

