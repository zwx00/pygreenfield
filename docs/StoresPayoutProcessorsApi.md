# swagger_client.StoresPayoutProcessorsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**greenfield_store_automated_lightning_payout_processors_controller_get_store_lightning_automated_payout_processors**](StoresPayoutProcessorsApi.md#greenfield_store_automated_lightning_payout_processors_controller_get_store_lightning_automated_payout_processors) | **GET** /api/v1/stores/{storeId}/payout-processors/LightningAutomatedTransferSenderFactory/{paymentMethod} | Get configured store Lightning automated payout processors
[**greenfield_store_automated_lightning_payout_processors_controller_get_store_lightning_automated_payout_processors_0**](StoresPayoutProcessorsApi.md#greenfield_store_automated_lightning_payout_processors_controller_get_store_lightning_automated_payout_processors_0) | **GET** /api/v1/stores/{storeId}/payout-processors/LightningAutomatedTransferSenderFactory | Get configured store Lightning automated payout processors
[**greenfield_store_automated_lightning_payout_processors_controller_update_store_lightning_automated_payout_processor**](StoresPayoutProcessorsApi.md#greenfield_store_automated_lightning_payout_processors_controller_update_store_lightning_automated_payout_processor) | **PUT** /api/v1/stores/{storeId}/payout-processors/LightningAutomatedTransferSenderFactory/{paymentMethod} | Update configured store Lightning automated payout processors
[**greenfield_store_automated_on_chain_payout_processors_controller_get_store_on_chain_automated_payout_processors**](StoresPayoutProcessorsApi.md#greenfield_store_automated_on_chain_payout_processors_controller_get_store_on_chain_automated_payout_processors) | **GET** /api/v1/stores/{storeId}/payout-processors/OnChainAutomatedTransferSenderFactory/{paymentMethod} | Get configured store onchain automated payout processors
[**greenfield_store_automated_on_chain_payout_processors_controller_get_store_on_chain_automated_payout_processors_0**](StoresPayoutProcessorsApi.md#greenfield_store_automated_on_chain_payout_processors_controller_get_store_on_chain_automated_payout_processors_0) | **GET** /api/v1/stores/{storeId}/payout-processors/OnChainAutomatedTransferSenderFactory | Get configured store onchain automated payout processors
[**greenfield_store_automated_on_chain_payout_processors_controller_update_store_on_chain_automated_payout_processor**](StoresPayoutProcessorsApi.md#greenfield_store_automated_on_chain_payout_processors_controller_update_store_on_chain_automated_payout_processor) | **PUT** /api/v1/stores/{storeId}/payout-processors/OnChainAutomatedTransferSenderFactory/{paymentMethod} | Update configured store onchain automated payout processors
[**greenfield_store_automated_on_chain_payout_processors_controller_update_store_on_chain_automated_payout_processor_0**](StoresPayoutProcessorsApi.md#greenfield_store_automated_on_chain_payout_processors_controller_update_store_on_chain_automated_payout_processor_0) | **PUT** /api/v1/stores/{storeId}/payout-processors/OnChainAutomatedTransferSenderFactory | Update configured store onchain automated payout processors
[**store_payout_processors_get_store_payout_processors**](StoresPayoutProcessorsApi.md#store_payout_processors_get_store_payout_processors) | **GET** /api/v1/stores/{storeId}/payout-processors | Get store configured payout processors
[**store_payout_processors_remove_store_payout_processor**](StoresPayoutProcessorsApi.md#store_payout_processors_remove_store_payout_processor) | **DELETE** /api/v1/stores/{storeId}/payout-processors/{processor}/{paymentMethod} | Remove store configured payout processor

# **greenfield_store_automated_lightning_payout_processors_controller_get_store_lightning_automated_payout_processors**
> list[LightningAutomatedTransferSettings] greenfield_store_automated_lightning_payout_processors_controller_get_store_lightning_automated_payout_processors(store_id, payment_method)

Get configured store Lightning automated payout processors

Get configured store Lightning automated payout processors

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
api_instance = swagger_client.StoresPayoutProcessorsApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | The store to fetch
payment_method = 'payment_method_example' # str | A specific payment method to fetch

try:
    # Get configured store Lightning automated payout processors
    api_response = api_instance.greenfield_store_automated_lightning_payout_processors_controller_get_store_lightning_automated_payout_processors(store_id, payment_method)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoresPayoutProcessorsApi->greenfield_store_automated_lightning_payout_processors_controller_get_store_lightning_automated_payout_processors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store to fetch | 
 **payment_method** | **str**| A specific payment method to fetch | 

### Return type

[**list[LightningAutomatedTransferSettings]**](LightningAutomatedTransferSettings.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **greenfield_store_automated_lightning_payout_processors_controller_get_store_lightning_automated_payout_processors_0**
> list[LightningAutomatedTransferSettings] greenfield_store_automated_lightning_payout_processors_controller_get_store_lightning_automated_payout_processors_0(store_id)

Get configured store Lightning automated payout processors

Get configured store Lightning automated payout processors

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
api_instance = swagger_client.StoresPayoutProcessorsApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | The store to fetch

try:
    # Get configured store Lightning automated payout processors
    api_response = api_instance.greenfield_store_automated_lightning_payout_processors_controller_get_store_lightning_automated_payout_processors_0(store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoresPayoutProcessorsApi->greenfield_store_automated_lightning_payout_processors_controller_get_store_lightning_automated_payout_processors_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store to fetch | 

### Return type

[**list[LightningAutomatedTransferSettings]**](LightningAutomatedTransferSettings.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **greenfield_store_automated_lightning_payout_processors_controller_update_store_lightning_automated_payout_processor**
> LightningAutomatedTransferSettings greenfield_store_automated_lightning_payout_processors_controller_update_store_lightning_automated_payout_processor(body, store_id, payment_method)

Update configured store Lightning automated payout processors

Update configured store Lightning automated payout processors

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
api_instance = swagger_client.StoresPayoutProcessorsApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateLightningAutomatedTransferSettings() # UpdateLightningAutomatedTransferSettings | 
store_id = 'store_id_example' # str | The store to fetch
payment_method = 'payment_method_example' # str | A specific payment method to fetch

try:
    # Update configured store Lightning automated payout processors
    api_response = api_instance.greenfield_store_automated_lightning_payout_processors_controller_update_store_lightning_automated_payout_processor(body, store_id, payment_method)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoresPayoutProcessorsApi->greenfield_store_automated_lightning_payout_processors_controller_update_store_lightning_automated_payout_processor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateLightningAutomatedTransferSettings**](UpdateLightningAutomatedTransferSettings.md)|  | 
 **store_id** | **str**| The store to fetch | 
 **payment_method** | **str**| A specific payment method to fetch | 

### Return type

[**LightningAutomatedTransferSettings**](LightningAutomatedTransferSettings.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **greenfield_store_automated_on_chain_payout_processors_controller_get_store_on_chain_automated_payout_processors**
> list[OnChainAutomatedTransferSettings] greenfield_store_automated_on_chain_payout_processors_controller_get_store_on_chain_automated_payout_processors(store_id, payment_method)

Get configured store onchain automated payout processors

Get configured store onchain automated payout processors

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
api_instance = swagger_client.StoresPayoutProcessorsApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | The store to fetch
payment_method = 'payment_method_example' # str | A specific payment method to fetch

try:
    # Get configured store onchain automated payout processors
    api_response = api_instance.greenfield_store_automated_on_chain_payout_processors_controller_get_store_on_chain_automated_payout_processors(store_id, payment_method)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoresPayoutProcessorsApi->greenfield_store_automated_on_chain_payout_processors_controller_get_store_on_chain_automated_payout_processors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store to fetch | 
 **payment_method** | **str**| A specific payment method to fetch | 

### Return type

[**list[OnChainAutomatedTransferSettings]**](OnChainAutomatedTransferSettings.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **greenfield_store_automated_on_chain_payout_processors_controller_get_store_on_chain_automated_payout_processors_0**
> list[OnChainAutomatedTransferSettings] greenfield_store_automated_on_chain_payout_processors_controller_get_store_on_chain_automated_payout_processors_0(store_id)

Get configured store onchain automated payout processors

Get configured store onchain automated payout processors

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
api_instance = swagger_client.StoresPayoutProcessorsApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | The store to fetch

try:
    # Get configured store onchain automated payout processors
    api_response = api_instance.greenfield_store_automated_on_chain_payout_processors_controller_get_store_on_chain_automated_payout_processors_0(store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoresPayoutProcessorsApi->greenfield_store_automated_on_chain_payout_processors_controller_get_store_on_chain_automated_payout_processors_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store to fetch | 

### Return type

[**list[OnChainAutomatedTransferSettings]**](OnChainAutomatedTransferSettings.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **greenfield_store_automated_on_chain_payout_processors_controller_update_store_on_chain_automated_payout_processor**
> OnChainAutomatedTransferSettings greenfield_store_automated_on_chain_payout_processors_controller_update_store_on_chain_automated_payout_processor(body, store_id, payment_method)

Update configured store onchain automated payout processors

Update configured store onchain automated payout processors

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
api_instance = swagger_client.StoresPayoutProcessorsApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateOnChainAutomatedTransferSettings() # UpdateOnChainAutomatedTransferSettings | 
store_id = 'store_id_example' # str | The store to fetch
payment_method = 'payment_method_example' # str | A specific payment method to fetch

try:
    # Update configured store onchain automated payout processors
    api_response = api_instance.greenfield_store_automated_on_chain_payout_processors_controller_update_store_on_chain_automated_payout_processor(body, store_id, payment_method)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoresPayoutProcessorsApi->greenfield_store_automated_on_chain_payout_processors_controller_update_store_on_chain_automated_payout_processor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateOnChainAutomatedTransferSettings**](UpdateOnChainAutomatedTransferSettings.md)|  | 
 **store_id** | **str**| The store to fetch | 
 **payment_method** | **str**| A specific payment method to fetch | 

### Return type

[**OnChainAutomatedTransferSettings**](OnChainAutomatedTransferSettings.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **greenfield_store_automated_on_chain_payout_processors_controller_update_store_on_chain_automated_payout_processor_0**
> OnChainAutomatedTransferSettings greenfield_store_automated_on_chain_payout_processors_controller_update_store_on_chain_automated_payout_processor_0(body, store_id, payment_method)

Update configured store onchain automated payout processors

Update configured store onchain automated payout processors

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
api_instance = swagger_client.StoresPayoutProcessorsApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateOnChainAutomatedTransferSettings() # UpdateOnChainAutomatedTransferSettings | 
store_id = 'store_id_example' # str | The store to fetch
payment_method = 'payment_method_example' # str | A specific payment method to fetch

try:
    # Update configured store onchain automated payout processors
    api_response = api_instance.greenfield_store_automated_on_chain_payout_processors_controller_update_store_on_chain_automated_payout_processor_0(body, store_id, payment_method)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoresPayoutProcessorsApi->greenfield_store_automated_on_chain_payout_processors_controller_update_store_on_chain_automated_payout_processor_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateOnChainAutomatedTransferSettings**](UpdateOnChainAutomatedTransferSettings.md)|  | 
 **store_id** | **str**| The store to fetch | 
 **payment_method** | **str**| A specific payment method to fetch | 

### Return type

[**OnChainAutomatedTransferSettings**](OnChainAutomatedTransferSettings.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_payout_processors_get_store_payout_processors**
> list[PayoutProcessorData] store_payout_processors_get_store_payout_processors(store_id)

Get store configured payout processors

Get store configured payout processors

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
api_instance = swagger_client.StoresPayoutProcessorsApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | The store to fetch

try:
    # Get store configured payout processors
    api_response = api_instance.store_payout_processors_get_store_payout_processors(store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoresPayoutProcessorsApi->store_payout_processors_get_store_payout_processors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store to fetch | 

### Return type

[**list[PayoutProcessorData]**](PayoutProcessorData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_payout_processors_remove_store_payout_processor**
> store_payout_processors_remove_store_payout_processor(store_id, processor, payment_method)

Remove store configured payout processor

Remove store configured payout processor

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
api_instance = swagger_client.StoresPayoutProcessorsApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | The store
processor = 'processor_example' # str | The processor
payment_method = 'payment_method_example' # str | The payment method

try:
    # Remove store configured payout processor
    api_instance.store_payout_processors_remove_store_payout_processor(store_id, processor, payment_method)
except ApiException as e:
    print("Exception when calling StoresPayoutProcessorsApi->store_payout_processors_remove_store_payout_processor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store | 
 **processor** | **str**| The processor | 
 **payment_method** | **str**| The payment method | 

### Return type

void (empty response body)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

