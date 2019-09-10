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


class StorageSnapshotSchedule(object):
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
        'frequency': 'str',
        'name': 'str',
        'protection_group': 'StorageProtectionGroupRef',
        'retention_time': 'str',
        'snapshot_time': 'str',
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
        'frequency': 'Frequency',
        'name': 'Name',
        'protection_group': 'ProtectionGroup',
        'retention_time': 'RetentionTime',
        'snapshot_time': 'SnapshotTime',
        'storage_array': 'StorageArray'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, domain_group_moid=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, shared_scope=None, tags=None, version_context=None, frequency=None, name=None, protection_group=None, retention_time=None, snapshot_time=None, storage_array=None):
        """
        StorageSnapshotSchedule - a model defined in Swagger
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
        self._frequency = None
        self._name = None
        self._protection_group = None
        self._retention_time = None
        self._snapshot_time = None
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
        if frequency is not None:
          self.frequency = frequency
        if name is not None:
          self.name = name
        if protection_group is not None:
          self.protection_group = protection_group
        if retention_time is not None:
          self.retention_time = retention_time
        if snapshot_time is not None:
          self.snapshot_time = snapshot_time
        if storage_array is not None:
          self.storage_array = storage_array

    @property
    def account_moid(self):
        """
        Gets the account_moid of this StorageSnapshotSchedule.
        The Account ID for this managed object.  

        :return: The account_moid of this StorageSnapshotSchedule.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this StorageSnapshotSchedule.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this StorageSnapshotSchedule.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this StorageSnapshotSchedule.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this StorageSnapshotSchedule.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this StorageSnapshotSchedule.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this StorageSnapshotSchedule.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this StorageSnapshotSchedule.
        The time when this managed object was created.  

        :return: The create_time of this StorageSnapshotSchedule.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this StorageSnapshotSchedule.
        The time when this managed object was created.  

        :param create_time: The create_time of this StorageSnapshotSchedule.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def domain_group_moid(self):
        """
        Gets the domain_group_moid of this StorageSnapshotSchedule.
        The DomainGroup ID for this managed object.  

        :return: The domain_group_moid of this StorageSnapshotSchedule.
        :rtype: str
        """
        return self._domain_group_moid

    @domain_group_moid.setter
    def domain_group_moid(self, domain_group_moid):
        """
        Sets the domain_group_moid of this StorageSnapshotSchedule.
        The DomainGroup ID for this managed object.  

        :param domain_group_moid: The domain_group_moid of this StorageSnapshotSchedule.
        :type: str
        """

        self._domain_group_moid = domain_group_moid

    @property
    def mod_time(self):
        """
        Gets the mod_time of this StorageSnapshotSchedule.
        The time when this managed object was last modified.  

        :return: The mod_time of this StorageSnapshotSchedule.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this StorageSnapshotSchedule.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this StorageSnapshotSchedule.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this StorageSnapshotSchedule.
        The unique identifier of this Managed Object instance.  

        :return: The moid of this StorageSnapshotSchedule.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this StorageSnapshotSchedule.
        The unique identifier of this Managed Object instance.  

        :param moid: The moid of this StorageSnapshotSchedule.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this StorageSnapshotSchedule.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this StorageSnapshotSchedule.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this StorageSnapshotSchedule.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this StorageSnapshotSchedule.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this StorageSnapshotSchedule.
        The array of owners which represent effective ownership of this object.   

        :return: The owners of this StorageSnapshotSchedule.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this StorageSnapshotSchedule.
        The array of owners which represent effective ownership of this object.   

        :param owners: The owners of this StorageSnapshotSchedule.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this StorageSnapshotSchedule.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this StorageSnapshotSchedule.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this StorageSnapshotSchedule.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this StorageSnapshotSchedule.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def shared_scope(self):
        """
        Gets the shared_scope of this StorageSnapshotSchedule.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :return: The shared_scope of this StorageSnapshotSchedule.
        :rtype: str
        """
        return self._shared_scope

    @shared_scope.setter
    def shared_scope(self, shared_scope):
        """
        Sets the shared_scope of this StorageSnapshotSchedule.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :param shared_scope: The shared_scope of this StorageSnapshotSchedule.
        :type: str
        """

        self._shared_scope = shared_scope

    @property
    def tags(self):
        """
        Gets the tags of this StorageSnapshotSchedule.
        The array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this StorageSnapshotSchedule.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this StorageSnapshotSchedule.
        The array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this StorageSnapshotSchedule.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this StorageSnapshotSchedule.
        The versioning info for this managed object.   

        :return: The version_context of this StorageSnapshotSchedule.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this StorageSnapshotSchedule.
        The versioning info for this managed object.   

        :param version_context: The version_context of this StorageSnapshotSchedule.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def frequency(self):
        """
        Gets the frequency of this StorageSnapshotSchedule.
        Snapshot frequency. It is an interval on which snapshot is set to trigger on source array. Examples:     PT2H, Snapshot is performed for every 2 hours.     P4D, Snapshot is scheduled for every 4 days.     PT2H34M56.123S is 2 hours, 34 minutes, 56 seconds and 123 milliseconds.   

        :return: The frequency of this StorageSnapshotSchedule.
        :rtype: str
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """
        Sets the frequency of this StorageSnapshotSchedule.
        Snapshot frequency. It is an interval on which snapshot is set to trigger on source array. Examples:     PT2H, Snapshot is performed for every 2 hours.     P4D, Snapshot is scheduled for every 4 days.     PT2H34M56.123S is 2 hours, 34 minutes, 56 seconds and 123 milliseconds.   

        :param frequency: The frequency of this StorageSnapshotSchedule.
        :type: str
        """

        self._frequency = frequency

    @property
    def name(self):
        """
        Gets the name of this StorageSnapshotSchedule.
        Name of the snapshot schedule.  

        :return: The name of this StorageSnapshotSchedule.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this StorageSnapshotSchedule.
        Name of the snapshot schedule.  

        :param name: The name of this StorageSnapshotSchedule.
        :type: str
        """

        self._name = name

    @property
    def protection_group(self):
        """
        Gets the protection_group of this StorageSnapshotSchedule.
        Protection group relationship object. 

        :return: The protection_group of this StorageSnapshotSchedule.
        :rtype: StorageProtectionGroupRef
        """
        return self._protection_group

    @protection_group.setter
    def protection_group(self, protection_group):
        """
        Sets the protection_group of this StorageSnapshotSchedule.
        Protection group relationship object. 

        :param protection_group: The protection_group of this StorageSnapshotSchedule.
        :type: StorageProtectionGroupRef
        """

        self._protection_group = protection_group

    @property
    def retention_time(self):
        """
        Gets the retention_time of this StorageSnapshotSchedule.
        Duration to keep the snapshots on the source array. Once the period expires, system deletes the snapshot automatically from source array. Examples: P200D,  200 days. PT2H34M56.123S, 2 hours, 34 minutes, 56 seconds and 123 milliseconds.   

        :return: The retention_time of this StorageSnapshotSchedule.
        :rtype: str
        """
        return self._retention_time

    @retention_time.setter
    def retention_time(self, retention_time):
        """
        Sets the retention_time of this StorageSnapshotSchedule.
        Duration to keep the snapshots on the source array. Once the period expires, system deletes the snapshot automatically from source array. Examples: P200D,  200 days. PT2H34M56.123S, 2 hours, 34 minutes, 56 seconds and 123 milliseconds.   

        :param retention_time: The retention_time of this StorageSnapshotSchedule.
        :type: str
        """

        self._retention_time = retention_time

    @property
    def snapshot_time(self):
        """
        Gets the snapshot_time of this StorageSnapshotSchedule.
        Preferred time of the day to capture the snapshot. it is applicable only if the frequency is set for a day or more. Format: hh:mm:ss Example: 08:30:00, Snapshot is set for 08:30 AM.    

        :return: The snapshot_time of this StorageSnapshotSchedule.
        :rtype: str
        """
        return self._snapshot_time

    @snapshot_time.setter
    def snapshot_time(self, snapshot_time):
        """
        Sets the snapshot_time of this StorageSnapshotSchedule.
        Preferred time of the day to capture the snapshot. it is applicable only if the frequency is set for a day or more. Format: hh:mm:ss Example: 08:30:00, Snapshot is set for 08:30 AM.    

        :param snapshot_time: The snapshot_time of this StorageSnapshotSchedule.
        :type: str
        """

        self._snapshot_time = snapshot_time

    @property
    def storage_array(self):
        """
        Gets the storage_array of this StorageSnapshotSchedule.
        Storage array managed object. 

        :return: The storage_array of this StorageSnapshotSchedule.
        :rtype: StorageGenericArrayRef
        """
        return self._storage_array

    @storage_array.setter
    def storage_array(self, storage_array):
        """
        Sets the storage_array of this StorageSnapshotSchedule.
        Storage array managed object. 

        :param storage_array: The storage_array of this StorageSnapshotSchedule.
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
        if not isinstance(other, StorageSnapshotSchedule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
