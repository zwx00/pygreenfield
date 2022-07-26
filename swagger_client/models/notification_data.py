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

class NotificationData(object):
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
        'body': 'str',
        'link': 'str',
        'created_time': 'AllOfNotificationDataCreatedTime',
        'seen': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'body': 'body',
        'link': 'link',
        'created_time': 'createdTime',
        'seen': 'seen'
    }

    def __init__(self, id=None, body=None, link=None, created_time=None, seen=None):  # noqa: E501
        """NotificationData - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._body = None
        self._link = None
        self._created_time = None
        self._seen = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if body is not None:
            self.body = body
        if link is not None:
            self.link = link
        if created_time is not None:
            self.created_time = created_time
        if seen is not None:
            self.seen = seen

    @property
    def id(self):
        """Gets the id of this NotificationData.  # noqa: E501

        The identifier of the notification  # noqa: E501

        :return: The id of this NotificationData.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NotificationData.

        The identifier of the notification  # noqa: E501

        :param id: The id of this NotificationData.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def body(self):
        """Gets the body of this NotificationData.  # noqa: E501

        The html body of the notifications  # noqa: E501

        :return: The body of this NotificationData.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this NotificationData.

        The html body of the notifications  # noqa: E501

        :param body: The body of this NotificationData.  # noqa: E501
        :type: str
        """

        self._body = body

    @property
    def link(self):
        """Gets the link of this NotificationData.  # noqa: E501

        The link of the notification  # noqa: E501

        :return: The link of this NotificationData.  # noqa: E501
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this NotificationData.

        The link of the notification  # noqa: E501

        :param link: The link of this NotificationData.  # noqa: E501
        :type: str
        """

        self._link = link

    @property
    def created_time(self):
        """Gets the created_time of this NotificationData.  # noqa: E501

        The creation time of the notification  # noqa: E501

        :return: The created_time of this NotificationData.  # noqa: E501
        :rtype: AllOfNotificationDataCreatedTime
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this NotificationData.

        The creation time of the notification  # noqa: E501

        :param created_time: The created_time of this NotificationData.  # noqa: E501
        :type: AllOfNotificationDataCreatedTime
        """

        self._created_time = created_time

    @property
    def seen(self):
        """Gets the seen of this NotificationData.  # noqa: E501

        If the notification has been seen by the user  # noqa: E501

        :return: The seen of this NotificationData.  # noqa: E501
        :rtype: bool
        """
        return self._seen

    @seen.setter
    def seen(self, seen):
        """Sets the seen of this NotificationData.

        If the notification has been seen by the user  # noqa: E501

        :param seen: The seen of this NotificationData.  # noqa: E501
        :type: bool
        """

        self._seen = seen

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
        if issubclass(NotificationData, dict):
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
        if not isinstance(other, NotificationData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
