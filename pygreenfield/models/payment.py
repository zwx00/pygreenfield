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

class Payment(object):
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
        'received_date': 'AllOfPaymentReceivedDate',
        'value': 'str',
        'fee': 'str',
        'status': 'PaymentStatus',
        'destination': 'str'
    }

    attribute_map = {
        'id': 'id',
        'received_date': 'receivedDate',
        'value': 'value',
        'fee': 'fee',
        'status': 'status',
        'destination': 'destination'
    }

    def __init__(self, id=None, received_date=None, value=None, fee=None, status=None, destination=None):  # noqa: E501
        """Payment - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._received_date = None
        self._value = None
        self._fee = None
        self._status = None
        self._destination = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if received_date is not None:
            self.received_date = received_date
        if value is not None:
            self.value = value
        if fee is not None:
            self.fee = fee
        if status is not None:
            self.status = status
        if destination is not None:
            self.destination = destination

    @property
    def id(self):
        """Gets the id of this Payment.  # noqa: E501

        A unique identifier for this payment  # noqa: E501

        :return: The id of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Payment.

        A unique identifier for this payment  # noqa: E501

        :param id: The id of this Payment.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def received_date(self):
        """Gets the received_date of this Payment.  # noqa: E501

        The date the payment was recorded  # noqa: E501

        :return: The received_date of this Payment.  # noqa: E501
        :rtype: AllOfPaymentReceivedDate
        """
        return self._received_date

    @received_date.setter
    def received_date(self, received_date):
        """Sets the received_date of this Payment.

        The date the payment was recorded  # noqa: E501

        :param received_date: The received_date of this Payment.  # noqa: E501
        :type: AllOfPaymentReceivedDate
        """

        self._received_date = received_date

    @property
    def value(self):
        """Gets the value of this Payment.  # noqa: E501

        The value of the payment  # noqa: E501

        :return: The value of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Payment.

        The value of the payment  # noqa: E501

        :param value: The value of this Payment.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def fee(self):
        """Gets the fee of this Payment.  # noqa: E501

        The fee paid for the payment  # noqa: E501

        :return: The fee of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._fee

    @fee.setter
    def fee(self, fee):
        """Sets the fee of this Payment.

        The fee paid for the payment  # noqa: E501

        :param fee: The fee of this Payment.  # noqa: E501
        :type: str
        """

        self._fee = fee

    @property
    def status(self):
        """Gets the status of this Payment.  # noqa: E501


        :return: The status of this Payment.  # noqa: E501
        :rtype: PaymentStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Payment.


        :param status: The status of this Payment.  # noqa: E501
        :type: PaymentStatus
        """

        self._status = status

    @property
    def destination(self):
        """Gets the destination of this Payment.  # noqa: E501

        The destination the payment was made to  # noqa: E501

        :return: The destination of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this Payment.

        The destination the payment was made to  # noqa: E501

        :param destination: The destination of this Payment.  # noqa: E501
        :type: str
        """

        self._destination = destination

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
        if issubclass(Payment, dict):
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
        if not isinstance(other, Payment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
