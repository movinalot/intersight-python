# coding: utf-8

"""
    Intersight REST API

    This is Intersight REST API 

    OpenAPI spec version: 1.0.9-255
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class HclDriver(object):
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
        'is_latest': 'bool',
        'name': 'str',
        'supported_date': 'str',
        'version': 'str'
    }

    attribute_map = {
        'is_latest': 'IsLatest',
        'name': 'Name',
        'supported_date': 'SupportedDate',
        'version': 'Version'
    }

    def __init__(self, is_latest=None, name=None, supported_date=None, version=None):
        """
        HclDriver - a model defined in Swagger
        """

        self._is_latest = None
        self._name = None
        self._supported_date = None
        self._version = None

        if is_latest is not None:
          self.is_latest = is_latest
        if name is not None:
          self.name = name
        if supported_date is not None:
          self.supported_date = supported_date
        if version is not None:
          self.version = version

    @property
    def is_latest(self):
        """
        Gets the is_latest of this HclDriver.
        is the driver version latest  

        :return: The is_latest of this HclDriver.
        :rtype: bool
        """
        return self._is_latest

    @is_latest.setter
    def is_latest(self, is_latest):
        """
        Sets the is_latest of this HclDriver.
        is the driver version latest  

        :param is_latest: The is_latest of this HclDriver.
        :type: bool
        """

        self._is_latest = is_latest

    @property
    def name(self):
        """
        Gets the name of this HclDriver.
        name of the driver as read by the OS  

        :return: The name of this HclDriver.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this HclDriver.
        name of the driver as read by the OS  

        :param name: The name of this HclDriver.
        :type: str
        """

        self._name = name

    @property
    def supported_date(self):
        """
        Gets the supported_date of this HclDriver.
        date when the support was claimed  

        :return: The supported_date of this HclDriver.
        :rtype: str
        """
        return self._supported_date

    @supported_date.setter
    def supported_date(self, supported_date):
        """
        Sets the supported_date of this HclDriver.
        date when the support was claimed  

        :param supported_date: The supported_date of this HclDriver.
        :type: str
        """

        self._supported_date = supported_date

    @property
    def version(self):
        """
        Gets the version of this HclDriver.
        version of the driver   

        :return: The version of this HclDriver.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this HclDriver.
        version of the driver   

        :param version: The version of this HclDriver.
        :type: str
        """

        self._version = version

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
        if not isinstance(other, HclDriver):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other