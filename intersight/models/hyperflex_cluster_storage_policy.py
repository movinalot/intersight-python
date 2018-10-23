# coding: utf-8

"""
    Intersight REST API

    This is Intersight REST API 

    OpenAPI spec version: 1.0.9-228
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class HyperflexClusterStoragePolicy(object):
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
        'mod_time': 'datetime',
        'moid': 'str',
        'object_type': 'str',
        'owners': 'list[str]',
        'parent': 'MoBaseMoRef',
        'tags': 'list[MoTag]',
        'version_context': 'MoVersionContext',
        'description': 'str',
        'name': 'str',
        'cluster_profiles': 'list[HyperflexClusterProfileRef]',
        'disk_partition_cleanup': 'bool',
        'logical_avalability_zone_config': 'HyperflexLogicalAvailabilityZone',
        'organization': 'IamAccountRef',
        'vdi_optimization': 'bool'
    }

    attribute_map = {
        'account_moid': 'AccountMoid',
        'ancestors': 'Ancestors',
        'create_time': 'CreateTime',
        'mod_time': 'ModTime',
        'moid': 'Moid',
        'object_type': 'ObjectType',
        'owners': 'Owners',
        'parent': 'Parent',
        'tags': 'Tags',
        'version_context': 'VersionContext',
        'description': 'Description',
        'name': 'Name',
        'cluster_profiles': 'ClusterProfiles',
        'disk_partition_cleanup': 'DiskPartitionCleanup',
        'logical_avalability_zone_config': 'LogicalAvalabilityZoneConfig',
        'organization': 'Organization',
        'vdi_optimization': 'VdiOptimization'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, version_context=None, description=None, name=None, cluster_profiles=None, disk_partition_cleanup=None, logical_avalability_zone_config=None, organization=None, vdi_optimization=None):
        """
        HyperflexClusterStoragePolicy - a model defined in Swagger
        """

        self._account_moid = None
        self._ancestors = None
        self._create_time = None
        self._mod_time = None
        self._moid = None
        self._object_type = None
        self._owners = None
        self._parent = None
        self._tags = None
        self._version_context = None
        self._description = None
        self._name = None
        self._cluster_profiles = None
        self._disk_partition_cleanup = None
        self._logical_avalability_zone_config = None
        self._organization = None
        self._vdi_optimization = None

        if account_moid is not None:
          self.account_moid = account_moid
        if ancestors is not None:
          self.ancestors = ancestors
        if create_time is not None:
          self.create_time = create_time
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
        if tags is not None:
          self.tags = tags
        if version_context is not None:
          self.version_context = version_context
        if description is not None:
          self.description = description
        if name is not None:
          self.name = name
        if cluster_profiles is not None:
          self.cluster_profiles = cluster_profiles
        if disk_partition_cleanup is not None:
          self.disk_partition_cleanup = disk_partition_cleanup
        if logical_avalability_zone_config is not None:
          self.logical_avalability_zone_config = logical_avalability_zone_config
        if organization is not None:
          self.organization = organization
        if vdi_optimization is not None:
          self.vdi_optimization = vdi_optimization

    @property
    def account_moid(self):
        """
        Gets the account_moid of this HyperflexClusterStoragePolicy.
        The Account ID for this managed object.  

        :return: The account_moid of this HyperflexClusterStoragePolicy.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this HyperflexClusterStoragePolicy.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this HyperflexClusterStoragePolicy.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this HyperflexClusterStoragePolicy.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this HyperflexClusterStoragePolicy.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this HyperflexClusterStoragePolicy.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this HyperflexClusterStoragePolicy.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this HyperflexClusterStoragePolicy.
        The time when this managed object was created.  

        :return: The create_time of this HyperflexClusterStoragePolicy.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this HyperflexClusterStoragePolicy.
        The time when this managed object was created.  

        :param create_time: The create_time of this HyperflexClusterStoragePolicy.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this HyperflexClusterStoragePolicy.
        The time when this managed object was last modified.  

        :return: The mod_time of this HyperflexClusterStoragePolicy.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this HyperflexClusterStoragePolicy.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this HyperflexClusterStoragePolicy.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this HyperflexClusterStoragePolicy.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this HyperflexClusterStoragePolicy.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this HyperflexClusterStoragePolicy.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this HyperflexClusterStoragePolicy.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this HyperflexClusterStoragePolicy.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this HyperflexClusterStoragePolicy.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this HyperflexClusterStoragePolicy.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this HyperflexClusterStoragePolicy.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this HyperflexClusterStoragePolicy.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this HyperflexClusterStoragePolicy.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this HyperflexClusterStoragePolicy.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this HyperflexClusterStoragePolicy.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this HyperflexClusterStoragePolicy.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this HyperflexClusterStoragePolicy.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this HyperflexClusterStoragePolicy.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this HyperflexClusterStoragePolicy.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this HyperflexClusterStoragePolicy.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this HyperflexClusterStoragePolicy.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this HyperflexClusterStoragePolicy.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this HyperflexClusterStoragePolicy.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this HyperflexClusterStoragePolicy.
        The versioning info for this managed object   

        :return: The version_context of this HyperflexClusterStoragePolicy.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this HyperflexClusterStoragePolicy.
        The versioning info for this managed object   

        :param version_context: The version_context of this HyperflexClusterStoragePolicy.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def description(self):
        """
        Gets the description of this HyperflexClusterStoragePolicy.
        Description of the policy.  

        :return: The description of this HyperflexClusterStoragePolicy.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this HyperflexClusterStoragePolicy.
        Description of the policy.  

        :param description: The description of this HyperflexClusterStoragePolicy.
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """
        Gets the name of this HyperflexClusterStoragePolicy.
        Name of the policy.   

        :return: The name of this HyperflexClusterStoragePolicy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this HyperflexClusterStoragePolicy.
        Name of the policy.   

        :param name: The name of this HyperflexClusterStoragePolicy.
        :type: str
        """

        self._name = name

    @property
    def cluster_profiles(self):
        """
        Gets the cluster_profiles of this HyperflexClusterStoragePolicy.
        List of cluster profiles using this policy 

        :return: The cluster_profiles of this HyperflexClusterStoragePolicy.
        :rtype: list[HyperflexClusterProfileRef]
        """
        return self._cluster_profiles

    @cluster_profiles.setter
    def cluster_profiles(self, cluster_profiles):
        """
        Sets the cluster_profiles of this HyperflexClusterStoragePolicy.
        List of cluster profiles using this policy 

        :param cluster_profiles: The cluster_profiles of this HyperflexClusterStoragePolicy.
        :type: list[HyperflexClusterProfileRef]
        """

        self._cluster_profiles = cluster_profiles

    @property
    def disk_partition_cleanup(self):
        """
        Gets the disk_partition_cleanup of this HyperflexClusterStoragePolicy.
        If enabled, formats existing disk partitions (destroys all user data)  

        :return: The disk_partition_cleanup of this HyperflexClusterStoragePolicy.
        :rtype: bool
        """
        return self._disk_partition_cleanup

    @disk_partition_cleanup.setter
    def disk_partition_cleanup(self, disk_partition_cleanup):
        """
        Sets the disk_partition_cleanup of this HyperflexClusterStoragePolicy.
        If enabled, formats existing disk partitions (destroys all user data)  

        :param disk_partition_cleanup: The disk_partition_cleanup of this HyperflexClusterStoragePolicy.
        :type: bool
        """

        self._disk_partition_cleanup = disk_partition_cleanup

    @property
    def logical_avalability_zone_config(self):
        """
        Gets the logical_avalability_zone_config of this HyperflexClusterStoragePolicy.
        Enable or disable Logical Availability Zones (LAZ). If enabled, HyperFlex Data Platform automatically selects and groups nodes into different availability zones. For HyperFlex Data Platform versions prior to 3.0 release, this setting does not apply. For HyperFlex Data Platform versions 3.0 or higher, this setting is only applicable to Fabric Interconnect attached HyperFlex systems with 8 or more converged nodes.  

        :return: The logical_avalability_zone_config of this HyperflexClusterStoragePolicy.
        :rtype: HyperflexLogicalAvailabilityZone
        """
        return self._logical_avalability_zone_config

    @logical_avalability_zone_config.setter
    def logical_avalability_zone_config(self, logical_avalability_zone_config):
        """
        Sets the logical_avalability_zone_config of this HyperflexClusterStoragePolicy.
        Enable or disable Logical Availability Zones (LAZ). If enabled, HyperFlex Data Platform automatically selects and groups nodes into different availability zones. For HyperFlex Data Platform versions prior to 3.0 release, this setting does not apply. For HyperFlex Data Platform versions 3.0 or higher, this setting is only applicable to Fabric Interconnect attached HyperFlex systems with 8 or more converged nodes.  

        :param logical_avalability_zone_config: The logical_avalability_zone_config of this HyperflexClusterStoragePolicy.
        :type: HyperflexLogicalAvailabilityZone
        """

        self._logical_avalability_zone_config = logical_avalability_zone_config

    @property
    def organization(self):
        """
        Gets the organization of this HyperflexClusterStoragePolicy.
        Organization 

        :return: The organization of this HyperflexClusterStoragePolicy.
        :rtype: IamAccountRef
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """
        Sets the organization of this HyperflexClusterStoragePolicy.
        Organization 

        :param organization: The organization of this HyperflexClusterStoragePolicy.
        :type: IamAccountRef
        """

        self._organization = organization

    @property
    def vdi_optimization(self):
        """
        Gets the vdi_optimization of this HyperflexClusterStoragePolicy.
        Enable or disable VDI optimization (hybrid HyperFlex systems only)   

        :return: The vdi_optimization of this HyperflexClusterStoragePolicy.
        :rtype: bool
        """
        return self._vdi_optimization

    @vdi_optimization.setter
    def vdi_optimization(self, vdi_optimization):
        """
        Sets the vdi_optimization of this HyperflexClusterStoragePolicy.
        Enable or disable VDI optimization (hybrid HyperFlex systems only)   

        :param vdi_optimization: The vdi_optimization of this HyperflexClusterStoragePolicy.
        :type: bool
        """

        self._vdi_optimization = vdi_optimization

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
        if not isinstance(other, HyperflexClusterStoragePolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
