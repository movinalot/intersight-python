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


class VnicFcInterruptSettings(object):
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
        'mode': 'str'
    }

    attribute_map = {
        'mode': 'Mode'
    }

    def __init__(self, mode='MSIx'):
        """
        VnicFcInterruptSettings - a model defined in Swagger
        """

        self._mode = None

        if mode is not None:
          self.mode = mode

    @property
    def mode(self):
        """
        Gets the mode of this VnicFcInterruptSettings.
        The preferred driver interrupt mode. This can be one of the following:- MSIx — Message Signaled Interrupts (MSI) with the optional extension. MSI   — MSI only. INTx  — PCI INTx interrupts. MSIx is the recommended option.   

        :return: The mode of this VnicFcInterruptSettings.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """
        Sets the mode of this VnicFcInterruptSettings.
        The preferred driver interrupt mode. This can be one of the following:- MSIx — Message Signaled Interrupts (MSI) with the optional extension. MSI   — MSI only. INTx  — PCI INTx interrupts. MSIx is the recommended option.   

        :param mode: The mode of this VnicFcInterruptSettings.
        :type: str
        """
        allowed_values = ["MSIx", "MSI", "INTx"]
        if mode not in allowed_values:
            raise ValueError(
                "Invalid value for `mode` ({0}), must be one of {1}"
                .format(mode, allowed_values)
            )

        self._mode = mode

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
        if not isinstance(other, VnicFcInterruptSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
