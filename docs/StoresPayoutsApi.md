# swagger_client.StoresPayoutsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**payouts_create_payout_through_store**](StoresPayoutsApi.md#payouts_create_payout_through_store) | **POST** /api/v1/stores/{storeId}/payouts | Create Payout 
[**pull_payments_approve_payout**](StoresPayoutsApi.md#pull_payments_approve_payout) | **POST** /api/v1/stores/{storeId}/payouts/{payoutId} | Approve Payout
[**pull_payments_cancel_payout**](StoresPayoutsApi.md#pull_payments_cancel_payout) | **DELETE** /api/v1/stores/{storeId}/payouts/{payoutId} | Cancel Payout
[**pull_payments_get_store_payouts**](StoresPayoutsApi.md#pull_payments_get_store_payouts) | **GET** /api/v1/stores/{storeId}/payouts | Get Store Payouts
[**pull_payments_mark_payout_paid**](StoresPayoutsApi.md#pull_payments_mark_payout_paid) | **POST** /api/v1/stores/{storeId}/payouts/{payoutId}/mark-paid | Mark Payout as Paid

# **payouts_create_payout_through_store**
> PayoutData payouts_create_payout_through_store(body, store_id)

Create Payout 

Create a new payout

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
api_instance = swagger_client.StoresPayoutsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreatePayoutThroughStoreRequest() # CreatePayoutThroughStoreRequest | 
store_id = 'store_id_example' # str | The ID of the store

try:
    # Create Payout 
    api_response = api_instance.payouts_create_payout_through_store(body, store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoresPayoutsApi->payouts_create_payout_through_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreatePayoutThroughStoreRequest**](CreatePayoutThroughStoreRequest.md)|  | 
 **store_id** | **str**| The ID of the store | 

### Return type

[**PayoutData**](PayoutData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pull_payments_approve_payout**
> PayoutData pull_payments_approve_payout(store_id, payout_id, body=body)

Approve Payout

Approve a payout

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
api_instance = swagger_client.StoresPayoutsApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | The ID of the store
payout_id = 'payout_id_example' # str | The ID of the payout
body = swagger_client.PayoutsPayoutIdBody() # PayoutsPayoutIdBody |  (optional)

try:
    # Approve Payout
    api_response = api_instance.pull_payments_approve_payout(store_id, payout_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoresPayoutsApi->pull_payments_approve_payout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The ID of the store | 
 **payout_id** | **str**| The ID of the payout | 
 **body** | [**PayoutsPayoutIdBody**](PayoutsPayoutIdBody.md)|  | [optional] 

### Return type

[**PayoutData**](PayoutData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pull_payments_cancel_payout**
> pull_payments_cancel_payout(store_id, payout_id)

Cancel Payout

Cancel the payout

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
api_instance = swagger_client.StoresPayoutsApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | The ID of the store
payout_id = 'payout_id_example' # str | The ID of the payout

try:
    # Cancel Payout
    api_instance.pull_payments_cancel_payout(store_id, payout_id)
except ApiException as e:
    print("Exception when calling StoresPayoutsApi->pull_payments_cancel_payout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The ID of the store | 
 **payout_id** | **str**| The ID of the payout | 

### Return type

void (empty response body)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pull_payments_get_store_payouts**
> PayoutDataList pull_payments_get_store_payouts(store_id, include_cancelled=include_cancelled)

Get Store Payouts

Get payouts

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StoresPayoutsApi()
store_id = 'store_id_example' # str | The ID of the store
include_cancelled = false # bool | Whether this should list cancelled payouts (optional) (default to false)

try:
    # Get Store Payouts
    api_response = api_instance.pull_payments_get_store_payouts(store_id, include_cancelled=include_cancelled)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoresPayoutsApi->pull_payments_get_store_payouts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The ID of the store | 
 **include_cancelled** | **bool**| Whether this should list cancelled payouts | [optional] [default to false]

### Return type

[**PayoutDataList**](PayoutDataList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pull_payments_mark_payout_paid**
> pull_payments_mark_payout_paid(store_id, payout_id)

Mark Payout as Paid

Mark a payout as paid

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
api_instance = swagger_client.StoresPayoutsApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | The ID of the store
payout_id = 'payout_id_example' # str | The ID of the payout

try:
    # Mark Payout as Paid
    api_instance.pull_payments_mark_payout_paid(store_id, payout_id)
except ApiException as e:
    print("Exception when calling StoresPayoutsApi->pull_payments_mark_payout_paid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The ID of the store | 
 **payout_id** | **str**| The ID of the payout | 

### Return type

void (empty response body)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

