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


class StorageProtectionGroup(object):
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
        'name': 'str',
        'prefix': 'str',
        'replication_enabled': 'bool',
        'snapshot_enabled': 'bool',
        'storage_array': 'StorageGenericArrayRef'
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
        'name': 'Name',
        'prefix': 'Prefix',
        'replication_enabled': 'ReplicationEnabled',
        'snapshot_enabled': 'SnapshotEnabled',
        'storage_array': 'StorageArray'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, domain_group_moid=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, shared_scope=None, tags=None, version_context=None, name=None, prefix=None, replication_enabled=None, snapshot_enabled=None, storage_array=None):
        """
        StorageProtectionGroup - a model defined in Swagger
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
        self._name = None
        self._prefix = None
        self._replication_enabled = None
        self._snapshot_enabled = None
        self._storage_array = None

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
        if name is not None:
          self.name = name
        if prefix is not None:
          self.prefix = prefix
        if replication_enabled is not None:
          self.replication_enabled = replication_enabled
        if snapshot_enabled is not None:
          self.snapshot_enabled = snapshot_enabled
        if storage_array is not None:
          self.storage_array = storage_array

    @property
    def account_moid(self):
        """
        Gets the account_moid of this StorageProtectionGroup.
        The Account ID for this managed object.  

        :return: The account_moid of this StorageProtectionGroup.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this StorageProtectionGroup.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this StorageProtectionGroup.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this StorageProtectionGroup.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this StorageProtectionGroup.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this StorageProtectionGroup.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this StorageProtectionGroup.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this StorageProtectionGroup.
        The time when this managed object was created.  

        :return: The create_time of this StorageProtectionGroup.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this StorageProtectionGroup.
        The time when this managed object was created.  

        :param create_time: The create_time of this StorageProtectionGroup.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def domain_group_moid(self):
        """
        Gets the domain_group_moid of this StorageProtectionGroup.
        The DomainGroup ID for this managed object.  

        :return: The domain_group_moid of this StorageProtectionGroup.
        :rtype: str
        """
        return self._domain_group_moid

    @domain_group_moid.setter
    def domain_group_moid(self, domain_group_moid):
        """
        Sets the domain_group_moid of this StorageProtectionGroup.
        The DomainGroup ID for this managed object.  

        :param domain_group_moid: The domain_group_moid of this StorageProtectionGroup.
        :type: str
        """

        self._domain_group_moid = domain_group_moid

    @property
    def mod_time(self):
        """
        Gets the mod_time of this StorageProtectionGroup.
        The time when this managed object was last modified.  

        :return: The mod_time of this StorageProtectionGroup.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this StorageProtectionGroup.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this StorageProtectionGroup.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this StorageProtectionGroup.
        The unique identifier of this Managed Object instance.  

        :return: The moid of this StorageProtectionGroup.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this StorageProtectionGroup.
        The unique identifier of this Managed Object instance.  

        :param moid: The moid of this StorageProtectionGroup.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this StorageProtectionGroup.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this StorageProtectionGroup.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this StorageProtectionGroup.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this StorageProtectionGroup.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this StorageProtectionGroup.
        The array of owners which represent effective ownership of this object.   

        :return: The owners of this StorageProtectionGroup.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this StorageProtectionGroup.
        The array of owners which represent effective ownership of this object.   

        :param owners: The owners of this StorageProtectionGroup.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this StorageProtectionGroup.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this StorageProtectionGroup.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this StorageProtectionGroup.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this StorageProtectionGroup.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def shared_scope(self):
        """
        Gets the shared_scope of this StorageProtectionGroup.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :return: The shared_scope of this StorageProtectionGroup.
        :rtype: str
        """
        return self._shared_scope

    @shared_scope.setter
    def shared_scope(self, shared_scope):
        """
        Sets the shared_scope of this StorageProtectionGroup.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :param shared_scope: The shared_scope of this StorageProtectionGroup.
        :type: str
        """

        self._shared_scope = shared_scope

    @property
    def tags(self):
        """
        Gets the tags of this StorageProtectionGroup.
        The array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this StorageProtectionGroup.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this StorageProtectionGroup.
        The array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this StorageProtectionGroup.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this StorageProtectionGroup.
        The versioning info for this managed object.   

        :return: The version_context of this StorageProtectionGroup.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this StorageProtectionGroup.
        The versioning info for this managed object.   

        :param version_context: The version_context of this StorageProtectionGroup.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def name(self):
        """
        Gets the name of this StorageProtectionGroup.
        Name of the protection Group.  

        :return: The name of this StorageProtectionGroup.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this StorageProtectionGroup.
        Name of the protection Group.  

        :param name: The name of this StorageProtectionGroup.
        :type: str
        """

        self._name = name

    @property
    def prefix(self):
        """
        Gets the prefix of this StorageProtectionGroup.
        Prefix used for all generated snapshots from the protection group.  

        :return: The prefix of this StorageProtectionGroup.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """
        Sets the prefix of this StorageProtectionGroup.
        Prefix used for all generated snapshots from the protection group.  

        :param prefix: The prefix of this StorageProtectionGroup.
        :type: str
        """

        self._prefix = prefix

    @property
    def replication_enabled(self):
        """
        Gets the replication_enabled of this StorageProtectionGroup.
        Flag to determine if the replication is enabled. Snapshots are created on target array if the flag is set.  

        :return: The replication_enabled of this StorageProtectionGroup.
        :rtype: bool
        """
        return self._replication_enabled

    @replication_enabled.setter
    def replication_enabled(self, replication_enabled):
        """
        Sets the replication_enabled of this StorageProtectionGroup.
        Flag to determine if the replication is enabled. Snapshots are created on target array if the flag is set.  

        :param replication_enabled: The replication_enabled of this StorageProtectionGroup.
        :type: bool
        """

        self._replication_enabled = replication_enabled

    @property
    def snapshot_enabled(self):
        """
        Gets the snapshot_enabled of this StorageProtectionGroup.
        Flag to determine if the snapshot is enabled. Snapshots are created on local array if the flag is set.   

        :return: The snapshot_enabled of this StorageProtectionGroup.
        :rtype: bool
        """
        return self._snapshot_enabled

    @snapshot_enabled.setter
    def snapshot_enabled(self, snapshot_enabled):
        """
        Sets the snapshot_enabled of this StorageProtectionGroup.
        Flag to determine if the snapshot is enabled. Snapshots are created on local array if the flag is set.   

        :param snapshot_enabled: The snapshot_enabled of this StorageProtectionGroup.
        :type: bool
        """

        self._snapshot_enabled = snapshot_enabled

    @property
    def storage_array(self):
        """
        Gets the storage_array of this StorageProtectionGroup.
        Storage array managed object. 

        :return: The storage_array of this StorageProtectionGroup.
        :rtype: StorageGenericArrayRef
        """
        return self._storage_array

    @storage_array.setter
    def storage_array(self, storage_array):
        """
        Sets the storage_array of this StorageProtectionGroup.
        Storage array managed object. 

        :param storage_array: The storage_array of this StorageProtectionGroup.
        :type: StorageGenericArrayRef
        """

        self._storage_array = storage_array

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
        if not isinstance(other, StorageProtectionGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other