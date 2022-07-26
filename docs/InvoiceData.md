# InvoiceData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The identifier of the invoice | [optional] 
**store_id** | **str** | The store identifier that the invoice belongs to | [optional] 
**amount** | **str** | The amount of the invoice | [optional] 
**currency** | **str** | The currency of the invoice | [optional] 
**type** | [**InvoiceType**](InvoiceType.md) |  | [optional] 
**checkout_link** | **str** | The link to the checkout page, where you can redirect the customer | [optional] 
**created_time** | **object** | The creation time of the invoice | [optional] 
**expiration_time** | **object** | The expiration time of the invoice | [optional] 
**monitoring_time** | **object** | The monitoring time of the invoice | [optional] 
**status** | [**InvoiceStatus**](InvoiceStatus.md) |  | [optional] 
**additional_status** | [**InvoiceAdditionalStatus**](InvoiceAdditionalStatus.md) |  | [optional] 
**available_statuses_for_manual_marking** | [**list[InvoiceStatus]**](InvoiceStatus.md) | The statuses the invoice can be manually marked as | [optional] 
**archived** | **bool** | true if the invoice is archived | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

