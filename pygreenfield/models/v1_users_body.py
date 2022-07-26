# coding: utf-8

"""
    BTCPay Greenfield API

    A full API to use your BTCPay Server  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class V1UsersBody(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'email': 'str',
        'password': 'str',
        'is_administrator': 'bool'
    }

    attribute_map = {
        'email': 'email',
        'password': 'password',
        'is_administrator': 'isAdministrator'
    }

    def __init__(self, email=None, password=None, is_administrator=False):  # noqa: E501
        """V1UsersBody - a model defined in Swagger"""  # noqa: E501
        self._email = None
        self._password = None
        self._is_administrator = None
        self.discriminator = None
        if email is not None:
            self.email = email
        if password is not None:
            self.password = password
        if is_administrator is not None:
            self.is_administrator = is_administrator

    @property
    def email(self):
        """Gets the email of this V1UsersBody.  # noqa: E501

        The email of the new user  # noqa: E501

        :return: The email of this V1UsersBody.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this V1UsersBody.

        The email of the new user  # noqa: E501

        :param email: The email of this V1UsersBody.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def password(self):
        """Gets the password of this V1UsersBody.  # noqa: E501

        The password of the new user  # noqa: E501

        :return: The password of this V1UsersBody.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this V1UsersBody.

        The password of the new user  # noqa: E501

        :param password: The password of this V1UsersBody.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def is_administrator(self):
        """Gets the is_administrator of this V1UsersBody.  # noqa: E501

        Make this user administrator (only if you have the `unrestricted` permission of a server administrator)  # noqa: E501

        :return: The is_administrator of this V1UsersBody.  # noqa: E501
        :rtype: bool
        """
        return self._is_administrator

    @is_administrator.setter
    def is_administrator(self, is_administrator):
        """Sets the is_administrator of this V1UsersBody.

        Make this user administrator (only if you have the `unrestricted` permission of a server administrator)  # noqa: E501

        :param is_administrator: The is_administrator of this V1UsersBody.  # noqa: E501
        :type: bool
        """

        self._is_administrator = is_administrator

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(V1UsersBody, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1UsersBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
