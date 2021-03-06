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


class ManagementController(object):
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
        'adapter_unit': 'AdapterUnitRef',
        'compute_blade': 'ComputeBladeRef',
        'compute_rack_unit': 'ComputeRackUnitRef',
        'management_interfaces': 'list[ManagementInterfaceRef]',
        'model': 'str',
        'network_element': 'NetworkElementRef',
        'registered_device': 'AssetDeviceRegistrationRef',
        'running_firmware': 'list[FirmwareRunningFirmwareRef]',
        'storage_sas_expander': 'StorageSasExpanderRef',
        'top_system': 'TopSystemRef'
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
        'adapter_unit': 'AdapterUnit',
        'compute_blade': 'ComputeBlade',
        'compute_rack_unit': 'ComputeRackUnit',
        'management_interfaces': 'ManagementInterfaces',
        'model': 'Model',
        'network_element': 'NetworkElement',
        'registered_device': 'RegisteredDevice',
        'running_firmware': 'RunningFirmware',
        'storage_sas_expander': 'StorageSasExpander',
        'top_system': 'TopSystem'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, domain_group_moid=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, shared_scope=None, tags=None, version_context=None, device_mo_id=None, dn=None, rn=None, adapter_unit=None, compute_blade=None, compute_rack_unit=None, management_interfaces=None, model=None, network_element=None, registered_device=None, running_firmware=None, storage_sas_expander=None, top_system=None):
        """
        ManagementController - a model defined in Swagger
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
        self._adapter_unit = None
        self._compute_blade = None
        self._compute_rack_unit = None
        self._management_interfaces = None
        self._model = None
        self._network_element = None
        self._registered_device = None
        self._running_firmware = None
        self._storage_sas_expander = None
        self._top_system = None

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
        if adapter_unit is not None:
          self.adapter_unit = adapter_unit
        if compute_blade is not None:
          self.compute_blade = compute_blade
        if compute_rack_unit is not None:
          self.compute_rack_unit = compute_rack_unit
        if management_interfaces is not None:
          self.management_interfaces = management_interfaces
        if model is not None:
          self.model = model
        if network_element is not None:
          self.network_element = network_element
        if registered_device is not None:
          self.registered_device = registered_device
        if running_firmware is not None:
          self.running_firmware = running_firmware
        if storage_sas_expander is not None:
          self.storage_sas_expander = storage_sas_expander
        if top_system is not None:
          self.top_system = top_system

    @property
    def account_moid(self):
        """
        Gets the account_moid of this ManagementController.
        The Account ID for this managed object.  

        :return: The account_moid of this ManagementController.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this ManagementController.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this ManagementController.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this ManagementController.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this ManagementController.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this ManagementController.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this ManagementController.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this ManagementController.
        The time when this managed object was created.  

        :return: The create_time of this ManagementController.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this ManagementController.
        The time when this managed object was created.  

        :param create_time: The create_time of this ManagementController.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def domain_group_moid(self):
        """
        Gets the domain_group_moid of this ManagementController.
        The DomainGroup ID for this managed object.  

        :return: The domain_group_moid of this ManagementController.
        :rtype: str
        """
        return self._domain_group_moid

    @domain_group_moid.setter
    def domain_group_moid(self, domain_group_moid):
        """
        Sets the domain_group_moid of this ManagementController.
        The DomainGroup ID for this managed object.  

        :param domain_group_moid: The domain_group_moid of this ManagementController.
        :type: str
        """

        self._domain_group_moid = domain_group_moid

    @property
    def mod_time(self):
        """
        Gets the mod_time of this ManagementController.
        The time when this managed object was last modified.  

        :return: The mod_time of this ManagementController.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this ManagementController.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this ManagementController.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this ManagementController.
        The unique identifier of this Managed Object instance.  

        :return: The moid of this ManagementController.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this ManagementController.
        The unique identifier of this Managed Object instance.  

        :param moid: The moid of this ManagementController.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this ManagementController.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this ManagementController.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this ManagementController.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this ManagementController.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this ManagementController.
        The array of owners which represent effective ownership of this object.   

        :return: The owners of this ManagementController.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this ManagementController.
        The array of owners which represent effective ownership of this object.   

        :param owners: The owners of this ManagementController.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this ManagementController.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this ManagementController.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this ManagementController.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this ManagementController.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def shared_scope(self):
        """
        Gets the shared_scope of this ManagementController.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :return: The shared_scope of this ManagementController.
        :rtype: str
        """
        return self._shared_scope

    @shared_scope.setter
    def shared_scope(self, shared_scope):
        """
        Sets the shared_scope of this ManagementController.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :param shared_scope: The shared_scope of this ManagementController.
        :type: str
        """

        self._shared_scope = shared_scope

    @property
    def tags(self):
        """
        Gets the tags of this ManagementController.
        The array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this ManagementController.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this ManagementController.
        The array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this ManagementController.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this ManagementController.
        The versioning info for this managed object.   

        :return: The version_context of this ManagementController.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this ManagementController.
        The versioning info for this managed object.   

        :param version_context: The version_context of this ManagementController.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def device_mo_id(self):
        """
        Gets the device_mo_id of this ManagementController.

        :return: The device_mo_id of this ManagementController.
        :rtype: str
        """
        return self._device_mo_id

    @device_mo_id.setter
    def device_mo_id(self, device_mo_id):
        """
        Sets the device_mo_id of this ManagementController.

        :param device_mo_id: The device_mo_id of this ManagementController.
        :type: str
        """

        self._device_mo_id = device_mo_id

    @property
    def dn(self):
        """
        Gets the dn of this ManagementController.

        :return: The dn of this ManagementController.
        :rtype: str
        """
        return self._dn

    @dn.setter
    def dn(self, dn):
        """
        Sets the dn of this ManagementController.

        :param dn: The dn of this ManagementController.
        :type: str
        """

        self._dn = dn

    @property
    def rn(self):
        """
        Gets the rn of this ManagementController.

        :return: The rn of this ManagementController.
        :rtype: str
        """
        return self._rn

    @rn.setter
    def rn(self, rn):
        """
        Sets the rn of this ManagementController.

        :param rn: The rn of this ManagementController.
        :type: str
        """

        self._rn = rn

    @property
    def adapter_unit(self):
        """
        Gets the adapter_unit of this ManagementController.
        A collection of references to the [adapter.Unit](mo://adapter.Unit) Managed Object.  When this managed object is deleted, the referenced [adapter.Unit](mo://adapter.Unit) MO unsets its reference to this deleted MO. 

        :return: The adapter_unit of this ManagementController.
        :rtype: AdapterUnitRef
        """
        return self._adapter_unit

    @adapter_unit.setter
    def adapter_unit(self, adapter_unit):
        """
        Sets the adapter_unit of this ManagementController.
        A collection of references to the [adapter.Unit](mo://adapter.Unit) Managed Object.  When this managed object is deleted, the referenced [adapter.Unit](mo://adapter.Unit) MO unsets its reference to this deleted MO. 

        :param adapter_unit: The adapter_unit of this ManagementController.
        :type: AdapterUnitRef
        """

        self._adapter_unit = adapter_unit

    @property
    def compute_blade(self):
        """
        Gets the compute_blade of this ManagementController.
        A collection of references to the [compute.Blade](mo://compute.Blade) Managed Object.  When this managed object is deleted, the referenced [compute.Blade](mo://compute.Blade) MO unsets its reference to this deleted MO. 

        :return: The compute_blade of this ManagementController.
        :rtype: ComputeBladeRef
        """
        return self._compute_blade

    @compute_blade.setter
    def compute_blade(self, compute_blade):
        """
        Sets the compute_blade of this ManagementController.
        A collection of references to the [compute.Blade](mo://compute.Blade) Managed Object.  When this managed object is deleted, the referenced [compute.Blade](mo://compute.Blade) MO unsets its reference to this deleted MO. 

        :param compute_blade: The compute_blade of this ManagementController.
        :type: ComputeBladeRef
        """

        self._compute_blade = compute_blade

    @property
    def compute_rack_unit(self):
        """
        Gets the compute_rack_unit of this ManagementController.
        A collection of references to the [compute.RackUnit](mo://compute.RackUnit) Managed Object.  When this managed object is deleted, the referenced [compute.RackUnit](mo://compute.RackUnit) MO unsets its reference to this deleted MO. 

        :return: The compute_rack_unit of this ManagementController.
        :rtype: ComputeRackUnitRef
        """
        return self._compute_rack_unit

    @compute_rack_unit.setter
    def compute_rack_unit(self, compute_rack_unit):
        """
        Sets the compute_rack_unit of this ManagementController.
        A collection of references to the [compute.RackUnit](mo://compute.RackUnit) Managed Object.  When this managed object is deleted, the referenced [compute.RackUnit](mo://compute.RackUnit) MO unsets its reference to this deleted MO. 

        :param compute_rack_unit: The compute_rack_unit of this ManagementController.
        :type: ComputeRackUnitRef
        """

        self._compute_rack_unit = compute_rack_unit

    @property
    def management_interfaces(self):
        """
        Gets the management_interfaces of this ManagementController.

        :return: The management_interfaces of this ManagementController.
        :rtype: list[ManagementInterfaceRef]
        """
        return self._management_interfaces

    @management_interfaces.setter
    def management_interfaces(self, management_interfaces):
        """
        Sets the management_interfaces of this ManagementController.

        :param management_interfaces: The management_interfaces of this ManagementController.
        :type: list[ManagementInterfaceRef]
        """

        self._management_interfaces = management_interfaces

    @property
    def model(self):
        """
        Gets the model of this ManagementController.
        Model of the endpoint that houses the management controller.   

        :return: The model of this ManagementController.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """
        Sets the model of this ManagementController.
        Model of the endpoint that houses the management controller.   

        :param model: The model of this ManagementController.
        :type: str
        """

        self._model = model

    @property
    def network_element(self):
        """
        Gets the network_element of this ManagementController.
        A collection of references to the [network.Element](mo://network.Element) Managed Object.  When this managed object is deleted, the referenced [network.Element](mo://network.Element) MO unsets its reference to this deleted MO. 

        :return: The network_element of this ManagementController.
        :rtype: NetworkElementRef
        """
        return self._network_element

    @network_element.setter
    def network_element(self, network_element):
        """
        Sets the network_element of this ManagementController.
        A collection of references to the [network.Element](mo://network.Element) Managed Object.  When this managed object is deleted, the referenced [network.Element](mo://network.Element) MO unsets its reference to this deleted MO. 

        :param network_element: The network_element of this ManagementController.
        :type: NetworkElementRef
        """

        self._network_element = network_element

    @property
    def registered_device(self):
        """
        Gets the registered_device of this ManagementController.
        The Device to which this Managed Object is associated. 

        :return: The registered_device of this ManagementController.
        :rtype: AssetDeviceRegistrationRef
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """
        Sets the registered_device of this ManagementController.
        The Device to which this Managed Object is associated. 

        :param registered_device: The registered_device of this ManagementController.
        :type: AssetDeviceRegistrationRef
        """

        self._registered_device = registered_device

    @property
    def running_firmware(self):
        """
        Gets the running_firmware of this ManagementController.

        :return: The running_firmware of this ManagementController.
        :rtype: list[FirmwareRunningFirmwareRef]
        """
        return self._running_firmware

    @running_firmware.setter
    def running_firmware(self, running_firmware):
        """
        Sets the running_firmware of this ManagementController.

        :param running_firmware: The running_firmware of this ManagementController.
        :type: list[FirmwareRunningFirmwareRef]
        """

        self._running_firmware = running_firmware

    @property
    def storage_sas_expander(self):
        """
        Gets the storage_sas_expander of this ManagementController.
        A collection of references to the [storage.SasExpander](mo://storage.SasExpander) Managed Object.  When this managed object is deleted, the referenced [storage.SasExpander](mo://storage.SasExpander) MO unsets its reference to this deleted MO. 

        :return: The storage_sas_expander of this ManagementController.
        :rtype: StorageSasExpanderRef
        """
        return self._storage_sas_expander

    @storage_sas_expander.setter
    def storage_sas_expander(self, storage_sas_expander):
        """
        Sets the storage_sas_expander of this ManagementController.
        A collection of references to the [storage.SasExpander](mo://storage.SasExpander) Managed Object.  When this managed object is deleted, the referenced [storage.SasExpander](mo://storage.SasExpander) MO unsets its reference to this deleted MO. 

        :param storage_sas_expander: The storage_sas_expander of this ManagementController.
        :type: StorageSasExpanderRef
        """

        self._storage_sas_expander = storage_sas_expander

    @property
    def top_system(self):
        """
        Gets the top_system of this ManagementController.
        A collection of references to the [top.System](mo://top.System) Managed Object.  When this managed object is deleted, the referenced [top.System](mo://top.System) MO unsets its reference to this deleted MO. 

        :return: The top_system of this ManagementController.
        :rtype: TopSystemRef
        """
        return self._top_system

    @top_system.setter
    def top_system(self, top_system):
        """
        Sets the top_system of this ManagementController.
        A collection of references to the [top.System](mo://top.System) Managed Object.  When this managed object is deleted, the referenced [top.System](mo://top.System) MO unsets its reference to this deleted MO. 

        :param top_system: The top_system of this ManagementController.
        :type: TopSystemRef
        """

        self._top_system = top_system

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
        if not isinstance(other, ManagementController):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
