# swagger_client.MiscelleneousApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**i_invoice_id_get**](MiscelleneousApi.md#i_invoice_id_get) | **GET** /i/{invoiceId} | Invoice checkout
[**lang_codes**](MiscelleneousApi.md#lang_codes) | **GET** /misc/lang | Language codes
[**permissions_metadata**](MiscelleneousApi.md#permissions_metadata) | **GET** /misc/permissions | Permissions metadata

# **i_invoice_id_get**
> i_invoice_id_get(invoice_id, lang=lang)

Invoice checkout

View the checkout page of an invoice

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MiscelleneousApi()
invoice_id = 'invoice_id_example' # str | The invoice id
lang = 'lang_example' # str | The preferred language of the checkout page. You can use \"auto\" to use the language of the customer's browser or see the list of language codes with [this operation](#operation/langCodes). (optional)

try:
    # Invoice checkout
    api_instance.i_invoice_id_get(invoice_id, lang=lang)
except ApiException as e:
    print("Exception when calling MiscelleneousApi->i_invoice_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**| The invoice id | 
 **lang** | **str**| The preferred language of the checkout page. You can use \&quot;auto\&quot; to use the language of the customer&#x27;s browser or see the list of language codes with [this operation](#operation/langCodes). | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lang_codes**
> list[InlineResponse2002] lang_codes()

Language codes

The supported language codes

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MiscelleneousApi()

try:
    # Language codes
    api_response = api_instance.lang_codes()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiscelleneousApi->lang_codes: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InlineResponse2002]**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permissions_metadata**
> list[InlineResponse2001] permissions_metadata()

Permissions metadata

The metadata of available permissions

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MiscelleneousApi()

try:
    # Permissions metadata
    api_response = api_instance.permissions_metadata()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiscelleneousApi->permissions_metadata: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InlineResponse2001]**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

