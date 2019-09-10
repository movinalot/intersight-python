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


class NetworkElementSummary(object):
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
        'admin_inband_interface_state': 'str',
        'device_mo_id': 'str',
        'dn': 'str',
        'fault_summary': 'int',
        'firmware': 'str',
        'inband_ip_address': 'str',
        'inband_ip_gateway': 'str',
        'inband_ip_mask': 'str',
        'inband_vlan': 'int',
        'ipv4_address': 'str',
        'model': 'str',
        'name': 'str',
        'num_ether_ports': 'int',
        'num_ether_ports_configured': 'int',
        'num_ether_ports_link_up': 'int',
        'num_expansion_modules': 'int',
        'num_fc_ports': 'int',
        'num_fc_ports_configured': 'int',
        'num_fc_ports_link_up': 'int',
        'out_of_band_ip_address': 'str',
        'out_of_band_ip_gateway': 'str',
        'out_of_band_ip_mask': 'str',
        'out_of_band_mac': 'str',
        'registered_device': 'AssetDeviceRegistrationRef',
        'revision': 'str',
        'rn': 'str',
        'serial': 'str',
        'source_object_type': 'str',
        'switch_id': 'str',
        'vendor': 'str',
        'version': 'str'
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
        'admin_inband_interface_state': 'AdminInbandInterfaceState',
        'device_mo_id': 'DeviceMoId',
        'dn': 'Dn',
        'fault_summary': 'FaultSummary',
        'firmware': 'Firmware',
        'inband_ip_address': 'InbandIpAddress',
        'inband_ip_gateway': 'InbandIpGateway',
        'inband_ip_mask': 'InbandIpMask',
        'inband_vlan': 'InbandVlan',
        'ipv4_address': 'Ipv4Address',
        'model': 'Model',
        'name': 'Name',
        'num_ether_ports': 'NumEtherPorts',
        'num_ether_ports_configured': 'NumEtherPortsConfigured',
        'num_ether_ports_link_up': 'NumEtherPortsLinkUp',
        'num_expansion_modules': 'NumExpansionModules',
        'num_fc_ports': 'NumFcPorts',
        'num_fc_ports_configured': 'NumFcPortsConfigured',
        'num_fc_ports_link_up': 'NumFcPortsLinkUp',
        'out_of_band_ip_address': 'OutOfBandIpAddress',
        'out_of_band_ip_gateway': 'OutOfBandIpGateway',
        'out_of_band_ip_mask': 'OutOfBandIpMask',
        'out_of_band_mac': 'OutOfBandMac',
        'registered_device': 'RegisteredDevice',
        'revision': 'Revision',
        'rn': 'Rn',
        'serial': 'Serial',
        'source_object_type': 'SourceObjectType',
        'switch_id': 'SwitchId',
        'vendor': 'Vendor',
        'version': 'Version'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, domain_group_moid=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, shared_scope=None, tags=None, version_context=None, admin_inband_interface_state=None, device_mo_id=None, dn=None, fault_summary=None, firmware=None, inband_ip_address=None, inband_ip_gateway=None, inband_ip_mask=None, inband_vlan=None, ipv4_address=None, model=None, name=None, num_ether_ports=None, num_ether_ports_configured=None, num_ether_ports_link_up=None, num_expansion_modules=None, num_fc_ports=None, num_fc_ports_configured=None, num_fc_ports_link_up=None, out_of_band_ip_address=None, out_of_band_ip_gateway=None, out_of_band_ip_mask=None, out_of_band_mac=None, registered_device=None, revision=None, rn=None, serial=None, source_object_type=None, switch_id=None, vendor=None, version=None):
        """
        NetworkElementSummary - a model defined in Swagger
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
        self._admin_inband_interface_state = None
        self._device_mo_id = None
        self._dn = None
        self._fault_summary = None
        self._firmware = None
        self._inband_ip_address = None
        self._inband_ip_gateway = None
        self._inband_ip_mask = None
        self._inband_vlan = None
        self._ipv4_address = None
        self._model = None
        self._name = None
        self._num_ether_ports = None
        self._num_ether_ports_configured = None
        self._num_ether_ports_link_up = None
        self._num_expansion_modules = None
        self._num_fc_ports = None
        self._num_fc_ports_configured = None
        self._num_fc_ports_link_up = None
        self._out_of_band_ip_address = None
        self._out_of_band_ip_gateway = None
        self._out_of_band_ip_mask = None
        self._out_of_band_mac = None
        self._registered_device = None
        self._revision = None
        self._rn = None
        self._serial = None
        self._source_object_type = None
        self._switch_id = None
        self._vendor = None
        self._version = None

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
        if admin_inband_interface_state is not None:
          self.admin_inband_interface_state = admin_inband_interface_state
        if device_mo_id is not None:
          self.device_mo_id = device_mo_id
        if dn is not None:
          self.dn = dn
        if fault_summary is not None:
          self.fault_summary = fault_summary
        if firmware is not None:
          self.firmware = firmware
        if inband_ip_address is not None:
          self.inband_ip_address = inband_ip_address
        if inband_ip_gateway is not None:
          self.inband_ip_gateway = inband_ip_gateway
        if inband_ip_mask is not None:
          self.inband_ip_mask = inband_ip_mask
        if inband_vlan is not None:
          self.inband_vlan = inband_vlan
        if ipv4_address is not None:
          self.ipv4_address = ipv4_address
        if model is not None:
          self.model = model
        if name is not None:
          self.name = name
        if num_ether_ports is not None:
          self.num_ether_ports = num_ether_ports
        if num_ether_ports_configured is not None:
          self.num_ether_ports_configured = num_ether_ports_configured
        if num_ether_ports_link_up is not None:
          self.num_ether_ports_link_up = num_ether_ports_link_up
        if num_expansion_modules is not None:
          self.num_expansion_modules = num_expansion_modules
        if num_fc_ports is not None:
          self.num_fc_ports = num_fc_ports
        if num_fc_ports_configured is not None:
          self.num_fc_ports_configured = num_fc_ports_configured
        if num_fc_ports_link_up is not None:
          self.num_fc_ports_link_up = num_fc_ports_link_up
        if out_of_band_ip_address is not None:
          self.out_of_band_ip_address = out_of_band_ip_address
        if out_of_band_ip_gateway is not None:
          self.out_of_band_ip_gateway = out_of_band_ip_gateway
        if out_of_band_ip_mask is not None:
          self.out_of_band_ip_mask = out_of_band_ip_mask
        if out_of_band_mac is not None:
          self.out_of_band_mac = out_of_band_mac
        if registered_device is not None:
          self.registered_device = registered_device
        if revision is not None:
          self.revision = revision
        if rn is not None:
          self.rn = rn
        if serial is not None:
          self.serial = serial
        if source_object_type is not None:
          self.source_object_type = source_object_type
        if switch_id is not None:
          self.switch_id = switch_id
        if vendor is not None:
          self.vendor = vendor
        if version is not None:
          self.version = version

    @property
    def account_moid(self):
        """
        Gets the account_moid of this NetworkElementSummary.
        The Account ID for this managed object.  

        :return: The account_moid of this NetworkElementSummary.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this NetworkElementSummary.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this NetworkElementSummary.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this NetworkElementSummary.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this NetworkElementSummary.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this NetworkElementSummary.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this NetworkElementSummary.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this NetworkElementSummary.
        The time when this managed object was created.  

        :return: The create_time of this NetworkElementSummary.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this NetworkElementSummary.
        The time when this managed object was created.  

        :param create_time: The create_time of this NetworkElementSummary.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def domain_group_moid(self):
        """
        Gets the domain_group_moid of this NetworkElementSummary.
        The DomainGroup ID for this managed object.  

        :return: The domain_group_moid of this NetworkElementSummary.
        :rtype: str
        """
        return self._domain_group_moid

    @domain_group_moid.setter
    def domain_group_moid(self, domain_group_moid):
        """
        Sets the domain_group_moid of this NetworkElementSummary.
        The DomainGroup ID for this managed object.  

        :param domain_group_moid: The domain_group_moid of this NetworkElementSummary.
        :type: str
        """

        self._domain_group_moid = domain_group_moid

    @property
    def mod_time(self):
        """
        Gets the mod_time of this NetworkElementSummary.
        The time when this managed object was last modified.  

        :return: The mod_time of this NetworkElementSummary.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this NetworkElementSummary.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this NetworkElementSummary.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this NetworkElementSummary.
        The unique identifier of this Managed Object instance.  

        :return: The moid of this NetworkElementSummary.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this NetworkElementSummary.
        The unique identifier of this Managed Object instance.  

        :param moid: The moid of this NetworkElementSummary.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this NetworkElementSummary.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this NetworkElementSummary.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this NetworkElementSummary.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this NetworkElementSummary.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this NetworkElementSummary.
        The array of owners which represent effective ownership of this object.   

        :return: The owners of this NetworkElementSummary.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this NetworkElementSummary.
        The array of owners which represent effective ownership of this object.   

        :param owners: The owners of this NetworkElementSummary.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this NetworkElementSummary.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this NetworkElementSummary.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this NetworkElementSummary.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this NetworkElementSummary.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def shared_scope(self):
        """
        Gets the shared_scope of this NetworkElementSummary.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :return: The shared_scope of this NetworkElementSummary.
        :rtype: str
        """
        return self._shared_scope

    @shared_scope.setter
    def shared_scope(self, shared_scope):
        """
        Sets the shared_scope of this NetworkElementSummary.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :param shared_scope: The shared_scope of this NetworkElementSummary.
        :type: str
        """

        self._shared_scope = shared_scope

    @property
    def tags(self):
        """
        Gets the tags of this NetworkElementSummary.
        The array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this NetworkElementSummary.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this NetworkElementSummary.
        The array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this NetworkElementSummary.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this NetworkElementSummary.
        The versioning info for this managed object.   

        :return: The version_context of this NetworkElementSummary.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this NetworkElementSummary.
        The versioning info for this managed object.   

        :param version_context: The version_context of this NetworkElementSummary.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def admin_inband_interface_state(self):
        """
        Gets the admin_inband_interface_state of this NetworkElementSummary.

        :return: The admin_inband_interface_state of this NetworkElementSummary.
        :rtype: str
        """
        return self._admin_inband_interface_state

    @admin_inband_interface_state.setter
    def admin_inband_interface_state(self, admin_inband_interface_state):
        """
        Sets the admin_inband_interface_state of this NetworkElementSummary.

        :param admin_inband_interface_state: The admin_inband_interface_state of this NetworkElementSummary.
        :type: str
        """

        self._admin_inband_interface_state = admin_inband_interface_state

    @property
    def device_mo_id(self):
        """
        Gets the device_mo_id of this NetworkElementSummary.

        :return: The device_mo_id of this NetworkElementSummary.
        :rtype: str
        """
        return self._device_mo_id

    @device_mo_id.setter
    def device_mo_id(self, device_mo_id):
        """
        Sets the device_mo_id of this NetworkElementSummary.

        :param device_mo_id: The device_mo_id of this NetworkElementSummary.
        :type: str
        """

        self._device_mo_id = device_mo_id

    @property
    def dn(self):
        """
        Gets the dn of this NetworkElementSummary.

        :return: The dn of this NetworkElementSummary.
        :rtype: str
        """
        return self._dn

    @dn.setter
    def dn(self, dn):
        """
        Sets the dn of this NetworkElementSummary.

        :param dn: The dn of this NetworkElementSummary.
        :type: str
        """

        self._dn = dn

    @property
    def fault_summary(self):
        """
        Gets the fault_summary of this NetworkElementSummary.

        :return: The fault_summary of this NetworkElementSummary.
        :rtype: int
        """
        return self._fault_summary

    @fault_summary.setter
    def fault_summary(self, fault_summary):
        """
        Sets the fault_summary of this NetworkElementSummary.

        :param fault_summary: The fault_summary of this NetworkElementSummary.
        :type: int
        """

        self._fault_summary = fault_summary

    @property
    def firmware(self):
        """
        Gets the firmware of this NetworkElementSummary.
        Running firmware information.  

        :return: The firmware of this NetworkElementSummary.
        :rtype: str
        """
        return self._firmware

    @firmware.setter
    def firmware(self, firmware):
        """
        Sets the firmware of this NetworkElementSummary.
        Running firmware information.  

        :param firmware: The firmware of this NetworkElementSummary.
        :type: str
        """

        self._firmware = firmware

    @property
    def inband_ip_address(self):
        """
        Gets the inband_ip_address of this NetworkElementSummary.

        :return: The inband_ip_address of this NetworkElementSummary.
        :rtype: str
        """
        return self._inband_ip_address

    @inband_ip_address.setter
    def inband_ip_address(self, inband_ip_address):
        """
        Sets the inband_ip_address of this NetworkElementSummary.

        :param inband_ip_address: The inband_ip_address of this NetworkElementSummary.
        :type: str
        """

        self._inband_ip_address = inband_ip_address

    @property
    def inband_ip_gateway(self):
        """
        Gets the inband_ip_gateway of this NetworkElementSummary.

        :return: The inband_ip_gateway of this NetworkElementSummary.
        :rtype: str
        """
        return self._inband_ip_gateway

    @inband_ip_gateway.setter
    def inband_ip_gateway(self, inband_ip_gateway):
        """
        Sets the inband_ip_gateway of this NetworkElementSummary.

        :param inband_ip_gateway: The inband_ip_gateway of this NetworkElementSummary.
        :type: str
        """

        self._inband_ip_gateway = inband_ip_gateway

    @property
    def inband_ip_mask(self):
        """
        Gets the inband_ip_mask of this NetworkElementSummary.

        :return: The inband_ip_mask of this NetworkElementSummary.
        :rtype: str
        """
        return self._inband_ip_mask

    @inband_ip_mask.setter
    def inband_ip_mask(self, inband_ip_mask):
        """
        Sets the inband_ip_mask of this NetworkElementSummary.

        :param inband_ip_mask: The inband_ip_mask of this NetworkElementSummary.
        :type: str
        """

        self._inband_ip_mask = inband_ip_mask

    @property
    def inband_vlan(self):
        """
        Gets the inband_vlan of this NetworkElementSummary.

        :return: The inband_vlan of this NetworkElementSummary.
        :rtype: int
        """
        return self._inband_vlan

    @inband_vlan.setter
    def inband_vlan(self, inband_vlan):
        """
        Sets the inband_vlan of this NetworkElementSummary.

        :param inband_vlan: The inband_vlan of this NetworkElementSummary.
        :type: int
        """

        self._inband_vlan = inband_vlan

    @property
    def ipv4_address(self):
        """
        Gets the ipv4_address of this NetworkElementSummary.
        IP version 4 address is saved in this property.  

        :return: The ipv4_address of this NetworkElementSummary.
        :rtype: str
        """
        return self._ipv4_address

    @ipv4_address.setter
    def ipv4_address(self, ipv4_address):
        """
        Sets the ipv4_address of this NetworkElementSummary.
        IP version 4 address is saved in this property.  

        :param ipv4_address: The ipv4_address of this NetworkElementSummary.
        :type: str
        """

        self._ipv4_address = ipv4_address

    @property
    def model(self):
        """
        Gets the model of this NetworkElementSummary.
        This field identifies the model of the given component.  

        :return: The model of this NetworkElementSummary.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """
        Sets the model of this NetworkElementSummary.
        This field identifies the model of the given component.  

        :param model: The model of this NetworkElementSummary.
        :type: str
        """

        self._model = model

    @property
    def name(self):
        """
        Gets the name of this NetworkElementSummary.
        Name of the ElementSummary object is saved in this property.  

        :return: The name of this NetworkElementSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this NetworkElementSummary.
        Name of the ElementSummary object is saved in this property.  

        :param name: The name of this NetworkElementSummary.
        :type: str
        """

        self._name = name

    @property
    def num_ether_ports(self):
        """
        Gets the num_ether_ports of this NetworkElementSummary.
        Total number of Ethernet ports.  

        :return: The num_ether_ports of this NetworkElementSummary.
        :rtype: int
        """
        return self._num_ether_ports

    @num_ether_ports.setter
    def num_ether_ports(self, num_ether_ports):
        """
        Sets the num_ether_ports of this NetworkElementSummary.
        Total number of Ethernet ports.  

        :param num_ether_ports: The num_ether_ports of this NetworkElementSummary.
        :type: int
        """

        self._num_ether_ports = num_ether_ports

    @property
    def num_ether_ports_configured(self):
        """
        Gets the num_ether_ports_configured of this NetworkElementSummary.
        Total number of configured Ethernet ports.  

        :return: The num_ether_ports_configured of this NetworkElementSummary.
        :rtype: int
        """
        return self._num_ether_ports_configured

    @num_ether_ports_configured.setter
    def num_ether_ports_configured(self, num_ether_ports_configured):
        """
        Sets the num_ether_ports_configured of this NetworkElementSummary.
        Total number of configured Ethernet ports.  

        :param num_ether_ports_configured: The num_ether_ports_configured of this NetworkElementSummary.
        :type: int
        """

        self._num_ether_ports_configured = num_ether_ports_configured

    @property
    def num_ether_ports_link_up(self):
        """
        Gets the num_ether_ports_link_up of this NetworkElementSummary.
        Total number of Ethernet ports which are UP.  

        :return: The num_ether_ports_link_up of this NetworkElementSummary.
        :rtype: int
        """
        return self._num_ether_ports_link_up

    @num_ether_ports_link_up.setter
    def num_ether_ports_link_up(self, num_ether_ports_link_up):
        """
        Sets the num_ether_ports_link_up of this NetworkElementSummary.
        Total number of Ethernet ports which are UP.  

        :param num_ether_ports_link_up: The num_ether_ports_link_up of this NetworkElementSummary.
        :type: int
        """

        self._num_ether_ports_link_up = num_ether_ports_link_up

    @property
    def num_expansion_modules(self):
        """
        Gets the num_expansion_modules of this NetworkElementSummary.
        Total number of expansion modules.  

        :return: The num_expansion_modules of this NetworkElementSummary.
        :rtype: int
        """
        return self._num_expansion_modules

    @num_expansion_modules.setter
    def num_expansion_modules(self, num_expansion_modules):
        """
        Sets the num_expansion_modules of this NetworkElementSummary.
        Total number of expansion modules.  

        :param num_expansion_modules: The num_expansion_modules of this NetworkElementSummary.
        :type: int
        """

        self._num_expansion_modules = num_expansion_modules

    @property
    def num_fc_ports(self):
        """
        Gets the num_fc_ports of this NetworkElementSummary.
        Total number of FC ports.  

        :return: The num_fc_ports of this NetworkElementSummary.
        :rtype: int
        """
        return self._num_fc_ports

    @num_fc_ports.setter
    def num_fc_ports(self, num_fc_ports):
        """
        Sets the num_fc_ports of this NetworkElementSummary.
        Total number of FC ports.  

        :param num_fc_ports: The num_fc_ports of this NetworkElementSummary.
        :type: int
        """

        self._num_fc_ports = num_fc_ports

    @property
    def num_fc_ports_configured(self):
        """
        Gets the num_fc_ports_configured of this NetworkElementSummary.
        Total number of configured FC ports.  

        :return: The num_fc_ports_configured of this NetworkElementSummary.
        :rtype: int
        """
        return self._num_fc_ports_configured

    @num_fc_ports_configured.setter
    def num_fc_ports_configured(self, num_fc_ports_configured):
        """
        Sets the num_fc_ports_configured of this NetworkElementSummary.
        Total number of configured FC ports.  

        :param num_fc_ports_configured: The num_fc_ports_configured of this NetworkElementSummary.
        :type: int
        """

        self._num_fc_ports_configured = num_fc_ports_configured

    @property
    def num_fc_ports_link_up(self):
        """
        Gets the num_fc_ports_link_up of this NetworkElementSummary.
        Total number of FC ports which are UP.  

        :return: The num_fc_ports_link_up of this NetworkElementSummary.
        :rtype: int
        """
        return self._num_fc_ports_link_up

    @num_fc_ports_link_up.setter
    def num_fc_ports_link_up(self, num_fc_ports_link_up):
        """
        Sets the num_fc_ports_link_up of this NetworkElementSummary.
        Total number of FC ports which are UP.  

        :param num_fc_ports_link_up: The num_fc_ports_link_up of this NetworkElementSummary.
        :type: int
        """

        self._num_fc_ports_link_up = num_fc_ports_link_up

    @property
    def out_of_band_ip_address(self):
        """
        Gets the out_of_band_ip_address of this NetworkElementSummary.

        :return: The out_of_band_ip_address of this NetworkElementSummary.
        :rtype: str
        """
        return self._out_of_band_ip_address

    @out_of_band_ip_address.setter
    def out_of_band_ip_address(self, out_of_band_ip_address):
        """
        Sets the out_of_band_ip_address of this NetworkElementSummary.

        :param out_of_band_ip_address: The out_of_band_ip_address of this NetworkElementSummary.
        :type: str
        """

        self._out_of_band_ip_address = out_of_band_ip_address

    @property
    def out_of_band_ip_gateway(self):
        """
        Gets the out_of_band_ip_gateway of this NetworkElementSummary.

        :return: The out_of_band_ip_gateway of this NetworkElementSummary.
        :rtype: str
        """
        return self._out_of_band_ip_gateway

    @out_of_band_ip_gateway.setter
    def out_of_band_ip_gateway(self, out_of_band_ip_gateway):
        """
        Sets the out_of_band_ip_gateway of this NetworkElementSummary.

        :param out_of_band_ip_gateway: The out_of_band_ip_gateway of this NetworkElementSummary.
        :type: str
        """

        self._out_of_band_ip_gateway = out_of_band_ip_gateway

    @property
    def out_of_band_ip_mask(self):
        """
        Gets the out_of_band_ip_mask of this NetworkElementSummary.

        :return: The out_of_band_ip_mask of this NetworkElementSummary.
        :rtype: str
        """
        return self._out_of_band_ip_mask

    @out_of_band_ip_mask.setter
    def out_of_band_ip_mask(self, out_of_band_ip_mask):
        """
        Sets the out_of_band_ip_mask of this NetworkElementSummary.

        :param out_of_band_ip_mask: The out_of_band_ip_mask of this NetworkElementSummary.
        :type: str
        """

        self._out_of_band_ip_mask = out_of_band_ip_mask

    @property
    def out_of_band_mac(self):
        """
        Gets the out_of_band_mac of this NetworkElementSummary.

        :return: The out_of_band_mac of this NetworkElementSummary.
        :rtype: str
        """
        return self._out_of_band_mac

    @out_of_band_mac.setter
    def out_of_band_mac(self, out_of_band_mac):
        """
        Sets the out_of_band_mac of this NetworkElementSummary.

        :param out_of_band_mac: The out_of_band_mac of this NetworkElementSummary.
        :type: str
        """

        self._out_of_band_mac = out_of_band_mac

    @property
    def registered_device(self):
        """
        Gets the registered_device of this NetworkElementSummary.
        The Device to which this Managed Object is associated. 

        :return: The registered_device of this NetworkElementSummary.
        :rtype: AssetDeviceRegistrationRef
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """
        Sets the registered_device of this NetworkElementSummary.
        The Device to which this Managed Object is associated. 

        :param registered_device: The registered_device of this NetworkElementSummary.
        :type: AssetDeviceRegistrationRef
        """

        self._registered_device = registered_device

    @property
    def revision(self):
        """
        Gets the revision of this NetworkElementSummary.

        :return: The revision of this NetworkElementSummary.
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """
        Sets the revision of this NetworkElementSummary.

        :param revision: The revision of this NetworkElementSummary.
        :type: str
        """

        self._revision = revision

    @property
    def rn(self):
        """
        Gets the rn of this NetworkElementSummary.

        :return: The rn of this NetworkElementSummary.
        :rtype: str
        """
        return self._rn

    @rn.setter
    def rn(self, rn):
        """
        Sets the rn of this NetworkElementSummary.

        :param rn: The rn of this NetworkElementSummary.
        :type: str
        """

        self._rn = rn

    @property
    def serial(self):
        """
        Gets the serial of this NetworkElementSummary.
        This field identifies the serial of the given component.  

        :return: The serial of this NetworkElementSummary.
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """
        Sets the serial of this NetworkElementSummary.
        This field identifies the serial of the given component.  

        :param serial: The serial of this NetworkElementSummary.
        :type: str
        """

        self._serial = serial

    @property
    def source_object_type(self):
        """
        Gets the source_object_type of this NetworkElementSummary.
        Specifies the source object type for View MO.  

        :return: The source_object_type of this NetworkElementSummary.
        :rtype: str
        """
        return self._source_object_type

    @source_object_type.setter
    def source_object_type(self, source_object_type):
        """
        Sets the source_object_type of this NetworkElementSummary.
        Specifies the source object type for View MO.  

        :param source_object_type: The source_object_type of this NetworkElementSummary.
        :type: str
        """

        self._source_object_type = source_object_type

    @property
    def switch_id(self):
        """
        Gets the switch_id of this NetworkElementSummary.

        :return: The switch_id of this NetworkElementSummary.
        :rtype: str
        """
        return self._switch_id

    @switch_id.setter
    def switch_id(self, switch_id):
        """
        Sets the switch_id of this NetworkElementSummary.

        :param switch_id: The switch_id of this NetworkElementSummary.
        :type: str
        """

        self._switch_id = switch_id

    @property
    def vendor(self):
        """
        Gets the vendor of this NetworkElementSummary.
        This field identifies the vendor of the given component.  

        :return: The vendor of this NetworkElementSummary.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """
        Sets the vendor of this NetworkElementSummary.
        This field identifies the vendor of the given component.  

        :param vendor: The vendor of this NetworkElementSummary.
        :type: str
        """

        self._vendor = vendor

    @property
    def version(self):
        """
        Gets the version of this NetworkElementSummary.
        Version holds the firmware version related information.   

        :return: The version of this NetworkElementSummary.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this NetworkElementSummary.
        Version holds the firmware version related information.   

        :param version: The version of this NetworkElementSummary.
        :type: str
        """

        self._version = version

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
        if not isinstance(other, NetworkElementSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
