# CheckoutOptions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**speed_policy** | [**SpeedPolicy**](SpeedPolicy.md) |  | [optional] 
**payment_methods** | **list[str]** | A specific set of payment methods to use for this invoice (ie. BTC, BTC-LightningNetwork). By default, select all payment methods enabled in the store. | [optional] 
**default_payment_method** | **str** | Default payment type for the invoice (e.g., BTC, BTC-LightningNetwork). Default payment method set for the store is used if this parameter is not specified. | [optional] 
**expiration_minutes** | **AllOfCheckoutOptionsExpirationMinutes** | The number of minutes after which an invoice becomes expired. Defaults to the store&#x27;s settings. (The default store settings is 15) | [optional] 
**monitoring_minutes** | **AllOfCheckoutOptionsMonitoringMinutes** | The number of minutes after an invoice expired after which we are still monitoring for incoming payments. Defaults to the store&#x27;s settings. (The default store settings is 1440, 1 day) | [optional] 
**payment_tolerance** | **float** | A percentage determining whether to count the invoice as paid when the invoice is paid within the specified margin of error. Defaults to the store&#x27;s settings. (The default store settings is 100) | [optional] 
**redirect_url** | **str** | When the customer has paid the invoice, the URL where the customer will be redirected when clicking on the &#x60;return to store&#x60; button. You can use placeholders &#x60;{InvoiceId}&#x60; or &#x60;{OrderId}&#x60; in the URL, BTCPay Server will replace those with this invoice &#x60;id&#x60; or &#x60;metadata.orderId&#x60; respectively. | [optional] 
**redirect_automatically** | **bool** | When the customer has paid the invoice, and a &#x60;redirectURL&#x60; is set, the checkout is redirected to &#x60;redirectURL&#x60; automatically if &#x60;redirectAutomatically&#x60; is true. Defaults to the store&#x27;s settings. (The default store settings is false) | [optional] 
**requires_refund_email** | **bool** | Invoice will require user to provide a refund email if this option is set to &#x60;true&#x60;. Has no effect if &#x60;buyerEmail&#x60; metadata is set as there is no email to collect in this case. | [optional] 
**default_language** | **str** | The language code (eg. en-US, en, fr-FR...) of the language presented to your customer in the checkout page. BTCPay Server tries to match the best language available. If null or not set, will fallback on the store&#x27;s default language. You can see the list of language codes with [this operation](#operation/langCodes). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

