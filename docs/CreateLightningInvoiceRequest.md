# CreateLightningInvoiceRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Amount wrapped in a string, represented in a millistatoshi string. (1000 millisatoshi &#x3D; 1 satoshi) | [optional] 
**description** | **str** | Description of the invoice in the BOLT11 | [optional] 
**description_hash** | **str** | Description hash of the invoice in the BOLT11 | [optional] 
**expiry** | **AllOfCreateLightningInvoiceRequestExpiry** | Expiration time in seconds | [optional] 
**private_route_hints** | **bool** | True if the invoice should include private route hints | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

