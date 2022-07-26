# swagger_client.PaymentRequestsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**payment_requests_archive_payment_request**](PaymentRequestsApi.md#payment_requests_archive_payment_request) | **DELETE** /api/v1/stores/{storeId}/payment-requests/{paymentRequestId} | Archive payment request
[**payment_requests_create_payment_request**](PaymentRequestsApi.md#payment_requests_create_payment_request) | **POST** /api/v1/stores/{storeId}/payment-requests | Create a new payment request
[**payment_requests_get_payment_request**](PaymentRequestsApi.md#payment_requests_get_payment_request) | **GET** /api/v1/stores/{storeId}/payment-requests/{paymentRequestId} | Get payment request
[**payment_requests_get_payment_requests**](PaymentRequestsApi.md#payment_requests_get_payment_requests) | **GET** /api/v1/stores/{storeId}/payment-requests | Get payment requests
[**payment_requests_update_payment_request**](PaymentRequestsApi.md#payment_requests_update_payment_request) | **PUT** /api/v1/stores/{storeId}/payment-requests/{paymentRequestId} | Update payment request

# **payment_requests_archive_payment_request**
> payment_requests_archive_payment_request(store_id, payment_request_id)

Archive payment request

Archives the specified payment request.

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
api_instance = swagger_client.PaymentRequestsApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | The store the payment request belongs to
payment_request_id = 'payment_request_id_example' # str | The payment request to remove

try:
    # Archive payment request
    api_instance.payment_requests_archive_payment_request(store_id, payment_request_id)
except ApiException as e:
    print("Exception when calling PaymentRequestsApi->payment_requests_archive_payment_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store the payment request belongs to | 
 **payment_request_id** | **str**| The payment request to remove | 

### Return type

void (empty response body)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_requests_create_payment_request**
> PaymentRequestData payment_requests_create_payment_request(body, store_id)

Create a new payment request

Create a new payment request

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
api_instance = swagger_client.PaymentRequestsApi(swagger_client.ApiClient(configuration))
body = swagger_client.PaymentRequestBaseData() # PaymentRequestBaseData | 
store_id = 'store_id_example' # str | The store to query

try:
    # Create a new payment request
    api_response = api_instance.payment_requests_create_payment_request(body, store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentRequestsApi->payment_requests_create_payment_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PaymentRequestBaseData**](PaymentRequestBaseData.md)|  | 
 **store_id** | **str**| The store to query | 

### Return type

[**PaymentRequestData**](PaymentRequestData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_requests_get_payment_request**
> PaymentRequestData payment_requests_get_payment_request(store_id, payment_request_id)

Get payment request

View information about the specified payment request

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
api_instance = swagger_client.PaymentRequestsApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | The store to fetch
payment_request_id = 'payment_request_id_example' # str | The payment request to fetch

try:
    # Get payment request
    api_response = api_instance.payment_requests_get_payment_request(store_id, payment_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentRequestsApi->payment_requests_get_payment_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store to fetch | 
 **payment_request_id** | **str**| The payment request to fetch | 

### Return type

[**PaymentRequestData**](PaymentRequestData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_requests_get_payment_requests**
> PaymentRequestDataList payment_requests_get_payment_requests(store_id)

Get payment requests

View information about the existing payment requests

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
api_instance = swagger_client.PaymentRequestsApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | The store to query

try:
    # Get payment requests
    api_response = api_instance.payment_requests_get_payment_requests(store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentRequestsApi->payment_requests_get_payment_requests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store to query | 

### Return type

[**PaymentRequestDataList**](PaymentRequestDataList.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_requests_update_payment_request**
> PaymentRequestData payment_requests_update_payment_request(body, store_id, payment_request_id)

Update payment request

Update a payment request

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
api_instance = swagger_client.PaymentRequestsApi(swagger_client.ApiClient(configuration))
body = swagger_client.PaymentRequestBaseData() # PaymentRequestBaseData | 
store_id = 'store_id_example' # str | The store to query
payment_request_id = 'payment_request_id_example' # str | The payment request to update

try:
    # Update payment request
    api_response = api_instance.payment_requests_update_payment_request(body, store_id, payment_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentRequestsApi->payment_requests_update_payment_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PaymentRequestBaseData**](PaymentRequestBaseData.md)|  | 
 **store_id** | **str**| The store to query | 
 **payment_request_id** | **str**| The payment request to update | 

### Return type

[**PaymentRequestData**](PaymentRequestData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

