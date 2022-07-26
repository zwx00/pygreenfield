# swagger_client.NotificationsCurrentUserApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**notifications_delete_notification**](NotificationsCurrentUserApi.md#notifications_delete_notification) | **DELETE** /api/v1/users/me/notifications/{id} | Remove Notification
[**notifications_get_notification**](NotificationsCurrentUserApi.md#notifications_get_notification) | **GET** /api/v1/users/me/notifications/{id} | Get notification
[**notifications_get_notifications**](NotificationsCurrentUserApi.md#notifications_get_notifications) | **GET** /api/v1/users/me/notifications | Get notifications
[**notifications_update_notification**](NotificationsCurrentUserApi.md#notifications_update_notification) | **PUT** /api/v1/users/me/notifications/{id} | Update notification

# **notifications_delete_notification**
> notifications_delete_notification(id)

Remove Notification

Removes the specified notification.

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
api_instance = swagger_client.NotificationsCurrentUserApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The notification to remove

try:
    # Remove Notification
    api_instance.notifications_delete_notification(id)
except ApiException as e:
    print("Exception when calling NotificationsCurrentUserApi->notifications_delete_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The notification to remove | 

### Return type

void (empty response body)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notifications_get_notification**
> NotificationData notifications_get_notification(id)

Get notification

View information about the specified notification

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
api_instance = swagger_client.NotificationsCurrentUserApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The notification to fetch

try:
    # Get notification
    api_response = api_instance.notifications_get_notification(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsCurrentUserApi->notifications_get_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The notification to fetch | 

### Return type

[**NotificationData**](NotificationData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notifications_get_notifications**
> NotificationData notifications_get_notifications(seen=seen, skip=skip, take=take)

Get notifications

View current user's notifications

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
api_instance = swagger_client.NotificationsCurrentUserApi(swagger_client.ApiClient(configuration))
seen = 'seen_example' # str | filter by seen notifications (optional)
skip = 1.2 # float | Number of records to skip (optional)
take = 1.2 # float | Number of records returned in response (optional)

try:
    # Get notifications
    api_response = api_instance.notifications_get_notifications(seen=seen, skip=skip, take=take)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsCurrentUserApi->notifications_get_notifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seen** | **str**| filter by seen notifications | [optional] 
 **skip** | **float**| Number of records to skip | [optional] 
 **take** | **float**| Number of records returned in response | [optional] 

### Return type

[**NotificationData**](NotificationData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notifications_update_notification**
> NotificationData notifications_update_notification(body, id)

Update notification

Updates the notification

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
api_instance = swagger_client.NotificationsCurrentUserApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateNotification() # UpdateNotification | 
id = 'id_example' # str | The notification to update

try:
    # Update notification
    api_response = api_instance.notifications_update_notification(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsCurrentUserApi->notifications_update_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateNotification**](UpdateNotification.md)|  | 
 **id** | **str**| The notification to update | 

### Return type

[**NotificationData**](NotificationData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

