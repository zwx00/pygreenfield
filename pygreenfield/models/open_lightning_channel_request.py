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

class OpenLightningChannelRequest(object):
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
        'node_uri': 'str',
        'channel_amount': 'str',
        'fee_rate': 'float'
    }

    attribute_map = {
        'node_uri': 'nodeURI',
        'channel_amount': 'channelAmount',
        'fee_rate': 'feeRate'
    }

    def __init__(self, node_uri=None, channel_amount=None, fee_rate=None):  # noqa: E501
        """OpenLightningChannelRequest - a model defined in Swagger"""  # noqa: E501
        self._node_uri = None
        self._channel_amount = None
        self._fee_rate = None
        self.discriminator = None
        if node_uri is not None:
            self.node_uri = node_uri
        if channel_amount is not None:
            self.channel_amount = channel_amount
        if fee_rate is not None:
            self.fee_rate = fee_rate

    @property
    def node_uri(self):
        """Gets the node_uri of this OpenLightningChannelRequest.  # noqa: E501

        Node URI in the form `pubkey@endpoint[:port]`  # noqa: E501

        :return: The node_uri of this OpenLightningChannelRequest.  # noqa: E501
        :rtype: str
        """
        return self._node_uri

    @node_uri.setter
    def node_uri(self, node_uri):
        """Sets the node_uri of this OpenLightningChannelRequest.

        Node URI in the form `pubkey@endpoint[:port]`  # noqa: E501

        :param node_uri: The node_uri of this OpenLightningChannelRequest.  # noqa: E501
        :type: str
        """

        self._node_uri = node_uri

    @property
    def channel_amount(self):
        """Gets the channel_amount of this OpenLightningChannelRequest.  # noqa: E501

        The amount to fund (in satoshi)  # noqa: E501

        :return: The channel_amount of this OpenLightningChannelRequest.  # noqa: E501
        :rtype: str
        """
        return self._channel_amount

    @channel_amount.setter
    def channel_amount(self, channel_amount):
        """Sets the channel_amount of this OpenLightningChannelRequest.

        The amount to fund (in satoshi)  # noqa: E501

        :param channel_amount: The channel_amount of this OpenLightningChannelRequest.  # noqa: E501
        :type: str
        """

        self._channel_amount = channel_amount

    @property
    def fee_rate(self):
        """Gets the fee_rate of this OpenLightningChannelRequest.  # noqa: E501

        The amount to fund (in satoshi per byte)  # noqa: E501

        :return: The fee_rate of this OpenLightningChannelRequest.  # noqa: E501
        :rtype: float
        """
        return self._fee_rate

    @fee_rate.setter
    def fee_rate(self, fee_rate):
        """Sets the fee_rate of this OpenLightningChannelRequest.

        The amount to fund (in satoshi per byte)  # noqa: E501

        :param fee_rate: The fee_rate of this OpenLightningChannelRequest.  # noqa: E501
        :type: float
        """

        self._fee_rate = fee_rate

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
        if issubclass(OpenLightningChannelRequest, dict):
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
        if not isinstance(other, OpenLightningChannelRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
