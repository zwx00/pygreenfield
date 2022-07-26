# swagger_client.StorePaymentMethodsOnChainApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_stores_store_id_payment_methods_onchain_crypto_code_delete**](StorePaymentMethodsOnChainApi.md#api_v1_stores_store_id_payment_methods_onchain_crypto_code_delete) | **DELETE** /api/v1/stores/{storeId}/payment-methods/onchain/{cryptoCode} | Remove store on-chain payment method
[**store_on_chain_payment_methods_generate_on_chain_wallet**](StorePaymentMethodsOnChainApi.md#store_on_chain_payment_methods_generate_on_chain_wallet) | **POST** /api/v1/stores/{storeId}/payment-methods/onchain/{cryptoCode}/generate | Generate store on-chain wallet
[**store_on_chain_payment_methods_get_on_chain_payment_method**](StorePaymentMethodsOnChainApi.md#store_on_chain_payment_methods_get_on_chain_payment_method) | **GET** /api/v1/stores/{storeId}/payment-methods/onchain/{cryptoCode} | Get store on-chain payment method
[**store_on_chain_payment_methods_get_on_chain_payment_method_preview**](StorePaymentMethodsOnChainApi.md#store_on_chain_payment_methods_get_on_chain_payment_method_preview) | **GET** /api/v1/stores/{storeId}/payment-methods/OnChain/{cryptoCode}/preview | Preview store on-chain payment method addresses
[**store_on_chain_payment_methods_get_on_chain_payment_methods**](StorePaymentMethodsOnChainApi.md#store_on_chain_payment_methods_get_on_chain_payment_methods) | **GET** /api/v1/stores/{storeId}/payment-methods/OnChain | Get store on-chain payment methods
[**store_on_chain_payment_methods_post_on_chain_payment_method_preview**](StorePaymentMethodsOnChainApi.md#store_on_chain_payment_methods_post_on_chain_payment_method_preview) | **POST** /api/v1/stores/{storeId}/payment-methods/OnChain/{cryptoCode}/preview | Preview proposed store on-chain payment method addresses
[**store_on_chain_payment_methods_update_on_chain_payment_method**](StorePaymentMethodsOnChainApi.md#store_on_chain_payment_methods_update_on_chain_payment_method) | **PUT** /api/v1/stores/{storeId}/payment-methods/onchain/{cryptoCode} | Update store on-chain payment method

# **api_v1_stores_store_id_payment_methods_onchain_crypto_code_delete**
> api_v1_stores_store_id_payment_methods_onchain_crypto_code_delete(store_id, crypto_code)

Remove store on-chain payment method

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
api_instance = swagger_client.StorePaymentMethodsOnChainApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | The store to fetch
crypto_code = 'crypto_code_example' # str | The crypto code of the payment method to update

try:
    # Remove store on-chain payment method
    api_instance.api_v1_stores_store_id_payment_methods_onchain_crypto_code_delete(store_id, crypto_code)
except ApiException as e:
    print("Exception when calling StorePaymentMethodsOnChainApi->api_v1_stores_store_id_payment_methods_onchain_crypto_code_delete: %s\n" % e)
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

# **store_on_chain_payment_methods_generate_on_chain_wallet**
> OnChainPaymentMethodDataWithSensitiveData store_on_chain_payment_methods_generate_on_chain_wallet(body, store_id, crypto_code)

Generate store on-chain wallet

Generate a wallet and update the specified store's payment method to it

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
api_instance = swagger_client.StorePaymentMethodsOnChainApi(swagger_client.ApiClient(configuration))
body = swagger_client.GenerateOnChainWalletRequest() # GenerateOnChainWalletRequest | 
store_id = 'store_id_example' # str | The store to fetch
crypto_code = 'crypto_code_example' # str | The crypto code of the payment method to update

try:
    # Generate store on-chain wallet
    api_response = api_instance.store_on_chain_payment_methods_generate_on_chain_wallet(body, store_id, crypto_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorePaymentMethodsOnChainApi->store_on_chain_payment_methods_generate_on_chain_wallet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GenerateOnChainWalletRequest**](GenerateOnChainWalletRequest.md)|  | 
 **store_id** | **str**| The store to fetch | 
 **crypto_code** | **str**| The crypto code of the payment method to update | 

### Return type

[**OnChainPaymentMethodDataWithSensitiveData**](OnChainPaymentMethodDataWithSensitiveData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_on_chain_payment_methods_get_on_chain_payment_method**
> OnChainPaymentMethodData store_on_chain_payment_methods_get_on_chain_payment_method(store_id, crypto_code)

Get store on-chain payment method

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
api_instance = swagger_client.StorePaymentMethodsOnChainApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | The store to fetch
crypto_code = 'crypto_code_example' # str | The crypto code of the payment method to fetch

try:
    # Get store on-chain payment method
    api_response = api_instance.store_on_chain_payment_methods_get_on_chain_payment_method(store_id, crypto_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorePaymentMethodsOnChainApi->store_on_chain_payment_methods_get_on_chain_payment_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store to fetch | 
 **crypto_code** | **str**| The crypto code of the payment method to fetch | 

### Return type

[**OnChainPaymentMethodData**](OnChainPaymentMethodData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_on_chain_payment_methods_get_on_chain_payment_method_preview**
> OnChainPaymentMethodPreviewResultData store_on_chain_payment_methods_get_on_chain_payment_method_preview(store_id, crypto_code, offset=offset, amount=amount)

Preview store on-chain payment method addresses

View addresses of the current payment method of the store

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
api_instance = swagger_client.StorePaymentMethodsOnChainApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | The store to fetch
crypto_code = 'crypto_code_example' # str | The crypto code of the payment method to fetch
offset = 1.2 # float | From which index to fetch the addresses (optional)
amount = 1.2 # float | Number of addresses to preview (optional)

try:
    # Preview store on-chain payment method addresses
    api_response = api_instance.store_on_chain_payment_methods_get_on_chain_payment_method_preview(store_id, crypto_code, offset=offset, amount=amount)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorePaymentMethodsOnChainApi->store_on_chain_payment_methods_get_on_chain_payment_method_preview: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store to fetch | 
 **crypto_code** | **str**| The crypto code of the payment method to fetch | 
 **offset** | **float**| From which index to fetch the addresses | [optional] 
 **amount** | **float**| Number of addresses to preview | [optional] 

### Return type

[**OnChainPaymentMethodPreviewResultData**](OnChainPaymentMethodPreviewResultData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_on_chain_payment_methods_get_on_chain_payment_methods**
> OnChainPaymentMethodDataList store_on_chain_payment_methods_get_on_chain_payment_methods(store_id, enabled=enabled)

Get store on-chain payment methods

View information about the stores' configured on-chain payment methods

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
api_instance = swagger_client.StorePaymentMethodsOnChainApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | The store to fetch
enabled = true # bool | Fetch payment methods that are enabled/disabled only (optional)

try:
    # Get store on-chain payment methods
    api_response = api_instance.store_on_chain_payment_methods_get_on_chain_payment_methods(store_id, enabled=enabled)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorePaymentMethodsOnChainApi->store_on_chain_payment_methods_get_on_chain_payment_methods: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store to fetch | 
 **enabled** | **bool**| Fetch payment methods that are enabled/disabled only | [optional] 

### Return type

[**OnChainPaymentMethodDataList**](OnChainPaymentMethodDataList.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_on_chain_payment_methods_post_on_chain_payment_method_preview**
> OnChainPaymentMethodPreviewResultData store_on_chain_payment_methods_post_on_chain_payment_method_preview(body, store_id, crypto_code, offset=offset, amount=amount)

Preview proposed store on-chain payment method addresses

View addresses of a proposed payment method of the store

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
api_instance = swagger_client.StorePaymentMethodsOnChainApi(swagger_client.ApiClient(configuration))
body = swagger_client.CryptoCodePreviewBody() # CryptoCodePreviewBody | 
store_id = 'store_id_example' # str | The store to fetch
crypto_code = 'crypto_code_example' # str | The crypto code of the payment method to fetch
offset = 1.2 # float | From which index to fetch the addresses (optional)
amount = 1.2 # float | Number of addresses to preview (optional)

try:
    # Preview proposed store on-chain payment method addresses
    api_response = api_instance.store_on_chain_payment_methods_post_on_chain_payment_method_preview(body, store_id, crypto_code, offset=offset, amount=amount)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorePaymentMethodsOnChainApi->store_on_chain_payment_methods_post_on_chain_payment_method_preview: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CryptoCodePreviewBody**](CryptoCodePreviewBody.md)|  | 
 **store_id** | **str**| The store to fetch | 
 **crypto_code** | **str**| The crypto code of the payment method to fetch | 
 **offset** | **float**| From which index to fetch the addresses | [optional] 
 **amount** | **float**| Number of addresses to preview | [optional] 

### Return type

[**OnChainPaymentMethodPreviewResultData**](OnChainPaymentMethodPreviewResultData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_on_chain_payment_methods_update_on_chain_payment_method**
> OnChainPaymentMethodData store_on_chain_payment_methods_update_on_chain_payment_method(body, store_id, crypto_code)

Update store on-chain payment method

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
api_instance = swagger_client.StorePaymentMethodsOnChainApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateOnChainPaymentMethodRequest() # UpdateOnChainPaymentMethodRequest | 
store_id = 'store_id_example' # str | The store to fetch
crypto_code = 'crypto_code_example' # str | The crypto code of the payment method to update

try:
    # Update store on-chain payment method
    api_response = api_instance.store_on_chain_payment_methods_update_on_chain_payment_method(body, store_id, crypto_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorePaymentMethodsOnChainApi->store_on_chain_payment_methods_update_on_chain_payment_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateOnChainPaymentMethodRequest**](UpdateOnChainPaymentMethodRequest.md)|  | 
 **store_id** | **str**| The store to fetch | 
 **crypto_code** | **str**| The crypto code of the payment method to update | 

### Return type

[**OnChainPaymentMethodData**](OnChainPaymentMethodData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

