# WebhookDataBase

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the webhook | [optional] 
**enabled** | **bool** | Whether this webhook is enabled or not | [optional] [default to True]
**automatic_redelivery** | **bool** | If true, BTCPay Server will retry to redeliver any failed delivery after 10 seconds, 1 minutes and up to 6 times after 10 minutes. | [optional] [default to True]
**url** | **str** | The endpoint where BTCPay Server will make the POST request with the webhook body | [optional] 
**authorized_events** | [**WebhookDataBaseAuthorizedEvents**](WebhookDataBaseAuthorizedEvents.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

