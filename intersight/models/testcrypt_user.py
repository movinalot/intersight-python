# coding: utf-8

"""
    Intersight REST API

    This is Intersight REST API 

    OpenAPI spec version: 1.0.9-228
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class TestcryptUser(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'is_password_set': 'bool',
        'password': 'str',
        'username': 'str'
    }

    attribute_map = {
        'is_password_set': 'IsPasswordSet',
        'password': 'Password',
        'username': 'Username'
    }

    def __init__(self, is_password_set=None, password=None, username=None):
        """
        TestcryptUser - a model defined in Swagger
        """

        self._is_password_set = None
        self._password = None
        self._username = None

        if is_password_set is not None:
          self.is_password_set = is_password_set
        if password is not None:
          self.password = password
        if username is not None:
          self.username = username

    @property
    def is_password_set(self):
        """
        Gets the is_password_set of this TestcryptUser.

        :return: The is_password_set of this TestcryptUser.
        :rtype: bool
        """
        return self._is_password_set

    @is_password_set.setter
    def is_password_set(self, is_password_set):
        """
        Sets the is_password_set of this TestcryptUser.

        :param is_password_set: The is_password_set of this TestcryptUser.
        :type: bool
        """

        self._is_password_set = is_password_set

    @property
    def password(self):
        """
        Gets the password of this TestcryptUser.

        :return: The password of this TestcryptUser.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this TestcryptUser.

        :param password: The password of this TestcryptUser.
        :type: str
        """

        self._password = password

    @property
    def username(self):
        """
        Gets the username of this TestcryptUser.

        :return: The username of this TestcryptUser.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this TestcryptUser.

        :param username: The username of this TestcryptUser.
        :type: str
        """

        self._username = username

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, TestcryptUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
