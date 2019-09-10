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


class WorkflowBatchApiExecutor(object):
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
        'account_moid': 'str',
        'ancestors': 'list[MoBaseMoRef]',
        'create_time': 'datetime',
        'domain_group_moid': 'str',
        'mod_time': 'datetime',
        'moid': 'str',
        'object_type': 'str',
        'owners': 'list[str]',
        'parent': 'MoBaseMoRef',
        'shared_scope': 'str',
        'tags': 'list[MoTag]',
        'version_context': 'MoVersionContext',
        'batch': 'list[WorkflowApi]',
        'constraints': 'str',
        'description': 'str',
        'name': 'str',
        'output': 'object',
        'skip_on_condition': 'str',
        'task_definition': 'WorkflowTaskDefinitionRef'
    }

    attribute_map = {
        'account_moid': 'AccountMoid',
        'ancestors': 'Ancestors',
        'create_time': 'CreateTime',
        'domain_group_moid': 'DomainGroupMoid',
        'mod_time': 'ModTime',
        'moid': 'Moid',
        'object_type': 'ObjectType',
        'owners': 'Owners',
        'parent': 'Parent',
        'shared_scope': 'SharedScope',
        'tags': 'Tags',
        'version_context': 'VersionContext',
        'batch': 'Batch',
        'constraints': 'Constraints',
        'description': 'Description',
        'name': 'Name',
        'output': 'Output',
        'skip_on_condition': 'SkipOnCondition',
        'task_definition': 'TaskDefinition'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, domain_group_moid=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, shared_scope=None, tags=None, version_context=None, batch=None, constraints=None, description=None, name=None, output=None, skip_on_condition=None, task_definition=None):
        """
        WorkflowBatchApiExecutor - a model defined in Swagger
        """

        self._account_moid = None
        self._ancestors = None
        self._create_time = None
        self._domain_group_moid = None
        self._mod_time = None
        self._moid = None
        self._object_type = None
        self._owners = None
        self._parent = None
        self._shared_scope = None
        self._tags = None
        self._version_context = None
        self._batch = None
        self._constraints = None
        self._description = None
        self._name = None
        self._output = None
        self._skip_on_condition = None
        self._task_definition = None

        if account_moid is not None:
          self.account_moid = account_moid
        if ancestors is not None:
          self.ancestors = ancestors
        if create_time is not None:
          self.create_time = create_time
        if domain_group_moid is not None:
          self.domain_group_moid = domain_group_moid
        if mod_time is not None:
          self.mod_time = mod_time
        if moid is not None:
          self.moid = moid
        if object_type is not None:
          self.object_type = object_type
        if owners is not None:
          self.owners = owners
        if parent is not None:
          self.parent = parent
        if shared_scope is not None:
          self.shared_scope = shared_scope
        if tags is not None:
          self.tags = tags
        if version_context is not None:
          self.version_context = version_context
        if batch is not None:
          self.batch = batch
        if constraints is not None:
          self.constraints = constraints
        if description is not None:
          self.description = description
        if name is not None:
          self.name = name
        if output is not None:
          self.output = output
        if skip_on_condition is not None:
          self.skip_on_condition = skip_on_condition
        if task_definition is not None:
          self.task_definition = task_definition

    @property
    def account_moid(self):
        """
        Gets the account_moid of this WorkflowBatchApiExecutor.
        The Account ID for this managed object.  

        :return: The account_moid of this WorkflowBatchApiExecutor.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this WorkflowBatchApiExecutor.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this WorkflowBatchApiExecutor.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this WorkflowBatchApiExecutor.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this WorkflowBatchApiExecutor.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this WorkflowBatchApiExecutor.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this WorkflowBatchApiExecutor.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this WorkflowBatchApiExecutor.
        The time when this managed object was created.  

        :return: The create_time of this WorkflowBatchApiExecutor.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this WorkflowBatchApiExecutor.
        The time when this managed object was created.  

        :param create_time: The create_time of this WorkflowBatchApiExecutor.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def domain_group_moid(self):
        """
        Gets the domain_group_moid of this WorkflowBatchApiExecutor.
        The DomainGroup ID for this managed object.  

        :return: The domain_group_moid of this WorkflowBatchApiExecutor.
        :rtype: str
        """
        return self._domain_group_moid

    @domain_group_moid.setter
    def domain_group_moid(self, domain_group_moid):
        """
        Sets the domain_group_moid of this WorkflowBatchApiExecutor.
        The DomainGroup ID for this managed object.  

        :param domain_group_moid: The domain_group_moid of this WorkflowBatchApiExecutor.
        :type: str
        """

        self._domain_group_moid = domain_group_moid

    @property
    def mod_time(self):
        """
        Gets the mod_time of this WorkflowBatchApiExecutor.
        The time when this managed object was last modified.  

        :return: The mod_time of this WorkflowBatchApiExecutor.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this WorkflowBatchApiExecutor.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this WorkflowBatchApiExecutor.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this WorkflowBatchApiExecutor.
        The unique identifier of this Managed Object instance.  

        :return: The moid of this WorkflowBatchApiExecutor.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this WorkflowBatchApiExecutor.
        The unique identifier of this Managed Object instance.  

        :param moid: The moid of this WorkflowBatchApiExecutor.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this WorkflowBatchApiExecutor.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this WorkflowBatchApiExecutor.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this WorkflowBatchApiExecutor.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this WorkflowBatchApiExecutor.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this WorkflowBatchApiExecutor.
        The array of owners which represent effective ownership of this object.   

        :return: The owners of this WorkflowBatchApiExecutor.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this WorkflowBatchApiExecutor.
        The array of owners which represent effective ownership of this object.   

        :param owners: The owners of this WorkflowBatchApiExecutor.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this WorkflowBatchApiExecutor.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this WorkflowBatchApiExecutor.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this WorkflowBatchApiExecutor.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this WorkflowBatchApiExecutor.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def shared_scope(self):
        """
        Gets the shared_scope of this WorkflowBatchApiExecutor.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :return: The shared_scope of this WorkflowBatchApiExecutor.
        :rtype: str
        """
        return self._shared_scope

    @shared_scope.setter
    def shared_scope(self, shared_scope):
        """
        Sets the shared_scope of this WorkflowBatchApiExecutor.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :param shared_scope: The shared_scope of this WorkflowBatchApiExecutor.
        :type: str
        """

        self._shared_scope = shared_scope

    @property
    def tags(self):
        """
        Gets the tags of this WorkflowBatchApiExecutor.
        The array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this WorkflowBatchApiExecutor.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this WorkflowBatchApiExecutor.
        The array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this WorkflowBatchApiExecutor.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this WorkflowBatchApiExecutor.
        The versioning info for this managed object.   

        :return: The version_context of this WorkflowBatchApiExecutor.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this WorkflowBatchApiExecutor.
        The versioning info for this managed object.   

        :param version_context: The version_context of this WorkflowBatchApiExecutor.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def batch(self):
        """
        Gets the batch of this WorkflowBatchApiExecutor.
        Intersight Orchestrator supports one or a batch of APIs to be executed as part of a task execution.  The batch cannot be empty.   

        :return: The batch of this WorkflowBatchApiExecutor.
        :rtype: list[WorkflowApi]
        """
        return self._batch

    @batch.setter
    def batch(self, batch):
        """
        Sets the batch of this WorkflowBatchApiExecutor.
        Intersight Orchestrator supports one or a batch of APIs to be executed as part of a task execution.  The batch cannot be empty.   

        :param batch: The batch of this WorkflowBatchApiExecutor.
        :type: list[WorkflowApi]
        """

        self._batch = batch

    @property
    def constraints(self):
        """
        Gets the constraints of this WorkflowBatchApiExecutor.
        Enter the constraints on when this task should match against the task definition.   

        :return: The constraints of this WorkflowBatchApiExecutor.
        :rtype: str
        """
        return self._constraints

    @constraints.setter
    def constraints(self, constraints):
        """
        Sets the constraints of this WorkflowBatchApiExecutor.
        Enter the constraints on when this task should match against the task definition.   

        :param constraints: The constraints of this WorkflowBatchApiExecutor.
        :type: str
        """

        self._constraints = constraints

    @property
    def description(self):
        """
        Gets the description of this WorkflowBatchApiExecutor.
        A detailed description about the batch APIs.   

        :return: The description of this WorkflowBatchApiExecutor.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this WorkflowBatchApiExecutor.
        A detailed description about the batch APIs.   

        :param description: The description of this WorkflowBatchApiExecutor.
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """
        Gets the name of this WorkflowBatchApiExecutor.
        Name for the batch API task.   

        :return: The name of this WorkflowBatchApiExecutor.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this WorkflowBatchApiExecutor.
        Name for the batch API task.   

        :param name: The name of this WorkflowBatchApiExecutor.
        :type: str
        """

        self._name = name

    @property
    def output(self):
        """
        Gets the output of this WorkflowBatchApiExecutor.
        Intersight Orchestrator allows the extraction of required values from API responses using the API response grammar. These extracted values can be mapped to task output parameters defined in task definition.  The mapping of API output parameters to the task output parameters is provided as JSON in this property.   

        :return: The output of this WorkflowBatchApiExecutor.
        :rtype: object
        """
        return self._output

    @output.setter
    def output(self, output):
        """
        Sets the output of this WorkflowBatchApiExecutor.
        Intersight Orchestrator allows the extraction of required values from API responses using the API response grammar. These extracted values can be mapped to task output parameters defined in task definition.  The mapping of API output parameters to the task output parameters is provided as JSON in this property.   

        :param output: The output of this WorkflowBatchApiExecutor.
        :type: object
        """

        self._output = output

    @property
    def skip_on_condition(self):
        """
        Gets the skip_on_condition of this WorkflowBatchApiExecutor.
        The skip expression, if provided, allows the batch API executor to skip the task execution when the given expression evaluates to true.  The expression is given as such a golang template that has to be evaluated to a final content true/false. The expression is an optional and in case not provided, the API will always be executed.    

        :return: The skip_on_condition of this WorkflowBatchApiExecutor.
        :rtype: str
        """
        return self._skip_on_condition

    @skip_on_condition.setter
    def skip_on_condition(self, skip_on_condition):
        """
        Sets the skip_on_condition of this WorkflowBatchApiExecutor.
        The skip expression, if provided, allows the batch API executor to skip the task execution when the given expression evaluates to true.  The expression is given as such a golang template that has to be evaluated to a final content true/false. The expression is an optional and in case not provided, the API will always be executed.    

        :param skip_on_condition: The skip_on_condition of this WorkflowBatchApiExecutor.
        :type: str
        """

        self._skip_on_condition = skip_on_condition

    @property
    def task_definition(self):
        """
        Gets the task_definition of this WorkflowBatchApiExecutor.
        The interface task definition for which this batch API is one of the implementation. 

        :return: The task_definition of this WorkflowBatchApiExecutor.
        :rtype: WorkflowTaskDefinitionRef
        """
        return self._task_definition

    @task_definition.setter
    def task_definition(self, task_definition):
        """
        Sets the task_definition of this WorkflowBatchApiExecutor.
        The interface task definition for which this batch API is one of the implementation. 

        :param task_definition: The task_definition of this WorkflowBatchApiExecutor.
        :type: WorkflowTaskDefinitionRef
        """

        self._task_definition = task_definition

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
        if not isinstance(other, WorkflowBatchApiExecutor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other