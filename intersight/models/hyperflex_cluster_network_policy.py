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


class HyperflexClusterNetworkPolicy(object):
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
        'description': 'str',
        'name': 'str',
        'cluster_profiles': 'list[HyperflexClusterProfileRef]',
        'jumbo_frame': 'bool',
        'kvm_ip_range': 'HyperflexIpAddrRange',
        'mac_prefix_range': 'HyperflexMacAddrPrefixRange',
        'mgmt_vlan': 'HyperflexNamedVlan',
        'organization': 'IamAccountRef',
        'uplink_speed': 'str',
        'vm_migration_vlan': 'HyperflexNamedVlan',
        'vm_network_vlans': 'list[HyperflexNamedVlan]'
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
        'description': 'Description',
        'name': 'Name',
        'cluster_profiles': 'ClusterProfiles',
        'jumbo_frame': 'JumboFrame',
        'kvm_ip_range': 'KvmIpRange',
        'mac_prefix_range': 'MacPrefixRange',
        'mgmt_vlan': 'MgmtVlan',
        'organization': 'Organization',
        'uplink_speed': 'UplinkSpeed',
        'vm_migration_vlan': 'VmMigrationVlan',
        'vm_network_vlans': 'VmNetworkVlans'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, domain_group_moid=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, shared_scope=None, tags=None, version_context=None, description=None, name=None, cluster_profiles=None, jumbo_frame=None, kvm_ip_range=None, mac_prefix_range=None, mgmt_vlan=None, organization=None, uplink_speed='default', vm_migration_vlan=None, vm_network_vlans=None):
        """
        HyperflexClusterNetworkPolicy - a model defined in Swagger
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
        self._description = None
        self._name = None
        self._cluster_profiles = None
        self._jumbo_frame = None
        self._kvm_ip_range = None
        self._mac_prefix_range = None
        self._mgmt_vlan = None
        self._organization = None
        self._uplink_speed = None
        self._vm_migration_vlan = None
        self._vm_network_vlans = None

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
        if description is not None:
          self.description = description
        if name is not None:
          self.name = name
        if cluster_profiles is not None:
          self.cluster_profiles = cluster_profiles
        if jumbo_frame is not None:
          self.jumbo_frame = jumbo_frame
        if kvm_ip_range is not None:
          self.kvm_ip_range = kvm_ip_range
        if mac_prefix_range is not None:
          self.mac_prefix_range = mac_prefix_range
        if mgmt_vlan is not None:
          self.mgmt_vlan = mgmt_vlan
        if organization is not None:
          self.organization = organization
        if uplink_speed is not None:
          self.uplink_speed = uplink_speed
        if vm_migration_vlan is not None:
          self.vm_migration_vlan = vm_migration_vlan
        if vm_network_vlans is not None:
          self.vm_network_vlans = vm_network_vlans

    @property
    def account_moid(self):
        """
        Gets the account_moid of this HyperflexClusterNetworkPolicy.
        The Account ID for this managed object.  

        :return: The account_moid of this HyperflexClusterNetworkPolicy.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this HyperflexClusterNetworkPolicy.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this HyperflexClusterNetworkPolicy.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this HyperflexClusterNetworkPolicy.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this HyperflexClusterNetworkPolicy.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this HyperflexClusterNetworkPolicy.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this HyperflexClusterNetworkPolicy.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this HyperflexClusterNetworkPolicy.
        The time when this managed object was created.  

        :return: The create_time of this HyperflexClusterNetworkPolicy.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this HyperflexClusterNetworkPolicy.
        The time when this managed object was created.  

        :param create_time: The create_time of this HyperflexClusterNetworkPolicy.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def domain_group_moid(self):
        """
        Gets the domain_group_moid of this HyperflexClusterNetworkPolicy.
        The DomainGroup ID for this managed object.  

        :return: The domain_group_moid of this HyperflexClusterNetworkPolicy.
        :rtype: str
        """
        return self._domain_group_moid

    @domain_group_moid.setter
    def domain_group_moid(self, domain_group_moid):
        """
        Sets the domain_group_moid of this HyperflexClusterNetworkPolicy.
        The DomainGroup ID for this managed object.  

        :param domain_group_moid: The domain_group_moid of this HyperflexClusterNetworkPolicy.
        :type: str
        """

        self._domain_group_moid = domain_group_moid

    @property
    def mod_time(self):
        """
        Gets the mod_time of this HyperflexClusterNetworkPolicy.
        The time when this managed object was last modified.  

        :return: The mod_time of this HyperflexClusterNetworkPolicy.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this HyperflexClusterNetworkPolicy.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this HyperflexClusterNetworkPolicy.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this HyperflexClusterNetworkPolicy.
        The unique identifier of this Managed Object instance.  

        :return: The moid of this HyperflexClusterNetworkPolicy.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this HyperflexClusterNetworkPolicy.
        The unique identifier of this Managed Object instance.  

        :param moid: The moid of this HyperflexClusterNetworkPolicy.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this HyperflexClusterNetworkPolicy.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this HyperflexClusterNetworkPolicy.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this HyperflexClusterNetworkPolicy.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this HyperflexClusterNetworkPolicy.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this HyperflexClusterNetworkPolicy.
        The array of owners which represent effective ownership of this object.   

        :return: The owners of this HyperflexClusterNetworkPolicy.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this HyperflexClusterNetworkPolicy.
        The array of owners which represent effective ownership of this object.   

        :param owners: The owners of this HyperflexClusterNetworkPolicy.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this HyperflexClusterNetworkPolicy.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this HyperflexClusterNetworkPolicy.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this HyperflexClusterNetworkPolicy.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this HyperflexClusterNetworkPolicy.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def shared_scope(self):
        """
        Gets the shared_scope of this HyperflexClusterNetworkPolicy.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :return: The shared_scope of this HyperflexClusterNetworkPolicy.
        :rtype: str
        """
        return self._shared_scope

    @shared_scope.setter
    def shared_scope(self, shared_scope):
        """
        Sets the shared_scope of this HyperflexClusterNetworkPolicy.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :param shared_scope: The shared_scope of this HyperflexClusterNetworkPolicy.
        :type: str
        """

        self._shared_scope = shared_scope

    @property
    def tags(self):
        """
        Gets the tags of this HyperflexClusterNetworkPolicy.
        The array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this HyperflexClusterNetworkPolicy.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this HyperflexClusterNetworkPolicy.
        The array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this HyperflexClusterNetworkPolicy.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this HyperflexClusterNetworkPolicy.
        The versioning info for this managed object.   

        :return: The version_context of this HyperflexClusterNetworkPolicy.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this HyperflexClusterNetworkPolicy.
        The versioning info for this managed object.   

        :param version_context: The version_context of this HyperflexClusterNetworkPolicy.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def description(self):
        """
        Gets the description of this HyperflexClusterNetworkPolicy.
        Description of the policy.  

        :return: The description of this HyperflexClusterNetworkPolicy.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this HyperflexClusterNetworkPolicy.
        Description of the policy.  

        :param description: The description of this HyperflexClusterNetworkPolicy.
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """
        Gets the name of this HyperflexClusterNetworkPolicy.
        Name of the concrete policy.   

        :return: The name of this HyperflexClusterNetworkPolicy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this HyperflexClusterNetworkPolicy.
        Name of the concrete policy.   

        :param name: The name of this HyperflexClusterNetworkPolicy.
        :type: str
        """

        self._name = name

    @property
    def cluster_profiles(self):
        """
        Gets the cluster_profiles of this HyperflexClusterNetworkPolicy.
        List of cluster profiles using this policy. 

        :return: The cluster_profiles of this HyperflexClusterNetworkPolicy.
        :rtype: list[HyperflexClusterProfileRef]
        """
        return self._cluster_profiles

    @cluster_profiles.setter
    def cluster_profiles(self, cluster_profiles):
        """
        Sets the cluster_profiles of this HyperflexClusterNetworkPolicy.
        List of cluster profiles using this policy. 

        :param cluster_profiles: The cluster_profiles of this HyperflexClusterNetworkPolicy.
        :type: list[HyperflexClusterProfileRef]
        """

        self._cluster_profiles = cluster_profiles

    @property
    def jumbo_frame(self):
        """
        Gets the jumbo_frame of this HyperflexClusterNetworkPolicy.
        Enable or disable jumbo frames.  

        :return: The jumbo_frame of this HyperflexClusterNetworkPolicy.
        :rtype: bool
        """
        return self._jumbo_frame

    @jumbo_frame.setter
    def jumbo_frame(self, jumbo_frame):
        """
        Sets the jumbo_frame of this HyperflexClusterNetworkPolicy.
        Enable or disable jumbo frames.  

        :param jumbo_frame: The jumbo_frame of this HyperflexClusterNetworkPolicy.
        :type: bool
        """

        self._jumbo_frame = jumbo_frame

    @property
    def kvm_ip_range(self):
        """
        Gets the kvm_ip_range of this HyperflexClusterNetworkPolicy.
        The Out-of-band KVM IP range.  Configures the service profiles to use IP addresses within this range for setting the KVM IP of a server.   

        :return: The kvm_ip_range of this HyperflexClusterNetworkPolicy.
        :rtype: HyperflexIpAddrRange
        """
        return self._kvm_ip_range

    @kvm_ip_range.setter
    def kvm_ip_range(self, kvm_ip_range):
        """
        Sets the kvm_ip_range of this HyperflexClusterNetworkPolicy.
        The Out-of-band KVM IP range.  Configures the service profiles to use IP addresses within this range for setting the KVM IP of a server.   

        :param kvm_ip_range: The kvm_ip_range of this HyperflexClusterNetworkPolicy.
        :type: HyperflexIpAddrRange
        """

        self._kvm_ip_range = kvm_ip_range

    @property
    def mac_prefix_range(self):
        """
        Gets the mac_prefix_range of this HyperflexClusterNetworkPolicy.
        The MAC address prefix range for configuring vNICs.  Configures the service profiles to use MAC address prefixes within this range for setting the MAC address of server vNICs.   

        :return: The mac_prefix_range of this HyperflexClusterNetworkPolicy.
        :rtype: HyperflexMacAddrPrefixRange
        """
        return self._mac_prefix_range

    @mac_prefix_range.setter
    def mac_prefix_range(self, mac_prefix_range):
        """
        Sets the mac_prefix_range of this HyperflexClusterNetworkPolicy.
        The MAC address prefix range for configuring vNICs.  Configures the service profiles to use MAC address prefixes within this range for setting the MAC address of server vNICs.   

        :param mac_prefix_range: The mac_prefix_range of this HyperflexClusterNetworkPolicy.
        :type: HyperflexMacAddrPrefixRange
        """

        self._mac_prefix_range = mac_prefix_range

    @property
    def mgmt_vlan(self):
        """
        Gets the mgmt_vlan of this HyperflexClusterNetworkPolicy.
        The VLAN for the management network.  

        :return: The mgmt_vlan of this HyperflexClusterNetworkPolicy.
        :rtype: HyperflexNamedVlan
        """
        return self._mgmt_vlan

    @mgmt_vlan.setter
    def mgmt_vlan(self, mgmt_vlan):
        """
        Sets the mgmt_vlan of this HyperflexClusterNetworkPolicy.
        The VLAN for the management network.  

        :param mgmt_vlan: The mgmt_vlan of this HyperflexClusterNetworkPolicy.
        :type: HyperflexNamedVlan
        """

        self._mgmt_vlan = mgmt_vlan

    @property
    def organization(self):
        """
        Gets the organization of this HyperflexClusterNetworkPolicy.
        Relationship to the Organization that owns the Managed Object. 

        :return: The organization of this HyperflexClusterNetworkPolicy.
        :rtype: IamAccountRef
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """
        Sets the organization of this HyperflexClusterNetworkPolicy.
        Relationship to the Organization that owns the Managed Object. 

        :param organization: The organization of this HyperflexClusterNetworkPolicy.
        :type: IamAccountRef
        """

        self._organization = organization

    @property
    def uplink_speed(self):
        """
        Gets the uplink_speed of this HyperflexClusterNetworkPolicy.
        Link speed of the server adapter port to the upstream switch. When the policy is attached to a cluster profile with EDGE management platform, the uplink speed can be '1G' or '10G'. When the policy is attached to a cluster profile with Fabric Interconnect management platform, the uplink speed can be 'default' only.  

        :return: The uplink_speed of this HyperflexClusterNetworkPolicy.
        :rtype: str
        """
        return self._uplink_speed

    @uplink_speed.setter
    def uplink_speed(self, uplink_speed):
        """
        Sets the uplink_speed of this HyperflexClusterNetworkPolicy.
        Link speed of the server adapter port to the upstream switch. When the policy is attached to a cluster profile with EDGE management platform, the uplink speed can be '1G' or '10G'. When the policy is attached to a cluster profile with Fabric Interconnect management platform, the uplink speed can be 'default' only.  

        :param uplink_speed: The uplink_speed of this HyperflexClusterNetworkPolicy.
        :type: str
        """
        allowed_values = ["default", "1G", "10G"]
        if uplink_speed not in allowed_values:
            raise ValueError(
                "Invalid value for `uplink_speed` ({0}), must be one of {1}"
                .format(uplink_speed, allowed_values)
            )

        self._uplink_speed = uplink_speed

    @property
    def vm_migration_vlan(self):
        """
        Gets the vm_migration_vlan of this HyperflexClusterNetworkPolicy.
        The VM migration VLAN.  This VLAN is used for transfering VMs from one host to another during operations such a cluster upgrade.   

        :return: The vm_migration_vlan of this HyperflexClusterNetworkPolicy.
        :rtype: HyperflexNamedVlan
        """
        return self._vm_migration_vlan

    @vm_migration_vlan.setter
    def vm_migration_vlan(self, vm_migration_vlan):
        """
        Sets the vm_migration_vlan of this HyperflexClusterNetworkPolicy.
        The VM migration VLAN.  This VLAN is used for transfering VMs from one host to another during operations such a cluster upgrade.   

        :param vm_migration_vlan: The vm_migration_vlan of this HyperflexClusterNetworkPolicy.
        :type: HyperflexNamedVlan
        """

        self._vm_migration_vlan = vm_migration_vlan

    @property
    def vm_network_vlans(self):
        """
        Gets the vm_network_vlans of this HyperflexClusterNetworkPolicy.
        The VLANs for VM traffic.  Guest VMs hosted on the HyperFlex cluster use these VLANs for network communication.    

        :return: The vm_network_vlans of this HyperflexClusterNetworkPolicy.
        :rtype: list[HyperflexNamedVlan]
        """
        return self._vm_network_vlans

    @vm_network_vlans.setter
    def vm_network_vlans(self, vm_network_vlans):
        """
        Sets the vm_network_vlans of this HyperflexClusterNetworkPolicy.
        The VLANs for VM traffic.  Guest VMs hosted on the HyperFlex cluster use these VLANs for network communication.    

        :param vm_network_vlans: The vm_network_vlans of this HyperflexClusterNetworkPolicy.
        :type: list[HyperflexNamedVlan]
        """

        self._vm_network_vlans = vm_network_vlans

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
        if not isinstance(other, HyperflexClusterNetworkPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
