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


class WorkflowWorkflowTask(object):
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
        'description': 'str',
        'label': 'str',
        'name': 'str'
    }

    attribute_map = {
        'description': 'Description',
        'label': 'Label',
        'name': 'Name'
    }

    def __init__(self, description=None, label=None, name=None):
        """
        WorkflowWorkflowTask - a model defined in Swagger
        """

        self._description = None
        self._label = None
        self._name = None

        if description is not None:
          self.description = description
        if label is not None:
          self.label = label
        if name is not None:
          self.name = name

    @property
    def description(self):
        """
        Gets the description of this WorkflowWorkflowTask.
        The description of this task instance in the workflow.  

        :return: The description of this WorkflowWorkflowTask.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this WorkflowWorkflowTask.
        The description of this task instance in the workflow.  

        :param description: The description of this WorkflowWorkflowTask.
        :type: str
        """

        self._description = description

    @property
    def label(self):
        """
        Gets the label of this WorkflowWorkflowTask.
        A user defined label identifier of the workflow task used for UI display.  

        :return: The label of this WorkflowWorkflowTask.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this WorkflowWorkflowTask.
        A user defined label identifier of the workflow task used for UI display.  

        :param label: The label of this WorkflowWorkflowTask.
        :type: str
        """

        self._label = label

    @property
    def name(self):
        """
        Gets the name of this WorkflowWorkflowTask.
        The name of the task within the workflow and it must be unique among all WorkflowTasks within a workflow definition. This name serves as the internal unique identifier for the task and is used to pick input and output parameters to feed into other tasks.   

        :return: The name of this WorkflowWorkflowTask.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this WorkflowWorkflowTask.
        The name of the task within the workflow and it must be unique among all WorkflowTasks within a workflow definition. This name serves as the internal unique identifier for the task and is used to pick input and output parameters to feed into other tasks.   

        :param name: The name of this WorkflowWorkflowTask.
        :type: str
        """

        self._name = name

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
        if not isinstance(other, WorkflowWorkflowTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
