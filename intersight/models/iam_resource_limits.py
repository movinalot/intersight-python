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


class IamResourceLimits(object):
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
        'per_account_user_limit': 'int'
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
        'per_account_user_limit': 'PerAccountUserLimit'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, domain_group_moid=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, shared_scope=None, tags=None, version_context=None, account=None, per_account_user_limit=None):
        """
        IamResourceLimits - a model defined in Swagger
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
        self._per_account_user_limit = None

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
        if per_account_user_limit is not None:
          self.per_account_user_limit = per_account_user_limit

    @property
    def account_moid(self):
        """
        Gets the account_moid of this IamResourceLimits.
        The Account ID for this managed object.  

        :return: The account_moid of this IamResourceLimits.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this IamResourceLimits.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this IamResourceLimits.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this IamResourceLimits.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this IamResourceLimits.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this IamResourceLimits.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this IamResourceLimits.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this IamResourceLimits.
        The time when this managed object was created.  

        :return: The create_time of this IamResourceLimits.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this IamResourceLimits.
        The time when this managed object was created.  

        :param create_time: The create_time of this IamResourceLimits.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def domain_group_moid(self):
        """
        Gets the domain_group_moid of this IamResourceLimits.
        The DomainGroup ID for this managed object.  

        :return: The domain_group_moid of this IamResourceLimits.
        :rtype: str
        """
        return self._domain_group_moid

    @domain_group_moid.setter
    def domain_group_moid(self, domain_group_moid):
        """
        Sets the domain_group_moid of this IamResourceLimits.
        The DomainGroup ID for this managed object.  

        :param domain_group_moid: The domain_group_moid of this IamResourceLimits.
        :type: str
        """

        self._domain_group_moid = domain_group_moid

    @property
    def mod_time(self):
        """
        Gets the mod_time of this IamResourceLimits.
        The time when this managed object was last modified.  

        :return: The mod_time of this IamResourceLimits.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this IamResourceLimits.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this IamResourceLimits.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this IamResourceLimits.
        The unique identifier of this Managed Object instance.  

        :return: The moid of this IamResourceLimits.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this IamResourceLimits.
        The unique identifier of this Managed Object instance.  

        :param moid: The moid of this IamResourceLimits.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this IamResourceLimits.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this IamResourceLimits.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this IamResourceLimits.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this IamResourceLimits.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this IamResourceLimits.
        The array of owners which represent effective ownership of this object.   

        :return: The owners of this IamResourceLimits.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this IamResourceLimits.
        The array of owners which represent effective ownership of this object.   

        :param owners: The owners of this IamResourceLimits.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this IamResourceLimits.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this IamResourceLimits.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this IamResourceLimits.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this IamResourceLimits.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def shared_scope(self):
        """
        Gets the shared_scope of this IamResourceLimits.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :return: The shared_scope of this IamResourceLimits.
        :rtype: str
        """
        return self._shared_scope

    @shared_scope.setter
    def shared_scope(self, shared_scope):
        """
        Sets the shared_scope of this IamResourceLimits.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :param shared_scope: The shared_scope of this IamResourceLimits.
        :type: str
        """

        self._shared_scope = shared_scope

    @property
    def tags(self):
        """
        Gets the tags of this IamResourceLimits.
        The array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this IamResourceLimits.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this IamResourceLimits.
        The array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this IamResourceLimits.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this IamResourceLimits.
        The versioning info for this managed object.   

        :return: The version_context of this IamResourceLimits.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this IamResourceLimits.
        The versioning info for this managed object.   

        :param version_context: The version_context of this IamResourceLimits.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def account(self):
        """
        Gets the account of this IamResourceLimits.
        A collection of references to the [iam.Account](mo://iam.Account) Managed Object.  When this managed object is deleted, the referenced [iam.Account](mo://iam.Account) MO unsets its reference to this deleted MO. 

        :return: The account of this IamResourceLimits.
        :rtype: IamAccountRef
        """
        return self._account

    @account.setter
    def account(self, account):
        """
        Sets the account of this IamResourceLimits.
        A collection of references to the [iam.Account](mo://iam.Account) Managed Object.  When this managed object is deleted, the referenced [iam.Account](mo://iam.Account) MO unsets its reference to this deleted MO. 

        :param account: The account of this IamResourceLimits.
        :type: IamAccountRef
        """

        self._account = account

    @property
    def per_account_user_limit(self):
        """
        Gets the per_account_user_limit of this IamResourceLimits.
        The maximum number of users allowed in an account. The default value is 200.   

        :return: The per_account_user_limit of this IamResourceLimits.
        :rtype: int
        """
        return self._per_account_user_limit

    @per_account_user_limit.setter
    def per_account_user_limit(self, per_account_user_limit):
        """
        Sets the per_account_user_limit of this IamResourceLimits.
        The maximum number of users allowed in an account. The default value is 200.   

        :param per_account_user_limit: The per_account_user_limit of this IamResourceLimits.
        :type: int
        """

        self._per_account_user_limit = per_account_user_limit

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
        if not isinstance(other, IamResourceLimits):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
