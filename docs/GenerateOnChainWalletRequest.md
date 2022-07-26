# GenerateOnChainWalletRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**existing_mnemonic** | **str** | An existing BIP39 mnemonic seed to generate the wallet with | [optional] 
**passphrase** | **str** | A passphrase for the BIP39 mnemonic seed | [optional] 
**account_number** | **float** | The account to derive from the BIP39 mnemonic seed | [optional] [default to 0]
**save_private_keys** | **bool** | Whether to store the seed inside BTCPay Server to enable some additional services. IF &#x60;false&#x60; AND &#x60;existingMnemonic&#x60; IS NOT SPECIFIED, BE SURE TO SECURELY STORE THE SEED IN THE RESPONSE! | [optional] [default to False]
**import_keys_to_rpc** | **bool** | Whether to import all addresses generated via BTCPay Server into the underlying node wallet. (Private keys will also be imported if &#x60;savePrivateKeys&#x60; is set to true. | [optional] [default to False]
**word_list** | **str** | If &#x60;existingMnemonic&#x60; is not set, a mnemonic is generated using the specified wordList. | [optional] [default to 'English']
**word_count** | **float** | If &#x60;existingMnemonic&#x60; is not set, a mnemonic is generated using the specified wordCount. | [optional] [default to Word_countEnum._12]
**script_pub_key_type** | **str** | the type of wallet to generate | [optional] [default to 'Segwit']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

