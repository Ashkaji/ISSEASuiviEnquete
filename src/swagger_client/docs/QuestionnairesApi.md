# swagger_client.QuestionnairesApi

All URIs are relative to *https://api.myserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_questionnaires_get**](QuestionnairesApi.md#api_v1_questionnaires_get) | **GET** /api/v1/questionnaires | Gets list of imported questionnaires
[**api_v1_questionnaires_id_get**](QuestionnairesApi.md#api_v1_questionnaires_id_get) | **GET** /api/v1/questionnaires/{id} | Gets list of imported questionnaires by questionnaire id
[**api_v1_questionnaires_id_version_document_get**](QuestionnairesApi.md#api_v1_questionnaires_id_version_document_get) | **GET** /api/v1/questionnaires/{id}/{version}/document | 
[**api_v1_questionnaires_id_version_get**](QuestionnairesApi.md#api_v1_questionnaires_id_version_get) | **GET** /api/v1/questionnaires/{id}/{version} | Gets imported questionnaire by id and version
[**api_v1_questionnaires_id_version_interviews_get**](QuestionnairesApi.md#api_v1_questionnaires_id_version_interviews_get) | **GET** /api/v1/questionnaires/{id}/{version}/interviews | 
[**api_v1_questionnaires_statuses_get**](QuestionnairesApi.md#api_v1_questionnaires_statuses_get) | **GET** /api/v1/questionnaires/statuses | Gets list of possible interview statuses
[**get_record_audio_setting**](QuestionnairesApi.md#get_record_audio_setting) | **GET** /api/v1/questionnaires/{id}/{version}/recordAudio | Gets audio recording enabled setting for provided questionnaire
[**set_record_audio_setting**](QuestionnairesApi.md#set_record_audio_setting) | **POST** /api/v1/questionnaires/{id}/{version}/recordAudio | Sets audio recording enabled setting for provided questionnaire

# **api_v1_questionnaires_get**
> QuestionnaireApiView api_v1_questionnaires_get(limit=limit, offset=offset)

Gets list of imported questionnaires

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
api_instance = swagger_client.QuestionnairesApi(swagger_client.ApiClient(configuration))
limit = 10 # int | Limit number of returned rows. Max allowed value is 40 (optional) (default to 10)
offset = 1 # int | Page number starting from 1. Actual skipped rows are calculated as `(offset - 1) * limit` (optional) (default to 1)

try:
    # Gets list of imported questionnaires
    api_response = api_instance.api_v1_questionnaires_get(limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionnairesApi->api_v1_questionnaires_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limit number of returned rows. Max allowed value is 40 | [optional] [default to 10]
 **offset** | **int**| Page number starting from 1. Actual skipped rows are calculated as &#x60;(offset - 1) * limit&#x60; | [optional] [default to 1]

### Return type

[**QuestionnaireApiView**](QuestionnaireApiView.md)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_questionnaires_id_get**
> QuestionnaireApiView api_v1_questionnaires_id_get(id, limit=limit, offset=offset)

Gets list of imported questionnaires by questionnaire id

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
api_instance = swagger_client.QuestionnairesApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Questionnaire Id
limit = 10 # int | Limit number of returned rows. Max allowed value is 40 (optional) (default to 10)
offset = 1 # int | Page number starting from 1. Actual skipped rows are calculated as `(offset - 1) * limit` (optional) (default to 1)

try:
    # Gets list of imported questionnaires by questionnaire id
    api_response = api_instance.api_v1_questionnaires_id_get(id, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionnairesApi->api_v1_questionnaires_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Questionnaire Id | 
 **limit** | **int**| Limit number of returned rows. Max allowed value is 40 | [optional] [default to 10]
 **offset** | **int**| Page number starting from 1. Actual skipped rows are calculated as &#x60;(offset - 1) * limit&#x60; | [optional] [default to 1]

### Return type

[**QuestionnaireApiView**](QuestionnaireApiView.md)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_questionnaires_id_version_document_get**
> api_v1_questionnaires_id_version_document_get(id, version)



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
api_instance = swagger_client.QuestionnairesApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
version = 789 # int | 

try:
    api_instance.api_v1_questionnaires_id_version_document_get(id, version)
except ApiException as e:
    print("Exception when calling QuestionnairesApi->api_v1_questionnaires_id_version_document_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **version** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_questionnaires_id_version_get**
> QuestionnaireApiItem api_v1_questionnaires_id_version_get(id, version)

Gets imported questionnaire by id and version

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
api_instance = swagger_client.QuestionnairesApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Questionnaire Id
version = 789 # int | Questionnaire version

try:
    # Gets imported questionnaire by id and version
    api_response = api_instance.api_v1_questionnaires_id_version_get(id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionnairesApi->api_v1_questionnaires_id_version_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Questionnaire Id | 
 **version** | **int**| Questionnaire version | 

### Return type

[**QuestionnaireApiItem**](QuestionnaireApiItem.md)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_questionnaires_id_version_interviews_get**
> InterviewApiView api_v1_questionnaires_id_version_interviews_get(id, version, limit=limit, offset=offset)



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
api_instance = swagger_client.QuestionnairesApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
version = 789 # int | 
limit = 10 # int |  (optional) (default to 10)
offset = 1 # int |  (optional) (default to 1)

try:
    api_response = api_instance.api_v1_questionnaires_id_version_interviews_get(id, version, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionnairesApi->api_v1_questionnaires_id_version_interviews_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **version** | **int**|  | 
 **limit** | **int**|  | [optional] [default to 10]
 **offset** | **int**|  | [optional] [default to 1]

### Return type

[**InterviewApiView**](InterviewApiView.md)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_questionnaires_statuses_get**
> InterviewStatus api_v1_questionnaires_statuses_get()

Gets list of possible interview statuses

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
api_instance = swagger_client.QuestionnairesApi(swagger_client.ApiClient(configuration))

try:
    # Gets list of possible interview statuses
    api_response = api_instance.api_v1_questionnaires_statuses_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionnairesApi->api_v1_questionnaires_statuses_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InterviewStatus**](InterviewStatus.md)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_record_audio_setting**
> AudioRecordingEnabled get_record_audio_setting(id, version)

Gets audio recording enabled setting for provided questionnaire

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
api_instance = swagger_client.QuestionnairesApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Questionnaire guid
version = 789 # int | Questionnaire version

try:
    # Gets audio recording enabled setting for provided questionnaire
    api_response = api_instance.get_record_audio_setting(id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionnairesApi->get_record_audio_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Questionnaire guid | 
 **version** | **int**| Questionnaire version | 

### Return type

[**AudioRecordingEnabled**](AudioRecordingEnabled.md)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_record_audio_setting**
> set_record_audio_setting(body, id, version)

Sets audio recording enabled setting for provided questionnaire

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
api_instance = swagger_client.QuestionnairesApi(swagger_client.ApiClient(configuration))
body = swagger_client.RecordAudioRequest() # RecordAudioRequest | 
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Questionnaire guid
version = 789 # int | Questionnaire version

try:
    # Sets audio recording enabled setting for provided questionnaire
    api_instance.set_record_audio_setting(body, id, version)
except ApiException as e:
    print("Exception when calling QuestionnairesApi->set_record_audio_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordAudioRequest**](RecordAudioRequest.md)|  | 
 **id** | [**str**](.md)| Questionnaire guid | 
 **version** | **int**| Questionnaire version | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

