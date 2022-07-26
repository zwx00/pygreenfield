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

class LedgerEntryData(object):
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
        'asset': 'str',
        'qty': 'float',
        'type': 'str'
    }

    attribute_map = {
        'asset': 'asset',
        'qty': 'qty',
        'type': 'type'
    }

    def __init__(self, asset=None, qty=None, type=None):  # noqa: E501
        """LedgerEntryData - a model defined in Swagger"""  # noqa: E501
        self._asset = None
        self._qty = None
        self._type = None
        self.discriminator = None
        if asset is not None:
            self.asset = asset
        if qty is not None:
            self.qty = qty
        if type is not None:
            self.type = type

    @property
    def asset(self):
        """Gets the asset of this LedgerEntryData.  # noqa: E501

        An asset.  # noqa: E501

        :return: The asset of this LedgerEntryData.  # noqa: E501
        :rtype: str
        """
        return self._asset

    @asset.setter
    def asset(self, asset):
        """Sets the asset of this LedgerEntryData.

        An asset.  # noqa: E501

        :param asset: The asset of this LedgerEntryData.  # noqa: E501
        :type: str
        """

        self._asset = asset

    @property
    def qty(self):
        """Gets the qty of this LedgerEntryData.  # noqa: E501

        The quantity changed of the asset. Can be positive or negative.  # noqa: E501

        :return: The qty of this LedgerEntryData.  # noqa: E501
        :rtype: float
        """
        return self._qty

    @qty.setter
    def qty(self, qty):
        """Sets the qty of this LedgerEntryData.

        The quantity changed of the asset. Can be positive or negative.  # noqa: E501

        :param qty: The qty of this LedgerEntryData.  # noqa: E501
        :type: float
        """

        self._qty = qty

    @property
    def type(self):
        """Gets the type of this LedgerEntryData.  # noqa: E501

        Trade, Fee or Withdrawal  # noqa: E501

        :return: The type of this LedgerEntryData.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this LedgerEntryData.

        Trade, Fee or Withdrawal  # noqa: E501

        :param type: The type of this LedgerEntryData.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(LedgerEntryData, dict):
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
        if not isinstance(other, LedgerEntryData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
