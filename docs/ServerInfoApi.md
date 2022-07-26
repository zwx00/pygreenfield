# swagger_client.ServerInfoApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**server_info_get_server_info**](ServerInfoApi.md#server_info_get_server_info) | **GET** /api/v1/server/info | Get server info

# **server_info_get_server_info**
> ApplicationServerInfoData server_info_get_server_info()

Get server info

Information about the server, chains and sync states

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
api_instance = swagger_client.ServerInfoApi(swagger_client.ApiClient(configuration))

try:
    # Get server info
    api_response = api_instance.server_info_get_server_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerInfoApi->server_info_get_server_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApplicationServerInfoData**](ApplicationServerInfoData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

