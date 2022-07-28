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

class CreateCustodianAccountRequest(object):
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
        'store_id': 'str',
        'custodian_code': 'str',
        'name': 'str',
        'config': 'object'
    }

    attribute_map = {
        'id': 'id',
        'store_id': 'storeId',
        'custodian_code': 'custodianCode',
        'name': 'name',
        'config': 'config'
    }

    def __init__(self, id=None, store_id=None, custodian_code=None, name=None, config=None):  # noqa: E501
        """CreateCustodianAccountRequest - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._store_id = None
        self._custodian_code = None
        self._name = None
        self._config = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if store_id is not None:
            self.store_id = store_id
        if custodian_code is not None:
            self.custodian_code = custodian_code
        if name is not None:
            self.name = name
        if config is not None:
            self.config = config

    @property
    def id(self):
        """Gets the id of this CreateCustodianAccountRequest.  # noqa: E501

        The unique code of the customer's account with this custodian. The format depends on the custodian.  # noqa: E501

        :return: The id of this CreateCustodianAccountRequest.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateCustodianAccountRequest.

        The unique code of the customer's account with this custodian. The format depends on the custodian.  # noqa: E501

        :param id: The id of this CreateCustodianAccountRequest.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def store_id(self):
        """Gets the store_id of this CreateCustodianAccountRequest.  # noqa: E501

        The store ID.  # noqa: E501

        :return: The store_id of this CreateCustodianAccountRequest.  # noqa: E501
        :rtype: str
        """
        return self._store_id

    @store_id.setter
    def store_id(self, store_id):
        """Sets the store_id of this CreateCustodianAccountRequest.

        The store ID.  # noqa: E501

        :param store_id: The store_id of this CreateCustodianAccountRequest.  # noqa: E501
        :type: str
        """

        self._store_id = store_id

    @property
    def custodian_code(self):
        """Gets the custodian_code of this CreateCustodianAccountRequest.  # noqa: E501

        The code for the custodian.  # noqa: E501

        :return: The custodian_code of this CreateCustodianAccountRequest.  # noqa: E501
        :rtype: str
        """
        return self._custodian_code

    @custodian_code.setter
    def custodian_code(self, custodian_code):
        """Sets the custodian_code of this CreateCustodianAccountRequest.

        The code for the custodian.  # noqa: E501

        :param custodian_code: The custodian_code of this CreateCustodianAccountRequest.  # noqa: E501
        :type: str
        """

        self._custodian_code = custodian_code

    @property
    def name(self):
        """Gets the name of this CreateCustodianAccountRequest.  # noqa: E501

        The name of the custodian account.  # noqa: E501

        :return: The name of this CreateCustodianAccountRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateCustodianAccountRequest.

        The name of the custodian account.  # noqa: E501

        :param name: The name of this CreateCustodianAccountRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def config(self):
        """Gets the config of this CreateCustodianAccountRequest.  # noqa: E501

        The configuration of this custodian account. Specific contents depend on the custodian and your access permissions.  # noqa: E501

        :return: The config of this CreateCustodianAccountRequest.  # noqa: E501
        :rtype: object
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this CreateCustodianAccountRequest.

        The configuration of this custodian account. Specific contents depend on the custodian and your access permissions.  # noqa: E501

        :param config: The config of this CreateCustodianAccountRequest.  # noqa: E501
        :type: object
        """

        self._config = config

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
        if issubclass(CreateCustodianAccountRequest, dict):
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
        if not isinstance(other, CreateCustodianAccountRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other