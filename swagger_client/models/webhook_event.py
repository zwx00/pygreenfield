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

class WebhookEvent(object):
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
        'delivery_id': 'str',
        'webhook_id': 'str',
        'original_delivery_id': 'str',
        'is_redelivery': 'bool',
        'type': 'str',
        'timestamp': 'AllOfWebhookEventTimestamp'
    }

    attribute_map = {
        'delivery_id': 'deliveryId',
        'webhook_id': 'webhookId',
        'original_delivery_id': 'originalDeliveryId',
        'is_redelivery': 'isRedelivery',
        'type': 'type',
        'timestamp': 'timestamp'
    }

    def __init__(self, delivery_id=None, webhook_id=None, original_delivery_id=None, is_redelivery=None, type=None, timestamp=None):  # noqa: E501
        """WebhookEvent - a model defined in Swagger"""  # noqa: E501
        self._delivery_id = None
        self._webhook_id = None
        self._original_delivery_id = None
        self._is_redelivery = None
        self._type = None
        self._timestamp = None
        self.discriminator = None
        if delivery_id is not None:
            self.delivery_id = delivery_id
        if webhook_id is not None:
            self.webhook_id = webhook_id
        if original_delivery_id is not None:
            self.original_delivery_id = original_delivery_id
        if is_redelivery is not None:
            self.is_redelivery = is_redelivery
        if type is not None:
            self.type = type
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def delivery_id(self):
        """Gets the delivery_id of this WebhookEvent.  # noqa: E501

        The delivery id of the webhook  # noqa: E501

        :return: The delivery_id of this WebhookEvent.  # noqa: E501
        :rtype: str
        """
        return self._delivery_id

    @delivery_id.setter
    def delivery_id(self, delivery_id):
        """Sets the delivery_id of this WebhookEvent.

        The delivery id of the webhook  # noqa: E501

        :param delivery_id: The delivery_id of this WebhookEvent.  # noqa: E501
        :type: str
        """

        self._delivery_id = delivery_id

    @property
    def webhook_id(self):
        """Gets the webhook_id of this WebhookEvent.  # noqa: E501

        The id of the webhook  # noqa: E501

        :return: The webhook_id of this WebhookEvent.  # noqa: E501
        :rtype: str
        """
        return self._webhook_id

    @webhook_id.setter
    def webhook_id(self, webhook_id):
        """Sets the webhook_id of this WebhookEvent.

        The id of the webhook  # noqa: E501

        :param webhook_id: The webhook_id of this WebhookEvent.  # noqa: E501
        :type: str
        """

        self._webhook_id = webhook_id

    @property
    def original_delivery_id(self):
        """Gets the original_delivery_id of this WebhookEvent.  # noqa: E501

        If this delivery is a redelivery, the is the delivery id of the original delivery.  # noqa: E501

        :return: The original_delivery_id of this WebhookEvent.  # noqa: E501
        :rtype: str
        """
        return self._original_delivery_id

    @original_delivery_id.setter
    def original_delivery_id(self, original_delivery_id):
        """Sets the original_delivery_id of this WebhookEvent.

        If this delivery is a redelivery, the is the delivery id of the original delivery.  # noqa: E501

        :param original_delivery_id: The original_delivery_id of this WebhookEvent.  # noqa: E501
        :type: str
        """

        self._original_delivery_id = original_delivery_id

    @property
    def is_redelivery(self):
        """Gets the is_redelivery of this WebhookEvent.  # noqa: E501

        True if this delivery is a redelivery  # noqa: E501

        :return: The is_redelivery of this WebhookEvent.  # noqa: E501
        :rtype: bool
        """
        return self._is_redelivery

    @is_redelivery.setter
    def is_redelivery(self, is_redelivery):
        """Sets the is_redelivery of this WebhookEvent.

        True if this delivery is a redelivery  # noqa: E501

        :param is_redelivery: The is_redelivery of this WebhookEvent.  # noqa: E501
        :type: bool
        """

        self._is_redelivery = is_redelivery

    @property
    def type(self):
        """Gets the type of this WebhookEvent.  # noqa: E501

        The type of this event, current available are `InvoiceCreated`, `InvoiceReceivedPayment`, `InvoiceProcessing`, `InvoiceExpired`, `InvoiceSettled`, `InvoiceInvalid`, and `InvoicePaymentSettled`.  # noqa: E501

        :return: The type of this WebhookEvent.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this WebhookEvent.

        The type of this event, current available are `InvoiceCreated`, `InvoiceReceivedPayment`, `InvoiceProcessing`, `InvoiceExpired`, `InvoiceSettled`, `InvoiceInvalid`, and `InvoicePaymentSettled`.  # noqa: E501

        :param type: The type of this WebhookEvent.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def timestamp(self):
        """Gets the timestamp of this WebhookEvent.  # noqa: E501

        The timestamp when this delivery has been created  # noqa: E501

        :return: The timestamp of this WebhookEvent.  # noqa: E501
        :rtype: AllOfWebhookEventTimestamp
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this WebhookEvent.

        The timestamp when this delivery has been created  # noqa: E501

        :param timestamp: The timestamp of this WebhookEvent.  # noqa: E501
        :type: AllOfWebhookEventTimestamp
        """

        self._timestamp = timestamp

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
        if issubclass(WebhookEvent, dict):
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
        if not isinstance(other, WebhookEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
