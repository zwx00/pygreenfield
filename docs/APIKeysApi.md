# swagger_client.APIKeysApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_api_keys_apikey_delete**](APIKeysApi.md#api_v1_api_keys_apikey_delete) | **DELETE** /api/v1/api-keys/{apikey} | Revoke an API Key
[**api_v1_api_keys_current_delete**](APIKeysApi.md#api_v1_api_keys_current_delete) | **DELETE** /api/v1/api-keys/current | Revoke the current API Key
[**api_v1_api_keys_current_get**](APIKeysApi.md#api_v1_api_keys_current_get) | **GET** /api/v1/api-keys/current | Get the current API Key information
[**api_v1_api_keys_post**](APIKeysApi.md#api_v1_api_keys_post) | **POST** /api/v1/api-keys | Create a new API Key

# **api_v1_api_keys_apikey_delete**
> api_v1_api_keys_apikey_delete(apikey)

Revoke an API Key

Revoke the current API key so that it cannot be used anymore

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: API_Key
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: Basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.APIKeysApi(swagger_client.ApiClient(configuration))
apikey = 'apikey_example' # str | The API Key to revoke

try:
    # Revoke an API Key
    api_instance.api_v1_api_keys_apikey_delete(apikey)
except ApiException as e:
    print("Exception when calling APIKeysApi->api_v1_api_keys_apikey_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apikey** | **str**| The API Key to revoke | 

### Return type

void (empty response body)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_api_keys_current_delete**
> ApiKeyData api_v1_api_keys_current_delete()

Revoke the current API Key

Revoke the current API key so that it cannot be used anymore

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: API_Key
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.APIKeysApi(swagger_client.ApiClient(configuration))

try:
    # Revoke the current API Key
    api_response = api_instance.api_v1_api_keys_current_delete()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIKeysApi->api_v1_api_keys_current_delete: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiKeyData**](ApiKeyData.md)

### Authorization

[API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_api_keys_current_get**
> ApiKeyData api_v1_api_keys_current_get()

Get the current API Key information

View information about the current API key

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: API_Key
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.APIKeysApi(swagger_client.ApiClient(configuration))

try:
    # Get the current API Key information
    api_response = api_instance.api_v1_api_keys_current_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIKeysApi->api_v1_api_keys_current_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiKeyData**](ApiKeyData.md)

### Authorization

[API_Key](../README.md#API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_api_keys_post**
> ApiKeyData api_v1_api_keys_post(body=body)

Create a new API Key

Create a new API Key

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: API_Key
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: Basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.APIKeysApi(swagger_client.ApiClient(configuration))
body = swagger_client.V1ApikeysBody() # V1ApikeysBody |  (optional)

try:
    # Create a new API Key
    api_response = api_instance.api_v1_api_keys_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIKeysApi->api_v1_api_keys_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ApikeysBody**](V1ApikeysBody.md)|  | [optional] 

### Return type

[**ApiKeyData**](ApiKeyData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

