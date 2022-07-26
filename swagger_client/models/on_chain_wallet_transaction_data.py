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

class OnChainWalletTransactionData(object):
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
        'transaction_hash': 'str',
        'comment': 'str',
        'amount': 'str',
        'block_hash': 'str',
        'block_height': 'str',
        'confirmations': 'str',
        'timestamp': 'AllOfOnChainWalletTransactionDataTimestamp',
        'status': 'TransactionStatus',
        'labels': 'list[LabelData]'
    }

    attribute_map = {
        'transaction_hash': 'transactionHash',
        'comment': 'comment',
        'amount': 'amount',
        'block_hash': 'blockHash',
        'block_height': 'blockHeight',
        'confirmations': 'confirmations',
        'timestamp': 'timestamp',
        'status': 'status',
        'labels': 'labels'
    }

    def __init__(self, transaction_hash=None, comment=None, amount=None, block_hash=None, block_height=None, confirmations=None, timestamp=None, status=None, labels=None):  # noqa: E501
        """OnChainWalletTransactionData - a model defined in Swagger"""  # noqa: E501
        self._transaction_hash = None
        self._comment = None
        self._amount = None
        self._block_hash = None
        self._block_height = None
        self._confirmations = None
        self._timestamp = None
        self._status = None
        self._labels = None
        self.discriminator = None
        if transaction_hash is not None:
            self.transaction_hash = transaction_hash
        if comment is not None:
            self.comment = comment
        if amount is not None:
            self.amount = amount
        if block_hash is not None:
            self.block_hash = block_hash
        if block_height is not None:
            self.block_height = block_height
        if confirmations is not None:
            self.confirmations = confirmations
        if timestamp is not None:
            self.timestamp = timestamp
        if status is not None:
            self.status = status
        if labels is not None:
            self.labels = labels

    @property
    def transaction_hash(self):
        """Gets the transaction_hash of this OnChainWalletTransactionData.  # noqa: E501

        The transaction id  # noqa: E501

        :return: The transaction_hash of this OnChainWalletTransactionData.  # noqa: E501
        :rtype: str
        """
        return self._transaction_hash

    @transaction_hash.setter
    def transaction_hash(self, transaction_hash):
        """Sets the transaction_hash of this OnChainWalletTransactionData.

        The transaction id  # noqa: E501

        :param transaction_hash: The transaction_hash of this OnChainWalletTransactionData.  # noqa: E501
        :type: str
        """

        self._transaction_hash = transaction_hash

    @property
    def comment(self):
        """Gets the comment of this OnChainWalletTransactionData.  # noqa: E501

        A comment linked to the transaction  # noqa: E501

        :return: The comment of this OnChainWalletTransactionData.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this OnChainWalletTransactionData.

        A comment linked to the transaction  # noqa: E501

        :param comment: The comment of this OnChainWalletTransactionData.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def amount(self):
        """Gets the amount of this OnChainWalletTransactionData.  # noqa: E501

        The amount the wallet balance changed with this transaction  # noqa: E501

        :return: The amount of this OnChainWalletTransactionData.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this OnChainWalletTransactionData.

        The amount the wallet balance changed with this transaction  # noqa: E501

        :param amount: The amount of this OnChainWalletTransactionData.  # noqa: E501
        :type: str
        """

        self._amount = amount

    @property
    def block_hash(self):
        """Gets the block_hash of this OnChainWalletTransactionData.  # noqa: E501

        The hash of the block that confirmed this transaction. Null if still unconfirmed.  # noqa: E501

        :return: The block_hash of this OnChainWalletTransactionData.  # noqa: E501
        :rtype: str
        """
        return self._block_hash

    @block_hash.setter
    def block_hash(self, block_hash):
        """Sets the block_hash of this OnChainWalletTransactionData.

        The hash of the block that confirmed this transaction. Null if still unconfirmed.  # noqa: E501

        :param block_hash: The block_hash of this OnChainWalletTransactionData.  # noqa: E501
        :type: str
        """

        self._block_hash = block_hash

    @property
    def block_height(self):
        """Gets the block_height of this OnChainWalletTransactionData.  # noqa: E501

        The height of the block that confirmed this transaction. Null if still unconfirmed.  # noqa: E501

        :return: The block_height of this OnChainWalletTransactionData.  # noqa: E501
        :rtype: str
        """
        return self._block_height

    @block_height.setter
    def block_height(self, block_height):
        """Sets the block_height of this OnChainWalletTransactionData.

        The height of the block that confirmed this transaction. Null if still unconfirmed.  # noqa: E501

        :param block_height: The block_height of this OnChainWalletTransactionData.  # noqa: E501
        :type: str
        """

        self._block_height = block_height

    @property
    def confirmations(self):
        """Gets the confirmations of this OnChainWalletTransactionData.  # noqa: E501

        The number of confirmations for this transaction  # noqa: E501

        :return: The confirmations of this OnChainWalletTransactionData.  # noqa: E501
        :rtype: str
        """
        return self._confirmations

    @confirmations.setter
    def confirmations(self, confirmations):
        """Sets the confirmations of this OnChainWalletTransactionData.

        The number of confirmations for this transaction  # noqa: E501

        :param confirmations: The confirmations of this OnChainWalletTransactionData.  # noqa: E501
        :type: str
        """

        self._confirmations = confirmations

    @property
    def timestamp(self):
        """Gets the timestamp of this OnChainWalletTransactionData.  # noqa: E501

        The time of the transaction  # noqa: E501

        :return: The timestamp of this OnChainWalletTransactionData.  # noqa: E501
        :rtype: AllOfOnChainWalletTransactionDataTimestamp
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this OnChainWalletTransactionData.

        The time of the transaction  # noqa: E501

        :param timestamp: The timestamp of this OnChainWalletTransactionData.  # noqa: E501
        :type: AllOfOnChainWalletTransactionDataTimestamp
        """

        self._timestamp = timestamp

    @property
    def status(self):
        """Gets the status of this OnChainWalletTransactionData.  # noqa: E501


        :return: The status of this OnChainWalletTransactionData.  # noqa: E501
        :rtype: TransactionStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this OnChainWalletTransactionData.


        :param status: The status of this OnChainWalletTransactionData.  # noqa: E501
        :type: TransactionStatus
        """

        self._status = status

    @property
    def labels(self):
        """Gets the labels of this OnChainWalletTransactionData.  # noqa: E501

        Labels linked to this transaction  # noqa: E501

        :return: The labels of this OnChainWalletTransactionData.  # noqa: E501
        :rtype: list[LabelData]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this OnChainWalletTransactionData.

        Labels linked to this transaction  # noqa: E501

        :param labels: The labels of this OnChainWalletTransactionData.  # noqa: E501
        :type: list[LabelData]
        """

        self._labels = labels

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
        if issubclass(OnChainWalletTransactionData, dict):
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
        if not isinstance(other, OnChainWalletTransactionData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
