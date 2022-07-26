# ApplicationUserData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the user | [optional] 
**email** | **str** | The email of the user | [optional] 
**email_confirmed** | **bool** | True if the email has been confirmed by the user | [optional] 
**requires_email_confirmation** | **bool** | True if the email requires email confirmation to log in | [optional] 
**created** | **AllOfApplicationUserDataCreated** | The creation date of the user as a unix timestamp. Null if created before v1.0.5.6 | [optional] 
**roles** | **list[str]** | The roles of the user | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

