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
from pygreenfield.models.webhook_invoice_event import WebhookInvoiceEvent  # noqa: F401,E501

class WebhookInvoiceReceivedPaymentEvent(WebhookInvoiceEvent):
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
        'after_expiration': 'bool',
        'payment_method': 'str',
        'payment': 'Payment'
    }
    if hasattr(WebhookInvoiceEvent, "swagger_types"):
        swagger_types.update(WebhookInvoiceEvent.swagger_types)

    attribute_map = {
        'after_expiration': 'afterExpiration',
        'payment_method': 'paymentMethod',
        'payment': 'payment'
    }
    if hasattr(WebhookInvoiceEvent, "attribute_map"):
        attribute_map.update(WebhookInvoiceEvent.attribute_map)

    def __init__(self, after_expiration=None, payment_method=None, payment=None, *args, **kwargs):  # noqa: E501
        """WebhookInvoiceReceivedPaymentEvent - a model defined in Swagger"""  # noqa: E501
        self._after_expiration = None
        self._payment_method = None
        self._payment = None
        self.discriminator = None
        if after_expiration is not None:
            self.after_expiration = after_expiration
        if payment_method is not None:
            self.payment_method = payment_method
        if payment is not None:
            self.payment = payment
        WebhookInvoiceEvent.__init__(self, *args, **kwargs)

    @property
    def after_expiration(self):
        """Gets the after_expiration of this WebhookInvoiceReceivedPaymentEvent.  # noqa: E501

        Whether this payment has been sent after expiration of the invoice  # noqa: E501

        :return: The after_expiration of this WebhookInvoiceReceivedPaymentEvent.  # noqa: E501
        :rtype: bool
        """
        return self._after_expiration

    @after_expiration.setter
    def after_expiration(self, after_expiration):
        """Sets the after_expiration of this WebhookInvoiceReceivedPaymentEvent.

        Whether this payment has been sent after expiration of the invoice  # noqa: E501

        :param after_expiration: The after_expiration of this WebhookInvoiceReceivedPaymentEvent.  # noqa: E501
        :type: bool
        """

        self._after_expiration = after_expiration

    @property
    def payment_method(self):
        """Gets the payment_method of this WebhookInvoiceReceivedPaymentEvent.  # noqa: E501

        What payment method was used for this payment  # noqa: E501

        :return: The payment_method of this WebhookInvoiceReceivedPaymentEvent.  # noqa: E501
        :rtype: str
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this WebhookInvoiceReceivedPaymentEvent.

        What payment method was used for this payment  # noqa: E501

        :param payment_method: The payment_method of this WebhookInvoiceReceivedPaymentEvent.  # noqa: E501
        :type: str
        """

        self._payment_method = payment_method

    @property
    def payment(self):
        """Gets the payment of this WebhookInvoiceReceivedPaymentEvent.  # noqa: E501


        :return: The payment of this WebhookInvoiceReceivedPaymentEvent.  # noqa: E501
        :rtype: Payment
        """
        return self._payment

    @payment.setter
    def payment(self, payment):
        """Sets the payment of this WebhookInvoiceReceivedPaymentEvent.


        :param payment: The payment of this WebhookInvoiceReceivedPaymentEvent.  # noqa: E501
        :type: Payment
        """

        self._payment = payment

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
        if issubclass(WebhookInvoiceReceivedPaymentEvent, dict):
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
        if not isinstance(other, WebhookInvoiceReceivedPaymentEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
