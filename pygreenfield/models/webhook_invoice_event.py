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
from pygreenfield.models.webhook_event import WebhookEvent  # noqa: F401,E501

class WebhookInvoiceEvent(WebhookEvent):
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
        'store_id': 'str',
        'invoice_id': 'str'
    }
    if hasattr(WebhookEvent, "swagger_types"):
        swagger_types.update(WebhookEvent.swagger_types)

    attribute_map = {
        'store_id': 'storeId',
        'invoice_id': 'invoiceId'
    }
    if hasattr(WebhookEvent, "attribute_map"):
        attribute_map.update(WebhookEvent.attribute_map)

    def __init__(self, store_id=None, invoice_id=None, *args, **kwargs):  # noqa: E501
        """WebhookInvoiceEvent - a model defined in Swagger"""  # noqa: E501
        self._store_id = None
        self._invoice_id = None
        self.discriminator = None
        if store_id is not None:
            self.store_id = store_id
        if invoice_id is not None:
            self.invoice_id = invoice_id
        WebhookEvent.__init__(self, *args, **kwargs)

    @property
    def store_id(self):
        """Gets the store_id of this WebhookInvoiceEvent.  # noqa: E501

        The store id of the invoice's event  # noqa: E501

        :return: The store_id of this WebhookInvoiceEvent.  # noqa: E501
        :rtype: str
        """
        return self._store_id

    @store_id.setter
    def store_id(self, store_id):
        """Sets the store_id of this WebhookInvoiceEvent.

        The store id of the invoice's event  # noqa: E501

        :param store_id: The store_id of this WebhookInvoiceEvent.  # noqa: E501
        :type: str
        """

        self._store_id = store_id

    @property
    def invoice_id(self):
        """Gets the invoice_id of this WebhookInvoiceEvent.  # noqa: E501

        The invoice id of the invoice's event  # noqa: E501

        :return: The invoice_id of this WebhookInvoiceEvent.  # noqa: E501
        :rtype: str
        """
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, invoice_id):
        """Sets the invoice_id of this WebhookInvoiceEvent.

        The invoice id of the invoice's event  # noqa: E501

        :param invoice_id: The invoice_id of this WebhookInvoiceEvent.  # noqa: E501
        :type: str
        """

        self._invoice_id = invoice_id

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
        if issubclass(WebhookInvoiceEvent, dict):
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
        if not isinstance(other, WebhookInvoiceEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
