# OnChainWalletUTXOData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | A comment linked to this utxo | [optional] 
**amount** | **str** | the value of this utxo | [optional] 
**link** | **str** | a link to the configured blockchain explorer to view the utxo | [optional] 
**outpoint** | **str** | outpoint of this utxo | [optional] 
**timestamp** | **AllOfOnChainWalletUTXODataTimestamp** | The time of the utxo | [optional] 
**key_path** | **str** | the derivation path in relation to the HD account | [optional] 
**address** | **str** | The wallet address of this utxo | [optional] 
**confirmations** | **float** | The number of confirmations of this utxo | [optional] 
**labels** | [**list[LabelData]**](LabelData.md) | Labels linked to this transaction | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

