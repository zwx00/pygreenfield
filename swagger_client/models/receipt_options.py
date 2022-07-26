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

class ReceiptOptions(object):
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
        'show_qr': 'bool',
        'show_payments': 'bool'
    }

    attribute_map = {
        'enabled': 'enabled',
        'show_qr': 'showQR',
        'show_payments': 'showPayments'
    }

    def __init__(self, enabled=None, show_qr=None, show_payments=None):  # noqa: E501
        """ReceiptOptions - a model defined in Swagger"""  # noqa: E501
        self._enabled = None
        self._show_qr = None
        self._show_payments = None
        self.discriminator = None
        if enabled is not None:
            self.enabled = enabled
        if show_qr is not None:
            self.show_qr = show_qr
        if show_payments is not None:
            self.show_payments = show_payments

    @property
    def enabled(self):
        """Gets the enabled of this ReceiptOptions.  # noqa: E501

        A public page will be accessible once the invoice is settled. If null or unspecified, it will fallback to the store's settings. (The default store settings is true)  # noqa: E501

        :return: The enabled of this ReceiptOptions.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ReceiptOptions.

        A public page will be accessible once the invoice is settled. If null or unspecified, it will fallback to the store's settings. (The default store settings is true)  # noqa: E501

        :param enabled: The enabled of this ReceiptOptions.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def show_qr(self):
        """Gets the show_qr of this ReceiptOptions.  # noqa: E501

        Show the QR code of the receipt in the public receipt page. If null or unspecified, it will fallback to the store's settings. (The default store setting is true)  # noqa: E501

        :return: The show_qr of this ReceiptOptions.  # noqa: E501
        :rtype: bool
        """
        return self._show_qr

    @show_qr.setter
    def show_qr(self, show_qr):
        """Sets the show_qr of this ReceiptOptions.

        Show the QR code of the receipt in the public receipt page. If null or unspecified, it will fallback to the store's settings. (The default store setting is true)  # noqa: E501

        :param show_qr: The show_qr of this ReceiptOptions.  # noqa: E501
        :type: bool
        """

        self._show_qr = show_qr

    @property
    def show_payments(self):
        """Gets the show_payments of this ReceiptOptions.  # noqa: E501

        Show the payment list in the public receipt page. If null or unspecified, it will fallback to the store's settings. (The default store setting is true)  # noqa: E501

        :return: The show_payments of this ReceiptOptions.  # noqa: E501
        :rtype: bool
        """
        return self._show_payments

    @show_payments.setter
    def show_payments(self, show_payments):
        """Sets the show_payments of this ReceiptOptions.

        Show the payment list in the public receipt page. If null or unspecified, it will fallback to the store's settings. (The default store setting is true)  # noqa: E501

        :param show_payments: The show_payments of this ReceiptOptions.  # noqa: E501
        :type: bool
        """

        self._show_payments = show_payments

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
        if issubclass(ReceiptOptions, dict):
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
        if not isinstance(other, ReceiptOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
