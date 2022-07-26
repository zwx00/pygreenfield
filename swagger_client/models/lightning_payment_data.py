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

class LightningPaymentData(object):
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
        'status': 'LightningPaymentStatus',
        'bolt11': 'str',
        'payment_hash': 'str',
        'preimage': 'str',
        'created_at': 'AllOfLightningPaymentDataCreatedAt',
        'total_amount': 'str',
        'fee_amount': 'str'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'bolt11': 'BOLT11',
        'payment_hash': 'paymentHash',
        'preimage': 'preimage',
        'created_at': 'createdAt',
        'total_amount': 'totalAmount',
        'fee_amount': 'feeAmount'
    }

    def __init__(self, id=None, status=None, bolt11=None, payment_hash=None, preimage=None, created_at=None, total_amount=None, fee_amount=None):  # noqa: E501
        """LightningPaymentData - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._status = None
        self._bolt11 = None
        self._payment_hash = None
        self._preimage = None
        self._created_at = None
        self._total_amount = None
        self._fee_amount = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if bolt11 is not None:
            self.bolt11 = bolt11
        if payment_hash is not None:
            self.payment_hash = payment_hash
        if preimage is not None:
            self.preimage = preimage
        if created_at is not None:
            self.created_at = created_at
        if total_amount is not None:
            self.total_amount = total_amount
        if fee_amount is not None:
            self.fee_amount = fee_amount

    @property
    def id(self):
        """Gets the id of this LightningPaymentData.  # noqa: E501

        The payment's ID  # noqa: E501

        :return: The id of this LightningPaymentData.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LightningPaymentData.

        The payment's ID  # noqa: E501

        :param id: The id of this LightningPaymentData.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def status(self):
        """Gets the status of this LightningPaymentData.  # noqa: E501


        :return: The status of this LightningPaymentData.  # noqa: E501
        :rtype: LightningPaymentStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this LightningPaymentData.


        :param status: The status of this LightningPaymentData.  # noqa: E501
        :type: LightningPaymentStatus
        """

        self._status = status

    @property
    def bolt11(self):
        """Gets the bolt11 of this LightningPaymentData.  # noqa: E501

        The BOLT11 representation of the payment  # noqa: E501

        :return: The bolt11 of this LightningPaymentData.  # noqa: E501
        :rtype: str
        """
        return self._bolt11

    @bolt11.setter
    def bolt11(self, bolt11):
        """Sets the bolt11 of this LightningPaymentData.

        The BOLT11 representation of the payment  # noqa: E501

        :param bolt11: The bolt11 of this LightningPaymentData.  # noqa: E501
        :type: str
        """

        self._bolt11 = bolt11

    @property
    def payment_hash(self):
        """Gets the payment_hash of this LightningPaymentData.  # noqa: E501

        The payment hash  # noqa: E501

        :return: The payment_hash of this LightningPaymentData.  # noqa: E501
        :rtype: str
        """
        return self._payment_hash

    @payment_hash.setter
    def payment_hash(self, payment_hash):
        """Sets the payment_hash of this LightningPaymentData.

        The payment hash  # noqa: E501

        :param payment_hash: The payment_hash of this LightningPaymentData.  # noqa: E501
        :type: str
        """

        self._payment_hash = payment_hash

    @property
    def preimage(self):
        """Gets the preimage of this LightningPaymentData.  # noqa: E501

        The payment preimage (available when status is complete)  # noqa: E501

        :return: The preimage of this LightningPaymentData.  # noqa: E501
        :rtype: str
        """
        return self._preimage

    @preimage.setter
    def preimage(self, preimage):
        """Sets the preimage of this LightningPaymentData.

        The payment preimage (available when status is complete)  # noqa: E501

        :param preimage: The preimage of this LightningPaymentData.  # noqa: E501
        :type: str
        """

        self._preimage = preimage

    @property
    def created_at(self):
        """Gets the created_at of this LightningPaymentData.  # noqa: E501

        The unix timestamp when the payment got created  # noqa: E501

        :return: The created_at of this LightningPaymentData.  # noqa: E501
        :rtype: AllOfLightningPaymentDataCreatedAt
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this LightningPaymentData.

        The unix timestamp when the payment got created  # noqa: E501

        :param created_at: The created_at of this LightningPaymentData.  # noqa: E501
        :type: AllOfLightningPaymentDataCreatedAt
        """

        self._created_at = created_at

    @property
    def total_amount(self):
        """Gets the total_amount of this LightningPaymentData.  # noqa: E501

        The total amount (including fees) in millisatoshi  # noqa: E501

        :return: The total_amount of this LightningPaymentData.  # noqa: E501
        :rtype: str
        """
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        """Sets the total_amount of this LightningPaymentData.

        The total amount (including fees) in millisatoshi  # noqa: E501

        :param total_amount: The total_amount of this LightningPaymentData.  # noqa: E501
        :type: str
        """

        self._total_amount = total_amount

    @property
    def fee_amount(self):
        """Gets the fee_amount of this LightningPaymentData.  # noqa: E501

        The total fees in millisatoshi  # noqa: E501

        :return: The fee_amount of this LightningPaymentData.  # noqa: E501
        :rtype: str
        """
        return self._fee_amount

    @fee_amount.setter
    def fee_amount(self, fee_amount):
        """Sets the fee_amount of this LightningPaymentData.

        The total fees in millisatoshi  # noqa: E501

        :param fee_amount: The fee_amount of this LightningPaymentData.  # noqa: E501
        :type: str
        """

        self._fee_amount = fee_amount

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
        if issubclass(LightningPaymentData, dict):
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
        if not isinstance(other, LightningPaymentData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
