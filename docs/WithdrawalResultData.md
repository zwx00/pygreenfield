# WithdrawalResultData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** | The asset that is being withdrawn. | [optional] 
**payment_method** | **str** | The payment method that is used (crypto code + network). | [optional] 
**ledger_entries** | [**list[LedgerEntryData]**](LedgerEntryData.md) | The asset entries that were changed during the withdrawal. The first item is always the withdrawal itself. It could also includes ledger entries for the costs and may include credits or exchange tokens to give a discount. | [optional] 
**withdrawal_id** | **str** | The unique ID of the withdrawal used by the exchange. | [optional] 
**account_id** | **str** | The unique ID of the custodian account used. | [optional] 
**custodian_code** | **str** | The code of the custodian used. | [optional] 
**status** | **str** | The status of the withdrawal: &#x27;Queued&#x27;, &#x27;Complete&#x27;, &#x27;Failed&#x27; or &#x27;Unknown&#x27;. | [optional] 
**transaction_id** | **str** | The transaction ID on the blockchain once the withdrawal has been executed. | [optional] 
**target_address** | **str** | The address where the funds were sent to once the withdrawal has been executed. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

