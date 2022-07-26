# swagger_client.LightningStoreApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**store_lightning_node_api_connect_to_node**](LightningStoreApi.md#store_lightning_node_api_connect_to_node) | **POST** /api/v1/stores/{storeId}/lightning/{cryptoCode}/connect | Connect to lightning node
[**store_lightning_node_api_create_invoice**](LightningStoreApi.md#store_lightning_node_api_create_invoice) | **POST** /api/v1/stores/{storeId}/lightning/{cryptoCode}/invoices | Create lightning invoice
[**store_lightning_node_api_get_balance**](LightningStoreApi.md#store_lightning_node_api_get_balance) | **GET** /api/v1/stores/{storeId}/lightning/{cryptoCode}/balance | Get node balance
[**store_lightning_node_api_get_channels**](LightningStoreApi.md#store_lightning_node_api_get_channels) | **GET** /api/v1/stores/{storeId}/lightning/{cryptoCode}/channels | Get channels
[**store_lightning_node_api_get_deposit_address**](LightningStoreApi.md#store_lightning_node_api_get_deposit_address) | **POST** /api/v1/stores/{storeId}/lightning/{cryptoCode}/address | Get deposit address
[**store_lightning_node_api_get_info**](LightningStoreApi.md#store_lightning_node_api_get_info) | **GET** /api/v1/stores/{storeId}/lightning/{cryptoCode}/info | Get node information
[**store_lightning_node_api_get_invoice**](LightningStoreApi.md#store_lightning_node_api_get_invoice) | **GET** /api/v1/stores/{storeId}/lightning/{cryptoCode}/invoices/{id} | Get invoice
[**store_lightning_node_api_get_payment**](LightningStoreApi.md#store_lightning_node_api_get_payment) | **GET** /api/v1/stores/{storeId}/lightning/{cryptoCode}/payments/{paymentHash} | Get payment
[**store_lightning_node_api_open_channel**](LightningStoreApi.md#store_lightning_node_api_open_channel) | **POST** /api/v1/stores/{storeId}/lightning/{cryptoCode}/channels | Open channel
[**store_lightning_node_api_pay_invoice**](LightningStoreApi.md#store_lightning_node_api_pay_invoice) | **POST** /api/v1/stores/{storeId}/lightning/{cryptoCode}/invoices/pay | Pay Lightning Invoice

# **store_lightning_node_api_connect_to_node**
> store_lightning_node_api_connect_to_node(body, crypto_code, store_id)

Connect to lightning node

Connect to another lightning node.

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
api_instance = swagger_client.LightningStoreApi(swagger_client.ApiClient(configuration))
body = swagger_client.ConnectToNodeRequest() # ConnectToNodeRequest | 
crypto_code = 'crypto_code_example' # str | The cryptoCode of the lightning-node to query
store_id = 'store_id_example' # str | The store id with the lightning-node configuration to query

try:
    # Connect to lightning node
    api_instance.store_lightning_node_api_connect_to_node(body, crypto_code, store_id)
except ApiException as e:
    print("Exception when calling LightningStoreApi->store_lightning_node_api_connect_to_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConnectToNodeRequest**](ConnectToNodeRequest.md)|  | 
 **crypto_code** | **str**| The cryptoCode of the lightning-node to query | 
 **store_id** | **str**| The store id with the lightning-node configuration to query | 

### Return type

void (empty response body)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_lightning_node_api_create_invoice**
> LightningInvoiceData store_lightning_node_api_create_invoice(body, crypto_code, store_id)

Create lightning invoice

Create a lightning invoice.

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
api_instance = swagger_client.LightningStoreApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateLightningInvoiceRequest() # CreateLightningInvoiceRequest | 
crypto_code = 'crypto_code_example' # str | The cryptoCode of the lightning-node to query
store_id = 'store_id_example' # str | The store id with the lightning-node configuration to query

try:
    # Create lightning invoice
    api_response = api_instance.store_lightning_node_api_create_invoice(body, crypto_code, store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LightningStoreApi->store_lightning_node_api_create_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateLightningInvoiceRequest**](CreateLightningInvoiceRequest.md)|  | 
 **crypto_code** | **str**| The cryptoCode of the lightning-node to query | 
 **store_id** | **str**| The store id with the lightning-node configuration to query | 

### Return type

[**LightningInvoiceData**](LightningInvoiceData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_lightning_node_api_get_balance**
> LightningNodeBalanceData store_lightning_node_api_get_balance(crypto_code, store_id)

Get node balance

View balance of the lightning node

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
api_instance = swagger_client.LightningStoreApi(swagger_client.ApiClient(configuration))
crypto_code = 'crypto_code_example' # str | The cryptoCode of the lightning-node to query
store_id = 'store_id_example' # str | The store id with the lightning-node configuration to query

try:
    # Get node balance
    api_response = api_instance.store_lightning_node_api_get_balance(crypto_code, store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LightningStoreApi->store_lightning_node_api_get_balance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crypto_code** | **str**| The cryptoCode of the lightning-node to query | 
 **store_id** | **str**| The store id with the lightning-node configuration to query | 

### Return type

[**LightningNodeBalanceData**](LightningNodeBalanceData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_lightning_node_api_get_channels**
> list[LightningChannelData] store_lightning_node_api_get_channels(crypto_code, store_id)

Get channels

View information about the current channels of the lightning node

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
api_instance = swagger_client.LightningStoreApi(swagger_client.ApiClient(configuration))
crypto_code = 'crypto_code_example' # str | The cryptoCode of the lightning-node to query
store_id = 'store_id_example' # str | The store id with the lightning-node configuration to query

try:
    # Get channels
    api_response = api_instance.store_lightning_node_api_get_channels(crypto_code, store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LightningStoreApi->store_lightning_node_api_get_channels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crypto_code** | **str**| The cryptoCode of the lightning-node to query | 
 **store_id** | **str**| The store id with the lightning-node configuration to query | 

### Return type

[**list[LightningChannelData]**](LightningChannelData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_lightning_node_api_get_deposit_address**
> str store_lightning_node_api_get_deposit_address(crypto_code, store_id)

Get deposit address

Get an on-chain deposit address for the lightning node 

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
api_instance = swagger_client.LightningStoreApi(swagger_client.ApiClient(configuration))
crypto_code = 'crypto_code_example' # str | The cryptoCode of the lightning-node to query
store_id = 'store_id_example' # str | The store id with the lightning-node configuration to query

try:
    # Get deposit address
    api_response = api_instance.store_lightning_node_api_get_deposit_address(crypto_code, store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LightningStoreApi->store_lightning_node_api_get_deposit_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crypto_code** | **str**| The cryptoCode of the lightning-node to query | 
 **store_id** | **str**| The store id with the lightning-node configuration to query | 

### Return type

**str**

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_lightning_node_api_get_info**
> LightningNodeInformationData store_lightning_node_api_get_info(crypto_code, store_id)

Get node information

View information about the lightning node

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
api_instance = swagger_client.LightningStoreApi(swagger_client.ApiClient(configuration))
crypto_code = 'crypto_code_example' # str | The cryptoCode of the lightning-node to query
store_id = 'store_id_example' # str | The store id with the lightning-node configuration to query

try:
    # Get node information
    api_response = api_instance.store_lightning_node_api_get_info(crypto_code, store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LightningStoreApi->store_lightning_node_api_get_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crypto_code** | **str**| The cryptoCode of the lightning-node to query | 
 **store_id** | **str**| The store id with the lightning-node configuration to query | 

### Return type

[**LightningNodeInformationData**](LightningNodeInformationData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_lightning_node_api_get_invoice**
> LightningInvoiceData store_lightning_node_api_get_invoice(crypto_code, store_id, id)

Get invoice

View information about the requested lightning invoice

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
api_instance = swagger_client.LightningStoreApi(swagger_client.ApiClient(configuration))
crypto_code = 'crypto_code_example' # str | The cryptoCode of the lightning-node to query
store_id = 'store_id_example' # str | The store id with the lightning-node configuration to query
id = 'id_example' # str | The id of the lightning invoice.

try:
    # Get invoice
    api_response = api_instance.store_lightning_node_api_get_invoice(crypto_code, store_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LightningStoreApi->store_lightning_node_api_get_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crypto_code** | **str**| The cryptoCode of the lightning-node to query | 
 **store_id** | **str**| The store id with the lightning-node configuration to query | 
 **id** | **str**| The id of the lightning invoice. | 

### Return type

[**LightningInvoiceData**](LightningInvoiceData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_lightning_node_api_get_payment**
> LightningPaymentData store_lightning_node_api_get_payment(crypto_code, store_id, payment_hash)

Get payment

View information about the requested lightning payment

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
api_instance = swagger_client.LightningStoreApi(swagger_client.ApiClient(configuration))
crypto_code = 'crypto_code_example' # str | The cryptoCode of the lightning-node to query
store_id = 'store_id_example' # str | The store id with the lightning-node configuration to query
payment_hash = 'payment_hash_example' # str | The payment hash of the lightning payment.

try:
    # Get payment
    api_response = api_instance.store_lightning_node_api_get_payment(crypto_code, store_id, payment_hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LightningStoreApi->store_lightning_node_api_get_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crypto_code** | **str**| The cryptoCode of the lightning-node to query | 
 **store_id** | **str**| The store id with the lightning-node configuration to query | 
 **payment_hash** | **str**| The payment hash of the lightning payment. | 

### Return type

[**LightningPaymentData**](LightningPaymentData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_lightning_node_api_open_channel**
> store_lightning_node_api_open_channel(body, crypto_code, store_id)

Open channel

Open a channel with another lightning node. You should connect to that node first.

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
api_instance = swagger_client.LightningStoreApi(swagger_client.ApiClient(configuration))
body = swagger_client.OpenLightningChannelRequest() # OpenLightningChannelRequest | 
crypto_code = 'crypto_code_example' # str | The cryptoCode of the lightning-node to query
store_id = 'store_id_example' # str | The store id with the lightning-node configuration to query

try:
    # Open channel
    api_instance.store_lightning_node_api_open_channel(body, crypto_code, store_id)
except ApiException as e:
    print("Exception when calling LightningStoreApi->store_lightning_node_api_open_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OpenLightningChannelRequest**](OpenLightningChannelRequest.md)|  | 
 **crypto_code** | **str**| The cryptoCode of the lightning-node to query | 
 **store_id** | **str**| The store id with the lightning-node configuration to query | 

### Return type

void (empty response body)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_lightning_node_api_pay_invoice**
> LightningPaymentData store_lightning_node_api_pay_invoice(body, crypto_code, store_id)

Pay Lightning Invoice

Pay a lightning invoice.

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
api_instance = swagger_client.LightningStoreApi(swagger_client.ApiClient(configuration))
body = swagger_client.PayLightningInvoiceRequest() # PayLightningInvoiceRequest | 
crypto_code = 'crypto_code_example' # str | The cryptoCode of the lightning-node to query
store_id = 'store_id_example' # str | The store id with the lightning-node configuration to query

try:
    # Pay Lightning Invoice
    api_response = api_instance.store_lightning_node_api_pay_invoice(body, crypto_code, store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LightningStoreApi->store_lightning_node_api_pay_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PayLightningInvoiceRequest**](PayLightningInvoiceRequest.md)|  | 
 **crypto_code** | **str**| The cryptoCode of the lightning-node to query | 
 **store_id** | **str**| The store id with the lightning-node configuration to query | 

### Return type

[**LightningPaymentData**](LightningPaymentData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

