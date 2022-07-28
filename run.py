import pygreenfield

configuration = pygreenfield.Configuration()
configuration.host = 'https://btcpay.whatever.si'
configuration.api_key["Authorization"] = "... "
configuration.api_key_prefix['Authorization'] = 'token'
lightning_node_api = pygreenfield.LightningInternalNodeApi(pygreenfield.ApiClient(configuration))
print(lightning_node_api.internal_lightning_node_api_get_info("BTC"))