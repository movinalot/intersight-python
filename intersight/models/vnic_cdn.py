# coding: utf-8

"""
    Intersight REST API

    This is Intersight REST API 

    OpenAPI spec version: 1.0.9-961
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class VnicCdn(object):
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
        'source': 'str',
        'value': 'str'
    }

    attribute_map = {
        'source': 'Source',
        'value': 'Value'
    }

    def __init__(self, source='vnic', value=None):
        """
        VnicCdn - a model defined in Swagger
        """

        self._source = None
        self._value = None

        if source is not None:
          self.source = source
        if value is not None:
          self.value = value

    @property
    def source(self):
        """
        Gets the source of this VnicCdn.
        Source of the CDN. It can either be user specified or be the same as the vNIC name.  

        :return: The source of this VnicCdn.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this VnicCdn.
        Source of the CDN. It can either be user specified or be the same as the vNIC name.  

        :param source: The source of this VnicCdn.
        :type: str
        """
        allowed_values = ["vnic", "user"]
        if source not in allowed_values:
            raise ValueError(
                "Invalid value for `source` ({0}), must be one of {1}"
                .format(source, allowed_values)
            )

        self._source = source

    @property
    def value(self):
        """
        Gets the value of this VnicCdn.
        The CDN value entered in case of user defined mode.   

        :return: The value of this VnicCdn.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this VnicCdn.
        The CDN value entered in case of user defined mode.   

        :param value: The value of this VnicCdn.
        :type: str
        """

        self._value = value

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
        if not isinstance(other, VnicCdn):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
