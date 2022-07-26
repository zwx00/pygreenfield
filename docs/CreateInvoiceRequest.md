# CreateInvoiceRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | The amount of the invoice. If null or unspecified, the invoice will be a top-up invoice. (ie. The invoice will consider any payment as a full payment) | [optional] 
**currency** | **str** | The currency of the invoice (if null, empty or unspecified, the currency will be the store&#x27;s settings default)&#x27; | [optional] 
**additional_search_terms** | **list[str]** | Additional search term to help you find this invoice via text search | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

