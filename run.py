import swagger_client

configuration = swagger_client.Configuration()
configuration.host = 'https://something.com'
configuration.api_key["Authorization"] = "***"
configuration.api_key_prefix['Authorization'] = 'token'
lightning_node_api = swagger_client.LightningInternalNodeApi(swagger_client.ApiClient(configuration))
print(lightning_node_api.internal_lightning_node_api_get_info("BTC"))