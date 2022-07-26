# swagger_client.PayoutProcessorsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**payout_processors_get_payout_processors**](PayoutProcessorsApi.md#payout_processors_get_payout_processors) | **GET** /api/v1/payout-processors | Get payout processors

# **payout_processors_get_payout_processors**
> list[PayoutProcessorData] payout_processors_get_payout_processors(store_id)

Get payout processors

Get payout processors available in this instance

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
api_instance = swagger_client.PayoutProcessorsApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | The store to fetch

try:
    # Get payout processors
    api_response = api_instance.payout_processors_get_payout_processors(store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayoutProcessorsApi->payout_processors_get_payout_processors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store to fetch | 

### Return type

[**list[PayoutProcessorData]**](PayoutProcessorData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

