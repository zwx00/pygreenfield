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
from pygreenfield.models.invoice_data_base import InvoiceDataBase  # noqa: F401,E501

class CreateInvoiceRequest(InvoiceDataBase):
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
        'amount': 'str',
        'currency': 'str',
        'additional_search_terms': 'list[str]'
    }
    if hasattr(InvoiceDataBase, "swagger_types"):
        swagger_types.update(InvoiceDataBase.swagger_types)

    attribute_map = {
        'amount': 'amount',
        'currency': 'currency',
        'additional_search_terms': 'additionalSearchTerms'
    }
    if hasattr(InvoiceDataBase, "attribute_map"):
        attribute_map.update(InvoiceDataBase.attribute_map)

    def __init__(self, amount=None, currency=None, additional_search_terms=None, *args, **kwargs):  # noqa: E501
        """CreateInvoiceRequest - a model defined in Swagger"""  # noqa: E501
        self._amount = None
        self._currency = None
        self._additional_search_terms = None
        self.discriminator = None
        if amount is not None:
            self.amount = amount
        if currency is not None:
            self.currency = currency
        if additional_search_terms is not None:
            self.additional_search_terms = additional_search_terms
        InvoiceDataBase.__init__(self, *args, **kwargs)

    @property
    def amount(self):
        """Gets the amount of this CreateInvoiceRequest.  # noqa: E501

        The amount of the invoice. If null or unspecified, the invoice will be a top-up invoice. (ie. The invoice will consider any payment as a full payment)  # noqa: E501

        :return: The amount of this CreateInvoiceRequest.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this CreateInvoiceRequest.

        The amount of the invoice. If null or unspecified, the invoice will be a top-up invoice. (ie. The invoice will consider any payment as a full payment)  # noqa: E501

        :param amount: The amount of this CreateInvoiceRequest.  # noqa: E501
        :type: str
        """

        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this CreateInvoiceRequest.  # noqa: E501

        The currency of the invoice (if null, empty or unspecified, the currency will be the store's settings default)'  # noqa: E501

        :return: The currency of this CreateInvoiceRequest.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this CreateInvoiceRequest.

        The currency of the invoice (if null, empty or unspecified, the currency will be the store's settings default)'  # noqa: E501

        :param currency: The currency of this CreateInvoiceRequest.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def additional_search_terms(self):
        """Gets the additional_search_terms of this CreateInvoiceRequest.  # noqa: E501

        Additional search term to help you find this invoice via text search  # noqa: E501

        :return: The additional_search_terms of this CreateInvoiceRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._additional_search_terms

    @additional_search_terms.setter
    def additional_search_terms(self, additional_search_terms):
        """Sets the additional_search_terms of this CreateInvoiceRequest.

        Additional search term to help you find this invoice via text search  # noqa: E501

        :param additional_search_terms: The additional_search_terms of this CreateInvoiceRequest.  # noqa: E501
        :type: list[str]
        """

        self._additional_search_terms = additional_search_terms

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
        if issubclass(CreateInvoiceRequest, dict):
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
        if not isinstance(other, CreateInvoiceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
