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

from pygreenfield.api_client import ApiClient


class PullPaymentsManagementApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def pull_payments_archive_pull_payment(self, store_id, pull_payment_id, **kwargs):  # noqa: E501
        """Archive a pull payment  # noqa: E501

        Archive this pull payment (Will cancel all payouts awaiting for payment)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pull_payments_archive_pull_payment(store_id, pull_payment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str store_id: The ID of the store (required)
        :param str pull_payment_id: The ID of the pull payment (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.pull_payments_archive_pull_payment_with_http_info(store_id, pull_payment_id, **kwargs)  # noqa: E501
        else:
            (data) = self.pull_payments_archive_pull_payment_with_http_info(store_id, pull_payment_id, **kwargs)  # noqa: E501
            return data

    def pull_payments_archive_pull_payment_with_http_info(self, store_id, pull_payment_id, **kwargs):  # noqa: E501
        """Archive a pull payment  # noqa: E501

        Archive this pull payment (Will cancel all payouts awaiting for payment)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pull_payments_archive_pull_payment_with_http_info(store_id, pull_payment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str store_id: The ID of the store (required)
        :param str pull_payment_id: The ID of the pull payment (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['store_id', 'pull_payment_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pull_payments_archive_pull_payment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'store_id' is set
        if ('store_id' not in params or
                params['store_id'] is None):
            raise ValueError("Missing the required parameter `store_id` when calling `pull_payments_archive_pull_payment`")  # noqa: E501
        # verify the required parameter 'pull_payment_id' is set
        if ('pull_payment_id' not in params or
                params['pull_payment_id'] is None):
            raise ValueError("Missing the required parameter `pull_payment_id` when calling `pull_payments_archive_pull_payment`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'store_id' in params:
            path_params['storeId'] = params['store_id']  # noqa: E501
        if 'pull_payment_id' in params:
            path_params['pullPaymentId'] = params['pull_payment_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['API_Key']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/stores/{storeId}/pull-payments/{pullPaymentId}', 'DELETE',
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

    def pull_payments_create_pull_payment(self, store_id, **kwargs):  # noqa: E501
        """Create a new pull payment  # noqa: E501

        A pull payment allows its receiver to ask for payouts up to `amount` of `currency` every `period`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pull_payments_create_pull_payment(store_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str store_id: The store ID (required)
        :param StoreIdPullpaymentsBody body:
        :return: PullPaymentData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.pull_payments_create_pull_payment_with_http_info(store_id, **kwargs)  # noqa: E501
        else:
            (data) = self.pull_payments_create_pull_payment_with_http_info(store_id, **kwargs)  # noqa: E501
            return data

    def pull_payments_create_pull_payment_with_http_info(self, store_id, **kwargs):  # noqa: E501
        """Create a new pull payment  # noqa: E501

        A pull payment allows its receiver to ask for payouts up to `amount` of `currency` every `period`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pull_payments_create_pull_payment_with_http_info(store_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str store_id: The store ID (required)
        :param StoreIdPullpaymentsBody body:
        :return: PullPaymentData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['store_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pull_payments_create_pull_payment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'store_id' is set
        if ('store_id' not in params or
                params['store_id'] is None):
            raise ValueError("Missing the required parameter `store_id` when calling `pull_payments_create_pull_payment`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'store_id' in params:
            path_params['storeId'] = params['store_id']  # noqa: E501

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
            '/api/v1/stores/{storeId}/pull-payments', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PullPaymentData',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def pull_payments_get_pull_payments(self, store_id, **kwargs):  # noqa: E501
        """Get store's pull payments  # noqa: E501

        Get the pull payments of a store  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pull_payments_get_pull_payments(store_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str store_id: The store ID (required)
        :param bool include_archived: Whether this should list archived pull payments
        :return: PullPaymentDataList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.pull_payments_get_pull_payments_with_http_info(store_id, **kwargs)  # noqa: E501
        else:
            (data) = self.pull_payments_get_pull_payments_with_http_info(store_id, **kwargs)  # noqa: E501
            return data

    def pull_payments_get_pull_payments_with_http_info(self, store_id, **kwargs):  # noqa: E501
        """Get store's pull payments  # noqa: E501

        Get the pull payments of a store  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pull_payments_get_pull_payments_with_http_info(store_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str store_id: The store ID (required)
        :param bool include_archived: Whether this should list archived pull payments
        :return: PullPaymentDataList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['store_id', 'include_archived']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pull_payments_get_pull_payments" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'store_id' is set
        if ('store_id' not in params or
                params['store_id'] is None):
            raise ValueError("Missing the required parameter `store_id` when calling `pull_payments_get_pull_payments`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'store_id' in params:
            path_params['storeId'] = params['store_id']  # noqa: E501

        query_params = []
        if 'include_archived' in params:
            query_params.append(('includeArchived', params['include_archived']))  # noqa: E501

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
            '/api/v1/stores/{storeId}/pull-payments', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PullPaymentDataList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)