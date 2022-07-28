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

class OnChainPaymentMethodPreviewResultAddressItem(object):
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
        'key_path': 'str',
        'address': 'str'
    }

    attribute_map = {
        'key_path': 'keyPath',
        'address': 'address'
    }

    def __init__(self, key_path=None, address=None):  # noqa: E501
        """OnChainPaymentMethodPreviewResultAddressItem - a model defined in Swagger"""  # noqa: E501
        self._key_path = None
        self._address = None
        self.discriminator = None
        if key_path is not None:
            self.key_path = key_path
        if address is not None:
            self.address = address

    @property
    def key_path(self):
        """Gets the key_path of this OnChainPaymentMethodPreviewResultAddressItem.  # noqa: E501

        The key path relative to the account key path.  # noqa: E501

        :return: The key_path of this OnChainPaymentMethodPreviewResultAddressItem.  # noqa: E501
        :rtype: str
        """
        return self._key_path

    @key_path.setter
    def key_path(self, key_path):
        """Sets the key_path of this OnChainPaymentMethodPreviewResultAddressItem.

        The key path relative to the account key path.  # noqa: E501

        :param key_path: The key_path of this OnChainPaymentMethodPreviewResultAddressItem.  # noqa: E501
        :type: str
        """

        self._key_path = key_path

    @property
    def address(self):
        """Gets the address of this OnChainPaymentMethodPreviewResultAddressItem.  # noqa: E501

        The address generated at the key path  # noqa: E501

        :return: The address of this OnChainPaymentMethodPreviewResultAddressItem.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this OnChainPaymentMethodPreviewResultAddressItem.

        The address generated at the key path  # noqa: E501

        :param address: The address of this OnChainPaymentMethodPreviewResultAddressItem.  # noqa: E501
        :type: str
        """

        self._address = address

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
        if issubclass(OnChainPaymentMethodPreviewResultAddressItem, dict):
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
        if not isinstance(other, OnChainPaymentMethodPreviewResultAddressItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other