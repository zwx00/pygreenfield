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

class LightningNodeBalanceData(object):
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
        'onchain': 'OnchainBalanceData',
        'offchain': 'OffchainBalanceData'
    }

    attribute_map = {
        'onchain': 'onchain',
        'offchain': 'offchain'
    }

    def __init__(self, onchain=None, offchain=None):  # noqa: E501
        """LightningNodeBalanceData - a model defined in Swagger"""  # noqa: E501
        self._onchain = None
        self._offchain = None
        self.discriminator = None
        if onchain is not None:
            self.onchain = onchain
        if offchain is not None:
            self.offchain = offchain

    @property
    def onchain(self):
        """Gets the onchain of this LightningNodeBalanceData.  # noqa: E501


        :return: The onchain of this LightningNodeBalanceData.  # noqa: E501
        :rtype: OnchainBalanceData
        """
        return self._onchain

    @onchain.setter
    def onchain(self, onchain):
        """Sets the onchain of this LightningNodeBalanceData.


        :param onchain: The onchain of this LightningNodeBalanceData.  # noqa: E501
        :type: OnchainBalanceData
        """

        self._onchain = onchain

    @property
    def offchain(self):
        """Gets the offchain of this LightningNodeBalanceData.  # noqa: E501


        :return: The offchain of this LightningNodeBalanceData.  # noqa: E501
        :rtype: OffchainBalanceData
        """
        return self._offchain

    @offchain.setter
    def offchain(self, offchain):
        """Sets the offchain of this LightningNodeBalanceData.


        :param offchain: The offchain of this LightningNodeBalanceData.  # noqa: E501
        :type: OffchainBalanceData
        """

        self._offchain = offchain

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
        if issubclass(LightningNodeBalanceData, dict):
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
        if not isinstance(other, LightningNodeBalanceData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other