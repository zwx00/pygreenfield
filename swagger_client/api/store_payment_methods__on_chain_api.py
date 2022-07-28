# coding: utf-8

"""
    BTCPay Greenfield API

    A full API to use your BTCPay Server  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class StorePaymentMethodsOnChainApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_v1_stores_store_id_payment_methods_onchain_crypto_code_delete(self, store_id, crypto_code, **kwargs):  # noqa: E501
        """Remove store on-chain payment method  # noqa: E501

        Removes the specified store payment method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_stores_store_id_payment_methods_onchain_crypto_code_delete(store_id, crypto_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str store_id: The store to fetch (required)
        :param str crypto_code: The crypto code of the payment method to update (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v1_stores_store_id_payment_methods_onchain_crypto_code_delete_with_http_info(store_id, crypto_code, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v1_stores_store_id_payment_methods_onchain_crypto_code_delete_with_http_info(store_id, crypto_code, **kwargs)  # noqa: E501
            return data

    def api_v1_stores_store_id_payment_methods_onchain_crypto_code_delete_with_http_info(self, store_id, crypto_code, **kwargs):  # noqa: E501
        """Remove store on-chain payment method  # noqa: E501

        Removes the specified store payment method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_stores_store_id_payment_methods_onchain_crypto_code_delete_with_http_info(store_id, crypto_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str store_id: The store to fetch (required)
        :param str crypto_code: The crypto code of the payment method to update (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['store_id', 'crypto_code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v1_stores_store_id_payment_methods_onchain_crypto_code_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'store_id' is set
        if ('store_id' not in params or
                params['store_id'] is None):
            raise ValueError("Missing the required parameter `store_id` when calling `api_v1_stores_store_id_payment_methods_onchain_crypto_code_delete`")  # noqa: E501
        # verify the required parameter 'crypto_code' is set
        if ('crypto_code' not in params or
                params['crypto_code'] is None):
            raise ValueError("Missing the required parameter `crypto_code` when calling `api_v1_stores_store_id_payment_methods_onchain_crypto_code_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'store_id' in params:
            path_params['storeId'] = params['store_id']  # noqa: E501
        if 'crypto_code' in params:
            path_params['cryptoCode'] = params['crypto_code']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API_Key']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/stores/{storeId}/payment-methods/onchain/{cryptoCode}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def store_on_chain_payment_methods_generate_on_chain_wallet(self, body, store_id, crypto_code, **kwargs):  # noqa: E501
        """Generate store on-chain wallet  # noqa: E501

        Generate a wallet and update the specified store's payment method to it  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.store_on_chain_payment_methods_generate_on_chain_wallet(body, store_id, crypto_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GenerateOnChainWalletRequest body: (required)
        :param str store_id: The store to fetch (required)
        :param str crypto_code: The crypto code of the payment method to update (required)
        :return: OnChainPaymentMethodDataWithSensitiveData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.store_on_chain_payment_methods_generate_on_chain_wallet_with_http_info(body, store_id, crypto_code, **kwargs)  # noqa: E501
        else:
            (data) = self.store_on_chain_payment_methods_generate_on_chain_wallet_with_http_info(body, store_id, crypto_code, **kwargs)  # noqa: E501
            return data

    def store_on_chain_payment_methods_generate_on_chain_wallet_with_http_info(self, body, store_id, crypto_code, **kwargs):  # noqa: E501
        """Generate store on-chain wallet  # noqa: E501

        Generate a wallet and update the specified store's payment method to it  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.store_on_chain_payment_methods_generate_on_chain_wallet_with_http_info(body, store_id, crypto_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GenerateOnChainWalletRequest body: (required)
        :param str store_id: The store to fetch (required)
        :param str crypto_code: The crypto code of the payment method to update (required)
        :return: OnChainPaymentMethodDataWithSensitiveData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'store_id', 'crypto_code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method store_on_chain_payment_methods_generate_on_chain_wallet" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `store_on_chain_payment_methods_generate_on_chain_wallet`")  # noqa: E501
        # verify the required parameter 'store_id' is set
        if ('store_id' not in params or
                params['store_id'] is None):
            raise ValueError("Missing the required parameter `store_id` when calling `store_on_chain_payment_methods_generate_on_chain_wallet`")  # noqa: E501
        # verify the required parameter 'crypto_code' is set
        if ('crypto_code' not in params or
                params['crypto_code'] is None):
            raise ValueError("Missing the required parameter `crypto_code` when calling `store_on_chain_payment_methods_generate_on_chain_wallet`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'store_id' in params:
            path_params['storeId'] = params['store_id']  # noqa: E501
        if 'crypto_code' in params:
            path_params['cryptoCode'] = params['crypto_code']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API_Key']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/stores/{storeId}/payment-methods/onchain/{cryptoCode}/generate', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OnChainPaymentMethodDataWithSensitiveData',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def store_on_chain_payment_methods_get_on_chain_payment_method(self, store_id, crypto_code, **kwargs):  # noqa: E501
        """Get store on-chain payment method  # noqa: E501

        View information about the specified payment method  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.store_on_chain_payment_methods_get_on_chain_payment_method(store_id, crypto_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str store_id: The store to fetch (required)
        :param str crypto_code: The crypto code of the payment method to fetch (required)
        :return: OnChainPaymentMethodData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.store_on_chain_payment_methods_get_on_chain_payment_method_with_http_info(store_id, crypto_code, **kwargs)  # noqa: E501
        else:
            (data) = self.store_on_chain_payment_methods_get_on_chain_payment_method_with_http_info(store_id, crypto_code, **kwargs)  # noqa: E501
            return data

    def store_on_chain_payment_methods_get_on_chain_payment_method_with_http_info(self, store_id, crypto_code, **kwargs):  # noqa: E501
        """Get store on-chain payment method  # noqa: E501

        View information about the specified payment method  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.store_on_chain_payment_methods_get_on_chain_payment_method_with_http_info(store_id, crypto_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str store_id: The store to fetch (required)
        :param str crypto_code: The crypto code of the payment method to fetch (required)
        :return: OnChainPaymentMethodData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['store_id', 'crypto_code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method store_on_chain_payment_methods_get_on_chain_payment_method" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'store_id' is set
        if ('store_id' not in params or
                params['store_id'] is None):
            raise ValueError("Missing the required parameter `store_id` when calling `store_on_chain_payment_methods_get_on_chain_payment_method`")  # noqa: E501
        # verify the required parameter 'crypto_code' is set
        if ('crypto_code' not in params or
                params['crypto_code'] is None):
            raise ValueError("Missing the required parameter `crypto_code` when calling `store_on_chain_payment_methods_get_on_chain_payment_method`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'store_id' in params:
            path_params['storeId'] = params['store_id']  # noqa: E501
        if 'crypto_code' in params:
            path_params['cryptoCode'] = params['crypto_code']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API_Key']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/stores/{storeId}/payment-methods/onchain/{cryptoCode}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OnChainPaymentMethodData',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def store_on_chain_payment_methods_get_on_chain_payment_method_preview(self, store_id, crypto_code, **kwargs):  # noqa: E501
        """Preview store on-chain payment method addresses  # noqa: E501

        View addresses of the current payment method of the store  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.store_on_chain_payment_methods_get_on_chain_payment_method_preview(store_id, crypto_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str store_id: The store to fetch (required)
        :param str crypto_code: The crypto code of the payment method to fetch (required)
        :param float offset: From which index to fetch the addresses
        :param float amount: Number of addresses to preview
        :return: OnChainPaymentMethodPreviewResultData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.store_on_chain_payment_methods_get_on_chain_payment_method_preview_with_http_info(store_id, crypto_code, **kwargs)  # noqa: E501
        else:
            (data) = self.store_on_chain_payment_methods_get_on_chain_payment_method_preview_with_http_info(store_id, crypto_code, **kwargs)  # noqa: E501
            return data

    def store_on_chain_payment_methods_get_on_chain_payment_method_preview_with_http_info(self, store_id, crypto_code, **kwargs):  # noqa: E501
        """Preview store on-chain payment method addresses  # noqa: E501

        View addresses of the current payment method of the store  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.store_on_chain_payment_methods_get_on_chain_payment_method_preview_with_http_info(store_id, crypto_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str store_id: The store to fetch (required)
        :param str crypto_code: The crypto code of the payment method to fetch (required)
        :param float offset: From which index to fetch the addresses
        :param float amount: Number of addresses to preview
        :return: OnChainPaymentMethodPreviewResultData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['store_id', 'crypto_code', 'offset', 'amount']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method store_on_chain_payment_methods_get_on_chain_payment_method_preview" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'store_id' is set
        if ('store_id' not in params or
                params['store_id'] is None):
            raise ValueError("Missing the required parameter `store_id` when calling `store_on_chain_payment_methods_get_on_chain_payment_method_preview`")  # noqa: E501
        # verify the required parameter 'crypto_code' is set
        if ('crypto_code' not in params or
                params['crypto_code'] is None):
            raise ValueError("Missing the required parameter `crypto_code` when calling `store_on_chain_payment_methods_get_on_chain_payment_method_preview`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'store_id' in params:
            path_params['storeId'] = params['store_id']  # noqa: E501
        if 'crypto_code' in params:
            path_params['cryptoCode'] = params['crypto_code']  # noqa: E501

        query_params = []
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'amount' in params:
            query_params.append(('amount', params['amount']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API_Key']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/stores/{storeId}/payment-methods/OnChain/{cryptoCode}/preview', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OnChainPaymentMethodPreviewResultData',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def store_on_chain_payment_methods_get_on_chain_payment_methods(self, store_id, **kwargs):  # noqa: E501
        """Get store on-chain payment methods  # noqa: E501

        View information about the stores' configured on-chain payment methods  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.store_on_chain_payment_methods_get_on_chain_payment_methods(store_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str store_id: The store to fetch (required)
        :param bool enabled: Fetch payment methods that are enabled/disabled only
        :return: OnChainPaymentMethodDataList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.store_on_chain_payment_methods_get_on_chain_payment_methods_with_http_info(store_id, **kwargs)  # noqa: E501
        else:
            (data) = self.store_on_chain_payment_methods_get_on_chain_payment_methods_with_http_info(store_id, **kwargs)  # noqa: E501
            return data

    def store_on_chain_payment_methods_get_on_chain_payment_methods_with_http_info(self, store_id, **kwargs):  # noqa: E501
        """Get store on-chain payment methods  # noqa: E501

        View information about the stores' configured on-chain payment methods  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.store_on_chain_payment_methods_get_on_chain_payment_methods_with_http_info(store_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str store_id: The store to fetch (required)
        :param bool enabled: Fetch payment methods that are enabled/disabled only
        :return: OnChainPaymentMethodDataList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['store_id', 'enabled']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method store_on_chain_payment_methods_get_on_chain_payment_methods" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'store_id' is set
        if ('store_id' not in params or
                params['store_id'] is None):
            raise ValueError("Missing the required parameter `store_id` when calling `store_on_chain_payment_methods_get_on_chain_payment_methods`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'store_id' in params:
            path_params['storeId'] = params['store_id']  # noqa: E501

        query_params = []
        if 'enabled' in params:
            query_params.append(('enabled', params['enabled']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API_Key']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/stores/{storeId}/payment-methods/OnChain', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OnChainPaymentMethodDataList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def store_on_chain_payment_methods_post_on_chain_payment_method_preview(self, body, store_id, crypto_code, **kwargs):  # noqa: E501
        """Preview proposed store on-chain payment method addresses  # noqa: E501

        View addresses of a proposed payment method of the store  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.store_on_chain_payment_methods_post_on_chain_payment_method_preview(body, store_id, crypto_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CryptoCodePreviewBody body: (required)
        :param str store_id: The store to fetch (required)
        :param str crypto_code: The crypto code of the payment method to fetch (required)
        :param float offset: From which index to fetch the addresses
        :param float amount: Number of addresses to preview
        :return: OnChainPaymentMethodPreviewResultData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.store_on_chain_payment_methods_post_on_chain_payment_method_preview_with_http_info(body, store_id, crypto_code, **kwargs)  # noqa: E501
        else:
            (data) = self.store_on_chain_payment_methods_post_on_chain_payment_method_preview_with_http_info(body, store_id, crypto_code, **kwargs)  # noqa: E501
            return data

    def store_on_chain_payment_methods_post_on_chain_payment_method_preview_with_http_info(self, body, store_id, crypto_code, **kwargs):  # noqa: E501
        """Preview proposed store on-chain payment method addresses  # noqa: E501

        View addresses of a proposed payment method of the store  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.store_on_chain_payment_methods_post_on_chain_payment_method_preview_with_http_info(body, store_id, crypto_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CryptoCodePreviewBody body: (required)
        :param str store_id: The store to fetch (required)
        :param str crypto_code: The crypto code of the payment method to fetch (required)
        :param float offset: From which index to fetch the addresses
        :param float amount: Number of addresses to preview
        :return: OnChainPaymentMethodPreviewResultData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'store_id', 'crypto_code', 'offset', 'amount']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method store_on_chain_payment_methods_post_on_chain_payment_method_preview" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `store_on_chain_payment_methods_post_on_chain_payment_method_preview`")  # noqa: E501
        # verify the required parameter 'store_id' is set
        if ('store_id' not in params or
                params['store_id'] is None):
            raise ValueError("Missing the required parameter `store_id` when calling `store_on_chain_payment_methods_post_on_chain_payment_method_preview`")  # noqa: E501
        # verify the required parameter 'crypto_code' is set
        if ('crypto_code' not in params or
                params['crypto_code'] is None):
            raise ValueError("Missing the required parameter `crypto_code` when calling `store_on_chain_payment_methods_post_on_chain_payment_method_preview`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'store_id' in params:
            path_params['storeId'] = params['store_id']  # noqa: E501
        if 'crypto_code' in params:
            path_params['cryptoCode'] = params['crypto_code']  # noqa: E501

        query_params = []
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'amount' in params:
            query_params.append(('amount', params['amount']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API_Key']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/stores/{storeId}/payment-methods/OnChain/{cryptoCode}/preview', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OnChainPaymentMethodPreviewResultData',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def store_on_chain_payment_methods_update_on_chain_payment_method(self, body, store_id, crypto_code, **kwargs):  # noqa: E501
        """Update store on-chain payment method  # noqa: E501

        Update the specified store's payment method  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.store_on_chain_payment_methods_update_on_chain_payment_method(body, store_id, crypto_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateOnChainPaymentMethodRequest body: (required)
        :param str store_id: The store to fetch (required)
        :param str crypto_code: The crypto code of the payment method to update (required)
        :return: OnChainPaymentMethodData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.store_on_chain_payment_methods_update_on_chain_payment_method_with_http_info(body, store_id, crypto_code, **kwargs)  # noqa: E501
        else:
            (data) = self.store_on_chain_payment_methods_update_on_chain_payment_method_with_http_info(body, store_id, crypto_code, **kwargs)  # noqa: E501
            return data

    def store_on_chain_payment_methods_update_on_chain_payment_method_with_http_info(self, body, store_id, crypto_code, **kwargs):  # noqa: E501
        """Update store on-chain payment method  # noqa: E501

        Update the specified store's payment method  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.store_on_chain_payment_methods_update_on_chain_payment_method_with_http_info(body, store_id, crypto_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateOnChainPaymentMethodRequest body: (required)
        :param str store_id: The store to fetch (required)
        :param str crypto_code: The crypto code of the payment method to update (required)
        :return: OnChainPaymentMethodData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'store_id', 'crypto_code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method store_on_chain_payment_methods_update_on_chain_payment_method" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `store_on_chain_payment_methods_update_on_chain_payment_method`")  # noqa: E501
        # verify the required parameter 'store_id' is set
        if ('store_id' not in params or
                params['store_id'] is None):
            raise ValueError("Missing the required parameter `store_id` when calling `store_on_chain_payment_methods_update_on_chain_payment_method`")  # noqa: E501
        # verify the required parameter 'crypto_code' is set
        if ('crypto_code' not in params or
                params['crypto_code'] is None):
            raise ValueError("Missing the required parameter `crypto_code` when calling `store_on_chain_payment_methods_update_on_chain_payment_method`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'store_id' in params:
            path_params['storeId'] = params['store_id']  # noqa: E501
        if 'crypto_code' in params:
            path_params['cryptoCode'] = params['crypto_code']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API_Key']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/stores/{storeId}/payment-methods/onchain/{cryptoCode}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OnChainPaymentMethodData',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
