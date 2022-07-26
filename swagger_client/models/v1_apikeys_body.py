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

class V1ApikeysBody(object):
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
        'label': 'str',
        'permissions': 'list[str]'
    }

    attribute_map = {
        'label': 'label',
        'permissions': 'permissions'
    }

    def __init__(self, label=None, permissions=None):  # noqa: E501
        """V1ApikeysBody - a model defined in Swagger"""  # noqa: E501
        self._label = None
        self._permissions = None
        self.discriminator = None
        if label is not None:
            self.label = label
        if permissions is not None:
            self.permissions = permissions

    @property
    def label(self):
        """Gets the label of this V1ApikeysBody.  # noqa: E501

        The label of the new API Key  # noqa: E501

        :return: The label of this V1ApikeysBody.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this V1ApikeysBody.

        The label of the new API Key  # noqa: E501

        :param label: The label of this V1ApikeysBody.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def permissions(self):
        """Gets the permissions of this V1ApikeysBody.  # noqa: E501

        The permissions granted to this API Key (See API Key Authentication)  # noqa: E501

        :return: The permissions of this V1ApikeysBody.  # noqa: E501
        :rtype: list[str]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this V1ApikeysBody.

        The permissions granted to this API Key (See API Key Authentication)  # noqa: E501

        :param permissions: The permissions of this V1ApikeysBody.  # noqa: E501
        :type: list[str]
        """

        self._permissions = permissions

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
        if issubclass(V1ApikeysBody, dict):
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
        if not isinstance(other, V1ApikeysBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
