# swagger_client.SettingsApi

All URIs are relative to *https://api.myserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_settings_globalnotice_delete**](SettingsApi.md#api_v1_settings_globalnotice_delete) | **DELETE** /api/v1/settings/globalnotice | Remove global notice for the headquarters application
[**api_v1_settings_globalnotice_get**](SettingsApi.md#api_v1_settings_globalnotice_get) | **GET** /api/v1/settings/globalnotice | Get global notice for the headquarters application
[**api_v1_settings_globalnotice_put**](SettingsApi.md#api_v1_settings_globalnotice_put) | **PUT** /api/v1/settings/globalnotice | Set global notice for the headquarters application

# **api_v1_settings_globalnotice_delete**
> api_v1_settings_globalnotice_delete()

Remove global notice for the headquarters application

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
api_instance = swagger_client.SettingsApi(swagger_client.ApiClient(configuration))

try:
    # Remove global notice for the headquarters application
    api_instance.api_v1_settings_globalnotice_delete()
except ApiException as e:
    print("Exception when calling SettingsApi->api_v1_settings_globalnotice_delete: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_settings_globalnotice_get**
> GlobalNoticeApiView api_v1_settings_globalnotice_get()

Get global notice for the headquarters application

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
api_instance = swagger_client.SettingsApi(swagger_client.ApiClient(configuration))

try:
    # Get global notice for the headquarters application
    api_response = api_instance.api_v1_settings_globalnotice_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->api_v1_settings_globalnotice_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GlobalNoticeApiView**](GlobalNoticeApiView.md)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_settings_globalnotice_put**
> api_v1_settings_globalnotice_put(body)

Set global notice for the headquarters application

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
api_instance = swagger_client.SettingsApi(swagger_client.ApiClient(configuration))
body = swagger_client.SetGlobalNoticeApiModel() # SetGlobalNoticeApiModel | 

try:
    # Set global notice for the headquarters application
    api_instance.api_v1_settings_globalnotice_put(body)
except ApiException as e:
    print("Exception when calling SettingsApi->api_v1_settings_globalnotice_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SetGlobalNoticeApiModel**](SetGlobalNoticeApiModel.md)|  | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

