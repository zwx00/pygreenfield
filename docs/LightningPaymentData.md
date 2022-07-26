# LightningPaymentData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The payment&#x27;s ID | [optional] 
**status** | [**LightningPaymentStatus**](LightningPaymentStatus.md) |  | [optional] 
**bolt11** | **str** | The BOLT11 representation of the payment | [optional] 
**payment_hash** | **str** | The payment hash | [optional] 
**preimage** | **str** | The payment preimage (available when status is complete) | [optional] 
**created_at** | **AllOfLightningPaymentDataCreatedAt** | The unix timestamp when the payment got created | [optional] 
**total_amount** | **str** | The total amount (including fees) in millisatoshi | [optional] 
**fee_amount** | **str** | The total fees in millisatoshi | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

