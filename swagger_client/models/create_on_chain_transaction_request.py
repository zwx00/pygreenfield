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

class CreateOnChainTransactionRequest(object):
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
        'destinations': 'list[CreateOnChainTransactionRequestDestination]',
        'feerate': 'float',
        'proceed_with_payjoin': 'bool',
        'proceed_with_broadcast': 'bool',
        'no_change': 'bool',
        'rbf': 'bool',
        'exclude_unconfirmed': 'bool',
        'selected_inputs': 'list[str]'
    }

    attribute_map = {
        'destinations': 'destinations',
        'feerate': 'feerate',
        'proceed_with_payjoin': 'proceedWithPayjoin',
        'proceed_with_broadcast': 'proceedWithBroadcast',
        'no_change': 'noChange',
        'rbf': 'rbf',
        'exclude_unconfirmed': 'excludeUnconfirmed',
        'selected_inputs': 'selectedInputs'
    }

    def __init__(self, destinations=None, feerate=None, proceed_with_payjoin=True, proceed_with_broadcast=True, no_change=False, rbf=None, exclude_unconfirmed=False, selected_inputs=None):  # noqa: E501
        """CreateOnChainTransactionRequest - a model defined in Swagger"""  # noqa: E501
        self._destinations = None
        self._feerate = None
        self._proceed_with_payjoin = None
        self._proceed_with_broadcast = None
        self._no_change = None
        self._rbf = None
        self._exclude_unconfirmed = None
        self._selected_inputs = None
        self.discriminator = None
        if destinations is not None:
            self.destinations = destinations
        if feerate is not None:
            self.feerate = feerate
        if proceed_with_payjoin is not None:
            self.proceed_with_payjoin = proceed_with_payjoin
        if proceed_with_broadcast is not None:
            self.proceed_with_broadcast = proceed_with_broadcast
        if no_change is not None:
            self.no_change = no_change
        if rbf is not None:
            self.rbf = rbf
        if exclude_unconfirmed is not None:
            self.exclude_unconfirmed = exclude_unconfirmed
        if selected_inputs is not None:
            self.selected_inputs = selected_inputs

    @property
    def destinations(self):
        """Gets the destinations of this CreateOnChainTransactionRequest.  # noqa: E501

        What and where to send money  # noqa: E501

        :return: The destinations of this CreateOnChainTransactionRequest.  # noqa: E501
        :rtype: list[CreateOnChainTransactionRequestDestination]
        """
        return self._destinations

    @destinations.setter
    def destinations(self, destinations):
        """Sets the destinations of this CreateOnChainTransactionRequest.

        What and where to send money  # noqa: E501

        :param destinations: The destinations of this CreateOnChainTransactionRequest.  # noqa: E501
        :type: list[CreateOnChainTransactionRequestDestination]
        """

        self._destinations = destinations

    @property
    def feerate(self):
        """Gets the feerate of this CreateOnChainTransactionRequest.  # noqa: E501

        Transaction fee.  # noqa: E501

        :return: The feerate of this CreateOnChainTransactionRequest.  # noqa: E501
        :rtype: float
        """
        return self._feerate

    @feerate.setter
    def feerate(self, feerate):
        """Sets the feerate of this CreateOnChainTransactionRequest.

        Transaction fee.  # noqa: E501

        :param feerate: The feerate of this CreateOnChainTransactionRequest.  # noqa: E501
        :type: float
        """

        self._feerate = feerate

    @property
    def proceed_with_payjoin(self):
        """Gets the proceed_with_payjoin of this CreateOnChainTransactionRequest.  # noqa: E501

        Whether to attempt to do a BIP78 payjoin if one of the destinations is a BIP21 with payjoin enabled  # noqa: E501

        :return: The proceed_with_payjoin of this CreateOnChainTransactionRequest.  # noqa: E501
        :rtype: bool
        """
        return self._proceed_with_payjoin

    @proceed_with_payjoin.setter
    def proceed_with_payjoin(self, proceed_with_payjoin):
        """Sets the proceed_with_payjoin of this CreateOnChainTransactionRequest.

        Whether to attempt to do a BIP78 payjoin if one of the destinations is a BIP21 with payjoin enabled  # noqa: E501

        :param proceed_with_payjoin: The proceed_with_payjoin of this CreateOnChainTransactionRequest.  # noqa: E501
        :type: bool
        """

        self._proceed_with_payjoin = proceed_with_payjoin

    @property
    def proceed_with_broadcast(self):
        """Gets the proceed_with_broadcast of this CreateOnChainTransactionRequest.  # noqa: E501

        Whether to broadcast the transaction after creating it or to simply return the transaction in hex format.  # noqa: E501

        :return: The proceed_with_broadcast of this CreateOnChainTransactionRequest.  # noqa: E501
        :rtype: bool
        """
        return self._proceed_with_broadcast

    @proceed_with_broadcast.setter
    def proceed_with_broadcast(self, proceed_with_broadcast):
        """Sets the proceed_with_broadcast of this CreateOnChainTransactionRequest.

        Whether to broadcast the transaction after creating it or to simply return the transaction in hex format.  # noqa: E501

        :param proceed_with_broadcast: The proceed_with_broadcast of this CreateOnChainTransactionRequest.  # noqa: E501
        :type: bool
        """

        self._proceed_with_broadcast = proceed_with_broadcast

    @property
    def no_change(self):
        """Gets the no_change of this CreateOnChainTransactionRequest.  # noqa: E501

        Whether to send all the spent coins to the destinations (THIS CAN COST YOU SIGNIFICANT AMOUNTS OF MONEY, LEAVE FALSE UNLESS YOU KNOW WHAT YOU ARE DOING).  # noqa: E501

        :return: The no_change of this CreateOnChainTransactionRequest.  # noqa: E501
        :rtype: bool
        """
        return self._no_change

    @no_change.setter
    def no_change(self, no_change):
        """Sets the no_change of this CreateOnChainTransactionRequest.

        Whether to send all the spent coins to the destinations (THIS CAN COST YOU SIGNIFICANT AMOUNTS OF MONEY, LEAVE FALSE UNLESS YOU KNOW WHAT YOU ARE DOING).  # noqa: E501

        :param no_change: The no_change of this CreateOnChainTransactionRequest.  # noqa: E501
        :type: bool
        """

        self._no_change = no_change

    @property
    def rbf(self):
        """Gets the rbf of this CreateOnChainTransactionRequest.  # noqa: E501

        Whether to enable RBF for the transaction. Leave blank to have it random (beneficial to privacy)  # noqa: E501

        :return: The rbf of this CreateOnChainTransactionRequest.  # noqa: E501
        :rtype: bool
        """
        return self._rbf

    @rbf.setter
    def rbf(self, rbf):
        """Sets the rbf of this CreateOnChainTransactionRequest.

        Whether to enable RBF for the transaction. Leave blank to have it random (beneficial to privacy)  # noqa: E501

        :param rbf: The rbf of this CreateOnChainTransactionRequest.  # noqa: E501
        :type: bool
        """

        self._rbf = rbf

    @property
    def exclude_unconfirmed(self):
        """Gets the exclude_unconfirmed of this CreateOnChainTransactionRequest.  # noqa: E501

        Whether to exclude unconfirmed UTXOs from the transaction.  # noqa: E501

        :return: The exclude_unconfirmed of this CreateOnChainTransactionRequest.  # noqa: E501
        :rtype: bool
        """
        return self._exclude_unconfirmed

    @exclude_unconfirmed.setter
    def exclude_unconfirmed(self, exclude_unconfirmed):
        """Sets the exclude_unconfirmed of this CreateOnChainTransactionRequest.

        Whether to exclude unconfirmed UTXOs from the transaction.  # noqa: E501

        :param exclude_unconfirmed: The exclude_unconfirmed of this CreateOnChainTransactionRequest.  # noqa: E501
        :type: bool
        """

        self._exclude_unconfirmed = exclude_unconfirmed

    @property
    def selected_inputs(self):
        """Gets the selected_inputs of this CreateOnChainTransactionRequest.  # noqa: E501

        Restrict the creation of the transactions from the outpoints provided ONLY (coin selection)  # noqa: E501

        :return: The selected_inputs of this CreateOnChainTransactionRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._selected_inputs

    @selected_inputs.setter
    def selected_inputs(self, selected_inputs):
        """Sets the selected_inputs of this CreateOnChainTransactionRequest.

        Restrict the creation of the transactions from the outpoints provided ONLY (coin selection)  # noqa: E501

        :param selected_inputs: The selected_inputs of this CreateOnChainTransactionRequest.  # noqa: E501
        :type: list[str]
        """

        self._selected_inputs = selected_inputs

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
        if issubclass(CreateOnChainTransactionRequest, dict):
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
        if not isinstance(other, CreateOnChainTransactionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other