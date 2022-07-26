# swagger_client.StoresUsersApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stores_add_store_user**](StoresUsersApi.md#stores_add_store_user) | **POST** /api/v1/stores/{storeId}/users | Add a store user
[**stores_get_store_users**](StoresUsersApi.md#stores_get_store_users) | **GET** /api/v1/stores/{storeId}/users | Get store users
[**stores_remove_store_user**](StoresUsersApi.md#stores_remove_store_user) | **DELETE** /api/v1/stores/{storeId}/users/{userId} | Remove Store User

# **stores_add_store_user**
> stores_add_store_user(body)

Add a store user

Add a store user

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
api_instance = swagger_client.StoresUsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.StoreUserData() # StoreUserData | 

try:
    # Add a store user
    api_instance.stores_add_store_user(body)
except ApiException as e:
    print("Exception when calling StoresUsersApi->stores_add_store_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StoreUserData**](StoreUserData.md)|  | 

### Return type

void (empty response body)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stores_get_store_users**
> StoreUserDataList stores_get_store_users(store_id)

Get store users

View users of the specified store

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
api_instance = swagger_client.StoresUsersApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | The store to fetch

try:
    # Get store users
    api_response = api_instance.stores_get_store_users(store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoresUsersApi->stores_get_store_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store to fetch | 

### Return type

[**StoreUserDataList**](StoreUserDataList.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stores_remove_store_user**
> stores_remove_store_user(store_id, user_id)

Remove Store User

Removes the specified store user. If there is no other owner, this endpoint will fail.

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
api_instance = swagger_client.StoresUsersApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | The store
user_id = 'user_id_example' # str | The user

try:
    # Remove Store User
    api_instance.stores_remove_store_user(store_id, user_id)
except ApiException as e:
    print("Exception when calling StoresUsersApi->stores_remove_store_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store | 
 **user_id** | **str**| The user | 

### Return type

void (empty response body)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

