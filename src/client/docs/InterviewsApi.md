# client.InterviewsApi

All URIs are relative to *https://api.myserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_interviews_get**](InterviewsApi.md#api_v1_interviews_get) | **GET** /api/v1/interviews | Gets list of interviews existing in the system
[**api_v1_interviews_id_approve_patch**](InterviewsApi.md#api_v1_interviews_id_approve_patch) | **PATCH** /api/v1/interviews/{id}/approve | Approves interview
[**api_v1_interviews_id_assign_patch**](InterviewsApi.md#api_v1_interviews_id_assign_patch) | **PATCH** /api/v1/interviews/{id}/assign | Assigns interview to interviewer
[**api_v1_interviews_id_assignsupervisor_patch**](InterviewsApi.md#api_v1_interviews_id_assignsupervisor_patch) | **PATCH** /api/v1/interviews/{id}/assignsupervisor | Assigns supervisor
[**api_v1_interviews_id_comment_by_variable_variable_post**](InterviewsApi.md#api_v1_interviews_id_comment_by_variable_variable_post) | **POST** /api/v1/interviews/{id}/comment-by-variable/{variable} | Leave a comment on a question using questionnaire variable name and roster vector
[**api_v1_interviews_id_comment_question_id_post**](InterviewsApi.md#api_v1_interviews_id_comment_question_id_post) | **POST** /api/v1/interviews/{id}/comment/{questionId} | Leave a comment on a question
[**api_v1_interviews_id_delete**](InterviewsApi.md#api_v1_interviews_id_delete) | **DELETE** /api/v1/interviews/{id} | Deletes interview
[**api_v1_interviews_id_get**](InterviewsApi.md#api_v1_interviews_id_get) | **GET** /api/v1/interviews/{id} | Gets all the answers for given interview
[**api_v1_interviews_id_history_get**](InterviewsApi.md#api_v1_interviews_id_history_get) | **GET** /api/v1/interviews/{id}/history | Get interview history
[**api_v1_interviews_id_hqapprove_patch**](InterviewsApi.md#api_v1_interviews_id_hqapprove_patch) | **PATCH** /api/v1/interviews/{id}/hqapprove | Approves interview as headquarters
[**api_v1_interviews_id_hqreject_patch**](InterviewsApi.md#api_v1_interviews_id_hqreject_patch) | **PATCH** /api/v1/interviews/{id}/hqreject | Rejects interview as headquarters
[**api_v1_interviews_id_hqunapprove_patch**](InterviewsApi.md#api_v1_interviews_id_hqunapprove_patch) | **PATCH** /api/v1/interviews/{id}/hqunapprove | Rejects interview from Approved by headquarters status
[**api_v1_interviews_id_pdf_get**](InterviewsApi.md#api_v1_interviews_id_pdf_get) | **GET** /api/v1/interviews/{id}/pdf | Get interview transcript in pdf file
[**api_v1_interviews_id_reject_patch**](InterviewsApi.md#api_v1_interviews_id_reject_patch) | **PATCH** /api/v1/interviews/{id}/reject | Rejects interview as supervisor
[**api_v1_interviews_id_stats_get**](InterviewsApi.md#api_v1_interviews_id_stats_get) | **GET** /api/v1/interviews/{id}/stats | Get statistics by interview

# **api_v1_interviews_get**
> InterviewApiView api_v1_interviews_get(questionnaire_id=questionnaire_id, questionnaire_version=questionnaire_version, status=status, interview_id=interview_id, page_size=page_size, page=page)

Gets list of interviews existing in the system

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
api_instance = client.InterviewsApi(client.ApiClient(configuration))
questionnaire_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Questionnaire id if filtering by this field is required (optional)
questionnaire_version = 789 # int | Questionnaire id if filtering by this field is required (optional)
status = client.InterviewStatus() # InterviewStatus | Filtering by interview status (optional)
interview_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Interview Id. This corresponds to the interview__id variable in data export files or the interview Id obtained through other API requests (optional)
page_size = 10 # int | Page size (optional) (default to 10)
page = 1 # int | Page number (starting from 1) (optional) (default to 1)

try:
    # Gets list of interviews existing in the system
    api_response = api_instance.api_v1_interviews_get(questionnaire_id=questionnaire_id, questionnaire_version=questionnaire_version, status=status, interview_id=interview_id, page_size=page_size, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterviewsApi->api_v1_interviews_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **questionnaire_id** | [**str**](.md)| Questionnaire id if filtering by this field is required | [optional] 
 **questionnaire_version** | **int**| Questionnaire id if filtering by this field is required | [optional] 
 **status** | [**InterviewStatus**](.md)| Filtering by interview status | [optional] 
 **interview_id** | [**str**](.md)| Interview Id. This corresponds to the interview__id variable in data export files or the interview Id obtained through other API requests | [optional] 
 **page_size** | **int**| Page size | [optional] [default to 10]
 **page** | **int**| Page number (starting from 1) | [optional] [default to 1]

### Return type

[**InterviewApiView**](InterviewApiView.md)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_interviews_id_approve_patch**
> api_v1_interviews_id_approve_patch(id, comment=comment)

Approves interview

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
api_instance = client.InterviewsApi(client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Interview Id. This corresponds to the interview__id variable in data export files or the interview Id obtained through other API requests
comment = 'comment_example' # str | Approval comment (optional)

try:
    # Approves interview
    api_instance.api_v1_interviews_id_approve_patch(id, comment=comment)
except ApiException as e:
    print("Exception when calling InterviewsApi->api_v1_interviews_id_approve_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Interview Id. This corresponds to the interview__id variable in data export files or the interview Id obtained through other API requests | 
 **comment** | **str**| Approval comment | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_interviews_id_assign_patch**
> api_v1_interviews_id_assign_patch(body, id)

Assigns interview to interviewer

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
api_instance = client.InterviewsApi(client.ApiClient(configuration))
body = client.AssignChangeApiModel() # AssignChangeApiModel | Responsible id or responsible name
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Interview Id. This corresponds to the interview__id variable in data export files or the interview Id obtained through other API requests

try:
    # Assigns interview to interviewer
    api_instance.api_v1_interviews_id_assign_patch(body, id)
except ApiException as e:
    print("Exception when calling InterviewsApi->api_v1_interviews_id_assign_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AssignChangeApiModel**](AssignChangeApiModel.md)| Responsible id or responsible name | 
 **id** | [**str**](.md)| Interview Id. This corresponds to the interview__id variable in data export files or the interview Id obtained through other API requests | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_interviews_id_assignsupervisor_patch**
> api_v1_interviews_id_assignsupervisor_patch(body, id)

Assigns supervisor

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
api_instance = client.InterviewsApi(client.ApiClient(configuration))
body = client.AssignChangeApiModel() # AssignChangeApiModel | 
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Interview Id. This corresponds to the interview__id variable in data export files or the interview Id obtained through other API requests

try:
    # Assigns supervisor
    api_instance.api_v1_interviews_id_assignsupervisor_patch(body, id)
except ApiException as e:
    print("Exception when calling InterviewsApi->api_v1_interviews_id_assignsupervisor_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AssignChangeApiModel**](AssignChangeApiModel.md)|  | 
 **id** | [**str**](.md)| Interview Id. This corresponds to the interview__id variable in data export files or the interview Id obtained through other API requests | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_interviews_id_comment_by_variable_variable_post**
> api_v1_interviews_id_comment_by_variable_variable_post(id, variable, comment, roster_vector=roster_vector)

Leave a comment on a question using questionnaire variable name and roster vector

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
api_instance = client.InterviewsApi(client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Interview Id. This corresponds to the interview__id variable in data export files or the interview Id obtained through other API requests
variable = 'variable_example' # str | Variable name. This is the variable name for a question in Designer or in an export file
comment = 'comment_example' # str | Comment. Comment to be posted to the chosen question
roster_vector = [56] # list[int] | Roster row. In simple rosters, the row code. In nested rosters, an array of row codes: first, the row code of the parent(s); followed by the row code of the target child roster (e.g., a question in a second-level roster needs 2 row codes, a question in a first-level roster only 1). For variables not in rosters, this parameter may be left blank (optional)

try:
    # Leave a comment on a question using questionnaire variable name and roster vector
    api_instance.api_v1_interviews_id_comment_by_variable_variable_post(id, variable, comment, roster_vector=roster_vector)
except ApiException as e:
    print("Exception when calling InterviewsApi->api_v1_interviews_id_comment_by_variable_variable_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Interview Id. This corresponds to the interview__id variable in data export files or the interview Id obtained through other API requests | 
 **variable** | **str**| Variable name. This is the variable name for a question in Designer or in an export file | 
 **comment** | **str**| Comment. Comment to be posted to the chosen question | 
 **roster_vector** | [**list[int]**](int.md)| Roster row. In simple rosters, the row code. In nested rosters, an array of row codes: first, the row code of the parent(s); followed by the row code of the target child roster (e.g., a question in a second-level roster needs 2 row codes, a question in a first-level roster only 1). For variables not in rosters, this parameter may be left blank | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_interviews_id_comment_question_id_post**
> api_v1_interviews_id_comment_question_id_post(id, question_id, comment)

Leave a comment on a question

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
api_instance = client.InterviewsApi(client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Interview Id. This corresponds to the interview__id variable in data export files or the interview Id obtained through other API requests
question_id = 'question_id_example' # str | Question Id. Identifier of the question constructed as follows. First, take the question GUID from the JSON version of the questionnaire. Then, remove all dashes. If the question is not in a roster, use this as the question Id. If the question is in a roster, append its address to the question Id using the following pattern : [questionId]_#-#-#, where [questionId] is the question GUID without dashes, # represents the row code of each roster from the top level of the questionnaire to the current question, and only the needed number of row codes is used (e.g., a question in a second-level roster needs 2 row codes, a question in a first-level roster only 1)
comment = 'comment_example' # str | Comment. Comment to be posted to the chosen question

try:
    # Leave a comment on a question
    api_instance.api_v1_interviews_id_comment_question_id_post(id, question_id, comment)
except ApiException as e:
    print("Exception when calling InterviewsApi->api_v1_interviews_id_comment_question_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Interview Id. This corresponds to the interview__id variable in data export files or the interview Id obtained through other API requests | 
 **question_id** | **str**| Question Id. Identifier of the question constructed as follows. First, take the question GUID from the JSON version of the questionnaire. Then, remove all dashes. If the question is not in a roster, use this as the question Id. If the question is in a roster, append its address to the question Id using the following pattern : [questionId]_#-#-#, where [questionId] is the question GUID without dashes, # represents the row code of each roster from the top level of the questionnaire to the current question, and only the needed number of row codes is used (e.g., a question in a second-level roster needs 2 row codes, a question in a first-level roster only 1) | 
 **comment** | **str**| Comment. Comment to be posted to the chosen question | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_interviews_id_delete**
> api_v1_interviews_id_delete(id)

Deletes interview

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
api_instance = client.InterviewsApi(client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Interview Id. This corresponds to the interview__id variable in data export files or the interview Id obtained through other API requests

try:
    # Deletes interview
    api_instance.api_v1_interviews_id_delete(id)
except ApiException as e:
    print("Exception when calling InterviewsApi->api_v1_interviews_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Interview Id. This corresponds to the interview__id variable in data export files or the interview Id obtained through other API requests | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_interviews_id_get**
> InterviewApiDetails api_v1_interviews_id_get(id)

Gets all the answers for given interview

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
api_instance = client.InterviewsApi(client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Interview Id. This corresponds to the interview__id variable in data export files or the interview Id obtained through other API requests

try:
    # Gets all the answers for given interview
    api_response = api_instance.api_v1_interviews_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterviewsApi->api_v1_interviews_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Interview Id. This corresponds to the interview__id variable in data export files or the interview Id obtained through other API requests | 

### Return type

[**InterviewApiDetails**](InterviewApiDetails.md)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_interviews_id_history_get**
> InterviewHistoryView api_v1_interviews_id_history_get(id)

Get interview history

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
api_instance = client.InterviewsApi(client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Interview id

try:
    # Get interview history
    api_response = api_instance.api_v1_interviews_id_history_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterviewsApi->api_v1_interviews_id_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Interview id | 

### Return type

[**InterviewHistoryView**](InterviewHistoryView.md)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_interviews_id_hqapprove_patch**
> api_v1_interviews_id_hqapprove_patch(id, comment=comment)

Approves interview as headquarters

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
api_instance = client.InterviewsApi(client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Interview Id. This corresponds to the interview__id variable in data export files or the interview Id obtained through other API requests
comment = 'comment_example' # str | Approve comment (optional)

try:
    # Approves interview as headquarters
    api_instance.api_v1_interviews_id_hqapprove_patch(id, comment=comment)
except ApiException as e:
    print("Exception when calling InterviewsApi->api_v1_interviews_id_hqapprove_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Interview Id. This corresponds to the interview__id variable in data export files or the interview Id obtained through other API requests | 
 **comment** | **str**| Approve comment | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_interviews_id_hqreject_patch**
> api_v1_interviews_id_hqreject_patch(id, comment=comment, responsible_id=responsible_id)

Rejects interview as headquarters

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
api_instance = client.InterviewsApi(client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Interview Id. This corresponds to the interview__id variable in data export files or the interview Id obtained through other API requests
comment = 'comment_example' # str | Rejection comment (optional)
responsible_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | New responsible id (optional)

try:
    # Rejects interview as headquarters
    api_instance.api_v1_interviews_id_hqreject_patch(id, comment=comment, responsible_id=responsible_id)
except ApiException as e:
    print("Exception when calling InterviewsApi->api_v1_interviews_id_hqreject_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Interview Id. This corresponds to the interview__id variable in data export files or the interview Id obtained through other API requests | 
 **comment** | **str**| Rejection comment | [optional] 
 **responsible_id** | [**str**](.md)| New responsible id | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_interviews_id_hqunapprove_patch**
> api_v1_interviews_id_hqunapprove_patch(id, comment=comment)

Rejects interview from Approved by headquarters status

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
api_instance = client.InterviewsApi(client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Interview Id. This corresponds to the interview__id variable in data export files or the interview Id obtained through other API requests
comment = 'comment_example' # str | Approve comment (optional)

try:
    # Rejects interview from Approved by headquarters status
    api_instance.api_v1_interviews_id_hqunapprove_patch(id, comment=comment)
except ApiException as e:
    print("Exception when calling InterviewsApi->api_v1_interviews_id_hqunapprove_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Interview Id. This corresponds to the interview__id variable in data export files or the interview Id obtained through other API requests | 
 **comment** | **str**| Approve comment | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_interviews_id_pdf_get**
> api_v1_interviews_id_pdf_get(id)

Get interview transcript in pdf file

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
api_instance = client.InterviewsApi(client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Interview id

try:
    # Get interview transcript in pdf file
    api_instance.api_v1_interviews_id_pdf_get(id)
except ApiException as e:
    print("Exception when calling InterviewsApi->api_v1_interviews_id_pdf_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Interview id | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_interviews_id_reject_patch**
> api_v1_interviews_id_reject_patch(id, comment=comment, responsible_id=responsible_id)

Rejects interview as supervisor

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
api_instance = client.InterviewsApi(client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Interview Id. This corresponds to the interview__id variable in data export files or the interview Id obtained through other API requests
comment = 'comment_example' # str | Rejection comment (optional)
responsible_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | New responsible id (optional)

try:
    # Rejects interview as supervisor
    api_instance.api_v1_interviews_id_reject_patch(id, comment=comment, responsible_id=responsible_id)
except ApiException as e:
    print("Exception when calling InterviewsApi->api_v1_interviews_id_reject_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Interview Id. This corresponds to the interview__id variable in data export files or the interview Id obtained through other API requests | 
 **comment** | **str**| Rejection comment | [optional] 
 **responsible_id** | [**str**](.md)| New responsible id | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_interviews_id_stats_get**
> InterviewApiStatistics api_v1_interviews_id_stats_get(id)

Get statistics by interview

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
api_instance = client.InterviewsApi(client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Interview id

try:
    # Get statistics by interview
    api_response = api_instance.api_v1_interviews_id_stats_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterviewsApi->api_v1_interviews_id_stats_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Interview id | 

### Return type

[**InterviewApiStatistics**](InterviewApiStatistics.md)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

