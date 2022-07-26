# swagger_client.StorePaymentMethodsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**store_payment_methods_get_store_payment_methods**](StorePaymentMethodsApi.md#store_payment_methods_get_store_payment_methods) | **GET** /api/v1/stores/{storeId}/payment-methods | Get store payment methods

# **store_payment_methods_get_store_payment_methods**
> list[GenericPaymentMethodData] store_payment_methods_get_store_payment_methods(store_id, enabled=enabled)

Get store payment methods

View information about the stores' configured payment methods

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
api_instance = swagger_client.StorePaymentMethodsApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | The store to fetch
enabled = true # bool | Fetch payment methods that are enabled/disabled only (optional)

try:
    # Get store payment methods
    api_response = api_instance.store_payment_methods_get_store_payment_methods(store_id, enabled=enabled)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorePaymentMethodsApi->store_payment_methods_get_store_payment_methods: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store to fetch | 
 **enabled** | **bool**| Fetch payment methods that are enabled/disabled only | [optional] 

### Return type

[**list[GenericPaymentMethodData]**](GenericPaymentMethodData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

