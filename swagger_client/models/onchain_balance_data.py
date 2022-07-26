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

class OnchainBalanceData(object):
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
        'confirmed': 'str',
        'unconfirmed': 'str',
        'reserved': 'str'
    }

    attribute_map = {
        'confirmed': 'confirmed',
        'unconfirmed': 'unconfirmed',
        'reserved': 'reserved'
    }

    def __init__(self, confirmed=None, unconfirmed=None, reserved=None):  # noqa: E501
        """OnchainBalanceData - a model defined in Swagger"""  # noqa: E501
        self._confirmed = None
        self._unconfirmed = None
        self._reserved = None
        self.discriminator = None
        if confirmed is not None:
            self.confirmed = confirmed
        if unconfirmed is not None:
            self.unconfirmed = unconfirmed
        if reserved is not None:
            self.reserved = reserved

    @property
    def confirmed(self):
        """Gets the confirmed of this OnchainBalanceData.  # noqa: E501

        The confirmed amount in satoshi  # noqa: E501

        :return: The confirmed of this OnchainBalanceData.  # noqa: E501
        :rtype: str
        """
        return self._confirmed

    @confirmed.setter
    def confirmed(self, confirmed):
        """Sets the confirmed of this OnchainBalanceData.

        The confirmed amount in satoshi  # noqa: E501

        :param confirmed: The confirmed of this OnchainBalanceData.  # noqa: E501
        :type: str
        """

        self._confirmed = confirmed

    @property
    def unconfirmed(self):
        """Gets the unconfirmed of this OnchainBalanceData.  # noqa: E501

        The unconfirmed amount in satoshi  # noqa: E501

        :return: The unconfirmed of this OnchainBalanceData.  # noqa: E501
        :rtype: str
        """
        return self._unconfirmed

    @unconfirmed.setter
    def unconfirmed(self, unconfirmed):
        """Sets the unconfirmed of this OnchainBalanceData.

        The unconfirmed amount in satoshi  # noqa: E501

        :param unconfirmed: The unconfirmed of this OnchainBalanceData.  # noqa: E501
        :type: str
        """

        self._unconfirmed = unconfirmed

    @property
    def reserved(self):
        """Gets the reserved of this OnchainBalanceData.  # noqa: E501

        The reserved amount in satoshi  # noqa: E501

        :return: The reserved of this OnchainBalanceData.  # noqa: E501
        :rtype: str
        """
        return self._reserved

    @reserved.setter
    def reserved(self, reserved):
        """Sets the reserved of this OnchainBalanceData.

        The reserved amount in satoshi  # noqa: E501

        :param reserved: The reserved of this OnchainBalanceData.  # noqa: E501
        :type: str
        """

        self._reserved = reserved

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
        if issubclass(OnchainBalanceData, dict):
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
        if not isinstance(other, OnchainBalanceData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
