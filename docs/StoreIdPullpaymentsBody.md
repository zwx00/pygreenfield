# StoreIdPullpaymentsBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the pull payment | [optional] 
**description** | **str** | The description of the pull payment | [optional] 
**amount** | **str** | The amount in &#x60;currency&#x60; of this pull payment as a decimal string | [optional] 
**currency** | **str** | The currency of the amount. | [optional] 
**period** | **int** | The length of each period in seconds. | [optional] 
**bolt11_expiration** | **str** | If lightning is activated, do not accept BOLT11 invoices with expiration less than … days | [optional] [default to '30']
**auto_approve_claims** | **bool** | Any payouts created for this pull payment will skip the approval phase upon creation | [optional] [default to False]
**starts_at** | **int** | When this pull payment is effective. Already started if null or unspecified. | [optional] 
**expires_at** | **int** | When this pull payment expires. Never expires if null or unspecified. | [optional] 
**payment_methods** | **list[str]** | The list of supported payment methods supported by this pull payment. Available options can be queried from the &#x60;StorePaymentMethods_GetStorePaymentMethods&#x60; endpoint | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

