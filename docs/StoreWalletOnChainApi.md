# swagger_client.StoreWalletOnChainApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**store_on_chain_wallets_create_on_chain_transaction**](StoreWalletOnChainApi.md#store_on_chain_wallets_create_on_chain_transaction) | **POST** /api/v1/stores/{storeId}/payment-methods/onchain/{cryptoCode}/wallet/transactions | Create store on-chain wallet transaction
[**store_on_chain_wallets_get_on_chain_fee_rate**](StoreWalletOnChainApi.md#store_on_chain_wallets_get_on_chain_fee_rate) | **GET** /api/v1/stores/{storeId}/payment-methods/onchain/{cryptoCode}/wallet/feerate | Get store on-chain wallet fee rate
[**store_on_chain_wallets_get_on_chain_wallet_receive_address**](StoreWalletOnChainApi.md#store_on_chain_wallets_get_on_chain_wallet_receive_address) | **GET** /api/v1/stores/{storeId}/payment-methods/onchain/{cryptoCode}/wallet/address | Get store on-chain wallet address
[**store_on_chain_wallets_get_on_chain_wallet_transaction**](StoreWalletOnChainApi.md#store_on_chain_wallets_get_on_chain_wallet_transaction) | **GET** /api/v1/stores/{storeId}/payment-methods/onchain/{cryptoCode}/wallet/transactions/{transactionId} | Get store on-chain wallet transaction
[**store_on_chain_wallets_get_on_chain_wallet_utx_os**](StoreWalletOnChainApi.md#store_on_chain_wallets_get_on_chain_wallet_utx_os) | **GET** /api/v1/stores/{storeId}/payment-methods/onchain/{cryptoCode}/wallet/utxos | Get store on-chain wallet UTXOS
[**store_on_chain_wallets_patch_on_chain_wallet_transaction**](StoreWalletOnChainApi.md#store_on_chain_wallets_patch_on_chain_wallet_transaction) | **PATCH** /api/v1/stores/{storeId}/payment-methods/onchain/{cryptoCode}/wallet/transactions/{transactionId} | Patch store on-chain wallet transaction info
[**store_on_chain_wallets_show_on_chain_wallet_overview**](StoreWalletOnChainApi.md#store_on_chain_wallets_show_on_chain_wallet_overview) | **GET** /api/v1/stores/{storeId}/payment-methods/onchain/{cryptoCode}/wallet | Get store on-chain wallet overview
[**store_on_chain_wallets_show_on_chain_wallet_transactions**](StoreWalletOnChainApi.md#store_on_chain_wallets_show_on_chain_wallet_transactions) | **GET** /api/v1/stores/{storeId}/payment-methods/onchain/{cryptoCode}/wallet/transactions | Get store on-chain wallet transactions
[**store_on_chain_wallets_un_reserve_on_chain_wallet_receive_address**](StoreWalletOnChainApi.md#store_on_chain_wallets_un_reserve_on_chain_wallet_receive_address) | **DELETE** /api/v1/stores/{storeId}/payment-methods/onchain/{cryptoCode}/wallet/address | UnReserve last store on-chain wallet address

# **store_on_chain_wallets_create_on_chain_transaction**
> InlineResponse2003 store_on_chain_wallets_create_on_chain_transaction(body, store_id, crypto_code)

Create store on-chain wallet transaction

Create store on-chain wallet transaction

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
api_instance = swagger_client.StoreWalletOnChainApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateOnChainTransactionRequest() # CreateOnChainTransactionRequest | 
store_id = 'store_id_example' # str | The store to fetch
crypto_code = 'crypto_code_example' # str | The crypto code of the wallet

try:
    # Create store on-chain wallet transaction
    api_response = api_instance.store_on_chain_wallets_create_on_chain_transaction(body, store_id, crypto_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreWalletOnChainApi->store_on_chain_wallets_create_on_chain_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateOnChainTransactionRequest**](CreateOnChainTransactionRequest.md)|  | 
 **store_id** | **str**| The store to fetch | 
 **crypto_code** | **str**| The crypto code of the wallet | 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_on_chain_wallets_get_on_chain_fee_rate**
> OnChainWalletFeeRateData store_on_chain_wallets_get_on_chain_fee_rate(store_id, crypto_code, block_target=block_target)

Get store on-chain wallet fee rate

Get wallet onchain fee rate

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
api_instance = swagger_client.StoreWalletOnChainApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | The store to fetch
crypto_code = 'crypto_code_example' # str | The crypto code of the payment method to fetch
block_target = 1.2 # float | The number of blocks away you are willing to target for confirmation. Defaults to the wallet's configured `RecommendedFeeBlockTarget` (optional)

try:
    # Get store on-chain wallet fee rate
    api_response = api_instance.store_on_chain_wallets_get_on_chain_fee_rate(store_id, crypto_code, block_target=block_target)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreWalletOnChainApi->store_on_chain_wallets_get_on_chain_fee_rate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store to fetch | 
 **crypto_code** | **str**| The crypto code of the payment method to fetch | 
 **block_target** | **float**| The number of blocks away you are willing to target for confirmation. Defaults to the wallet&#x27;s configured &#x60;RecommendedFeeBlockTarget&#x60; | [optional] 

### Return type

[**OnChainWalletFeeRateData**](OnChainWalletFeeRateData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_on_chain_wallets_get_on_chain_wallet_receive_address**
> OnChainWalletAddressData store_on_chain_wallets_get_on_chain_wallet_receive_address(store_id, crypto_code, force_generate=force_generate)

Get store on-chain wallet address

Get or generate address for wallet

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
api_instance = swagger_client.StoreWalletOnChainApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | The store to fetch
crypto_code = 'crypto_code_example' # str | The crypto code of the payment method to fetch
force_generate = false # bool | Whether to generate a new address for this request even if the previous one was not used (optional) (default to false)

try:
    # Get store on-chain wallet address
    api_response = api_instance.store_on_chain_wallets_get_on_chain_wallet_receive_address(store_id, crypto_code, force_generate=force_generate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreWalletOnChainApi->store_on_chain_wallets_get_on_chain_wallet_receive_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store to fetch | 
 **crypto_code** | **str**| The crypto code of the payment method to fetch | 
 **force_generate** | **bool**| Whether to generate a new address for this request even if the previous one was not used | [optional] [default to false]

### Return type

[**OnChainWalletAddressData**](OnChainWalletAddressData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_on_chain_wallets_get_on_chain_wallet_transaction**
> OnChainWalletTransactionData store_on_chain_wallets_get_on_chain_wallet_transaction(store_id, crypto_code, transaction_id)

Get store on-chain wallet transaction

Get store on-chain wallet transaction

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
api_instance = swagger_client.StoreWalletOnChainApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | The store to fetch
crypto_code = 'crypto_code_example' # str | The crypto code of the wallet to fetch
transaction_id = 'transaction_id_example' # str | The transaction id to fetch

try:
    # Get store on-chain wallet transaction
    api_response = api_instance.store_on_chain_wallets_get_on_chain_wallet_transaction(store_id, crypto_code, transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreWalletOnChainApi->store_on_chain_wallets_get_on_chain_wallet_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store to fetch | 
 **crypto_code** | **str**| The crypto code of the wallet to fetch | 
 **transaction_id** | **str**| The transaction id to fetch | 

### Return type

[**OnChainWalletTransactionData**](OnChainWalletTransactionData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_on_chain_wallets_get_on_chain_wallet_utx_os**
> list[OnChainWalletUTXOData] store_on_chain_wallets_get_on_chain_wallet_utx_os(store_id, crypto_code)

Get store on-chain wallet UTXOS

Get store on-chain wallet utxos

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
api_instance = swagger_client.StoreWalletOnChainApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | The store to fetch
crypto_code = 'crypto_code_example' # str | The crypto code of the wallet to fetch

try:
    # Get store on-chain wallet UTXOS
    api_response = api_instance.store_on_chain_wallets_get_on_chain_wallet_utx_os(store_id, crypto_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreWalletOnChainApi->store_on_chain_wallets_get_on_chain_wallet_utx_os: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store to fetch | 
 **crypto_code** | **str**| The crypto code of the wallet to fetch | 

### Return type

[**list[OnChainWalletUTXOData]**](OnChainWalletUTXOData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_on_chain_wallets_patch_on_chain_wallet_transaction**
> OnChainWalletTransactionData store_on_chain_wallets_patch_on_chain_wallet_transaction(body, store_id, crypto_code, transaction_id)

Patch store on-chain wallet transaction info

Patch store on-chain wallet transaction info

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
api_instance = swagger_client.StoreWalletOnChainApi(swagger_client.ApiClient(configuration))
body = swagger_client.PatchOnChainTransactionRequest() # PatchOnChainTransactionRequest | 
store_id = 'store_id_example' # str | The store to fetch
crypto_code = 'crypto_code_example' # str | The crypto code of the wallet to fetch
transaction_id = 'transaction_id_example' # str | The transaction id to fetch

try:
    # Patch store on-chain wallet transaction info
    api_response = api_instance.store_on_chain_wallets_patch_on_chain_wallet_transaction(body, store_id, crypto_code, transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreWalletOnChainApi->store_on_chain_wallets_patch_on_chain_wallet_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PatchOnChainTransactionRequest**](PatchOnChainTransactionRequest.md)|  | 
 **store_id** | **str**| The store to fetch | 
 **crypto_code** | **str**| The crypto code of the wallet to fetch | 
 **transaction_id** | **str**| The transaction id to fetch | 

### Return type

[**OnChainWalletTransactionData**](OnChainWalletTransactionData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_on_chain_wallets_show_on_chain_wallet_overview**
> OnChainWalletOverviewData store_on_chain_wallets_show_on_chain_wallet_overview(store_id, crypto_code)

Get store on-chain wallet overview

View information about the specified wallet

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
api_instance = swagger_client.StoreWalletOnChainApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | The store to fetch
crypto_code = 'crypto_code_example' # str | The crypto code of the payment method to fetch

try:
    # Get store on-chain wallet overview
    api_response = api_instance.store_on_chain_wallets_show_on_chain_wallet_overview(store_id, crypto_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreWalletOnChainApi->store_on_chain_wallets_show_on_chain_wallet_overview: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store to fetch | 
 **crypto_code** | **str**| The crypto code of the payment method to fetch | 

### Return type

[**OnChainWalletOverviewData**](OnChainWalletOverviewData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_on_chain_wallets_show_on_chain_wallet_transactions**
> list[OnChainWalletTransactionData] store_on_chain_wallets_show_on_chain_wallet_transactions(store_id, crypto_code, status_filter=status_filter, label_filter=label_filter, skip=skip, limit=limit)

Get store on-chain wallet transactions

Get store on-chain wallet transactions

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
api_instance = swagger_client.StoreWalletOnChainApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | The store to fetch
crypto_code = 'crypto_code_example' # str | The crypto code of the wallet to fetch
status_filter = [swagger_client.TransactionStatus()] # list[TransactionStatus] | Statuses to filter the transactions with (optional)
label_filter = 'label_filter_example' # str | Transaction label to filter by (optional)
skip = 56 # int | Number of transactions to skip from the start (optional)
limit = 56 # int | Maximum number of transactions to return (optional)

try:
    # Get store on-chain wallet transactions
    api_response = api_instance.store_on_chain_wallets_show_on_chain_wallet_transactions(store_id, crypto_code, status_filter=status_filter, label_filter=label_filter, skip=skip, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreWalletOnChainApi->store_on_chain_wallets_show_on_chain_wallet_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store to fetch | 
 **crypto_code** | **str**| The crypto code of the wallet to fetch | 
 **status_filter** | [**list[TransactionStatus]**](TransactionStatus.md)| Statuses to filter the transactions with | [optional] 
 **label_filter** | **str**| Transaction label to filter by | [optional] 
 **skip** | **int**| Number of transactions to skip from the start | [optional] 
 **limit** | **int**| Maximum number of transactions to return | [optional] 

### Return type

[**list[OnChainWalletTransactionData]**](OnChainWalletTransactionData.md)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_on_chain_wallets_un_reserve_on_chain_wallet_receive_address**
> store_on_chain_wallets_un_reserve_on_chain_wallet_receive_address(store_id, crypto_code)

UnReserve last store on-chain wallet address

UnReserve address

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
api_instance = swagger_client.StoreWalletOnChainApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | The store to fetch
crypto_code = 'crypto_code_example' # str | The crypto code of the payment method to fetch

try:
    # UnReserve last store on-chain wallet address
    api_instance.store_on_chain_wallets_un_reserve_on_chain_wallet_receive_address(store_id, crypto_code)
except ApiException as e:
    print("Exception when calling StoreWalletOnChainApi->store_on_chain_wallets_un_reserve_on_chain_wallet_receive_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The store to fetch | 
 **crypto_code** | **str**| The crypto code of the payment method to fetch | 

### Return type

void (empty response body)

### Authorization

[API_Key](../README.md#API_Key), [Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

