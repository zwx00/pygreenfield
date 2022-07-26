# InvoicePaymentMethodDataModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_method** | **str** | Payment method available for the invoice (e.g., \&quot;BTC\&quot; or \&quot;BTC-LightningNetwork\&quot; or \&quot;BTC-LNURLPAY\&quot;) | [optional] 
**crypto_code** | **str** | Crypto code of the payment method (e.g., \&quot;BTC\&quot; or \&quot;LTC\&quot;) | [optional] 
**destination** | **str** | The destination the payment must be made to | [optional] 
**payment_link** | **str** | A payment link that helps pay to the payment destination | [optional] 
**rate** | **str** | The rate between this payment method&#x27;s currency and the invoice currency | [optional] 
**payment_method_paid** | **str** | The amount paid by this payment method | [optional] 
**total_paid** | **str** | The total amount paid by all payment methods to the invoice, converted to this payment method&#x27;s currency | [optional] 
**due** | **str** | The total amount left to be paid, converted to this payment method&#x27;s currency (will be negative if overpaid) | [optional] 
**amount** | **str** | The invoice amount, converted to this payment method&#x27;s currency | [optional] 
**network_fee** | **str** | The added merchant fee to pay for network costs of this payment method. | [optional] 
**payments** | [**list[Payment]**](Payment.md) | Payments made with this payment method. | [optional] 
**activated** | **bool** | If the payment method is activated (when lazy payments option is enabled | [optional] 
**additional_data** | **AnyOfInvoicePaymentMethodDataModelAdditionalData** | Additional data provided by the payment method. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

