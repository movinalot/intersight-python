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


class EquipmentFanModule(object):
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
        'device_mo_id': 'str',
        'dn': 'str',
        'rn': 'str',
        'model': 'str',
        'revision': 'str',
        'serial': 'str',
        'vendor': 'str',
        'compute_rack_unit': 'ComputeRackUnitRef',
        'description': 'str',
        'equipment_chassis': 'EquipmentChassisRef',
        'equipment_rack_enclosure': 'EquipmentRackEnclosureRef',
        'fans': 'list[EquipmentFanRef]',
        'module_id': 'int',
        'network_element': 'NetworkElementRef',
        'oper_state': 'str',
        'part_number': 'str',
        'pid': 'str',
        'presence': 'str',
        'registered_device': 'AssetDeviceRegistrationRef',
        'sku': 'str',
        'tray_id': 'int',
        'vid': 'str'
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
        'device_mo_id': 'DeviceMoId',
        'dn': 'Dn',
        'rn': 'Rn',
        'model': 'Model',
        'revision': 'Revision',
        'serial': 'Serial',
        'vendor': 'Vendor',
        'compute_rack_unit': 'ComputeRackUnit',
        'description': 'Description',
        'equipment_chassis': 'EquipmentChassis',
        'equipment_rack_enclosure': 'EquipmentRackEnclosure',
        'fans': 'Fans',
        'module_id': 'ModuleId',
        'network_element': 'NetworkElement',
        'oper_state': 'OperState',
        'part_number': 'PartNumber',
        'pid': 'Pid',
        'presence': 'Presence',
        'registered_device': 'RegisteredDevice',
        'sku': 'Sku',
        'tray_id': 'TrayId',
        'vid': 'Vid'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, domain_group_moid=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, shared_scope=None, tags=None, version_context=None, device_mo_id=None, dn=None, rn=None, model=None, revision=None, serial=None, vendor=None, compute_rack_unit=None, description=None, equipment_chassis=None, equipment_rack_enclosure=None, fans=None, module_id=None, network_element=None, oper_state=None, part_number=None, pid=None, presence=None, registered_device=None, sku=None, tray_id=None, vid=None):
        """
        EquipmentFanModule - a model defined in Swagger
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
        self._device_mo_id = None
        self._dn = None
        self._rn = None
        self._model = None
        self._revision = None
        self._serial = None
        self._vendor = None
        self._compute_rack_unit = None
        self._description = None
        self._equipment_chassis = None
        self._equipment_rack_enclosure = None
        self._fans = None
        self._module_id = None
        self._network_element = None
        self._oper_state = None
        self._part_number = None
        self._pid = None
        self._presence = None
        self._registered_device = None
        self._sku = None
        self._tray_id = None
        self._vid = None

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
        if device_mo_id is not None:
          self.device_mo_id = device_mo_id
        if dn is not None:
          self.dn = dn
        if rn is not None:
          self.rn = rn
        if model is not None:
          self.model = model
        if revision is not None:
          self.revision = revision
        if serial is not None:
          self.serial = serial
        if vendor is not None:
          self.vendor = vendor
        if compute_rack_unit is not None:
          self.compute_rack_unit = compute_rack_unit
        if description is not None:
          self.description = description
        if equipment_chassis is not None:
          self.equipment_chassis = equipment_chassis
        if equipment_rack_enclosure is not None:
          self.equipment_rack_enclosure = equipment_rack_enclosure
        if fans is not None:
          self.fans = fans
        if module_id is not None:
          self.module_id = module_id
        if network_element is not None:
          self.network_element = network_element
        if oper_state is not None:
          self.oper_state = oper_state
        if part_number is not None:
          self.part_number = part_number
        if pid is not None:
          self.pid = pid
        if presence is not None:
          self.presence = presence
        if registered_device is not None:
          self.registered_device = registered_device
        if sku is not None:
          self.sku = sku
        if tray_id is not None:
          self.tray_id = tray_id
        if vid is not None:
          self.vid = vid

    @property
    def account_moid(self):
        """
        Gets the account_moid of this EquipmentFanModule.
        The Account ID for this managed object.  

        :return: The account_moid of this EquipmentFanModule.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this EquipmentFanModule.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this EquipmentFanModule.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this EquipmentFanModule.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this EquipmentFanModule.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this EquipmentFanModule.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this EquipmentFanModule.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this EquipmentFanModule.
        The time when this managed object was created.  

        :return: The create_time of this EquipmentFanModule.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this EquipmentFanModule.
        The time when this managed object was created.  

        :param create_time: The create_time of this EquipmentFanModule.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def domain_group_moid(self):
        """
        Gets the domain_group_moid of this EquipmentFanModule.
        The DomainGroup ID for this managed object.  

        :return: The domain_group_moid of this EquipmentFanModule.
        :rtype: str
        """
        return self._domain_group_moid

    @domain_group_moid.setter
    def domain_group_moid(self, domain_group_moid):
        """
        Sets the domain_group_moid of this EquipmentFanModule.
        The DomainGroup ID for this managed object.  

        :param domain_group_moid: The domain_group_moid of this EquipmentFanModule.
        :type: str
        """

        self._domain_group_moid = domain_group_moid

    @property
    def mod_time(self):
        """
        Gets the mod_time of this EquipmentFanModule.
        The time when this managed object was last modified.  

        :return: The mod_time of this EquipmentFanModule.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this EquipmentFanModule.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this EquipmentFanModule.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this EquipmentFanModule.
        The unique identifier of this Managed Object instance.  

        :return: The moid of this EquipmentFanModule.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this EquipmentFanModule.
        The unique identifier of this Managed Object instance.  

        :param moid: The moid of this EquipmentFanModule.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this EquipmentFanModule.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this EquipmentFanModule.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this EquipmentFanModule.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this EquipmentFanModule.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this EquipmentFanModule.
        The array of owners which represent effective ownership of this object.   

        :return: The owners of this EquipmentFanModule.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this EquipmentFanModule.
        The array of owners which represent effective ownership of this object.   

        :param owners: The owners of this EquipmentFanModule.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this EquipmentFanModule.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this EquipmentFanModule.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this EquipmentFanModule.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this EquipmentFanModule.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def shared_scope(self):
        """
        Gets the shared_scope of this EquipmentFanModule.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :return: The shared_scope of this EquipmentFanModule.
        :rtype: str
        """
        return self._shared_scope

    @shared_scope.setter
    def shared_scope(self, shared_scope):
        """
        Sets the shared_scope of this EquipmentFanModule.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :param shared_scope: The shared_scope of this EquipmentFanModule.
        :type: str
        """

        self._shared_scope = shared_scope

    @property
    def tags(self):
        """
        Gets the tags of this EquipmentFanModule.
        The array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this EquipmentFanModule.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this EquipmentFanModule.
        The array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this EquipmentFanModule.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this EquipmentFanModule.
        The versioning info for this managed object.   

        :return: The version_context of this EquipmentFanModule.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this EquipmentFanModule.
        The versioning info for this managed object.   

        :param version_context: The version_context of this EquipmentFanModule.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def device_mo_id(self):
        """
        Gets the device_mo_id of this EquipmentFanModule.

        :return: The device_mo_id of this EquipmentFanModule.
        :rtype: str
        """
        return self._device_mo_id

    @device_mo_id.setter
    def device_mo_id(self, device_mo_id):
        """
        Sets the device_mo_id of this EquipmentFanModule.

        :param device_mo_id: The device_mo_id of this EquipmentFanModule.
        :type: str
        """

        self._device_mo_id = device_mo_id

    @property
    def dn(self):
        """
        Gets the dn of this EquipmentFanModule.

        :return: The dn of this EquipmentFanModule.
        :rtype: str
        """
        return self._dn

    @dn.setter
    def dn(self, dn):
        """
        Sets the dn of this EquipmentFanModule.

        :param dn: The dn of this EquipmentFanModule.
        :type: str
        """

        self._dn = dn

    @property
    def rn(self):
        """
        Gets the rn of this EquipmentFanModule.

        :return: The rn of this EquipmentFanModule.
        :rtype: str
        """
        return self._rn

    @rn.setter
    def rn(self, rn):
        """
        Sets the rn of this EquipmentFanModule.

        :param rn: The rn of this EquipmentFanModule.
        :type: str
        """

        self._rn = rn

    @property
    def model(self):
        """
        Gets the model of this EquipmentFanModule.
        This field identifies the model of the given component.  

        :return: The model of this EquipmentFanModule.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """
        Sets the model of this EquipmentFanModule.
        This field identifies the model of the given component.  

        :param model: The model of this EquipmentFanModule.
        :type: str
        """

        self._model = model

    @property
    def revision(self):
        """
        Gets the revision of this EquipmentFanModule.

        :return: The revision of this EquipmentFanModule.
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """
        Sets the revision of this EquipmentFanModule.

        :param revision: The revision of this EquipmentFanModule.
        :type: str
        """

        self._revision = revision

    @property
    def serial(self):
        """
        Gets the serial of this EquipmentFanModule.
        This field identifies the serial of the given component.  

        :return: The serial of this EquipmentFanModule.
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """
        Sets the serial of this EquipmentFanModule.
        This field identifies the serial of the given component.  

        :param serial: The serial of this EquipmentFanModule.
        :type: str
        """

        self._serial = serial

    @property
    def vendor(self):
        """
        Gets the vendor of this EquipmentFanModule.
        This field identifies the vendor of the given component.   

        :return: The vendor of this EquipmentFanModule.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """
        Sets the vendor of this EquipmentFanModule.
        This field identifies the vendor of the given component.   

        :param vendor: The vendor of this EquipmentFanModule.
        :type: str
        """

        self._vendor = vendor

    @property
    def compute_rack_unit(self):
        """
        Gets the compute_rack_unit of this EquipmentFanModule.
        A collection of references to the [compute.RackUnit](mo://compute.RackUnit) Managed Object.  When this managed object is deleted, the referenced [compute.RackUnit](mo://compute.RackUnit) MO unsets its reference to this deleted MO. 

        :return: The compute_rack_unit of this EquipmentFanModule.
        :rtype: ComputeRackUnitRef
        """
        return self._compute_rack_unit

    @compute_rack_unit.setter
    def compute_rack_unit(self, compute_rack_unit):
        """
        Sets the compute_rack_unit of this EquipmentFanModule.
        A collection of references to the [compute.RackUnit](mo://compute.RackUnit) Managed Object.  When this managed object is deleted, the referenced [compute.RackUnit](mo://compute.RackUnit) MO unsets its reference to this deleted MO. 

        :param compute_rack_unit: The compute_rack_unit of this EquipmentFanModule.
        :type: ComputeRackUnitRef
        """

        self._compute_rack_unit = compute_rack_unit

    @property
    def description(self):
        """
        Gets the description of this EquipmentFanModule.
        This field is to provide description for the fan module.  

        :return: The description of this EquipmentFanModule.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this EquipmentFanModule.
        This field is to provide description for the fan module.  

        :param description: The description of this EquipmentFanModule.
        :type: str
        """

        self._description = description

    @property
    def equipment_chassis(self):
        """
        Gets the equipment_chassis of this EquipmentFanModule.
        A collection of references to the [equipment.Chassis](mo://equipment.Chassis) Managed Object.  When this managed object is deleted, the referenced [equipment.Chassis](mo://equipment.Chassis) MO unsets its reference to this deleted MO. 

        :return: The equipment_chassis of this EquipmentFanModule.
        :rtype: EquipmentChassisRef
        """
        return self._equipment_chassis

    @equipment_chassis.setter
    def equipment_chassis(self, equipment_chassis):
        """
        Sets the equipment_chassis of this EquipmentFanModule.
        A collection of references to the [equipment.Chassis](mo://equipment.Chassis) Managed Object.  When this managed object is deleted, the referenced [equipment.Chassis](mo://equipment.Chassis) MO unsets its reference to this deleted MO. 

        :param equipment_chassis: The equipment_chassis of this EquipmentFanModule.
        :type: EquipmentChassisRef
        """

        self._equipment_chassis = equipment_chassis

    @property
    def equipment_rack_enclosure(self):
        """
        Gets the equipment_rack_enclosure of this EquipmentFanModule.
        A collection of references to the [equipment.RackEnclosure](mo://equipment.RackEnclosure) Managed Object.  When this managed object is deleted, the referenced [equipment.RackEnclosure](mo://equipment.RackEnclosure) MO unsets its reference to this deleted MO. 

        :return: The equipment_rack_enclosure of this EquipmentFanModule.
        :rtype: EquipmentRackEnclosureRef
        """
        return self._equipment_rack_enclosure

    @equipment_rack_enclosure.setter
    def equipment_rack_enclosure(self, equipment_rack_enclosure):
        """
        Sets the equipment_rack_enclosure of this EquipmentFanModule.
        A collection of references to the [equipment.RackEnclosure](mo://equipment.RackEnclosure) Managed Object.  When this managed object is deleted, the referenced [equipment.RackEnclosure](mo://equipment.RackEnclosure) MO unsets its reference to this deleted MO. 

        :param equipment_rack_enclosure: The equipment_rack_enclosure of this EquipmentFanModule.
        :type: EquipmentRackEnclosureRef
        """

        self._equipment_rack_enclosure = equipment_rack_enclosure

    @property
    def fans(self):
        """
        Gets the fans of this EquipmentFanModule.

        :return: The fans of this EquipmentFanModule.
        :rtype: list[EquipmentFanRef]
        """
        return self._fans

    @fans.setter
    def fans(self, fans):
        """
        Sets the fans of this EquipmentFanModule.

        :param fans: The fans of this EquipmentFanModule.
        :type: list[EquipmentFanRef]
        """

        self._fans = fans

    @property
    def module_id(self):
        """
        Gets the module_id of this EquipmentFanModule.
        This field acts as the identifier for this particular Module, within the Fabric Interconnect.  

        :return: The module_id of this EquipmentFanModule.
        :rtype: int
        """
        return self._module_id

    @module_id.setter
    def module_id(self, module_id):
        """
        Sets the module_id of this EquipmentFanModule.
        This field acts as the identifier for this particular Module, within the Fabric Interconnect.  

        :param module_id: The module_id of this EquipmentFanModule.
        :type: int
        """

        self._module_id = module_id

    @property
    def network_element(self):
        """
        Gets the network_element of this EquipmentFanModule.
        A collection of references to the [network.Element](mo://network.Element) Managed Object.  When this managed object is deleted, the referenced [network.Element](mo://network.Element) MO unsets its reference to this deleted MO. 

        :return: The network_element of this EquipmentFanModule.
        :rtype: NetworkElementRef
        """
        return self._network_element

    @network_element.setter
    def network_element(self, network_element):
        """
        Sets the network_element of this EquipmentFanModule.
        A collection of references to the [network.Element](mo://network.Element) Managed Object.  When this managed object is deleted, the referenced [network.Element](mo://network.Element) MO unsets its reference to this deleted MO. 

        :param network_element: The network_element of this EquipmentFanModule.
        :type: NetworkElementRef
        """

        self._network_element = network_element

    @property
    def oper_state(self):
        """
        Gets the oper_state of this EquipmentFanModule.
        This field is used to indicate this fan module's operational state.  

        :return: The oper_state of this EquipmentFanModule.
        :rtype: str
        """
        return self._oper_state

    @oper_state.setter
    def oper_state(self, oper_state):
        """
        Sets the oper_state of this EquipmentFanModule.
        This field is used to indicate this fan module's operational state.  

        :param oper_state: The oper_state of this EquipmentFanModule.
        :type: str
        """

        self._oper_state = oper_state

    @property
    def part_number(self):
        """
        Gets the part_number of this EquipmentFanModule.
        This field identifies the Part Number for this Fan Module.  

        :return: The part_number of this EquipmentFanModule.
        :rtype: str
        """
        return self._part_number

    @part_number.setter
    def part_number(self, part_number):
        """
        Sets the part_number of this EquipmentFanModule.
        This field identifies the Part Number for this Fan Module.  

        :param part_number: The part_number of this EquipmentFanModule.
        :type: str
        """

        self._part_number = part_number

    @property
    def pid(self):
        """
        Gets the pid of this EquipmentFanModule.
        This field identifies the Product ID for the fan module.  

        :return: The pid of this EquipmentFanModule.
        :rtype: str
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        """
        Sets the pid of this EquipmentFanModule.
        This field identifies the Product ID for the fan module.  

        :param pid: The pid of this EquipmentFanModule.
        :type: str
        """

        self._pid = pid

    @property
    def presence(self):
        """
        Gets the presence of this EquipmentFanModule.
        This field is used to indicate this fan module's presence.  

        :return: The presence of this EquipmentFanModule.
        :rtype: str
        """
        return self._presence

    @presence.setter
    def presence(self, presence):
        """
        Sets the presence of this EquipmentFanModule.
        This field is used to indicate this fan module's presence.  

        :param presence: The presence of this EquipmentFanModule.
        :type: str
        """

        self._presence = presence

    @property
    def registered_device(self):
        """
        Gets the registered_device of this EquipmentFanModule.
        The Device to which this Managed Object is associated. 

        :return: The registered_device of this EquipmentFanModule.
        :rtype: AssetDeviceRegistrationRef
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """
        Sets the registered_device of this EquipmentFanModule.
        The Device to which this Managed Object is associated. 

        :param registered_device: The registered_device of this EquipmentFanModule.
        :type: AssetDeviceRegistrationRef
        """

        self._registered_device = registered_device

    @property
    def sku(self):
        """
        Gets the sku of this EquipmentFanModule.
        This field identifies the Stockkeeping Unit for this Fan Module.  

        :return: The sku of this EquipmentFanModule.
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """
        Sets the sku of this EquipmentFanModule.
        This field identifies the Stockkeeping Unit for this Fan Module.  

        :param sku: The sku of this EquipmentFanModule.
        :type: str
        """

        self._sku = sku

    @property
    def tray_id(self):
        """
        Gets the tray_id of this EquipmentFanModule.
        Tray identifier for the fan module.  

        :return: The tray_id of this EquipmentFanModule.
        :rtype: int
        """
        return self._tray_id

    @tray_id.setter
    def tray_id(self, tray_id):
        """
        Sets the tray_id of this EquipmentFanModule.
        Tray identifier for the fan module.  

        :param tray_id: The tray_id of this EquipmentFanModule.
        :type: int
        """

        self._tray_id = tray_id

    @property
    def vid(self):
        """
        Gets the vid of this EquipmentFanModule.
        This field identifies the Vendor ID for this Fan Module.   

        :return: The vid of this EquipmentFanModule.
        :rtype: str
        """
        return self._vid

    @vid.setter
    def vid(self, vid):
        """
        Sets the vid of this EquipmentFanModule.
        This field identifies the Vendor ID for this Fan Module.   

        :param vid: The vid of this EquipmentFanModule.
        :type: str
        """

        self._vid = vid

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
        if not isinstance(other, EquipmentFanModule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
