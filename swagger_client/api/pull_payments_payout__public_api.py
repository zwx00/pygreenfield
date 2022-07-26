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


class PullPaymentsPayoutPublicApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def pull_payments_get_payout(self, pull_payment_id, payout_id, **kwargs):  # noqa: E501
        """Get Payout  # noqa: E501

        Get payout  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pull_payments_get_payout(pull_payment_id, payout_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str pull_payment_id: The ID of the pull payment (required)
        :param str payout_id: The ID of the pull payment payout (required)
        :return: PayoutData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.pull_payments_get_payout_with_http_info(pull_payment_id, payout_id, **kwargs)  # noqa: E501
        else:
            (data) = self.pull_payments_get_payout_with_http_info(pull_payment_id, payout_id, **kwargs)  # noqa: E501
            return data

    def pull_payments_get_payout_with_http_info(self, pull_payment_id, payout_id, **kwargs):  # noqa: E501
        """Get Payout  # noqa: E501

        Get payout  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pull_payments_get_payout_with_http_info(pull_payment_id, payout_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str pull_payment_id: The ID of the pull payment (required)
        :param str payout_id: The ID of the pull payment payout (required)
        :return: PayoutData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['pull_payment_id', 'payout_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pull_payments_get_payout" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'pull_payment_id' is set
        if ('pull_payment_id' not in params or
                params['pull_payment_id'] is None):
            raise ValueError("Missing the required parameter `pull_payment_id` when calling `pull_payments_get_payout`")  # noqa: E501
        # verify the required parameter 'payout_id' is set
        if ('payout_id' not in params or
                params['payout_id'] is None):
            raise ValueError("Missing the required parameter `payout_id` when calling `pull_payments_get_payout`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'pull_payment_id' in params:
            path_params['pullPaymentId'] = params['pull_payment_id']  # noqa: E501
        if 'payout_id' in params:
            path_params['payoutId'] = params['payout_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/pull-payments/{pullPaymentId}/payouts/{payoutId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PayoutData',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
