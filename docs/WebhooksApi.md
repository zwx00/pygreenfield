# swagger_client.WebhooksApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_stores_store_id_webhooks_post**](WebhooksApi.md#api_v1_stores_store_id_webhooks_post) | **POST** /api/v1/stores/{storeId}/webhooks | Create a new webhook
[**api_v1_stores_store_id_webhooks_webhook_id_delete**](WebhooksApi.md#api_v1_stores_store_id_webhooks_webhook_id_delete) | **DELETE** /api/v1/stores/{storeId}/webhooks/{webhookId} | Delete a webhook
[**api_v1_stores_store_id_webhooks_webhook_id_deliveries_delivery_id_get**](WebhooksApi.md#api_v1_stores_store_id_webhooks_webhook_id_deliveries_delivery_id_get) | **GET** /api/v1/stores/{storeId}/webhooks/{webhookId}/deliveries/{deliveryId} | Get a webhook delivery
[**api_v1_stores_store_id_webhooks_webhook_id_deliveries_delivery_id_redeliver_post**](WebhooksApi.md#api_v1_stores_store_id_webhooks_webhook_id_deliveries_delivery_id_redeliver_post) | **POST** /api/v1/stores/{storeId}/webhooks/{webhookId}/deliveries/{deliveryId}/redeliver | Redeliver the delivery
[**api_v1_stores_store_id_webhooks_webhook_id_deliveries_delivery_id_request_get**](WebhooksApi.md#api_v1_stores_store_id_webhooks_webhook_id_deliveries_delivery_id_request_get) | **GET** /api/v1/stores/{storeId}/webhooks/{webhookId}/deliveries/{deliveryId}/request | Get the delivery&#x27;s request
[**api_v1_stores_store_id_webhooks_webhook_id_deliveries_get**](WebhooksApi.md#api_v1_stores_store_id_webhooks_webhook_id_deliveries_get) | **GET** /api/v1/stores/{storeId}/webhooks/{webhookId}/deliveries | Get latest deliveries
[**api_v1_stores_store_id_webhooks_webhook_id_put**](WebhooksApi.md#api_v1_stores_store_id_webhooks_webhook_id_put) | **PUT** /api/v1/stores/{storeId}/webhooks/{webhookId} | Update a webhook
[**webhokks_get_webhook**](WebhooksApi.md#webhokks_get_webhook) | **GET** /api/v1/stores/{storeId}/webhooks/{webhookId} | Get a webhook of a store
[**webhokks_get_webhooks**](WebhooksApi.md#webhokks_get_webhooks) | **GET** /api/v1/stores/{storeId}/webhooks | Get webhooks of a store

# **api_v1_stores_store_id_webhooks_post**
> WebhookDataCreate api_v1_stores_store_id_webhooks_post(body, store_id)

Create a new webhook

Create a new webhook

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
api_instance = swagger_client.WebhooksApi(swagger_client.ApiClient(configuration))
body = swagger_client.WebhookDataCreate() # WebhookDataCreate | 
store_id = 'store_id_example' # str | The store id

try:
    # Create a new webhook
    api_response = api_instance.api_v1_stores_store_id_webhooks_post(body, store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->api_v1_stores_store_id_webhooks_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WebhookDataCreate**](WebhookDataCreate.md)|  | 
 **store_id** | **str**| The store id | 

### Return type

[**WebhookDataCreate**](WebhookDataCreate.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_stores_store_id_webhooks_webhook_id_delete**
> api_v1_stores_store_id_webhooks_webhook_id_delete(store_id, webhook_id)

Delete a webhook

Delete a webhook

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
api_instance = swagger_client.WebhooksApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | The store id
webhook_id = 'webhook_id_example' # str | The webhook id

try:
    # Delete a webhook
    api_instance.api_v1_stores_store_id_webhooks_webhook_id_delete(store_id, webhook_id)
except ApiException as e:
    print("Exception when calling WebhooksApi->api_v1_stores_store_id_webhooks_webhook_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store id | 
 **webhook_id** | **str**| The webhook id | 

### Return type

void (empty response body)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_stores_store_id_webhooks_webhook_id_deliveries_delivery_id_get**
> WebhookDeliveryData api_v1_stores_store_id_webhooks_webhook_id_deliveries_delivery_id_get(store_id, webhook_id, delivery_id)

Get a webhook delivery

Information about a webhook delivery

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
api_instance = swagger_client.WebhooksApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | The store id
webhook_id = 'webhook_id_example' # str | The webhook id
delivery_id = 'delivery_id_example' # str | The id of the delivery

try:
    # Get a webhook delivery
    api_response = api_instance.api_v1_stores_store_id_webhooks_webhook_id_deliveries_delivery_id_get(store_id, webhook_id, delivery_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->api_v1_stores_store_id_webhooks_webhook_id_deliveries_delivery_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store id | 
 **webhook_id** | **str**| The webhook id | 
 **delivery_id** | **str**| The id of the delivery | 

### Return type

[**WebhookDeliveryData**](WebhookDeliveryData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_stores_store_id_webhooks_webhook_id_deliveries_delivery_id_redeliver_post**
> str api_v1_stores_store_id_webhooks_webhook_id_deliveries_delivery_id_redeliver_post(store_id, webhook_id, delivery_id)

Redeliver the delivery

Redeliver the delivery

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
api_instance = swagger_client.WebhooksApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | The store id
webhook_id = 'webhook_id_example' # str | The webhook id
delivery_id = 'delivery_id_example' # str | The id of the delivery

try:
    # Redeliver the delivery
    api_response = api_instance.api_v1_stores_store_id_webhooks_webhook_id_deliveries_delivery_id_redeliver_post(store_id, webhook_id, delivery_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->api_v1_stores_store_id_webhooks_webhook_id_deliveries_delivery_id_redeliver_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store id | 
 **webhook_id** | **str**| The webhook id | 
 **delivery_id** | **str**| The id of the delivery | 

### Return type

**str**

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_stores_store_id_webhooks_webhook_id_deliveries_delivery_id_request_get**
> dict(str, object) api_v1_stores_store_id_webhooks_webhook_id_deliveries_delivery_id_request_get(store_id, webhook_id, delivery_id)

Get the delivery's request

The delivery's JSON request sent to the endpoint

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
api_instance = swagger_client.WebhooksApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | The store id
webhook_id = 'webhook_id_example' # str | The webhook id
delivery_id = 'delivery_id_example' # str | The id of the delivery

try:
    # Get the delivery's request
    api_response = api_instance.api_v1_stores_store_id_webhooks_webhook_id_deliveries_delivery_id_request_get(store_id, webhook_id, delivery_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->api_v1_stores_store_id_webhooks_webhook_id_deliveries_delivery_id_request_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store id | 
 **webhook_id** | **str**| The webhook id | 
 **delivery_id** | **str**| The id of the delivery | 

### Return type

**dict(str, object)**

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_stores_store_id_webhooks_webhook_id_deliveries_get**
> WebhookDeliveryList api_v1_stores_store_id_webhooks_webhook_id_deliveries_get(store_id, webhook_id, count=count)

Get latest deliveries

List the latest deliveries to the webhook, ordered from the most recent

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
api_instance = swagger_client.WebhooksApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | The store id
webhook_id = 'webhook_id_example' # str | The webhook id
count = 'count_example' # str | The number of latest deliveries to fetch (optional)

try:
    # Get latest deliveries
    api_response = api_instance.api_v1_stores_store_id_webhooks_webhook_id_deliveries_get(store_id, webhook_id, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->api_v1_stores_store_id_webhooks_webhook_id_deliveries_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store id | 
 **webhook_id** | **str**| The webhook id | 
 **count** | **str**| The number of latest deliveries to fetch | [optional] 

### Return type

[**WebhookDeliveryList**](WebhookDeliveryList.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_stores_store_id_webhooks_webhook_id_put**
> WebhookData api_v1_stores_store_id_webhooks_webhook_id_put(body, store_id, webhook_id)

Update a webhook

Update a webhook

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
api_instance = swagger_client.WebhooksApi(swagger_client.ApiClient(configuration))
body = swagger_client.WebhookDataBase() # WebhookDataBase | 
store_id = 'store_id_example' # str | The store id
webhook_id = 'webhook_id_example' # str | The webhook id

try:
    # Update a webhook
    api_response = api_instance.api_v1_stores_store_id_webhooks_webhook_id_put(body, store_id, webhook_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->api_v1_stores_store_id_webhooks_webhook_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WebhookDataBase**](WebhookDataBase.md)|  | 
 **store_id** | **str**| The store id | 
 **webhook_id** | **str**| The webhook id | 

### Return type

[**WebhookData**](WebhookData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhokks_get_webhook**
> WebhookData webhokks_get_webhook(store_id, webhook_id)

Get a webhook of a store

View webhook of a store

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
api_instance = swagger_client.WebhooksApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | The store id
webhook_id = 'webhook_id_example' # str | The webhook id

try:
    # Get a webhook of a store
    api_response = api_instance.webhokks_get_webhook(store_id, webhook_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->webhokks_get_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store id | 
 **webhook_id** | **str**| The webhook id | 

### Return type

[**WebhookData**](WebhookData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhokks_get_webhooks**
> WebhookDataList webhokks_get_webhooks(store_id)

Get webhooks of a store

View webhooks of a store

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
api_instance = swagger_client.WebhooksApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | The store id

try:
    # Get webhooks of a store
    api_response = api_instance.webhokks_get_webhooks(store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->webhokks_get_webhooks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store id | 

### Return type

[**WebhookDataList**](WebhookDataList.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

