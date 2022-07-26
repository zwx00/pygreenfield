# swagger_client.StoresEmailApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_stores_store_id_email_send_post**](StoresEmailApi.md#api_v1_stores_store_id_email_send_post) | **POST** /api/v1/stores/{storeId}/email/send | Send an email for a store
[**stores_get_store_email_settings**](StoresEmailApi.md#stores_get_store_email_settings) | **GET** /api/v1/stores/{storeId}/email | Get store email settings
[**stores_update_store_email_settings**](StoresEmailApi.md#stores_update_store_email_settings) | **PUT** /api/v1/stores/{storeId}/email | Update store email settings

# **api_v1_stores_store_id_email_send_post**
> api_v1_stores_store_id_email_send_post(body)

Send an email for a store

Send an email using the store's SMTP server

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: Basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.StoresEmailApi(swagger_client.ApiClient(configuration))
body = swagger_client.EmailData() # EmailData | 

try:
    # Send an email for a store
    api_instance.api_v1_stores_store_id_email_send_post(body)
except ApiException as e:
    print("Exception when calling StoresEmailApi->api_v1_stores_store_id_email_send_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmailData**](EmailData.md)|  | 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stores_get_store_email_settings**
> EmailSettingsData stores_get_store_email_settings(store_id)

Get store email settings

View email settings of the specified store

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
api_instance = swagger_client.StoresEmailApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | The store to fetch

try:
    # Get store email settings
    api_response = api_instance.stores_get_store_email_settings(store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoresEmailApi->stores_get_store_email_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store to fetch | 

### Return type

[**EmailSettingsData**](EmailSettingsData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stores_update_store_email_settings**
> EmailSettingsData stores_update_store_email_settings(body)

Update store email settings

Update a store's email settings

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
api_instance = swagger_client.StoresEmailApi(swagger_client.ApiClient(configuration))
body = swagger_client.EmailSettingsData() # EmailSettingsData | 

try:
    # Update store email settings
    api_response = api_instance.stores_update_store_email_settings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoresEmailApi->stores_update_store_email_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmailSettingsData**](EmailSettingsData.md)|  | 

### Return type

[**EmailSettingsData**](EmailSettingsData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

