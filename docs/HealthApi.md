# swagger_client.HealthApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**health_get_health**](HealthApi.md#health_get_health) | **GET** /api/v1/health | Get health status

# **health_get_health**
> ApplicationHealthData health_get_health()

Get health status

Check the instance health status

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HealthApi()

try:
    # Get health status
    api_response = api_instance.health_get_health()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HealthApi->health_get_health: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApplicationHealthData**](ApplicationHealthData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

