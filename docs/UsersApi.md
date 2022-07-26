# swagger_client.UsersApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_users_get**](UsersApi.md#api_v1_users_get) | **GET** /api/v1/users | Get all users
[**api_v1_users_id_or_email_delete**](UsersApi.md#api_v1_users_id_or_email_delete) | **DELETE** /api/v1/users/{idOrEmail} | Delete user
[**api_v1_users_id_or_email_get**](UsersApi.md#api_v1_users_id_or_email_get) | **GET** /api/v1/users/{idOrEmail} | Get user by ID or Email
[**api_v1_users_id_or_email_lock_delete**](UsersApi.md#api_v1_users_id_or_email_lock_delete) | **DELETE** /api/v1/users/{idOrEmail}/lock | Toggle user
[**api_v1_users_post**](UsersApi.md#api_v1_users_post) | **POST** /api/v1/users | Create user
[**users_delete_current_user**](UsersApi.md#users_delete_current_user) | **DELETE** /api/v1/users/me | Deletes user profile
[**users_get_current_user**](UsersApi.md#users_get_current_user) | **GET** /api/v1/users/me | Get current user information

# **api_v1_users_get**
> api_v1_users_get()

Get all users

Load all users that exist.

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))

try:
    # Get all users
    api_instance.api_v1_users_get()
except ApiException as e:
    print("Exception when calling UsersApi->api_v1_users_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_users_id_or_email_delete**
> api_v1_users_id_or_email_delete(user_id)

Delete user

Delete a user.  Must be an admin to perform this operation.  Attempting to delete the only admin user will not succeed.  All data associated with the user will be deleted as well if the operation succeeds.

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | The ID of the user to be deleted

try:
    # Delete user
    api_instance.api_v1_users_id_or_email_delete(user_id)
except ApiException as e:
    print("Exception when calling UsersApi->api_v1_users_id_or_email_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The ID of the user to be deleted | 

### Return type

void (empty response body)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_users_id_or_email_get**
> api_v1_users_id_or_email_get(id_or_email)

Get user by ID or Email

Get 1 user by ID or Email.

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
id_or_email = 'id_or_email_example' # str | The ID or email of the user to load

try:
    # Get user by ID or Email
    api_instance.api_v1_users_id_or_email_get(id_or_email)
except ApiException as e:
    print("Exception when calling UsersApi->api_v1_users_id_or_email_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_email** | **str**| The ID or email of the user to load | 

### Return type

void (empty response body)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_users_id_or_email_lock_delete**
> api_v1_users_id_or_email_lock_delete(user_id, body=body)

Toggle user

Lock or unlock a user.  Must be an admin to perform this operation.  Attempting to lock the only admin user will not succeed.

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | The ID of the user to be un/locked
body = swagger_client.LockUserRequest() # LockUserRequest |  (optional)

try:
    # Toggle user
    api_instance.api_v1_users_id_or_email_lock_delete(user_id, body=body)
except ApiException as e:
    print("Exception when calling UsersApi->api_v1_users_id_or_email_lock_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The ID of the user to be un/locked | 
 **body** | [**LockUserRequest**](LockUserRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_users_post**
> ApplicationUserData api_v1_users_post(body)

Create user

Create a new user.  This operation can be called without authentication in any of this cases: * There is not any administrator yet on the server, * The subscriptions are not disabled in the server's policies.  If the first administrator is created by this call, subscriptions are automatically disabled.

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.V1UsersBody() # V1UsersBody | 

try:
    # Create user
    api_response = api_instance.api_v1_users_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->api_v1_users_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1UsersBody**](V1UsersBody.md)|  | 

### Return type

[**ApplicationUserData**](ApplicationUserData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_delete_current_user**
> users_delete_current_user()

Deletes user profile

Deletes user profile and associated user data for user making the request

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))

try:
    # Deletes user profile
    api_instance.users_delete_current_user()
except ApiException as e:
    print("Exception when calling UsersApi->users_delete_current_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_get_current_user**
> ApplicationUserData users_get_current_user()

Get current user information

View information about the current user

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))

try:
    # Get current user information
    api_response = api_instance.users_get_current_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_get_current_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApplicationUserData**](ApplicationUserData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

