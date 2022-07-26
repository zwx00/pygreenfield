# OnChainWalletTransactionData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_hash** | **str** | The transaction id | [optional] 
**comment** | **str** | A comment linked to the transaction | [optional] 
**amount** | **str** | The amount the wallet balance changed with this transaction | [optional] 
**block_hash** | **str** | The hash of the block that confirmed this transaction. Null if still unconfirmed. | [optional] 
**block_height** | **str** | The height of the block that confirmed this transaction. Null if still unconfirmed. | [optional] 
**confirmations** | **str** | The number of confirmations for this transaction | [optional] 
**timestamp** | **AllOfOnChainWalletTransactionDataTimestamp** | The time of the transaction | [optional] 
**status** | [**TransactionStatus**](TransactionStatus.md) |  | [optional] 
**labels** | [**list[LabelData]**](LabelData.md) | Labels linked to this transaction | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

