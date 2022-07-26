# swagger_client.PullPaymentsManagementApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pull_payments_archive_pull_payment**](PullPaymentsManagementApi.md#pull_payments_archive_pull_payment) | **DELETE** /api/v1/stores/{storeId}/pull-payments/{pullPaymentId} | Archive a pull payment
[**pull_payments_create_pull_payment**](PullPaymentsManagementApi.md#pull_payments_create_pull_payment) | **POST** /api/v1/stores/{storeId}/pull-payments | Create a new pull payment
[**pull_payments_get_pull_payments**](PullPaymentsManagementApi.md#pull_payments_get_pull_payments) | **GET** /api/v1/stores/{storeId}/pull-payments | Get store&#x27;s pull payments

# **pull_payments_archive_pull_payment**
> pull_payments_archive_pull_payment(store_id, pull_payment_id)

Archive a pull payment

Archive this pull payment (Will cancel all payouts awaiting for payment)

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
api_instance = swagger_client.PullPaymentsManagementApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | The ID of the store
pull_payment_id = 'pull_payment_id_example' # str | The ID of the pull payment

try:
    # Archive a pull payment
    api_instance.pull_payments_archive_pull_payment(store_id, pull_payment_id)
except ApiException as e:
    print("Exception when calling PullPaymentsManagementApi->pull_payments_archive_pull_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The ID of the store | 
 **pull_payment_id** | **str**| The ID of the pull payment | 

### Return type

void (empty response body)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pull_payments_create_pull_payment**
> PullPaymentData pull_payments_create_pull_payment(store_id, body=body)

Create a new pull payment

A pull payment allows its receiver to ask for payouts up to `amount` of `currency` every `period`.

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
api_instance = swagger_client.PullPaymentsManagementApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | The store ID
body = swagger_client.StoreIdPullpaymentsBody() # StoreIdPullpaymentsBody |  (optional)

try:
    # Create a new pull payment
    api_response = api_instance.pull_payments_create_pull_payment(store_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PullPaymentsManagementApi->pull_payments_create_pull_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store ID | 
 **body** | [**StoreIdPullpaymentsBody**](StoreIdPullpaymentsBody.md)|  | [optional] 

### Return type

[**PullPaymentData**](PullPaymentData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pull_payments_get_pull_payments**
> PullPaymentDataList pull_payments_get_pull_payments(store_id, include_archived=include_archived)

Get store's pull payments

Get the pull payments of a store

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
api_instance = swagger_client.PullPaymentsManagementApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | The store ID
include_archived = false # bool | Whether this should list archived pull payments (optional) (default to false)

try:
    # Get store's pull payments
    api_response = api_instance.pull_payments_get_pull_payments(store_id, include_archived=include_archived)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PullPaymentsManagementApi->pull_payments_get_pull_payments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store ID | 
 **include_archived** | **bool**| Whether this should list archived pull payments | [optional] [default to false]

### Return type

[**PullPaymentDataList**](PullPaymentDataList.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

