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


class CommIpV6Interface(object):
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
        'gateway': 'str',
        'ip_address': 'str',
        'prefix': 'str'
    }

    attribute_map = {
        'gateway': 'Gateway',
        'ip_address': 'IpAddress',
        'prefix': 'Prefix'
    }

    def __init__(self, gateway=None, ip_address=None, prefix=None):
        """
        CommIpV6Interface - a model defined in Swagger
        """

        self._gateway = None
        self._ip_address = None
        self._prefix = None

        if gateway is not None:
          self.gateway = gateway
        if ip_address is not None:
          self.ip_address = ip_address
        if prefix is not None:
          self.prefix = prefix

    @property
    def gateway(self):
        """
        Gets the gateway of this CommIpV6Interface.
        The IPv6 address of the default gateway.  

        :return: The gateway of this CommIpV6Interface.
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """
        Sets the gateway of this CommIpV6Interface.
        The IPv6 address of the default gateway.  

        :param gateway: The gateway of this CommIpV6Interface.
        :type: str
        """

        self._gateway = gateway

    @property
    def ip_address(self):
        """
        Gets the ip_address of this CommIpV6Interface.
        The IPv6 Address, represented as eight groups of four hexadecimal digits, separated by colons.  

        :return: The ip_address of this CommIpV6Interface.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this CommIpV6Interface.
        The IPv6 Address, represented as eight groups of four hexadecimal digits, separated by colons.  

        :param ip_address: The ip_address of this CommIpV6Interface.
        :type: str
        """

        self._ip_address = ip_address

    @property
    def prefix(self):
        """
        Gets the prefix of this CommIpV6Interface.
        The IPv6 Prefix, represented as eight groups of four hexadecimal digits, separated by colons.   

        :return: The prefix of this CommIpV6Interface.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """
        Sets the prefix of this CommIpV6Interface.
        The IPv6 Prefix, represented as eight groups of four hexadecimal digits, separated by colons.   

        :param prefix: The prefix of this CommIpV6Interface.
        :type: str
        """

        self._prefix = prefix

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
        if not isinstance(other, CommIpV6Interface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
