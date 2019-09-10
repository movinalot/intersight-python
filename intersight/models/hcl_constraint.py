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


class HclConstraint(object):
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
        'constraint_name': 'str',
        'constraint_value': 'str'
    }

    attribute_map = {
        'constraint_name': 'ConstraintName',
        'constraint_value': 'ConstraintValue'
    }

    def __init__(self, constraint_name=None, constraint_value=None):
        """
        HclConstraint - a model defined in Swagger
        """

        self._constraint_name = None
        self._constraint_value = None

        if constraint_name is not None:
          self.constraint_name = constraint_name
        if constraint_value is not None:
          self.constraint_value = constraint_value

    @property
    def constraint_name(self):
        """
        Gets the constraint_name of this HclConstraint.
        Name or key of the applicable compatibility constraint.  

        :return: The constraint_name of this HclConstraint.
        :rtype: str
        """
        return self._constraint_name

    @constraint_name.setter
    def constraint_name(self, constraint_name):
        """
        Sets the constraint_name of this HclConstraint.
        Name or key of the applicable compatibility constraint.  

        :param constraint_name: The constraint_name of this HclConstraint.
        :type: str
        """

        self._constraint_name = constraint_name

    @property
    def constraint_value(self):
        """
        Gets the constraint_value of this HclConstraint.
        Value of the applicable compatibility constraint. Could either be a string value or a regex.   

        :return: The constraint_value of this HclConstraint.
        :rtype: str
        """
        return self._constraint_value

    @constraint_value.setter
    def constraint_value(self, constraint_value):
        """
        Sets the constraint_value of this HclConstraint.
        Value of the applicable compatibility constraint. Could either be a string value or a regex.   

        :param constraint_value: The constraint_value of this HclConstraint.
        :type: str
        """

        self._constraint_value = constraint_value

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
        if not isinstance(other, HclConstraint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
