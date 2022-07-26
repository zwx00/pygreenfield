# swagger_client.AuthorizationApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_keys_authorize_get**](AuthorizationApi.md#api_keys_authorize_get) | **GET** /api-keys/authorize | Authorize User

# **api_keys_authorize_get**
> api_keys_authorize_get(permissions=permissions, application_name=application_name, strict=strict, selective_stores=selective_stores, redirect=redirect, application_identifier=application_identifier)

Authorize User

Redirect the browser to this endpoint to request the user to generate an api-key with specific permissions

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthorizationApi()
permissions = ['permissions_example'] # list[str] | The permissions to request. (See API Key authentication) (optional)
application_name = 'application_name_example' # str | The name of your application (optional)
strict = true # bool | If permissions are specified, and strict is set to false, it will allow the user to reject some of permissions the application is requesting. (optional) (default to true)
selective_stores = false # bool | If the application is requesting the CanModifyStoreSettings permission and selectiveStores is set to true, this allows the user to only grant permissions to selected stores under the user's control. (optional) (default to false)
redirect = 'redirect_example' # str | The url to redirect to after the user consents, with the query parameters appended to it: permissions, user-id, api-key. If not specified, user is redirected to their API Key list. (optional)
application_identifier = 'application_identifier_example' # str | If specified, BTCPay Server will check if there is an existing API key associated with the user that also has this application identifier, redirect host AND the permissions required match(takes selectiveStores and strict into account). `applicationIdentifier` is ignored if redirect is not specified. (optional)

try:
    # Authorize User
    api_instance.api_keys_authorize_get(permissions=permissions, application_name=application_name, strict=strict, selective_stores=selective_stores, redirect=redirect, application_identifier=application_identifier)
except ApiException as e:
    print("Exception when calling AuthorizationApi->api_keys_authorize_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permissions** | [**list[str]**](str.md)| The permissions to request. (See API Key authentication) | [optional] 
 **application_name** | **str**| The name of your application | [optional] 
 **strict** | **bool**| If permissions are specified, and strict is set to false, it will allow the user to reject some of permissions the application is requesting. | [optional] [default to true]
 **selective_stores** | **bool**| If the application is requesting the CanModifyStoreSettings permission and selectiveStores is set to true, this allows the user to only grant permissions to selected stores under the user&#x27;s control. | [optional] [default to false]
 **redirect** | **str**| The url to redirect to after the user consents, with the query parameters appended to it: permissions, user-id, api-key. If not specified, user is redirected to their API Key list. | [optional] 
 **application_identifier** | **str**| If specified, BTCPay Server will check if there is an existing API key associated with the user that also has this application identifier, redirect host AND the permissions required match(takes selectiveStores and strict into account). &#x60;applicationIdentifier&#x60; is ignored if redirect is not specified. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

