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


class IamDomainGroup(object):
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
        'name': 'str',
        'partition1': 'int',
        'partition2': 'int',
        'partition3': 'int',
        'partition_key': 'str',
        'usage': 'int'
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
        'name': 'Name',
        'partition1': 'Partition1',
        'partition2': 'Partition2',
        'partition3': 'Partition3',
        'partition_key': 'PartitionKey',
        'usage': 'Usage'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, domain_group_moid=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, shared_scope=None, tags=None, version_context=None, account=None, name=None, partition1=None, partition2=None, partition3=None, partition_key=None, usage=None):
        """
        IamDomainGroup - a model defined in Swagger
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
        self._name = None
        self._partition1 = None
        self._partition2 = None
        self._partition3 = None
        self._partition_key = None
        self._usage = None

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
        if name is not None:
          self.name = name
        if partition1 is not None:
          self.partition1 = partition1
        if partition2 is not None:
          self.partition2 = partition2
        if partition3 is not None:
          self.partition3 = partition3
        if partition_key is not None:
          self.partition_key = partition_key
        if usage is not None:
          self.usage = usage

    @property
    def account_moid(self):
        """
        Gets the account_moid of this IamDomainGroup.
        The Account ID for this managed object.  

        :return: The account_moid of this IamDomainGroup.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this IamDomainGroup.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this IamDomainGroup.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this IamDomainGroup.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this IamDomainGroup.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this IamDomainGroup.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this IamDomainGroup.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this IamDomainGroup.
        The time when this managed object was created.  

        :return: The create_time of this IamDomainGroup.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this IamDomainGroup.
        The time when this managed object was created.  

        :param create_time: The create_time of this IamDomainGroup.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def domain_group_moid(self):
        """
        Gets the domain_group_moid of this IamDomainGroup.
        The DomainGroup ID for this managed object.  

        :return: The domain_group_moid of this IamDomainGroup.
        :rtype: str
        """
        return self._domain_group_moid

    @domain_group_moid.setter
    def domain_group_moid(self, domain_group_moid):
        """
        Sets the domain_group_moid of this IamDomainGroup.
        The DomainGroup ID for this managed object.  

        :param domain_group_moid: The domain_group_moid of this IamDomainGroup.
        :type: str
        """

        self._domain_group_moid = domain_group_moid

    @property
    def mod_time(self):
        """
        Gets the mod_time of this IamDomainGroup.
        The time when this managed object was last modified.  

        :return: The mod_time of this IamDomainGroup.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this IamDomainGroup.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this IamDomainGroup.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this IamDomainGroup.
        The unique identifier of this Managed Object instance.  

        :return: The moid of this IamDomainGroup.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this IamDomainGroup.
        The unique identifier of this Managed Object instance.  

        :param moid: The moid of this IamDomainGroup.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this IamDomainGroup.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this IamDomainGroup.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this IamDomainGroup.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this IamDomainGroup.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this IamDomainGroup.
        The array of owners which represent effective ownership of this object.   

        :return: The owners of this IamDomainGroup.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this IamDomainGroup.
        The array of owners which represent effective ownership of this object.   

        :param owners: The owners of this IamDomainGroup.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this IamDomainGroup.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this IamDomainGroup.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this IamDomainGroup.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this IamDomainGroup.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def shared_scope(self):
        """
        Gets the shared_scope of this IamDomainGroup.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :return: The shared_scope of this IamDomainGroup.
        :rtype: str
        """
        return self._shared_scope

    @shared_scope.setter
    def shared_scope(self, shared_scope):
        """
        Sets the shared_scope of this IamDomainGroup.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :param shared_scope: The shared_scope of this IamDomainGroup.
        :type: str
        """

        self._shared_scope = shared_scope

    @property
    def tags(self):
        """
        Gets the tags of this IamDomainGroup.
        The array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this IamDomainGroup.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this IamDomainGroup.
        The array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this IamDomainGroup.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this IamDomainGroup.
        The versioning info for this managed object.   

        :return: The version_context of this IamDomainGroup.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this IamDomainGroup.
        The versioning info for this managed object.   

        :param version_context: The version_context of this IamDomainGroup.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def account(self):
        """
        Gets the account of this IamDomainGroup.
        A collection of references to the [iam.Account](mo://iam.Account) Managed Object.  When this managed object is deleted, the referenced [iam.Account](mo://iam.Account) MO unsets its reference to this deleted MO. 

        :return: The account of this IamDomainGroup.
        :rtype: IamAccountRef
        """
        return self._account

    @account.setter
    def account(self, account):
        """
        Sets the account of this IamDomainGroup.
        A collection of references to the [iam.Account](mo://iam.Account) Managed Object.  When this managed object is deleted, the referenced [iam.Account](mo://iam.Account) MO unsets its reference to this deleted MO. 

        :param account: The account of this IamDomainGroup.
        :type: IamAccountRef
        """

        self._account = account

    @property
    def name(self):
        """
        Gets the name of this IamDomainGroup.
        The name of the domain-group.   

        :return: The name of this IamDomainGroup.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this IamDomainGroup.
        The name of the domain-group.   

        :param name: The name of this IamDomainGroup.
        :type: str
        """

        self._name = name

    @property
    def partition1(self):
        """
        Gets the partition1 of this IamDomainGroup.
        The partition number domain group related messages are produced for 'Partition1' category service topics.   

        :return: The partition1 of this IamDomainGroup.
        :rtype: int
        """
        return self._partition1

    @partition1.setter
    def partition1(self, partition1):
        """
        Sets the partition1 of this IamDomainGroup.
        The partition number domain group related messages are produced for 'Partition1' category service topics.   

        :param partition1: The partition1 of this IamDomainGroup.
        :type: int
        """

        self._partition1 = partition1

    @property
    def partition2(self):
        """
        Gets the partition2 of this IamDomainGroup.
        In a cloud environment this parameter will indicate to which partition number domain group related messages are produced for 'Partition2' category service topics.   

        :return: The partition2 of this IamDomainGroup.
        :rtype: int
        """
        return self._partition2

    @partition2.setter
    def partition2(self, partition2):
        """
        Sets the partition2 of this IamDomainGroup.
        In a cloud environment this parameter will indicate to which partition number domain group related messages are produced for 'Partition2' category service topics.   

        :param partition2: The partition2 of this IamDomainGroup.
        :type: int
        """

        self._partition2 = partition2

    @property
    def partition3(self):
        """
        Gets the partition3 of this IamDomainGroup.
        In a cloud environment this parameter will indicate to which partition number domain group related messages are produced for 'Partition3' category service topics.   

        :return: The partition3 of this IamDomainGroup.
        :rtype: int
        """
        return self._partition3

    @partition3.setter
    def partition3(self, partition3):
        """
        Sets the partition3 of this IamDomainGroup.
        In a cloud environment this parameter will indicate to which partition number domain group related messages are produced for 'Partition3' category service topics.   

        :param partition3: The partition3 of this IamDomainGroup.
        :type: int
        """

        self._partition3 = partition3

    @property
    def partition_key(self):
        """
        Gets the partition_key of this IamDomainGroup.
        Partition key used for producing messages to Kafka partitions. By default Domain-group id will be used as parition key. For Domain-groups belonging to Early adopters domain-group id will be prefixed with 'H' and used as partition key, such partition key will be treated differently and messages will always be produced to partition 0.   

        :return: The partition_key of this IamDomainGroup.
        :rtype: str
        """
        return self._partition_key

    @partition_key.setter
    def partition_key(self, partition_key):
        """
        Sets the partition_key of this IamDomainGroup.
        Partition key used for producing messages to Kafka partitions. By default Domain-group id will be used as parition key. For Domain-groups belonging to Early adopters domain-group id will be prefixed with 'H' and used as partition key, such partition key will be treated differently and messages will always be produced to partition 0.   

        :param partition_key: The partition_key of this IamDomainGroup.
        :type: str
        """

        self._partition_key = partition_key

    @property
    def usage(self):
        """
        Gets the usage of this IamDomainGroup.
        The number of devices in the domain-group. Device registration notifications are processed to update the usage of the domain-group. The on-boarding account will have multiple domain-groups, and during the device registration least used domain-group will be selected for the device.    

        :return: The usage of this IamDomainGroup.
        :rtype: int
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """
        Sets the usage of this IamDomainGroup.
        The number of devices in the domain-group. Device registration notifications are processed to update the usage of the domain-group. The on-boarding account will have multiple domain-groups, and during the device registration least used domain-group will be selected for the device.    

        :param usage: The usage of this IamDomainGroup.
        :type: int
        """

        self._usage = usage

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
        if not isinstance(other, IamDomainGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
