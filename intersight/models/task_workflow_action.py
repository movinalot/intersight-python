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


class TaskWorkflowAction(object):
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
        'account': 'IamAccountRef',
        'action': 'str',
        'input_params': 'str',
        'is_dynamic': 'bool',
        'wait_on_duplicate': 'bool',
        'workflow_context': 'str',
        'workflow_file': 'TaskFileDownloadInfo'
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
        'account': 'Account',
        'action': 'Action',
        'input_params': 'InputParams',
        'is_dynamic': 'IsDynamic',
        'wait_on_duplicate': 'WaitOnDuplicate',
        'workflow_context': 'WorkflowContext',
        'workflow_file': 'WorkflowFile'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, domain_group_moid=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, shared_scope=None, tags=None, version_context=None, account=None, action='start', input_params=None, is_dynamic=None, wait_on_duplicate=None, workflow_context=None, workflow_file=None):
        """
        TaskWorkflowAction - a model defined in Swagger
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
        self._account = None
        self._action = None
        self._input_params = None
        self._is_dynamic = None
        self._wait_on_duplicate = None
        self._workflow_context = None
        self._workflow_file = None

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
        if account is not None:
          self.account = account
        if action is not None:
          self.action = action
        if input_params is not None:
          self.input_params = input_params
        if is_dynamic is not None:
          self.is_dynamic = is_dynamic
        if wait_on_duplicate is not None:
          self.wait_on_duplicate = wait_on_duplicate
        if workflow_context is not None:
          self.workflow_context = workflow_context
        if workflow_file is not None:
          self.workflow_file = workflow_file

    @property
    def account_moid(self):
        """
        Gets the account_moid of this TaskWorkflowAction.
        The Account ID for this managed object.  

        :return: The account_moid of this TaskWorkflowAction.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this TaskWorkflowAction.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this TaskWorkflowAction.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this TaskWorkflowAction.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this TaskWorkflowAction.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this TaskWorkflowAction.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this TaskWorkflowAction.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this TaskWorkflowAction.
        The time when this managed object was created.  

        :return: The create_time of this TaskWorkflowAction.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this TaskWorkflowAction.
        The time when this managed object was created.  

        :param create_time: The create_time of this TaskWorkflowAction.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def domain_group_moid(self):
        """
        Gets the domain_group_moid of this TaskWorkflowAction.
        The DomainGroup ID for this managed object.  

        :return: The domain_group_moid of this TaskWorkflowAction.
        :rtype: str
        """
        return self._domain_group_moid

    @domain_group_moid.setter
    def domain_group_moid(self, domain_group_moid):
        """
        Sets the domain_group_moid of this TaskWorkflowAction.
        The DomainGroup ID for this managed object.  

        :param domain_group_moid: The domain_group_moid of this TaskWorkflowAction.
        :type: str
        """

        self._domain_group_moid = domain_group_moid

    @property
    def mod_time(self):
        """
        Gets the mod_time of this TaskWorkflowAction.
        The time when this managed object was last modified.  

        :return: The mod_time of this TaskWorkflowAction.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this TaskWorkflowAction.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this TaskWorkflowAction.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this TaskWorkflowAction.
        The unique identifier of this Managed Object instance.  

        :return: The moid of this TaskWorkflowAction.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this TaskWorkflowAction.
        The unique identifier of this Managed Object instance.  

        :param moid: The moid of this TaskWorkflowAction.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this TaskWorkflowAction.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this TaskWorkflowAction.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this TaskWorkflowAction.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this TaskWorkflowAction.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this TaskWorkflowAction.
        The array of owners which represent effective ownership of this object.   

        :return: The owners of this TaskWorkflowAction.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this TaskWorkflowAction.
        The array of owners which represent effective ownership of this object.   

        :param owners: The owners of this TaskWorkflowAction.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this TaskWorkflowAction.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this TaskWorkflowAction.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this TaskWorkflowAction.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this TaskWorkflowAction.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def shared_scope(self):
        """
        Gets the shared_scope of this TaskWorkflowAction.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :return: The shared_scope of this TaskWorkflowAction.
        :rtype: str
        """
        return self._shared_scope

    @shared_scope.setter
    def shared_scope(self, shared_scope):
        """
        Sets the shared_scope of this TaskWorkflowAction.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :param shared_scope: The shared_scope of this TaskWorkflowAction.
        :type: str
        """

        self._shared_scope = shared_scope

    @property
    def tags(self):
        """
        Gets the tags of this TaskWorkflowAction.
        The array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this TaskWorkflowAction.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this TaskWorkflowAction.
        The array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this TaskWorkflowAction.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this TaskWorkflowAction.
        The versioning info for this managed object.   

        :return: The version_context of this TaskWorkflowAction.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this TaskWorkflowAction.
        The versioning info for this managed object.   

        :param version_context: The version_context of this TaskWorkflowAction.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def account(self):
        """
        Gets the account of this TaskWorkflowAction.

        :return: The account of this TaskWorkflowAction.
        :rtype: IamAccountRef
        """
        return self._account

    @account.setter
    def account(self, account):
        """
        Sets the account of this TaskWorkflowAction.

        :param account: The account of this TaskWorkflowAction.
        :type: IamAccountRef
        """

        self._account = account

    @property
    def action(self):
        """
        Gets the action of this TaskWorkflowAction.
        Action for test workflow.  

        :return: The action of this TaskWorkflowAction.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this TaskWorkflowAction.
        Action for test workflow.  

        :param action: The action of this TaskWorkflowAction.
        :type: str
        """
        allowed_values = ["start", "stop"]
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def input_params(self):
        """
        Gets the input_params of this TaskWorkflowAction.
        Json formatted string input parameters to workflow.  

        :return: The input_params of this TaskWorkflowAction.
        :rtype: str
        """
        return self._input_params

    @input_params.setter
    def input_params(self, input_params):
        """
        Sets the input_params of this TaskWorkflowAction.
        Json formatted string input parameters to workflow.  

        :param input_params: The input_params of this TaskWorkflowAction.
        :type: str
        """

        self._input_params = input_params

    @property
    def is_dynamic(self):
        """
        Gets the is_dynamic of this TaskWorkflowAction.
        When true, this workflow type will be triggered as a dynamic workflow, if not it will be treated as a static workflow.  

        :return: The is_dynamic of this TaskWorkflowAction.
        :rtype: bool
        """
        return self._is_dynamic

    @is_dynamic.setter
    def is_dynamic(self, is_dynamic):
        """
        Sets the is_dynamic of this TaskWorkflowAction.
        When true, this workflow type will be triggered as a dynamic workflow, if not it will be treated as a static workflow.  

        :param is_dynamic: The is_dynamic of this TaskWorkflowAction.
        :type: bool
        """

        self._is_dynamic = is_dynamic

    @property
    def wait_on_duplicate(self):
        """
        Gets the wait_on_duplicate of this TaskWorkflowAction.
        When true, the workflow will wait for previous one to complete before starting a new one.  

        :return: The wait_on_duplicate of this TaskWorkflowAction.
        :rtype: bool
        """
        return self._wait_on_duplicate

    @wait_on_duplicate.setter
    def wait_on_duplicate(self, wait_on_duplicate):
        """
        Sets the wait_on_duplicate of this TaskWorkflowAction.
        When true, the workflow will wait for previous one to complete before starting a new one.  

        :param wait_on_duplicate: The wait_on_duplicate of this TaskWorkflowAction.
        :type: bool
        """

        self._wait_on_duplicate = wait_on_duplicate

    @property
    def workflow_context(self):
        """
        Gets the workflow_context of this TaskWorkflowAction.
        Json formatted string that has the contents of the workflow context used when starting a workflow.  

        :return: The workflow_context of this TaskWorkflowAction.
        :rtype: str
        """
        return self._workflow_context

    @workflow_context.setter
    def workflow_context(self, workflow_context):
        """
        Sets the workflow_context of this TaskWorkflowAction.
        Json formatted string that has the contents of the workflow context used when starting a workflow.  

        :param workflow_context: The workflow_context of this TaskWorkflowAction.
        :type: str
        """

        self._workflow_context = workflow_context

    @property
    def workflow_file(self):
        """
        Gets the workflow_file of this TaskWorkflowAction.
        Path to workflow metadata file that will be published and started.   

        :return: The workflow_file of this TaskWorkflowAction.
        :rtype: TaskFileDownloadInfo
        """
        return self._workflow_file

    @workflow_file.setter
    def workflow_file(self, workflow_file):
        """
        Sets the workflow_file of this TaskWorkflowAction.
        Path to workflow metadata file that will be published and started.   

        :param workflow_file: The workflow_file of this TaskWorkflowAction.
        :type: TaskFileDownloadInfo
        """

        self._workflow_file = workflow_file

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
        if not isinstance(other, TaskWorkflowAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
