# client.AssignmentsApi

All URIs are relative to *https://api.myserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_assignments_get**](AssignmentsApi.md#api_v1_assignments_get) | **GET** /api/v1/assignments | List all assignments with filtering
[**api_v1_assignments_id_archive_patch**](AssignmentsApi.md#api_v1_assignments_id_archive_patch) | **PATCH** /api/v1/assignments/{id}/archive | Archive assignment
[**api_v1_assignments_id_assign_patch**](AssignmentsApi.md#api_v1_assignments_id_assign_patch) | **PATCH** /api/v1/assignments/{id}/assign | Assign new responsible person for assignment
[**api_v1_assignments_id_assignment_quantity_settings_get**](AssignmentsApi.md#api_v1_assignments_id_assignment_quantity_settings_get) | **GET** /api/v1/assignments/{id}/assignmentQuantitySettings | Gets Quantity Settings for provided assignment
[**api_v1_assignments_id_change_quantity_patch**](AssignmentsApi.md#api_v1_assignments_id_change_quantity_patch) | **PATCH** /api/v1/assignments/{id}/changeQuantity | Change assignments limit on created interviews
[**api_v1_assignments_id_close_patch**](AssignmentsApi.md#api_v1_assignments_id_close_patch) | **PATCH** /api/v1/assignments/{id}/close | Close assignment by setting Size to the amount of collected interviews
[**api_v1_assignments_id_close_post**](AssignmentsApi.md#api_v1_assignments_id_close_post) | **POST** /api/v1/assignments/{id}/close | 
[**api_v1_assignments_id_get**](AssignmentsApi.md#api_v1_assignments_id_get) | **GET** /api/v1/assignments/{id} | Single assignment details
[**api_v1_assignments_id_history_get**](AssignmentsApi.md#api_v1_assignments_id_history_get) | **GET** /api/v1/assignments/{id}/history | Gets history of the assignment
[**api_v1_assignments_id_record_audio_get**](AssignmentsApi.md#api_v1_assignments_id_record_audio_get) | **GET** /api/v1/assignments/{id}/recordAudio | Get status of audio recording for provided assignment
[**api_v1_assignments_id_record_audio_patch**](AssignmentsApi.md#api_v1_assignments_id_record_audio_patch) | **PATCH** /api/v1/assignments/{id}/recordAudio | Set audio recording setting for assignment
[**api_v1_assignments_id_unarchive_patch**](AssignmentsApi.md#api_v1_assignments_id_unarchive_patch) | **PATCH** /api/v1/assignments/{id}/unarchive | Unarchive assignment
[**api_v1_assignments_post**](AssignmentsApi.md#api_v1_assignments_post) | **POST** /api/v1/assignments | Create new assignment

# **api_v1_assignments_get**
> AssignmentsListView api_v1_assignments_get(search_by=search_by, questionnaire_id=questionnaire_id, responsible=responsible, supervisor_id=supervisor_id, show_archive=show_archive, order=order, offset=offset, limit=limit)

List all assignments with filtering

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
api_instance = client.AssignmentsApi(client.ApiClient(configuration))
search_by = 'search_by_example' # str | Filter result by custom search query (optional)
questionnaire_id = 'questionnaire_id_example' # str | Questionnaire Id in format of `{QuestionnaireId}${Version}` (optional)
responsible = 'responsible_example' # str | Responsible user Id on name (optional)
supervisor_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Supervisor id (optional)
show_archive = true # bool | Search for only archived assignments (optional)
order = 'order_example' # str | Possible values are  Id, ResponsibleName, InterviewsCount, Quantity, UpdatedAtUtc, CreatedAtUtc  Followed by ordering direction \"ASC\" or \"DESC\" (optional)
offset = 56 # int |  (optional)
limit = 56 # int |  (optional)

try:
    # List all assignments with filtering
    api_response = api_instance.api_v1_assignments_get(search_by=search_by, questionnaire_id=questionnaire_id, responsible=responsible, supervisor_id=supervisor_id, show_archive=show_archive, order=order, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssignmentsApi->api_v1_assignments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_by** | **str**| Filter result by custom search query | [optional] 
 **questionnaire_id** | **str**| Questionnaire Id in format of &#x60;{QuestionnaireId}${Version}&#x60; | [optional] 
 **responsible** | **str**| Responsible user Id on name | [optional] 
 **supervisor_id** | **str**| Supervisor id | [optional] 
 **show_archive** | **bool**| Search for only archived assignments | [optional] 
 **order** | **str**| Possible values are  Id, ResponsibleName, InterviewsCount, Quantity, UpdatedAtUtc, CreatedAtUtc  Followed by ordering direction \&quot;ASC\&quot; or \&quot;DESC\&quot; | [optional] 
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 

### Return type

[**AssignmentsListView**](AssignmentsListView.md)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_assignments_id_archive_patch**
> AssignmentDetails api_v1_assignments_id_archive_patch(id)

Archive assignment

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
api_instance = client.AssignmentsApi(client.ApiClient(configuration))
id = 56 # int | Assignment id

try:
    # Archive assignment
    api_response = api_instance.api_v1_assignments_id_archive_patch(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssignmentsApi->api_v1_assignments_id_archive_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Assignment id | 

### Return type

[**AssignmentDetails**](AssignmentDetails.md)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_assignments_id_assign_patch**
> AssignmentDetails api_v1_assignments_id_assign_patch(body, id)

Assign new responsible person for assignment

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
api_instance = client.AssignmentsApi(client.ApiClient(configuration))
body = client.AssignmentAssignRequest() # AssignmentAssignRequest | Responsible user id or name
id = 56 # int | Assignment id

try:
    # Assign new responsible person for assignment
    api_response = api_instance.api_v1_assignments_id_assign_patch(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssignmentsApi->api_v1_assignments_id_assign_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AssignmentAssignRequest**](AssignmentAssignRequest.md)| Responsible user id or name | 
 **id** | **int**| Assignment id | 

### Return type

[**AssignmentDetails**](AssignmentDetails.md)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_assignments_id_assignment_quantity_settings_get**
> AssignmentQuantitySettings api_v1_assignments_id_assignment_quantity_settings_get(id)

Gets Quantity Settings for provided assignment

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
api_instance = client.AssignmentsApi(client.ApiClient(configuration))
id = 56 # int | Assignment id

try:
    # Gets Quantity Settings for provided assignment
    api_response = api_instance.api_v1_assignments_id_assignment_quantity_settings_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssignmentsApi->api_v1_assignments_id_assignment_quantity_settings_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Assignment id | 

### Return type

[**AssignmentQuantitySettings**](AssignmentQuantitySettings.md)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_assignments_id_change_quantity_patch**
> AssignmentDetails api_v1_assignments_id_change_quantity_patch(id, body=body)

Change assignments limit on created interviews

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
api_instance = client.AssignmentsApi(client.ApiClient(configuration))
id = 56 # int | Assignment id
body = 56 # int | New limit on created interviews (optional)

try:
    # Change assignments limit on created interviews
    api_response = api_instance.api_v1_assignments_id_change_quantity_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssignmentsApi->api_v1_assignments_id_change_quantity_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Assignment id | 
 **body** | [**int**](int.md)| New limit on created interviews | [optional] 

### Return type

[**AssignmentDetails**](AssignmentDetails.md)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_assignments_id_close_patch**
> AssignmentDetails api_v1_assignments_id_close_patch(id)

Close assignment by setting Size to the amount of collected interviews

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
api_instance = client.AssignmentsApi(client.ApiClient(configuration))
id = 56 # int | Assignment id

try:
    # Close assignment by setting Size to the amount of collected interviews
    api_response = api_instance.api_v1_assignments_id_close_patch(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssignmentsApi->api_v1_assignments_id_close_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Assignment id | 

### Return type

[**AssignmentDetails**](AssignmentDetails.md)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_assignments_id_close_post**
> api_v1_assignments_id_close_post(id)



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
api_instance = client.AssignmentsApi(client.ApiClient(configuration))
id = 56 # int | 

try:
    api_instance.api_v1_assignments_id_close_post(id)
except ApiException as e:
    print("Exception when calling AssignmentsApi->api_v1_assignments_id_close_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_assignments_id_get**
> FullAssignmentDetails api_v1_assignments_id_get(id)

Single assignment details

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
api_instance = client.AssignmentsApi(client.ApiClient(configuration))
id = 56 # int | 

try:
    # Single assignment details
    api_response = api_instance.api_v1_assignments_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssignmentsApi->api_v1_assignments_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**FullAssignmentDetails**](FullAssignmentDetails.md)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_assignments_id_history_get**
> AssignmentHistory api_v1_assignments_id_history_get(id, start=start, length=length)

Gets history of the assignment

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
api_instance = client.AssignmentsApi(client.ApiClient(configuration))
id = 56 # int | Assignment id
start = 0 # int |  (optional) (default to 0)
length = 30 # int | Limit of events to return (optional) (default to 30)

try:
    # Gets history of the assignment
    api_response = api_instance.api_v1_assignments_id_history_get(id, start=start, length=length)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssignmentsApi->api_v1_assignments_id_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Assignment id | 
 **start** | **int**|  | [optional] [default to 0]
 **length** | **int**| Limit of events to return | [optional] [default to 30]

### Return type

[**AssignmentHistory**](AssignmentHistory.md)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_assignments_id_record_audio_get**
> AudioRecordingEnabled api_v1_assignments_id_record_audio_get(id)

Get status of audio recording for provided assignment

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
api_instance = client.AssignmentsApi(client.ApiClient(configuration))
id = 56 # int | Assignment id

try:
    # Get status of audio recording for provided assignment
    api_response = api_instance.api_v1_assignments_id_record_audio_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssignmentsApi->api_v1_assignments_id_record_audio_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Assignment id | 

### Return type

[**AudioRecordingEnabled**](AudioRecordingEnabled.md)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_assignments_id_record_audio_patch**
> api_v1_assignments_id_record_audio_patch(id, body=body)

Set audio recording setting for assignment

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
api_instance = client.AssignmentsApi(client.ApiClient(configuration))
id = 56 # int | Assignment id
body = client.UpdateRecordingRequest() # UpdateRecordingRequest |  (optional)

try:
    # Set audio recording setting for assignment
    api_instance.api_v1_assignments_id_record_audio_patch(id, body=body)
except ApiException as e:
    print("Exception when calling AssignmentsApi->api_v1_assignments_id_record_audio_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Assignment id | 
 **body** | [**UpdateRecordingRequest**](UpdateRecordingRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_assignments_id_unarchive_patch**
> AssignmentDetails api_v1_assignments_id_unarchive_patch(id)

Unarchive assignment

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
api_instance = client.AssignmentsApi(client.ApiClient(configuration))
id = 56 # int | Assignment id

try:
    # Unarchive assignment
    api_response = api_instance.api_v1_assignments_id_unarchive_patch(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssignmentsApi->api_v1_assignments_id_unarchive_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Assignment id | 

### Return type

[**AssignmentDetails**](AssignmentDetails.md)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_assignments_post**
> CreateAssignmentResult api_v1_assignments_post(body)

Create new assignment

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
api_instance = client.AssignmentsApi(client.ApiClient(configuration))
body = client.CreateAssignmentApiRequest() # CreateAssignmentApiRequest | New assignments options

try:
    # Create new assignment
    api_response = api_instance.api_v1_assignments_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssignmentsApi->api_v1_assignments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateAssignmentApiRequest**](CreateAssignmentApiRequest.md)| New assignments options | 

### Return type

[**CreateAssignmentResult**](CreateAssignmentResult.md)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

