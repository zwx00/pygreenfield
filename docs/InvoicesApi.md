# swagger_client.InvoicesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**invoices_activate_payment_method**](InvoicesApi.md#invoices_activate_payment_method) | **POST** /api/v1/stores/{storeId}/invoices/{invoiceId}/payment-methods/{paymentMethod}/activate | Activate Payment Method
[**invoices_archive_invoice**](InvoicesApi.md#invoices_archive_invoice) | **DELETE** /api/v1/stores/{storeId}/invoices/{invoiceId} | Archive invoice
[**invoices_create_invoice**](InvoicesApi.md#invoices_create_invoice) | **POST** /api/v1/stores/{storeId}/invoices | Create a new invoice
[**invoices_get_invoice**](InvoicesApi.md#invoices_get_invoice) | **GET** /api/v1/stores/{storeId}/invoices/{invoiceId} | Get invoice
[**invoices_get_invoice_payment_methods**](InvoicesApi.md#invoices_get_invoice_payment_methods) | **GET** /api/v1/stores/{storeId}/invoices/{invoiceId}/payment-methods | Get invoice payment methods
[**invoices_get_invoices**](InvoicesApi.md#invoices_get_invoices) | **GET** /api/v1/stores/{storeId}/invoices | Get invoices
[**invoices_mark_invoice_status**](InvoicesApi.md#invoices_mark_invoice_status) | **POST** /api/v1/stores/{storeId}/invoices/{invoiceId}/status | Mark invoice status
[**invoices_unarchive_invoice**](InvoicesApi.md#invoices_unarchive_invoice) | **POST** /api/v1/stores/{storeId}/invoices/{invoiceId}/unarchive | Unarchive invoice
[**invoices_update_invoice**](InvoicesApi.md#invoices_update_invoice) | **PUT** /api/v1/stores/{storeId}/invoices/{invoiceId} | Update invoice

# **invoices_activate_payment_method**
> invoices_activate_payment_method(store_id, invoice_id, payment_method)

Activate Payment Method

Activate an invoice payment method (if lazy payments mode is enabled)

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
api_instance = swagger_client.InvoicesApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | The store to query
invoice_id = 'invoice_id_example' # str | The invoice to update
payment_method = 'payment_method_example' # str | The payment method to activate

try:
    # Activate Payment Method
    api_instance.invoices_activate_payment_method(store_id, invoice_id, payment_method)
except ApiException as e:
    print("Exception when calling InvoicesApi->invoices_activate_payment_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store to query | 
 **invoice_id** | **str**| The invoice to update | 
 **payment_method** | **str**| The payment method to activate | 

### Return type

void (empty response body)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_archive_invoice**
> invoices_archive_invoice(store_id, invoice_id)

Archive invoice

Archives the specified invoice.

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
api_instance = swagger_client.InvoicesApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | The store the invoice belongs to
invoice_id = 'invoice_id_example' # str | The invoice to remove

try:
    # Archive invoice
    api_instance.invoices_archive_invoice(store_id, invoice_id)
except ApiException as e:
    print("Exception when calling InvoicesApi->invoices_archive_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store the invoice belongs to | 
 **invoice_id** | **str**| The invoice to remove | 

### Return type

void (empty response body)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_create_invoice**
> InvoiceData invoices_create_invoice(body, store_id)

Create a new invoice

Create a new invoice

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
api_instance = swagger_client.InvoicesApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateInvoiceRequest() # CreateInvoiceRequest | 
store_id = 'store_id_example' # str | The store to query

try:
    # Create a new invoice
    api_response = api_instance.invoices_create_invoice(body, store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->invoices_create_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateInvoiceRequest**](CreateInvoiceRequest.md)|  | 
 **store_id** | **str**| The store to query | 

### Return type

[**InvoiceData**](InvoiceData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_get_invoice**
> InvoiceData invoices_get_invoice(store_id, invoice_id)

Get invoice

View information about the specified invoice

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
api_instance = swagger_client.InvoicesApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | The store to fetch
invoice_id = 'invoice_id_example' # str | The invoice to fetch

try:
    # Get invoice
    api_response = api_instance.invoices_get_invoice(store_id, invoice_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->invoices_get_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store to fetch | 
 **invoice_id** | **str**| The invoice to fetch | 

### Return type

[**InvoiceData**](InvoiceData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_get_invoice_payment_methods**
> list[InvoicePaymentMethodDataModel] invoices_get_invoice_payment_methods(store_id, invoice_id, only_accounted_payments=only_accounted_payments)

Get invoice payment methods

View information about the specified invoice's payment methods

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
api_instance = swagger_client.InvoicesApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | The store to fetch
invoice_id = 'invoice_id_example' # str | The invoice to fetch
only_accounted_payments = true # bool | If default or true, only returns payments which are accounted (in Bitcoin, this mean not returning RBF'd or double spent payments) (optional) (default to true)

try:
    # Get invoice payment methods
    api_response = api_instance.invoices_get_invoice_payment_methods(store_id, invoice_id, only_accounted_payments=only_accounted_payments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->invoices_get_invoice_payment_methods: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store to fetch | 
 **invoice_id** | **str**| The invoice to fetch | 
 **only_accounted_payments** | **bool**| If default or true, only returns payments which are accounted (in Bitcoin, this mean not returning RBF&#x27;d or double spent payments) | [optional] [default to true]

### Return type

[**list[InvoicePaymentMethodDataModel]**](InvoicePaymentMethodDataModel.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_get_invoices**
> InvoiceDataList invoices_get_invoices(store_id, order_id=order_id, text_search=text_search, skip=skip, take=take)

Get invoices

View information about the existing invoices

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
api_instance = swagger_client.InvoicesApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | The store to query
order_id = ['order_id_example'] # list[str] | Array of OrderIds to fetch the invoices for (optional)
text_search = 'text_search_example' # str | A term that can help locating specific invoices. (optional)
skip = 1.2 # float | Number of records to skip (optional)
take = 1.2 # float | Number of records returned in response (optional)

try:
    # Get invoices
    api_response = api_instance.invoices_get_invoices(store_id, order_id=order_id, text_search=text_search, skip=skip, take=take)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->invoices_get_invoices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store to query | 
 **order_id** | [**list[str]**](str.md)| Array of OrderIds to fetch the invoices for | [optional] 
 **text_search** | **str**| A term that can help locating specific invoices. | [optional] 
 **skip** | **float**| Number of records to skip | [optional] 
 **take** | **float**| Number of records returned in response | [optional] 

### Return type

[**InvoiceDataList**](InvoiceDataList.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_mark_invoice_status**
> InvoiceData invoices_mark_invoice_status(body, store_id, invoice_id)

Mark invoice status

Mark an invoice as invalid or settled.

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
api_instance = swagger_client.InvoicesApi(swagger_client.ApiClient(configuration))
body = swagger_client.MarkInvoiceStatusRequest() # MarkInvoiceStatusRequest | 
store_id = 'store_id_example' # str | The store to query
invoice_id = 'invoice_id_example' # str | The invoice to update

try:
    # Mark invoice status
    api_response = api_instance.invoices_mark_invoice_status(body, store_id, invoice_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->invoices_mark_invoice_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MarkInvoiceStatusRequest**](MarkInvoiceStatusRequest.md)|  | 
 **store_id** | **str**| The store to query | 
 **invoice_id** | **str**| The invoice to update | 

### Return type

[**InvoiceData**](InvoiceData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_unarchive_invoice**
> InvoiceData invoices_unarchive_invoice(store_id, invoice_id)

Unarchive invoice

Unarchive an invoice

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
api_instance = swagger_client.InvoicesApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | The store to query
invoice_id = 'invoice_id_example' # str | The invoice to update

try:
    # Unarchive invoice
    api_response = api_instance.invoices_unarchive_invoice(store_id, invoice_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->invoices_unarchive_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store to query | 
 **invoice_id** | **str**| The invoice to update | 

### Return type

[**InvoiceData**](InvoiceData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_update_invoice**
> InvoiceData invoices_update_invoice(body, store_id, invoice_id)

Update invoice

Updates the specified invoice.

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
api_instance = swagger_client.InvoicesApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateInvoiceRequest() # UpdateInvoiceRequest | 
store_id = 'store_id_example' # str | The store the invoice belongs to
invoice_id = 'invoice_id_example' # str | The invoice to update

try:
    # Update invoice
    api_response = api_instance.invoices_update_invoice(body, store_id, invoice_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->invoices_update_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateInvoiceRequest**](UpdateInvoiceRequest.md)|  | 
 **store_id** | **str**| The store the invoice belongs to | 
 **invoice_id** | **str**| The invoice to update | 

### Return type

[**InvoiceData**](InvoiceData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

