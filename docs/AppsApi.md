# swagger_client.AppsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apps_create_point_of_sale_app**](AppsApi.md#apps_create_point_of_sale_app) | **POST** /api/v1/stores/{storeId}/apps/pos | Create a new Point of Sale app
[**apps_delete_point_of_sale_app**](AppsApi.md#apps_delete_point_of_sale_app) | **DELETE** /api/v1/apps/{appId} | Delete app
[**apps_get_point_of_sale_app**](AppsApi.md#apps_get_point_of_sale_app) | **GET** /api/v1/apps/{appId} | Get basic app data

# **apps_create_point_of_sale_app**
> PointOfSaleAppData apps_create_point_of_sale_app(store_id, body=body)

Create a new Point of Sale app

Point of Sale apps allows accepting payments for items in a virtual store

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
api_instance = swagger_client.AppsApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | The store ID
body = swagger_client.AppsPosBody() # AppsPosBody |  (optional)

try:
    # Create a new Point of Sale app
    api_response = api_instance.apps_create_point_of_sale_app(store_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsApi->apps_create_point_of_sale_app: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store ID | 
 **body** | [**AppsPosBody**](AppsPosBody.md)|  | [optional] 

### Return type

[**PointOfSaleAppData**](PointOfSaleAppData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_delete_point_of_sale_app**
> apps_delete_point_of_sale_app()

Delete app

Deletes apps with specified ID

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
api_instance = swagger_client.AppsApi(swagger_client.ApiClient(configuration))

try:
    # Delete app
    api_instance.apps_delete_point_of_sale_app()
except ApiException as e:
    print("Exception when calling AppsApi->apps_delete_point_of_sale_app: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_get_point_of_sale_app**
> BasicAppData apps_get_point_of_sale_app()

Get basic app data

Returns basic app data shared between all types of apps

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
api_instance = swagger_client.AppsApi(swagger_client.ApiClient(configuration))

try:
    # Get basic app data
    api_response = api_instance.apps_get_point_of_sale_app()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsApi->apps_get_point_of_sale_app: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**BasicAppData**](BasicAppData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

