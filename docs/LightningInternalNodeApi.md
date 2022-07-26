# swagger_client.LightningInternalNodeApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**internal_lightning_node_api_connect_to_node**](LightningInternalNodeApi.md#internal_lightning_node_api_connect_to_node) | **POST** /api/v1/server/lightning/{cryptoCode}/connect | Connect to lightning node
[**internal_lightning_node_api_create_invoice**](LightningInternalNodeApi.md#internal_lightning_node_api_create_invoice) | **POST** /api/v1/server/lightning/{cryptoCode}/invoices | Create lightning invoice
[**internal_lightning_node_api_get_balance**](LightningInternalNodeApi.md#internal_lightning_node_api_get_balance) | **GET** /api/v1/server/lightning/{cryptoCode}/balance | Get node balance
[**internal_lightning_node_api_get_channels**](LightningInternalNodeApi.md#internal_lightning_node_api_get_channels) | **GET** /api/v1/server/lightning/{cryptoCode}/channels | Get channels
[**internal_lightning_node_api_get_deposit_address**](LightningInternalNodeApi.md#internal_lightning_node_api_get_deposit_address) | **POST** /api/v1/server/lightning/{cryptoCode}/address | Get deposit address
[**internal_lightning_node_api_get_info**](LightningInternalNodeApi.md#internal_lightning_node_api_get_info) | **GET** /api/v1/server/lightning/{cryptoCode}/info | Get node information
[**internal_lightning_node_api_get_invoice**](LightningInternalNodeApi.md#internal_lightning_node_api_get_invoice) | **GET** /api/v1/server/lightning/{cryptoCode}/invoices/{id} | Get invoice
[**internal_lightning_node_api_get_payment**](LightningInternalNodeApi.md#internal_lightning_node_api_get_payment) | **GET** /api/v1/server/lightning/{cryptoCode}/payments/{paymentHash} | Get payment
[**internal_lightning_node_api_open_channel**](LightningInternalNodeApi.md#internal_lightning_node_api_open_channel) | **POST** /api/v1/server/lightning/{cryptoCode}/channels | Open channel
[**internal_lightning_node_api_pay_invoice**](LightningInternalNodeApi.md#internal_lightning_node_api_pay_invoice) | **POST** /api/v1/server/lightning/{cryptoCode}/invoices/pay | Pay Lightning Invoice

# **internal_lightning_node_api_connect_to_node**
> internal_lightning_node_api_connect_to_node(body, crypto_code)

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
api_instance = swagger_client.LightningInternalNodeApi(swagger_client.ApiClient(configuration))
body = swagger_client.ConnectToNodeRequest() # ConnectToNodeRequest | 
crypto_code = 'crypto_code_example' # str | The cryptoCode of the lightning-node to query

try:
    # Connect to lightning node
    api_instance.internal_lightning_node_api_connect_to_node(body, crypto_code)
except ApiException as e:
    print("Exception when calling LightningInternalNodeApi->internal_lightning_node_api_connect_to_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConnectToNodeRequest**](ConnectToNodeRequest.md)|  | 
 **crypto_code** | **str**| The cryptoCode of the lightning-node to query | 

### Return type

void (empty response body)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_lightning_node_api_create_invoice**
> LightningInvoiceData internal_lightning_node_api_create_invoice(body, crypto_code)

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
api_instance = swagger_client.LightningInternalNodeApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateLightningInvoiceRequest() # CreateLightningInvoiceRequest | 
crypto_code = 'crypto_code_example' # str | The cryptoCode of the lightning-node to query

try:
    # Create lightning invoice
    api_response = api_instance.internal_lightning_node_api_create_invoice(body, crypto_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LightningInternalNodeApi->internal_lightning_node_api_create_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateLightningInvoiceRequest**](CreateLightningInvoiceRequest.md)|  | 
 **crypto_code** | **str**| The cryptoCode of the lightning-node to query | 

### Return type

[**LightningInvoiceData**](LightningInvoiceData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_lightning_node_api_get_balance**
> LightningNodeBalanceData internal_lightning_node_api_get_balance(crypto_code)

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
api_instance = swagger_client.LightningInternalNodeApi(swagger_client.ApiClient(configuration))
crypto_code = 'crypto_code_example' # str | The cryptoCode of the lightning-node to query

try:
    # Get node balance
    api_response = api_instance.internal_lightning_node_api_get_balance(crypto_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LightningInternalNodeApi->internal_lightning_node_api_get_balance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crypto_code** | **str**| The cryptoCode of the lightning-node to query | 

### Return type

[**LightningNodeBalanceData**](LightningNodeBalanceData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_lightning_node_api_get_channels**
> list[LightningChannelData] internal_lightning_node_api_get_channels(crypto_code)

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
api_instance = swagger_client.LightningInternalNodeApi(swagger_client.ApiClient(configuration))
crypto_code = 'crypto_code_example' # str | The cryptoCode of the lightning-node to query

try:
    # Get channels
    api_response = api_instance.internal_lightning_node_api_get_channels(crypto_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LightningInternalNodeApi->internal_lightning_node_api_get_channels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crypto_code** | **str**| The cryptoCode of the lightning-node to query | 

### Return type

[**list[LightningChannelData]**](LightningChannelData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_lightning_node_api_get_deposit_address**
> str internal_lightning_node_api_get_deposit_address(crypto_code)

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
api_instance = swagger_client.LightningInternalNodeApi(swagger_client.ApiClient(configuration))
crypto_code = 'crypto_code_example' # str | The cryptoCode of the lightning-node to query

try:
    # Get deposit address
    api_response = api_instance.internal_lightning_node_api_get_deposit_address(crypto_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LightningInternalNodeApi->internal_lightning_node_api_get_deposit_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crypto_code** | **str**| The cryptoCode of the lightning-node to query | 

### Return type

**str**

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_lightning_node_api_get_info**
> LightningNodeInformationData internal_lightning_node_api_get_info(crypto_code)

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
api_instance = swagger_client.LightningInternalNodeApi(swagger_client.ApiClient(configuration))
crypto_code = 'crypto_code_example' # str | The cryptoCode of the lightning-node to query

try:
    # Get node information
    api_response = api_instance.internal_lightning_node_api_get_info(crypto_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LightningInternalNodeApi->internal_lightning_node_api_get_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crypto_code** | **str**| The cryptoCode of the lightning-node to query | 

### Return type

[**LightningNodeInformationData**](LightningNodeInformationData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_lightning_node_api_get_invoice**
> LightningInvoiceData internal_lightning_node_api_get_invoice(crypto_code, id)

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
api_instance = swagger_client.LightningInternalNodeApi(swagger_client.ApiClient(configuration))
crypto_code = 'crypto_code_example' # str | The cryptoCode of the lightning-node to query
id = 'id_example' # str | The id of the lightning invoice.

try:
    # Get invoice
    api_response = api_instance.internal_lightning_node_api_get_invoice(crypto_code, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LightningInternalNodeApi->internal_lightning_node_api_get_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crypto_code** | **str**| The cryptoCode of the lightning-node to query | 
 **id** | **str**| The id of the lightning invoice. | 

### Return type

[**LightningInvoiceData**](LightningInvoiceData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_lightning_node_api_get_payment**
> LightningPaymentData internal_lightning_node_api_get_payment(crypto_code, payment_hash)

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
api_instance = swagger_client.LightningInternalNodeApi(swagger_client.ApiClient(configuration))
crypto_code = 'crypto_code_example' # str | The cryptoCode of the lightning-node to query
payment_hash = 'payment_hash_example' # str | The payment hash of the lightning payment.

try:
    # Get payment
    api_response = api_instance.internal_lightning_node_api_get_payment(crypto_code, payment_hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LightningInternalNodeApi->internal_lightning_node_api_get_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crypto_code** | **str**| The cryptoCode of the lightning-node to query | 
 **payment_hash** | **str**| The payment hash of the lightning payment. | 

### Return type

[**LightningPaymentData**](LightningPaymentData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_lightning_node_api_open_channel**
> internal_lightning_node_api_open_channel(body, crypto_code)

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
api_instance = swagger_client.LightningInternalNodeApi(swagger_client.ApiClient(configuration))
body = swagger_client.OpenLightningChannelRequest() # OpenLightningChannelRequest | 
crypto_code = 'crypto_code_example' # str | The cryptoCode of the lightning-node to query

try:
    # Open channel
    api_instance.internal_lightning_node_api_open_channel(body, crypto_code)
except ApiException as e:
    print("Exception when calling LightningInternalNodeApi->internal_lightning_node_api_open_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OpenLightningChannelRequest**](OpenLightningChannelRequest.md)|  | 
 **crypto_code** | **str**| The cryptoCode of the lightning-node to query | 

### Return type

void (empty response body)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_lightning_node_api_pay_invoice**
> LightningPaymentData internal_lightning_node_api_pay_invoice(body, crypto_code)

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
api_instance = swagger_client.LightningInternalNodeApi(swagger_client.ApiClient(configuration))
body = swagger_client.PayLightningInvoiceRequest() # PayLightningInvoiceRequest | 
crypto_code = 'crypto_code_example' # str | The cryptoCode of the lightning-node to query

try:
    # Pay Lightning Invoice
    api_response = api_instance.internal_lightning_node_api_pay_invoice(body, crypto_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LightningInternalNodeApi->internal_lightning_node_api_pay_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PayLightningInvoiceRequest**](PayLightningInvoiceRequest.md)|  | 
 **crypto_code** | **str**| The cryptoCode of the lightning-node to query | 

### Return type

[**LightningPaymentData**](LightningPaymentData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

