# WebhookDeliveryData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the delivery | [optional] 
**timestamp** | **AllOfWebhookDeliveryDataTimestamp** | Timestamp of when the delivery got broadcasted | [optional] 
**http_code** | **float** | HTTP code received by the remote service, if any. | [optional] 
**error_message** | **str** | User friendly error message, if any. | [optional] 
**status** | **str** | Whether the delivery failed or not (possible values are: &#x60;Failed&#x60;, &#x60;HttpError&#x60;, &#x60;HttpSuccess&#x60;) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

