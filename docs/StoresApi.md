# swagger_client.StoresApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_stores_post**](StoresApi.md#api_v1_stores_post) | **POST** /api/v1/stores | Create a new store
[**api_v1_stores_store_id_delete**](StoresApi.md#api_v1_stores_store_id_delete) | **DELETE** /api/v1/stores/{storeId} | Remove Store
[**stores_get_store**](StoresApi.md#stores_get_store) | **GET** /api/v1/stores/{storeId} | Get store
[**stores_get_stores**](StoresApi.md#stores_get_stores) | **GET** /api/v1/stores | Get stores
[**stores_update_store**](StoresApi.md#stores_update_store) | **PUT** /api/v1/stores/{storeId} | Update store

# **api_v1_stores_post**
> StoreData api_v1_stores_post(body)

Create a new store

Create a new store

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
api_instance = swagger_client.StoresApi(swagger_client.ApiClient(configuration))
body = swagger_client.StoreBaseData() # StoreBaseData | 

try:
    # Create a new store
    api_response = api_instance.api_v1_stores_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoresApi->api_v1_stores_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StoreBaseData**](StoreBaseData.md)|  | 

### Return type

[**StoreData**](StoreData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_stores_store_id_delete**
> api_v1_stores_store_id_delete(store_id)

Remove Store

Removes the specified store. If there is another user with access, only your access will be removed.

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
api_instance = swagger_client.StoresApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | The store to remove

try:
    # Remove Store
    api_instance.api_v1_stores_store_id_delete(store_id)
except ApiException as e:
    print("Exception when calling StoresApi->api_v1_stores_store_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store to remove | 

### Return type

void (empty response body)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stores_get_store**
> StoreData stores_get_store(store_id)

Get store

View information about the specified store

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
api_instance = swagger_client.StoresApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | The store to fetch

try:
    # Get store
    api_response = api_instance.stores_get_store(store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoresApi->stores_get_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store to fetch | 

### Return type

[**StoreData**](StoreData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stores_get_stores**
> StoreDataList stores_get_stores()

Get stores

View information about the available stores

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
api_instance = swagger_client.StoresApi(swagger_client.ApiClient(configuration))

try:
    # Get stores
    api_response = api_instance.stores_get_stores()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoresApi->stores_get_stores: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StoreDataList**](StoreDataList.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stores_update_store**
> StoreData stores_update_store(body, store_id)

Update store

Update the specified store

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
api_instance = swagger_client.StoresApi(swagger_client.ApiClient(configuration))
body = swagger_client.StoreData() # StoreData | 
store_id = 'store_id_example' # str | The store to update

try:
    # Update store
    api_response = api_instance.stores_update_store(body, store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoresApi->stores_update_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StoreData**](StoreData.md)|  | 
 **store_id** | **str**| The store to update | 

### Return type

[**StoreData**](StoreData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

