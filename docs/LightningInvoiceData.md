# LightningInvoiceData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The invoice&#x27;s ID | [optional] 
**status** | [**LightningInvoiceStatus**](LightningInvoiceStatus.md) |  | [optional] 
**bolt11** | **str** | The BOLT11 representation of the invoice | [optional] 
**paid_at** | **AllOfLightningInvoiceDataPaidAt** | The unix timestamp when the invoice got paid | [optional] 
**expires_at** | **AllOfLightningInvoiceDataExpiresAt** | The unix timestamp when the invoice expires | [optional] 
**amount** | **str** | The amount of the invoice in millisatoshi | [optional] 
**amount_received** | **str** | The amount received in millisatoshi | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

