# swagger_client.PullPaymentsPayoutPublicApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pull_payments_get_payout**](PullPaymentsPayoutPublicApi.md#pull_payments_get_payout) | **GET** /api/v1/pull-payments/{pullPaymentId}/payouts/{payoutId} | Get Payout

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
api_instance = swagger_client.PullPaymentsPayoutPublicApi()
pull_payment_id = 'pull_payment_id_example' # str | The ID of the pull payment
payout_id = 'payout_id_example' # str | The ID of the pull payment payout

try:
    # Get Payout
    api_response = api_instance.pull_payments_get_payout(pull_payment_id, payout_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PullPaymentsPayoutPublicApi->pull_payments_get_payout: %s\n" % e)
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

