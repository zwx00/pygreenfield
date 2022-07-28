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


class AppsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def apps_create_point_of_sale_app(self, store_id, **kwargs):  # noqa: E501
        """Create a new Point of Sale app  # noqa: E501

        Point of Sale apps allows accepting payments for items in a virtual store  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.apps_create_point_of_sale_app(store_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str store_id: The store ID (required)
        :param AppsPosBody body:
        :return: PointOfSaleAppData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.apps_create_point_of_sale_app_with_http_info(store_id, **kwargs)  # noqa: E501
        else:
            (data) = self.apps_create_point_of_sale_app_with_http_info(store_id, **kwargs)  # noqa: E501
            return data

    def apps_create_point_of_sale_app_with_http_info(self, store_id, **kwargs):  # noqa: E501
        """Create a new Point of Sale app  # noqa: E501

        Point of Sale apps allows accepting payments for items in a virtual store  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.apps_create_point_of_sale_app_with_http_info(store_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str store_id: The store ID (required)
        :param AppsPosBody body:
        :return: PointOfSaleAppData
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
                    " to method apps_create_point_of_sale_app" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'store_id' is set
        if ('store_id' not in params or
                params['store_id'] is None):
            raise ValueError("Missing the required parameter `store_id` when calling `apps_create_point_of_sale_app`")  # noqa: E501

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
            '/api/v1/stores/{storeId}/apps/pos', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PointOfSaleAppData',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def apps_delete_point_of_sale_app(self, **kwargs):  # noqa: E501
        """Delete app  # noqa: E501

        Deletes apps with specified ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.apps_delete_point_of_sale_app(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.apps_delete_point_of_sale_app_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.apps_delete_point_of_sale_app_with_http_info(**kwargs)  # noqa: E501
            return data

    def apps_delete_point_of_sale_app_with_http_info(self, **kwargs):  # noqa: E501
        """Delete app  # noqa: E501

        Deletes apps with specified ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.apps_delete_point_of_sale_app_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method apps_delete_point_of_sale_app" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['API_Key']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/apps/{appId}', 'DELETE',
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

    def apps_get_point_of_sale_app(self, **kwargs):  # noqa: E501
        """Get basic app data  # noqa: E501

        Returns basic app data shared between all types of apps  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.apps_get_point_of_sale_app(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: BasicAppData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.apps_get_point_of_sale_app_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.apps_get_point_of_sale_app_with_http_info(**kwargs)  # noqa: E501
            return data

    def apps_get_point_of_sale_app_with_http_info(self, **kwargs):  # noqa: E501
        """Get basic app data  # noqa: E501

        Returns basic app data shared between all types of apps  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.apps_get_point_of_sale_app_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: BasicAppData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method apps_get_point_of_sale_app" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/api/v1/apps/{appId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BasicAppData',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
