# swagger_client.StorePaymentMethodsLightningNetworkApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_stores_store_id_payment_methods_lightning_network_crypto_code_delete**](StorePaymentMethodsLightningNetworkApi.md#api_v1_stores_store_id_payment_methods_lightning_network_crypto_code_delete) | **DELETE** /api/v1/stores/{storeId}/payment-methods/LightningNetwork/{cryptoCode} | Remove store Lightning Network payment method
[**store_lightning_network_payment_methods_get_lightning_network_payment_method**](StorePaymentMethodsLightningNetworkApi.md#store_lightning_network_payment_methods_get_lightning_network_payment_method) | **GET** /api/v1/stores/{storeId}/payment-methods/LightningNetwork/{cryptoCode} | Get store Lightning Network payment method
[**store_lightning_network_payment_methods_get_lightning_network_payment_methods**](StorePaymentMethodsLightningNetworkApi.md#store_lightning_network_payment_methods_get_lightning_network_payment_methods) | **GET** /api/v1/stores/{storeId}/payment-methods/LightningNetwork | Get store Lightning Network payment methods
[**store_lightning_network_payment_methods_update_lightning_network_payment_method**](StorePaymentMethodsLightningNetworkApi.md#store_lightning_network_payment_methods_update_lightning_network_payment_method) | **PUT** /api/v1/stores/{storeId}/payment-methods/LightningNetwork/{cryptoCode} | Update store Lightning Network payment method

# **api_v1_stores_store_id_payment_methods_lightning_network_crypto_code_delete**
> api_v1_stores_store_id_payment_methods_lightning_network_crypto_code_delete(store_id, crypto_code)

Remove store Lightning Network payment method

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
api_instance = swagger_client.StorePaymentMethodsLightningNetworkApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | The store to fetch
crypto_code = 'crypto_code_example' # str | The crypto code of the payment method to update

try:
    # Remove store Lightning Network payment method
    api_instance.api_v1_stores_store_id_payment_methods_lightning_network_crypto_code_delete(store_id, crypto_code)
except ApiException as e:
    print("Exception when calling StorePaymentMethodsLightningNetworkApi->api_v1_stores_store_id_payment_methods_lightning_network_crypto_code_delete: %s\n" % e)
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

# **store_lightning_network_payment_methods_get_lightning_network_payment_method**
> LightningNetworkPaymentMethodData store_lightning_network_payment_methods_get_lightning_network_payment_method(store_id, crypto_code)

Get store Lightning Network payment method

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
api_instance = swagger_client.StorePaymentMethodsLightningNetworkApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | The store to fetch
crypto_code = 'crypto_code_example' # str | The crypto code of the payment method to fetch

try:
    # Get store Lightning Network payment method
    api_response = api_instance.store_lightning_network_payment_methods_get_lightning_network_payment_method(store_id, crypto_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorePaymentMethodsLightningNetworkApi->store_lightning_network_payment_methods_get_lightning_network_payment_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store to fetch | 
 **crypto_code** | **str**| The crypto code of the payment method to fetch | 

### Return type

[**LightningNetworkPaymentMethodData**](LightningNetworkPaymentMethodData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_lightning_network_payment_methods_get_lightning_network_payment_methods**
> LightningNetworkPaymentMethodDataList store_lightning_network_payment_methods_get_lightning_network_payment_methods(store_id, enabled=enabled)

Get store Lightning Network payment methods

View information about the stores' configured Lightning Network payment methods

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
api_instance = swagger_client.StorePaymentMethodsLightningNetworkApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | The store to fetch
enabled = true # bool | Fetch payment methods that are enabled/disabled only (optional)

try:
    # Get store Lightning Network payment methods
    api_response = api_instance.store_lightning_network_payment_methods_get_lightning_network_payment_methods(store_id, enabled=enabled)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorePaymentMethodsLightningNetworkApi->store_lightning_network_payment_methods_get_lightning_network_payment_methods: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store to fetch | 
 **enabled** | **bool**| Fetch payment methods that are enabled/disabled only | [optional] 

### Return type

[**LightningNetworkPaymentMethodDataList**](LightningNetworkPaymentMethodDataList.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_lightning_network_payment_methods_update_lightning_network_payment_method**
> LightningNetworkPaymentMethodData store_lightning_network_payment_methods_update_lightning_network_payment_method(body, store_id, crypto_code)

Update store Lightning Network payment method

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
api_instance = swagger_client.StorePaymentMethodsLightningNetworkApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateLightningNetworkPaymentMethodRequest() # UpdateLightningNetworkPaymentMethodRequest | 
store_id = 'store_id_example' # str | The store to fetch
crypto_code = 'crypto_code_example' # str | The crypto code of the payment method to update

try:
    # Update store Lightning Network payment method
    api_response = api_instance.store_lightning_network_payment_methods_update_lightning_network_payment_method(body, store_id, crypto_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorePaymentMethodsLightningNetworkApi->store_lightning_network_payment_methods_update_lightning_network_payment_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateLightningNetworkPaymentMethodRequest**](UpdateLightningNetworkPaymentMethodRequest.md)|  | 
 **store_id** | **str**| The store to fetch | 
 **crypto_code** | **str**| The crypto code of the payment method to update | 

### Return type

[**LightningNetworkPaymentMethodData**](LightningNetworkPaymentMethodData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

