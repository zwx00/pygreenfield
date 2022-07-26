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

class InvoiceDataBase(object):
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
        'metadata': 'InvoiceMetadata',
        'checkout': 'CheckoutOptions',
        'receipt': 'ReceiptOptions'
    }

    attribute_map = {
        'metadata': 'metadata',
        'checkout': 'checkout',
        'receipt': 'receipt'
    }

    def __init__(self, metadata=None, checkout=None, receipt=None):  # noqa: E501
        """InvoiceDataBase - a model defined in Swagger"""  # noqa: E501
        self._metadata = None
        self._checkout = None
        self._receipt = None
        self.discriminator = None
        if metadata is not None:
            self.metadata = metadata
        if checkout is not None:
            self.checkout = checkout
        if receipt is not None:
            self.receipt = receipt

    @property
    def metadata(self):
        """Gets the metadata of this InvoiceDataBase.  # noqa: E501


        :return: The metadata of this InvoiceDataBase.  # noqa: E501
        :rtype: InvoiceMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this InvoiceDataBase.


        :param metadata: The metadata of this InvoiceDataBase.  # noqa: E501
        :type: InvoiceMetadata
        """

        self._metadata = metadata

    @property
    def checkout(self):
        """Gets the checkout of this InvoiceDataBase.  # noqa: E501


        :return: The checkout of this InvoiceDataBase.  # noqa: E501
        :rtype: CheckoutOptions
        """
        return self._checkout

    @checkout.setter
    def checkout(self, checkout):
        """Sets the checkout of this InvoiceDataBase.


        :param checkout: The checkout of this InvoiceDataBase.  # noqa: E501
        :type: CheckoutOptions
        """

        self._checkout = checkout

    @property
    def receipt(self):
        """Gets the receipt of this InvoiceDataBase.  # noqa: E501


        :return: The receipt of this InvoiceDataBase.  # noqa: E501
        :rtype: ReceiptOptions
        """
        return self._receipt

    @receipt.setter
    def receipt(self, receipt):
        """Sets the receipt of this InvoiceDataBase.


        :param receipt: The receipt of this InvoiceDataBase.  # noqa: E501
        :type: ReceiptOptions
        """

        self._receipt = receipt

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
        if issubclass(InvoiceDataBase, dict):
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
        if not isinstance(other, InvoiceDataBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
