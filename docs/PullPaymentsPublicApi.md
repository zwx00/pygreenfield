# swagger_client.PullPaymentsPublicApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pull_payments_create_payout**](PullPaymentsPublicApi.md#pull_payments_create_payout) | **POST** /api/v1/pull-payments/{pullPaymentId}/payouts | Create Payout
[**pull_payments_get_payout**](PullPaymentsPublicApi.md#pull_payments_get_payout) | **GET** /api/v1/pull-payments/{pullPaymentId}/payouts/{payoutId} | Get Payout
[**pull_payments_get_payouts**](PullPaymentsPublicApi.md#pull_payments_get_payouts) | **GET** /api/v1/pull-payments/{pullPaymentId}/payouts | Get Payouts
[**pull_payments_get_pull_payment**](PullPaymentsPublicApi.md#pull_payments_get_pull_payment) | **GET** /api/v1/pull-payments/{pullPaymentId} | Get Pull Payment

# **pull_payments_create_payout**
> PayoutData pull_payments_create_payout(body, pull_payment_id)

Create Payout

Create a new payout

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PullPaymentsPublicApi()
body = swagger_client.CreatePayoutRequest() # CreatePayoutRequest | 
pull_payment_id = 'pull_payment_id_example' # str | The ID of the pull payment

try:
    # Create Payout
    api_response = api_instance.pull_payments_create_payout(body, pull_payment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PullPaymentsPublicApi->pull_payments_create_payout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreatePayoutRequest**](CreatePayoutRequest.md)|  | 
 **pull_payment_id** | **str**| The ID of the pull payment | 

### Return type

[**PayoutData**](PayoutData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pull_payments_get_payout**
> PayoutData pull_payments_get_payout(pull_payment_id, payout_id)

Get Payout

Get payout

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PullPaymentsPublicApi()
pull_payment_id = 'pull_payment_id_example' # str | The ID of the pull payment
payout_id = 'payout_id_example' # str | The ID of the pull payment payout

try:
    # Get Payout
    api_response = api_instance.pull_payments_get_payout(pull_payment_id, payout_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PullPaymentsPublicApi->pull_payments_get_payout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pull_payment_id** | **str**| The ID of the pull payment | 
 **payout_id** | **str**| The ID of the pull payment payout | 

### Return type

[**PayoutData**](PayoutData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pull_payments_get_payouts**
> PayoutDataList pull_payments_get_payouts(pull_payment_id, include_cancelled=include_cancelled)

Get Payouts

Get payouts

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PullPaymentsPublicApi()
pull_payment_id = 'pull_payment_id_example' # str | The ID of the pull payment
include_cancelled = false # bool | Whether this should list cancelled payouts (optional) (default to false)

try:
    # Get Payouts
    api_response = api_instance.pull_payments_get_payouts(pull_payment_id, include_cancelled=include_cancelled)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PullPaymentsPublicApi->pull_payments_get_payouts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pull_payment_id** | **str**| The ID of the pull payment | 
 **include_cancelled** | **bool**| Whether this should list cancelled payouts | [optional] [default to false]

### Return type

[**PayoutDataList**](PayoutDataList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pull_payments_get_pull_payment**
> PullPaymentData pull_payments_get_pull_payment(pull_payment_id)

Get Pull Payment

Get a pull payment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PullPaymentsPublicApi()
pull_payment_id = 'pull_payment_id_example' # str | The ID of the pull payment

try:
    # Get Pull Payment
    api_response = api_instance.pull_payments_get_pull_payment(pull_payment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PullPaymentsPublicApi->pull_payments_get_pull_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pull_payment_id** | **str**| The ID of the pull payment | 

### Return type

[**PullPaymentData**](PullPaymentData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

