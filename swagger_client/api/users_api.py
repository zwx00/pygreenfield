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


class UsersApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_v1_users_get(self, **kwargs):  # noqa: E501
        """Get all users  # noqa: E501

        Load all users that exist.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_users_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v1_users_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_v1_users_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_v1_users_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get all users  # noqa: E501

        Load all users that exist.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_users_get_with_http_info(async_req=True)
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
                    " to method api_v1_users_get" % key
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
        auth_settings = ['API_Key', 'Basic']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/users', 'GET',
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

    def api_v1_users_id_or_email_delete(self, user_id, **kwargs):  # noqa: E501
        """Delete user  # noqa: E501

        Delete a user.  Must be an admin to perform this operation.  Attempting to delete the only admin user will not succeed.  All data associated with the user will be deleted as well if the operation succeeds.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_users_id_or_email_delete(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: The ID of the user to be deleted (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v1_users_id_or_email_delete_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v1_users_id_or_email_delete_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def api_v1_users_id_or_email_delete_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """Delete user  # noqa: E501

        Delete a user.  Must be an admin to perform this operation.  Attempting to delete the only admin user will not succeed.  All data associated with the user will be deleted as well if the operation succeeds.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_users_id_or_email_delete_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: The ID of the user to be deleted (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v1_users_id_or_email_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `api_v1_users_id_or_email_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['API_Key', 'Basic']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/users/{idOrEmail}', 'DELETE',
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

    def api_v1_users_id_or_email_get(self, id_or_email, **kwargs):  # noqa: E501
        """Get user by ID or Email  # noqa: E501

        Get 1 user by ID or Email.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_users_id_or_email_get(id_or_email, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id_or_email: The ID or email of the user to load (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v1_users_id_or_email_get_with_http_info(id_or_email, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v1_users_id_or_email_get_with_http_info(id_or_email, **kwargs)  # noqa: E501
            return data

    def api_v1_users_id_or_email_get_with_http_info(self, id_or_email, **kwargs):  # noqa: E501
        """Get user by ID or Email  # noqa: E501

        Get 1 user by ID or Email.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_users_id_or_email_get_with_http_info(id_or_email, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id_or_email: The ID or email of the user to load (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id_or_email']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v1_users_id_or_email_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id_or_email' is set
        if ('id_or_email' not in params or
                params['id_or_email'] is None):
            raise ValueError("Missing the required parameter `id_or_email` when calling `api_v1_users_id_or_email_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id_or_email' in params:
            path_params['idOrEmail'] = params['id_or_email']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['API_Key', 'Basic']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/users/{idOrEmail}', 'GET',
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

    def api_v1_users_id_or_email_lock_delete(self, user_id, **kwargs):  # noqa: E501
        """Toggle user  # noqa: E501

        Lock or unlock a user.  Must be an admin to perform this operation.  Attempting to lock the only admin user will not succeed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_users_id_or_email_lock_delete(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: The ID of the user to be un/locked (required)
        :param LockUserRequest body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v1_users_id_or_email_lock_delete_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v1_users_id_or_email_lock_delete_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def api_v1_users_id_or_email_lock_delete_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """Toggle user  # noqa: E501

        Lock or unlock a user.  Must be an admin to perform this operation.  Attempting to lock the only admin user will not succeed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_users_id_or_email_lock_delete_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: The ID of the user to be un/locked (required)
        :param LockUserRequest body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v1_users_id_or_email_lock_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `api_v1_users_id_or_email_lock_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API_Key', 'Basic']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/users/{idOrEmail}/lock', 'DELETE',
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

    def api_v1_users_post(self, body, **kwargs):  # noqa: E501
        """Create user  # noqa: E501

        Create a new user.  This operation can be called without authentication in any of this cases: * There is not any administrator yet on the server, * The subscriptions are not disabled in the server's policies.  If the first administrator is created by this call, subscriptions are automatically disabled.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_users_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1UsersBody body: (required)
        :return: ApplicationUserData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v1_users_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v1_users_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def api_v1_users_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create user  # noqa: E501

        Create a new user.  This operation can be called without authentication in any of this cases: * There is not any administrator yet on the server, * The subscriptions are not disabled in the server's policies.  If the first administrator is created by this call, subscriptions are automatically disabled.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_users_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1UsersBody body: (required)
        :return: ApplicationUserData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v1_users_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `api_v1_users_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

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
        auth_settings = ['API_Key', 'Basic']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/users', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApplicationUserData',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def users_delete_current_user(self, **kwargs):  # noqa: E501
        """Deletes user profile  # noqa: E501

        Deletes user profile and associated user data for user making the request  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.users_delete_current_user(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.users_delete_current_user_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.users_delete_current_user_with_http_info(**kwargs)  # noqa: E501
            return data

    def users_delete_current_user_with_http_info(self, **kwargs):  # noqa: E501
        """Deletes user profile  # noqa: E501

        Deletes user profile and associated user data for user making the request  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.users_delete_current_user_with_http_info(async_req=True)
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
                    " to method users_delete_current_user" % key
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
        auth_settings = ['API_Key', 'Basic']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/users/me', 'DELETE',
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

    def users_get_current_user(self, **kwargs):  # noqa: E501
        """Get current user information  # noqa: E501

        View information about the current user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.users_get_current_user(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ApplicationUserData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.users_get_current_user_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.users_get_current_user_with_http_info(**kwargs)  # noqa: E501
            return data

    def users_get_current_user_with_http_info(self, **kwargs):  # noqa: E501
        """Get current user information  # noqa: E501

        View information about the current user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.users_get_current_user_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ApplicationUserData
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
                    " to method users_get_current_user" % key
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
        auth_settings = ['API_Key', 'Basic']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/users/me', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApplicationUserData',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
