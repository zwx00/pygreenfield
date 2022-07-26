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
from swagger_client.models.webhook_invoice_event import WebhookInvoiceEvent  # noqa: F401,E501

class WebhookInvoiceInvalidEvent(WebhookInvoiceEvent):
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
        'manually_marked': 'bool'
    }
    if hasattr(WebhookInvoiceEvent, "swagger_types"):
        swagger_types.update(WebhookInvoiceEvent.swagger_types)

    attribute_map = {
        'manually_marked': 'manuallyMarked'
    }
    if hasattr(WebhookInvoiceEvent, "attribute_map"):
        attribute_map.update(WebhookInvoiceEvent.attribute_map)

    def __init__(self, manually_marked=None, *args, **kwargs):  # noqa: E501
        """WebhookInvoiceInvalidEvent - a model defined in Swagger"""  # noqa: E501
        self._manually_marked = None
        self.discriminator = None
        if manually_marked is not None:
            self.manually_marked = manually_marked
        WebhookInvoiceEvent.__init__(self, *args, **kwargs)

    @property
    def manually_marked(self):
        """Gets the manually_marked of this WebhookInvoiceInvalidEvent.  # noqa: E501

        Whether the invoice have been manually marked as confirmed. If false, this invoice has received payments which could not confirm in time.  # noqa: E501

        :return: The manually_marked of this WebhookInvoiceInvalidEvent.  # noqa: E501
        :rtype: bool
        """
        return self._manually_marked

    @manually_marked.setter
    def manually_marked(self, manually_marked):
        """Sets the manually_marked of this WebhookInvoiceInvalidEvent.

        Whether the invoice have been manually marked as confirmed. If false, this invoice has received payments which could not confirm in time.  # noqa: E501

        :param manually_marked: The manually_marked of this WebhookInvoiceInvalidEvent.  # noqa: E501
        :type: bool
        """

        self._manually_marked = manually_marked

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
        if issubclass(WebhookInvoiceInvalidEvent, dict):
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
        if not isinstance(other, WebhookInvoiceInvalidEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
