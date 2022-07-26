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

class LightningNetworkPaymentMethodBaseData(object):
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
        'connection_string': 'str',
        'disable_bolt11_payment_option': 'bool'
    }

    attribute_map = {
        'connection_string': 'connectionString',
        'disable_bolt11_payment_option': 'disableBOLT11PaymentOption'
    }

    def __init__(self, connection_string=None, disable_bolt11_payment_option=None):  # noqa: E501
        """LightningNetworkPaymentMethodBaseData - a model defined in Swagger"""  # noqa: E501
        self._connection_string = None
        self._disable_bolt11_payment_option = None
        self.discriminator = None
        if connection_string is not None:
            self.connection_string = connection_string
        if disable_bolt11_payment_option is not None:
            self.disable_bolt11_payment_option = disable_bolt11_payment_option

    @property
    def connection_string(self):
        """Gets the connection_string of this LightningNetworkPaymentMethodBaseData.  # noqa: E501

        The lightning connection string. Set to 'Internal Node' to use the internal node. (See [this doc](https://github.com/btcpayserver/BTCPayServer.Lightning/blob/master/README.md#examples) for some example)  # noqa: E501

        :return: The connection_string of this LightningNetworkPaymentMethodBaseData.  # noqa: E501
        :rtype: str
        """
        return self._connection_string

    @connection_string.setter
    def connection_string(self, connection_string):
        """Sets the connection_string of this LightningNetworkPaymentMethodBaseData.

        The lightning connection string. Set to 'Internal Node' to use the internal node. (See [this doc](https://github.com/btcpayserver/BTCPayServer.Lightning/blob/master/README.md#examples) for some example)  # noqa: E501

        :param connection_string: The connection_string of this LightningNetworkPaymentMethodBaseData.  # noqa: E501
        :type: str
        """

        self._connection_string = connection_string

    @property
    def disable_bolt11_payment_option(self):
        """Gets the disable_bolt11_payment_option of this LightningNetworkPaymentMethodBaseData.  # noqa: E501

        Whether to disable generation of bolt11 invoices. Useful when wanting to only use LNURL Pay exclusively.  # noqa: E501

        :return: The disable_bolt11_payment_option of this LightningNetworkPaymentMethodBaseData.  # noqa: E501
        :rtype: bool
        """
        return self._disable_bolt11_payment_option

    @disable_bolt11_payment_option.setter
    def disable_bolt11_payment_option(self, disable_bolt11_payment_option):
        """Sets the disable_bolt11_payment_option of this LightningNetworkPaymentMethodBaseData.

        Whether to disable generation of bolt11 invoices. Useful when wanting to only use LNURL Pay exclusively.  # noqa: E501

        :param disable_bolt11_payment_option: The disable_bolt11_payment_option of this LightningNetworkPaymentMethodBaseData.  # noqa: E501
        :type: bool
        """

        self._disable_bolt11_payment_option = disable_bolt11_payment_option

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
        if issubclass(LightningNetworkPaymentMethodBaseData, dict):
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
        if not isinstance(other, LightningNetworkPaymentMethodBaseData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
