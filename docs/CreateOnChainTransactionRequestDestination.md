# CreateOnChainTransactionRequestDestination

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination** | **str** | A wallet address or a BIP21 payment link | [optional] 
**amount** | **str** | The amount to send. If &#x60;destination&#x60; is a BIP21 link, the amount must be the same or null. | [optional] 
**subtract_from_amount** | **bool** | Whether to subtract the transaction fee from the provided amount. This makes the receiver receive less, or in other words: he or she pays the transaction fee. Also useful if you want to clear out your wallet. Must be false if &#x60;destination&#x60; is a BIP21 link | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

