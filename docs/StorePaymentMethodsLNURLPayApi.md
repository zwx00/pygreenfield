# swagger_client.StorePaymentMethodsLNURLPayApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_stores_store_id_payment_methods_lnurl_crypto_code_delete**](StorePaymentMethodsLNURLPayApi.md#api_v1_stores_store_id_payment_methods_lnurl_crypto_code_delete) | **DELETE** /api/v1/stores/{storeId}/payment-methods/LNURL/{cryptoCode} | Remove store LNURL Pay payment method
[**store_lnurl_pay_payment_methods_get_lnurl_pay_payment_method**](StorePaymentMethodsLNURLPayApi.md#store_lnurl_pay_payment_methods_get_lnurl_pay_payment_method) | **GET** /api/v1/stores/{storeId}/payment-methods/LNURL/{cryptoCode} | Get store LNURL Pay payment method
[**store_lnurl_pay_payment_methods_get_lnurl_pay_payment_methods**](StorePaymentMethodsLNURLPayApi.md#store_lnurl_pay_payment_methods_get_lnurl_pay_payment_methods) | **GET** /api/v1/stores/{storeId}/payment-methods/LNURL | Get store LNURL payment methods
[**store_lnurl_pay_payment_methods_update_lnurl_pay_payment_method**](StorePaymentMethodsLNURLPayApi.md#store_lnurl_pay_payment_methods_update_lnurl_pay_payment_method) | **PUT** /api/v1/stores/{storeId}/payment-methods/LNURL/{cryptoCode} | Update store LNURL Pay payment method

# **api_v1_stores_store_id_payment_methods_lnurl_crypto_code_delete**
> api_v1_stores_store_id_payment_methods_lnurl_crypto_code_delete(store_id, crypto_code)

Remove store LNURL Pay payment method

Removes the specified store payment method.

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
api_instance = swagger_client.StorePaymentMethodsLNURLPayApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | The store to fetch
crypto_code = 'crypto_code_example' # str | The crypto code of the payment method to update

try:
    # Remove store LNURL Pay payment method
    api_instance.api_v1_stores_store_id_payment_methods_lnurl_crypto_code_delete(store_id, crypto_code)
except ApiException as e:
    print("Exception when calling StorePaymentMethodsLNURLPayApi->api_v1_stores_store_id_payment_methods_lnurl_crypto_code_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store to fetch | 
 **crypto_code** | **str**| The crypto code of the payment method to update | 

### Return type

void (empty response body)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_lnurl_pay_payment_methods_get_lnurl_pay_payment_method**
> LNURLPayPaymentMethodData store_lnurl_pay_payment_methods_get_lnurl_pay_payment_method(store_id, crypto_code)

Get store LNURL Pay payment method

View information about the specified payment method

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
api_instance = swagger_client.StorePaymentMethodsLNURLPayApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | The store to fetch
crypto_code = 'crypto_code_example' # str | The crypto code of the payment method to fetch

try:
    # Get store LNURL Pay payment method
    api_response = api_instance.store_lnurl_pay_payment_methods_get_lnurl_pay_payment_method(store_id, crypto_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorePaymentMethodsLNURLPayApi->store_lnurl_pay_payment_methods_get_lnurl_pay_payment_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store to fetch | 
 **crypto_code** | **str**| The crypto code of the payment method to fetch | 

### Return type

[**LNURLPayPaymentMethodData**](LNURLPayPaymentMethodData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_lnurl_pay_payment_methods_get_lnurl_pay_payment_methods**
> LNURLPayPaymentMethodDataList store_lnurl_pay_payment_methods_get_lnurl_pay_payment_methods(store_id, enabled=enabled)

Get store LNURL payment methods

View information about the stores' configured LNURL payment methods

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
api_instance = swagger_client.StorePaymentMethodsLNURLPayApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | The store to fetch
enabled = true # bool | Fetch payment methods that are enabled/disabled only (optional)

try:
    # Get store LNURL payment methods
    api_response = api_instance.store_lnurl_pay_payment_methods_get_lnurl_pay_payment_methods(store_id, enabled=enabled)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorePaymentMethodsLNURLPayApi->store_lnurl_pay_payment_methods_get_lnurl_pay_payment_methods: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store to fetch | 
 **enabled** | **bool**| Fetch payment methods that are enabled/disabled only | [optional] 

### Return type

[**LNURLPayPaymentMethodDataList**](LNURLPayPaymentMethodDataList.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_lnurl_pay_payment_methods_update_lnurl_pay_payment_method**
> LNURLPayPaymentMethodData store_lnurl_pay_payment_methods_update_lnurl_pay_payment_method(body, store_id, crypto_code)

Update store LNURL Pay payment method

Update the specified store's payment method

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
api_instance = swagger_client.StorePaymentMethodsLNURLPayApi(swagger_client.ApiClient(configuration))
body = swagger_client.LNURLPayPaymentMethodData() # LNURLPayPaymentMethodData | 
store_id = 'store_id_example' # str | The store to fetch
crypto_code = 'crypto_code_example' # str | The crypto code of the payment method to update

try:
    # Update store LNURL Pay payment method
    api_response = api_instance.store_lnurl_pay_payment_methods_update_lnurl_pay_payment_method(body, store_id, crypto_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorePaymentMethodsLNURLPayApi->store_lnurl_pay_payment_methods_update_lnurl_pay_payment_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LNURLPayPaymentMethodData**](LNURLPayPaymentMethodData.md)|  | 
 **store_id** | **str**| The store to fetch | 
 **crypto_code** | **str**| The crypto code of the payment method to update | 

### Return type

[**LNURLPayPaymentMethodData**](LNURLPayPaymentMethodData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

