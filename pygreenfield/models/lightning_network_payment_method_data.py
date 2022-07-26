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
from pygreenfield.models.lightning_network_payment_method_base_data import LightningNetworkPaymentMethodBaseData  # noqa: F401,E501

class LightningNetworkPaymentMethodData(LightningNetworkPaymentMethodBaseData):
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
        'enabled': 'bool',
        'crypto_code': 'str',
        'payment_method': 'str'
    }
    if hasattr(LightningNetworkPaymentMethodBaseData, "swagger_types"):
        swagger_types.update(LightningNetworkPaymentMethodBaseData.swagger_types)

    attribute_map = {
        'enabled': 'enabled',
        'crypto_code': 'cryptoCode',
        'payment_method': 'paymentMethod'
    }
    if hasattr(LightningNetworkPaymentMethodBaseData, "attribute_map"):
        attribute_map.update(LightningNetworkPaymentMethodBaseData.attribute_map)

    def __init__(self, enabled=None, crypto_code=None, payment_method=None, *args, **kwargs):  # noqa: E501
        """LightningNetworkPaymentMethodData - a model defined in Swagger"""  # noqa: E501
        self._enabled = None
        self._crypto_code = None
        self._payment_method = None
        self.discriminator = None
        if enabled is not None:
            self.enabled = enabled
        if crypto_code is not None:
            self.crypto_code = crypto_code
        if payment_method is not None:
            self.payment_method = payment_method
        LightningNetworkPaymentMethodBaseData.__init__(self, *args, **kwargs)

    @property
    def enabled(self):
        """Gets the enabled of this LightningNetworkPaymentMethodData.  # noqa: E501

        Whether the payment method is enabled  # noqa: E501

        :return: The enabled of this LightningNetworkPaymentMethodData.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this LightningNetworkPaymentMethodData.

        Whether the payment method is enabled  # noqa: E501

        :param enabled: The enabled of this LightningNetworkPaymentMethodData.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def crypto_code(self):
        """Gets the crypto_code of this LightningNetworkPaymentMethodData.  # noqa: E501

        Crypto code of the payment method  # noqa: E501

        :return: The crypto_code of this LightningNetworkPaymentMethodData.  # noqa: E501
        :rtype: str
        """
        return self._crypto_code

    @crypto_code.setter
    def crypto_code(self, crypto_code):
        """Sets the crypto_code of this LightningNetworkPaymentMethodData.

        Crypto code of the payment method  # noqa: E501

        :param crypto_code: The crypto_code of this LightningNetworkPaymentMethodData.  # noqa: E501
        :type: str
        """

        self._crypto_code = crypto_code

    @property
    def payment_method(self):
        """Gets the payment_method of this LightningNetworkPaymentMethodData.  # noqa: E501

        The payment method  # noqa: E501

        :return: The payment_method of this LightningNetworkPaymentMethodData.  # noqa: E501
        :rtype: str
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this LightningNetworkPaymentMethodData.

        The payment method  # noqa: E501

        :param payment_method: The payment_method of this LightningNetworkPaymentMethodData.  # noqa: E501
        :type: str
        """

        self._payment_method = payment_method

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
        if issubclass(LightningNetworkPaymentMethodData, dict):
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
        if not isinstance(other, LightningNetworkPaymentMethodData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
