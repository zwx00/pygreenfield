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

class ApplicationUserData(object):
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
        'email': 'str',
        'email_confirmed': 'bool',
        'requires_email_confirmation': 'bool',
        'created': 'AllOfApplicationUserDataCreated',
        'roles': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'email': 'email',
        'email_confirmed': 'emailConfirmed',
        'requires_email_confirmation': 'requiresEmailConfirmation',
        'created': 'created',
        'roles': 'roles'
    }

    def __init__(self, id=None, email=None, email_confirmed=None, requires_email_confirmation=None, created=None, roles=None):  # noqa: E501
        """ApplicationUserData - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._email = None
        self._email_confirmed = None
        self._requires_email_confirmation = None
        self._created = None
        self._roles = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if email is not None:
            self.email = email
        if email_confirmed is not None:
            self.email_confirmed = email_confirmed
        if requires_email_confirmation is not None:
            self.requires_email_confirmation = requires_email_confirmation
        if created is not None:
            self.created = created
        if roles is not None:
            self.roles = roles

    @property
    def id(self):
        """Gets the id of this ApplicationUserData.  # noqa: E501

        The id of the user  # noqa: E501

        :return: The id of this ApplicationUserData.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApplicationUserData.

        The id of the user  # noqa: E501

        :param id: The id of this ApplicationUserData.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def email(self):
        """Gets the email of this ApplicationUserData.  # noqa: E501

        The email of the user  # noqa: E501

        :return: The email of this ApplicationUserData.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ApplicationUserData.

        The email of the user  # noqa: E501

        :param email: The email of this ApplicationUserData.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def email_confirmed(self):
        """Gets the email_confirmed of this ApplicationUserData.  # noqa: E501

        True if the email has been confirmed by the user  # noqa: E501

        :return: The email_confirmed of this ApplicationUserData.  # noqa: E501
        :rtype: bool
        """
        return self._email_confirmed

    @email_confirmed.setter
    def email_confirmed(self, email_confirmed):
        """Sets the email_confirmed of this ApplicationUserData.

        True if the email has been confirmed by the user  # noqa: E501

        :param email_confirmed: The email_confirmed of this ApplicationUserData.  # noqa: E501
        :type: bool
        """

        self._email_confirmed = email_confirmed

    @property
    def requires_email_confirmation(self):
        """Gets the requires_email_confirmation of this ApplicationUserData.  # noqa: E501

        True if the email requires email confirmation to log in  # noqa: E501

        :return: The requires_email_confirmation of this ApplicationUserData.  # noqa: E501
        :rtype: bool
        """
        return self._requires_email_confirmation

    @requires_email_confirmation.setter
    def requires_email_confirmation(self, requires_email_confirmation):
        """Sets the requires_email_confirmation of this ApplicationUserData.

        True if the email requires email confirmation to log in  # noqa: E501

        :param requires_email_confirmation: The requires_email_confirmation of this ApplicationUserData.  # noqa: E501
        :type: bool
        """

        self._requires_email_confirmation = requires_email_confirmation

    @property
    def created(self):
        """Gets the created of this ApplicationUserData.  # noqa: E501

        The creation date of the user as a unix timestamp. Null if created before v1.0.5.6  # noqa: E501

        :return: The created of this ApplicationUserData.  # noqa: E501
        :rtype: AllOfApplicationUserDataCreated
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ApplicationUserData.

        The creation date of the user as a unix timestamp. Null if created before v1.0.5.6  # noqa: E501

        :param created: The created of this ApplicationUserData.  # noqa: E501
        :type: AllOfApplicationUserDataCreated
        """

        self._created = created

    @property
    def roles(self):
        """Gets the roles of this ApplicationUserData.  # noqa: E501

        The roles of the user  # noqa: E501

        :return: The roles of this ApplicationUserData.  # noqa: E501
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this ApplicationUserData.

        The roles of the user  # noqa: E501

        :param roles: The roles of this ApplicationUserData.  # noqa: E501
        :type: list[str]
        """

        self._roles = roles

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
        if issubclass(ApplicationUserData, dict):
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
        if not isinstance(other, ApplicationUserData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other