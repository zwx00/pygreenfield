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

class WebhookDeliveryData(object):
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
        'id': 'str',
        'timestamp': 'AllOfWebhookDeliveryDataTimestamp',
        'http_code': 'float',
        'error_message': 'str',
        'status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'timestamp': 'timestamp',
        'http_code': 'httpCode',
        'error_message': 'errorMessage',
        'status': 'status'
    }

    def __init__(self, id=None, timestamp=None, http_code=None, error_message=None, status=None):  # noqa: E501
        """WebhookDeliveryData - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._timestamp = None
        self._http_code = None
        self._error_message = None
        self._status = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if timestamp is not None:
            self.timestamp = timestamp
        if http_code is not None:
            self.http_code = http_code
        if error_message is not None:
            self.error_message = error_message
        if status is not None:
            self.status = status

    @property
    def id(self):
        """Gets the id of this WebhookDeliveryData.  # noqa: E501

        The id of the delivery  # noqa: E501

        :return: The id of this WebhookDeliveryData.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WebhookDeliveryData.

        The id of the delivery  # noqa: E501

        :param id: The id of this WebhookDeliveryData.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def timestamp(self):
        """Gets the timestamp of this WebhookDeliveryData.  # noqa: E501

        Timestamp of when the delivery got broadcasted  # noqa: E501

        :return: The timestamp of this WebhookDeliveryData.  # noqa: E501
        :rtype: AllOfWebhookDeliveryDataTimestamp
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this WebhookDeliveryData.

        Timestamp of when the delivery got broadcasted  # noqa: E501

        :param timestamp: The timestamp of this WebhookDeliveryData.  # noqa: E501
        :type: AllOfWebhookDeliveryDataTimestamp
        """

        self._timestamp = timestamp

    @property
    def http_code(self):
        """Gets the http_code of this WebhookDeliveryData.  # noqa: E501

        HTTP code received by the remote service, if any.  # noqa: E501

        :return: The http_code of this WebhookDeliveryData.  # noqa: E501
        :rtype: float
        """
        return self._http_code

    @http_code.setter
    def http_code(self, http_code):
        """Sets the http_code of this WebhookDeliveryData.

        HTTP code received by the remote service, if any.  # noqa: E501

        :param http_code: The http_code of this WebhookDeliveryData.  # noqa: E501
        :type: float
        """

        self._http_code = http_code

    @property
    def error_message(self):
        """Gets the error_message of this WebhookDeliveryData.  # noqa: E501

        User friendly error message, if any.  # noqa: E501

        :return: The error_message of this WebhookDeliveryData.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this WebhookDeliveryData.

        User friendly error message, if any.  # noqa: E501

        :param error_message: The error_message of this WebhookDeliveryData.  # noqa: E501
        :type: str
        """

        self._error_message = error_message

    @property
    def status(self):
        """Gets the status of this WebhookDeliveryData.  # noqa: E501

        Whether the delivery failed or not (possible values are: `Failed`, `HttpError`, `HttpSuccess`)  # noqa: E501

        :return: The status of this WebhookDeliveryData.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this WebhookDeliveryData.

        Whether the delivery failed or not (possible values are: `Failed`, `HttpError`, `HttpSuccess`)  # noqa: E501

        :param status: The status of this WebhookDeliveryData.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if issubclass(WebhookDeliveryData, dict):
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
        if not isinstance(other, WebhookDeliveryData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
