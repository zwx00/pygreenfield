# swagger_client.CustodiansApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_stores_store_id_custodian_accounts_account_id_addresses_payment_method_get**](CustodiansApi.md#api_v1_stores_store_id_custodian_accounts_account_id_addresses_payment_method_get) | **GET** /api/v1/stores/{storeId}/custodian-accounts/{accountId}/addresses/{paymentMethod} | Get a deposit address for custodian
[**api_v1_stores_store_id_custodian_accounts_account_id_delete**](CustodiansApi.md#api_v1_stores_store_id_custodian_accounts_account_id_delete) | **DELETE** /api/v1/stores/{storeId}/custodian-accounts/{accountId} | Delete store custodian account
[**api_v1_stores_store_id_custodian_accounts_account_id_get**](CustodiansApi.md#api_v1_stores_store_id_custodian_accounts_account_id_get) | **GET** /api/v1/stores/{storeId}/custodian-accounts/{accountId} | Get store custodian account
[**api_v1_stores_store_id_custodian_accounts_account_id_put**](CustodiansApi.md#api_v1_stores_store_id_custodian_accounts_account_id_put) | **PUT** /api/v1/stores/{storeId}/custodian-accounts/{accountId} | Update custodial account
[**api_v1_stores_store_id_custodian_accounts_account_id_trades_market_post**](CustodiansApi.md#api_v1_stores_store_id_custodian_accounts_account_id_trades_market_post) | **POST** /api/v1/stores/{storeId}/custodian-accounts/{accountId}/trades/market | Trade one asset for another
[**api_v1_stores_store_id_custodian_accounts_account_id_trades_quote_get**](CustodiansApi.md#api_v1_stores_store_id_custodian_accounts_account_id_trades_quote_get) | **GET** /api/v1/stores/{storeId}/custodian-accounts/{accountId}/trades/quote | Get quote for trading one asset for another
[**api_v1_stores_store_id_custodian_accounts_account_id_withdrawals_post**](CustodiansApi.md#api_v1_stores_store_id_custodian_accounts_account_id_withdrawals_post) | **POST** /api/v1/stores/{storeId}/custodian-accounts/{accountId}/withdrawals | Withdraw to store wallet
[**api_v1_stores_store_id_custodian_accounts_account_id_withdrawals_withdrawal_id_post**](CustodiansApi.md#api_v1_stores_store_id_custodian_accounts_account_id_withdrawals_withdrawal_id_post) | **POST** /api/v1/stores/{storeId}/custodian-accounts/{accountId}/withdrawals/{withdrawalId} | Get withdrawal info
[**api_v1_stores_store_id_custodian_accounts_get**](CustodiansApi.md#api_v1_stores_store_id_custodian_accounts_get) | **GET** /api/v1/stores/{storeId}/custodian-accounts | List store custodian accounts
[**api_v1_stores_store_id_custodian_accounts_post**](CustodiansApi.md#api_v1_stores_store_id_custodian_accounts_post) | **POST** /api/v1/stores/{storeId}/custodian-accounts | Add a custodial account to a store.
[**custodians_get_supported_custodians**](CustodiansApi.md#custodians_get_supported_custodians) | **GET** /api/v1/custodians | List supported custodians

# **api_v1_stores_store_id_custodian_accounts_account_id_addresses_payment_method_get**
> InlineResponse200 api_v1_stores_store_id_custodian_accounts_account_id_addresses_payment_method_get(store_id, account_id, payment_method)

Get a deposit address for custodian

Get a new deposit address for the custodian using the specified payment method (network + crypto code).

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
api_instance = swagger_client.CustodiansApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | The Store ID
account_id = 'account_id_example' # str | The Custodian Account ID.
payment_method = 'payment_method_example' # str | The payment method to use for the deposit. Example: \"BTC-OnChain\" or \"BTC-Lightning\"

try:
    # Get a deposit address for custodian
    api_response = api_instance.api_v1_stores_store_id_custodian_accounts_account_id_addresses_payment_method_get(store_id, account_id, payment_method)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustodiansApi->api_v1_stores_store_id_custodian_accounts_account_id_addresses_payment_method_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The Store ID | 
 **account_id** | **str**| The Custodian Account ID. | 
 **payment_method** | **str**| The payment method to use for the deposit. Example: \&quot;BTC-OnChain\&quot; or \&quot;BTC-Lightning\&quot; | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_stores_store_id_custodian_accounts_account_id_delete**
> api_v1_stores_store_id_custodian_accounts_account_id_delete()

Delete store custodian account

Deletes a custodial account

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
api_instance = swagger_client.CustodiansApi(swagger_client.ApiClient(configuration))

try:
    # Delete store custodian account
    api_instance.api_v1_stores_store_id_custodian_accounts_account_id_delete()
except ApiException as e:
    print("Exception when calling CustodiansApi->api_v1_stores_store_id_custodian_accounts_account_id_delete: %s\n" % e)
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

# **api_v1_stores_store_id_custodian_accounts_account_id_get**
> CustodianAccountData api_v1_stores_store_id_custodian_accounts_account_id_get(store_id, account_id, asset_balances=asset_balances)

Get store custodian account

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
api_instance = swagger_client.CustodiansApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | The Store ID
account_id = 'account_id_example' # str | The Custodian Account ID
asset_balances = false # bool | Enable if you want the result to include the 'assetBalances' field. This will make the call slower or could cause the call to fail if the asset balances cannot be loaded (i.e. due to a bad API key). (optional) (default to false)

try:
    # Get store custodian account
    api_response = api_instance.api_v1_stores_store_id_custodian_accounts_account_id_get(store_id, account_id, asset_balances=asset_balances)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustodiansApi->api_v1_stores_store_id_custodian_accounts_account_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The Store ID | 
 **account_id** | **str**| The Custodian Account ID | 
 **asset_balances** | **bool**| Enable if you want the result to include the &#x27;assetBalances&#x27; field. This will make the call slower or could cause the call to fail if the asset balances cannot be loaded (i.e. due to a bad API key). | [optional] [default to false]

### Return type

[**CustodianAccountData**](CustodianAccountData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_stores_store_id_custodian_accounts_account_id_put**
> CustodianAccountData api_v1_stores_store_id_custodian_accounts_account_id_put(body)

Update custodial account

Update custodial account

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
api_instance = swagger_client.CustodiansApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateCustodianAccountRequest() # CreateCustodianAccountRequest | 

try:
    # Update custodial account
    api_response = api_instance.api_v1_stores_store_id_custodian_accounts_account_id_put(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustodiansApi->api_v1_stores_store_id_custodian_accounts_account_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateCustodianAccountRequest**](CreateCustodianAccountRequest.md)|  | 

### Return type

[**CustodianAccountData**](CustodianAccountData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_stores_store_id_custodian_accounts_account_id_trades_market_post**
> TradeResultData api_v1_stores_store_id_custodian_accounts_account_id_trades_market_post(store_id, account_id, body=body)

Trade one asset for another

Trade one asset for another using a market order (=instant purchase with instant result or failure). A suitable asset pair will automatically be selected. If no asset pair is available, the call will fail.

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
api_instance = swagger_client.CustodiansApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | The Store ID
account_id = 'account_id_example' # str | The Custodian Account ID.
body = swagger_client.TradeRequestData() # TradeRequestData |  (optional)

try:
    # Trade one asset for another
    api_response = api_instance.api_v1_stores_store_id_custodian_accounts_account_id_trades_market_post(store_id, account_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustodiansApi->api_v1_stores_store_id_custodian_accounts_account_id_trades_market_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The Store ID | 
 **account_id** | **str**| The Custodian Account ID. | 
 **body** | [**TradeRequestData**](TradeRequestData.md)|  | [optional] 

### Return type

[**TradeResultData**](TradeResultData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_stores_store_id_custodian_accounts_account_id_trades_quote_get**
> QuoteResultData api_v1_stores_store_id_custodian_accounts_account_id_trades_quote_get(store_id, account_id, from_asset, to_asset)

Get quote for trading one asset for another

Get the current bid and ask price for converting one asset into another.

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
api_instance = swagger_client.CustodiansApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | The Store ID
account_id = 'account_id_example' # str | The Custodian Account ID.
from_asset = 'from_asset_example' # str | The asset to convert.
to_asset = 'to_asset_example' # str | The asset you want.

try:
    # Get quote for trading one asset for another
    api_response = api_instance.api_v1_stores_store_id_custodian_accounts_account_id_trades_quote_get(store_id, account_id, from_asset, to_asset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustodiansApi->api_v1_stores_store_id_custodian_accounts_account_id_trades_quote_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The Store ID | 
 **account_id** | **str**| The Custodian Account ID. | 
 **from_asset** | **str**| The asset to convert. | 
 **to_asset** | **str**| The asset you want. | 

### Return type

[**QuoteResultData**](QuoteResultData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_stores_store_id_custodian_accounts_account_id_withdrawals_post**
> WithdrawalResultData api_v1_stores_store_id_custodian_accounts_account_id_withdrawals_post(body, store_id, account_id)

Withdraw to store wallet

Withdraw an asset to your store wallet.

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
api_instance = swagger_client.CustodiansApi(swagger_client.ApiClient(configuration))
body = swagger_client.WithdrawalRequestData() # WithdrawalRequestData | 
store_id = 'store_id_example' # str | The Store ID
account_id = 'account_id_example' # str | The Custodian Account ID.

try:
    # Withdraw to store wallet
    api_response = api_instance.api_v1_stores_store_id_custodian_accounts_account_id_withdrawals_post(body, store_id, account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustodiansApi->api_v1_stores_store_id_custodian_accounts_account_id_withdrawals_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WithdrawalRequestData**](WithdrawalRequestData.md)|  | 
 **store_id** | **str**| The Store ID | 
 **account_id** | **str**| The Custodian Account ID. | 

### Return type

[**WithdrawalResultData**](WithdrawalResultData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_stores_store_id_custodian_accounts_account_id_withdrawals_withdrawal_id_post**
> WithdrawalResultData api_v1_stores_store_id_custodian_accounts_account_id_withdrawals_withdrawal_id_post(store_id, account_id, withdrawal_id)

Get withdrawal info

Get the details about a past withdrawal.

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
api_instance = swagger_client.CustodiansApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | The Store ID
account_id = 'account_id_example' # str | The Custodian Account ID.
withdrawal_id = 'withdrawal_id_example' # str | The Withdrawal ID.

try:
    # Get withdrawal info
    api_response = api_instance.api_v1_stores_store_id_custodian_accounts_account_id_withdrawals_withdrawal_id_post(store_id, account_id, withdrawal_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustodiansApi->api_v1_stores_store_id_custodian_accounts_account_id_withdrawals_withdrawal_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The Store ID | 
 **account_id** | **str**| The Custodian Account ID. | 
 **withdrawal_id** | **str**| The Withdrawal ID. | 

### Return type

[**WithdrawalResultData**](WithdrawalResultData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_stores_store_id_custodian_accounts_get**
> list[CustodianAccountData] api_v1_stores_store_id_custodian_accounts_get(store_id, asset_balances=asset_balances)

List store custodian accounts

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
api_instance = swagger_client.CustodiansApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | The Store ID
asset_balances = false # bool | Enable if you want the result to include the 'assetBalances' field. This will make the call slower or could cause the call to fail if the asset balances cannot be loaded (i.e. due to a bad API key). (optional) (default to false)

try:
    # List store custodian accounts
    api_response = api_instance.api_v1_stores_store_id_custodian_accounts_get(store_id, asset_balances=asset_balances)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustodiansApi->api_v1_stores_store_id_custodian_accounts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The Store ID | 
 **asset_balances** | **bool**| Enable if you want the result to include the &#x27;assetBalances&#x27; field. This will make the call slower or could cause the call to fail if the asset balances cannot be loaded (i.e. due to a bad API key). | [optional] [default to false]

### Return type

[**list[CustodianAccountData]**](CustodianAccountData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_stores_store_id_custodian_accounts_post**
> CustodianAccountData api_v1_stores_store_id_custodian_accounts_post(body)

Add a custodial account to a store.

Add a custodial account to a store.

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
api_instance = swagger_client.CustodiansApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateCustodianAccountRequest() # CreateCustodianAccountRequest | 

try:
    # Add a custodial account to a store.
    api_response = api_instance.api_v1_stores_store_id_custodian_accounts_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustodiansApi->api_v1_stores_store_id_custodian_accounts_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateCustodianAccountRequest**](CreateCustodianAccountRequest.md)|  | 

### Return type

[**CustodianAccountData**](CustodianAccountData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custodians_get_supported_custodians**
> list[CustodianData] custodians_get_supported_custodians()

List supported custodians

List all supported custodians for the BTCPay instance. You can install plugins to add more custodians.

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
api_instance = swagger_client.CustodiansApi(swagger_client.ApiClient(configuration))

try:
    # List supported custodians
    api_response = api_instance.custodians_get_supported_custodians()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustodiansApi->custodians_get_supported_custodians: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CustodianData]**](CustodianData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

