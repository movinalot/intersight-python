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


class StorageController(object):
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
        'compute_board': 'ComputeBoardRef',
        'controller_flags': 'str',
        'controller_id': 'str',
        'controller_status': 'str',
        'hw_revision': 'str',
        'oob_interface_supported': 'str',
        'oper_state': 'str',
        'operability': 'str',
        'pci_addr': 'str',
        'pci_slot': 'str',
        'physical_disk_extensions': 'list[StoragePhysicalDiskExtensionRef]',
        'physical_disks': 'list[StoragePhysicalDiskRef]',
        'presence': 'str',
        'raid_support': 'str',
        'rebuild_rate': 'str',
        'registered_device': 'AssetDeviceRegistrationRef',
        'running_firmware': 'list[FirmwareRunningFirmwareRef]',
        'self_encrypt_enabled': 'str',
        'type': 'str',
        'virtual_drive_extensions': 'list[StorageVirtualDriveExtensionRef]',
        'virtual_drives': 'list[StorageVirtualDriveRef]'
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
        'compute_board': 'ComputeBoard',
        'controller_flags': 'ControllerFlags',
        'controller_id': 'ControllerId',
        'controller_status': 'ControllerStatus',
        'hw_revision': 'HwRevision',
        'oob_interface_supported': 'OobInterfaceSupported',
        'oper_state': 'OperState',
        'operability': 'Operability',
        'pci_addr': 'PciAddr',
        'pci_slot': 'PciSlot',
        'physical_disk_extensions': 'PhysicalDiskExtensions',
        'physical_disks': 'PhysicalDisks',
        'presence': 'Presence',
        'raid_support': 'RaidSupport',
        'rebuild_rate': 'RebuildRate',
        'registered_device': 'RegisteredDevice',
        'running_firmware': 'RunningFirmware',
        'self_encrypt_enabled': 'SelfEncryptEnabled',
        'type': 'Type',
        'virtual_drive_extensions': 'VirtualDriveExtensions',
        'virtual_drives': 'VirtualDrives'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, domain_group_moid=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, shared_scope=None, tags=None, version_context=None, device_mo_id=None, dn=None, rn=None, model=None, revision=None, serial=None, vendor=None, compute_board=None, controller_flags=None, controller_id=None, controller_status=None, hw_revision=None, oob_interface_supported=None, oper_state=None, operability=None, pci_addr=None, pci_slot=None, physical_disk_extensions=None, physical_disks=None, presence=None, raid_support=None, rebuild_rate=None, registered_device=None, running_firmware=None, self_encrypt_enabled=None, type=None, virtual_drive_extensions=None, virtual_drives=None):
        """
        StorageController - a model defined in Swagger
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
        self._compute_board = None
        self._controller_flags = None
        self._controller_id = None
        self._controller_status = None
        self._hw_revision = None
        self._oob_interface_supported = None
        self._oper_state = None
        self._operability = None
        self._pci_addr = None
        self._pci_slot = None
        self._physical_disk_extensions = None
        self._physical_disks = None
        self._presence = None
        self._raid_support = None
        self._rebuild_rate = None
        self._registered_device = None
        self._running_firmware = None
        self._self_encrypt_enabled = None
        self._type = None
        self._virtual_drive_extensions = None
        self._virtual_drives = None

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
        if compute_board is not None:
          self.compute_board = compute_board
        if controller_flags is not None:
          self.controller_flags = controller_flags
        if controller_id is not None:
          self.controller_id = controller_id
        if controller_status is not None:
          self.controller_status = controller_status
        if hw_revision is not None:
          self.hw_revision = hw_revision
        if oob_interface_supported is not None:
          self.oob_interface_supported = oob_interface_supported
        if oper_state is not None:
          self.oper_state = oper_state
        if operability is not None:
          self.operability = operability
        if pci_addr is not None:
          self.pci_addr = pci_addr
        if pci_slot is not None:
          self.pci_slot = pci_slot
        if physical_disk_extensions is not None:
          self.physical_disk_extensions = physical_disk_extensions
        if physical_disks is not None:
          self.physical_disks = physical_disks
        if presence is not None:
          self.presence = presence
        if raid_support is not None:
          self.raid_support = raid_support
        if rebuild_rate is not None:
          self.rebuild_rate = rebuild_rate
        if registered_device is not None:
          self.registered_device = registered_device
        if running_firmware is not None:
          self.running_firmware = running_firmware
        if self_encrypt_enabled is not None:
          self.self_encrypt_enabled = self_encrypt_enabled
        if type is not None:
          self.type = type
        if virtual_drive_extensions is not None:
          self.virtual_drive_extensions = virtual_drive_extensions
        if virtual_drives is not None:
          self.virtual_drives = virtual_drives

    @property
    def account_moid(self):
        """
        Gets the account_moid of this StorageController.
        The Account ID for this managed object.  

        :return: The account_moid of this StorageController.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this StorageController.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this StorageController.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this StorageController.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this StorageController.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this StorageController.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this StorageController.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this StorageController.
        The time when this managed object was created.  

        :return: The create_time of this StorageController.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this StorageController.
        The time when this managed object was created.  

        :param create_time: The create_time of this StorageController.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def domain_group_moid(self):
        """
        Gets the domain_group_moid of this StorageController.
        The DomainGroup ID for this managed object.  

        :return: The domain_group_moid of this StorageController.
        :rtype: str
        """
        return self._domain_group_moid

    @domain_group_moid.setter
    def domain_group_moid(self, domain_group_moid):
        """
        Sets the domain_group_moid of this StorageController.
        The DomainGroup ID for this managed object.  

        :param domain_group_moid: The domain_group_moid of this StorageController.
        :type: str
        """

        self._domain_group_moid = domain_group_moid

    @property
    def mod_time(self):
        """
        Gets the mod_time of this StorageController.
        The time when this managed object was last modified.  

        :return: The mod_time of this StorageController.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this StorageController.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this StorageController.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this StorageController.
        The unique identifier of this Managed Object instance.  

        :return: The moid of this StorageController.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this StorageController.
        The unique identifier of this Managed Object instance.  

        :param moid: The moid of this StorageController.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this StorageController.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this StorageController.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this StorageController.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this StorageController.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this StorageController.
        The array of owners which represent effective ownership of this object.   

        :return: The owners of this StorageController.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this StorageController.
        The array of owners which represent effective ownership of this object.   

        :param owners: The owners of this StorageController.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this StorageController.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this StorageController.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this StorageController.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this StorageController.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def shared_scope(self):
        """
        Gets the shared_scope of this StorageController.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :return: The shared_scope of this StorageController.
        :rtype: str
        """
        return self._shared_scope

    @shared_scope.setter
    def shared_scope(self, shared_scope):
        """
        Sets the shared_scope of this StorageController.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :param shared_scope: The shared_scope of this StorageController.
        :type: str
        """

        self._shared_scope = shared_scope

    @property
    def tags(self):
        """
        Gets the tags of this StorageController.
        The array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this StorageController.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this StorageController.
        The array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this StorageController.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this StorageController.
        The versioning info for this managed object.   

        :return: The version_context of this StorageController.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this StorageController.
        The versioning info for this managed object.   

        :param version_context: The version_context of this StorageController.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def device_mo_id(self):
        """
        Gets the device_mo_id of this StorageController.

        :return: The device_mo_id of this StorageController.
        :rtype: str
        """
        return self._device_mo_id

    @device_mo_id.setter
    def device_mo_id(self, device_mo_id):
        """
        Sets the device_mo_id of this StorageController.

        :param device_mo_id: The device_mo_id of this StorageController.
        :type: str
        """

        self._device_mo_id = device_mo_id

    @property
    def dn(self):
        """
        Gets the dn of this StorageController.

        :return: The dn of this StorageController.
        :rtype: str
        """
        return self._dn

    @dn.setter
    def dn(self, dn):
        """
        Sets the dn of this StorageController.

        :param dn: The dn of this StorageController.
        :type: str
        """

        self._dn = dn

    @property
    def rn(self):
        """
        Gets the rn of this StorageController.

        :return: The rn of this StorageController.
        :rtype: str
        """
        return self._rn

    @rn.setter
    def rn(self, rn):
        """
        Sets the rn of this StorageController.

        :param rn: The rn of this StorageController.
        :type: str
        """

        self._rn = rn

    @property
    def model(self):
        """
        Gets the model of this StorageController.
        This field identifies the model of the given component.  

        :return: The model of this StorageController.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """
        Sets the model of this StorageController.
        This field identifies the model of the given component.  

        :param model: The model of this StorageController.
        :type: str
        """

        self._model = model

    @property
    def revision(self):
        """
        Gets the revision of this StorageController.

        :return: The revision of this StorageController.
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """
        Sets the revision of this StorageController.

        :param revision: The revision of this StorageController.
        :type: str
        """

        self._revision = revision

    @property
    def serial(self):
        """
        Gets the serial of this StorageController.
        This field identifies the serial of the given component.  

        :return: The serial of this StorageController.
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """
        Sets the serial of this StorageController.
        This field identifies the serial of the given component.  

        :param serial: The serial of this StorageController.
        :type: str
        """

        self._serial = serial

    @property
    def vendor(self):
        """
        Gets the vendor of this StorageController.
        This field identifies the vendor of the given component.   

        :return: The vendor of this StorageController.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """
        Sets the vendor of this StorageController.
        This field identifies the vendor of the given component.   

        :param vendor: The vendor of this StorageController.
        :type: str
        """

        self._vendor = vendor

    @property
    def compute_board(self):
        """
        Gets the compute_board of this StorageController.
        A collection of references to the [compute.Board](mo://compute.Board) Managed Object.  When this managed object is deleted, the referenced [compute.Board](mo://compute.Board) MO unsets its reference to this deleted MO. 

        :return: The compute_board of this StorageController.
        :rtype: ComputeBoardRef
        """
        return self._compute_board

    @compute_board.setter
    def compute_board(self, compute_board):
        """
        Sets the compute_board of this StorageController.
        A collection of references to the [compute.Board](mo://compute.Board) Managed Object.  When this managed object is deleted, the referenced [compute.Board](mo://compute.Board) MO unsets its reference to this deleted MO. 

        :param compute_board: The compute_board of this StorageController.
        :type: ComputeBoardRef
        """

        self._compute_board = compute_board

    @property
    def controller_flags(self):
        """
        Gets the controller_flags of this StorageController.

        :return: The controller_flags of this StorageController.
        :rtype: str
        """
        return self._controller_flags

    @controller_flags.setter
    def controller_flags(self, controller_flags):
        """
        Sets the controller_flags of this StorageController.

        :param controller_flags: The controller_flags of this StorageController.
        :type: str
        """

        self._controller_flags = controller_flags

    @property
    def controller_id(self):
        """
        Gets the controller_id of this StorageController.
        It shows the Id of controller.  

        :return: The controller_id of this StorageController.
        :rtype: str
        """
        return self._controller_id

    @controller_id.setter
    def controller_id(self, controller_id):
        """
        Sets the controller_id of this StorageController.
        It shows the Id of controller.  

        :param controller_id: The controller_id of this StorageController.
        :type: str
        """

        self._controller_id = controller_id

    @property
    def controller_status(self):
        """
        Gets the controller_status of this StorageController.
        It shows the current status of controller.  

        :return: The controller_status of this StorageController.
        :rtype: str
        """
        return self._controller_status

    @controller_status.setter
    def controller_status(self, controller_status):
        """
        Sets the controller_status of this StorageController.
        It shows the current status of controller.  

        :param controller_status: The controller_status of this StorageController.
        :type: str
        """

        self._controller_status = controller_status

    @property
    def hw_revision(self):
        """
        Gets the hw_revision of this StorageController.
        It shows the hardware revision of controller.  

        :return: The hw_revision of this StorageController.
        :rtype: str
        """
        return self._hw_revision

    @hw_revision.setter
    def hw_revision(self, hw_revision):
        """
        Sets the hw_revision of this StorageController.
        It shows the hardware revision of controller.  

        :param hw_revision: The hw_revision of this StorageController.
        :type: str
        """

        self._hw_revision = hw_revision

    @property
    def oob_interface_supported(self):
        """
        Gets the oob_interface_supported of this StorageController.
        It shows CIMC support for out-of-band configuration of controller.  

        :return: The oob_interface_supported of this StorageController.
        :rtype: str
        """
        return self._oob_interface_supported

    @oob_interface_supported.setter
    def oob_interface_supported(self, oob_interface_supported):
        """
        Sets the oob_interface_supported of this StorageController.
        It shows CIMC support for out-of-band configuration of controller.  

        :param oob_interface_supported: The oob_interface_supported of this StorageController.
        :type: str
        """

        self._oob_interface_supported = oob_interface_supported

    @property
    def oper_state(self):
        """
        Gets the oper_state of this StorageController.

        :return: The oper_state of this StorageController.
        :rtype: str
        """
        return self._oper_state

    @oper_state.setter
    def oper_state(self, oper_state):
        """
        Sets the oper_state of this StorageController.

        :param oper_state: The oper_state of this StorageController.
        :type: str
        """

        self._oper_state = oper_state

    @property
    def operability(self):
        """
        Gets the operability of this StorageController.

        :return: The operability of this StorageController.
        :rtype: str
        """
        return self._operability

    @operability.setter
    def operability(self, operability):
        """
        Sets the operability of this StorageController.

        :param operability: The operability of this StorageController.
        :type: str
        """

        self._operability = operability

    @property
    def pci_addr(self):
        """
        Gets the pci_addr of this StorageController.
        It shows the current pci address of controller.  

        :return: The pci_addr of this StorageController.
        :rtype: str
        """
        return self._pci_addr

    @pci_addr.setter
    def pci_addr(self, pci_addr):
        """
        Sets the pci_addr of this StorageController.
        It shows the current pci address of controller.  

        :param pci_addr: The pci_addr of this StorageController.
        :type: str
        """

        self._pci_addr = pci_addr

    @property
    def pci_slot(self):
        """
        Gets the pci_slot of this StorageController.
        It shows the pci slot name for the controller.  

        :return: The pci_slot of this StorageController.
        :rtype: str
        """
        return self._pci_slot

    @pci_slot.setter
    def pci_slot(self, pci_slot):
        """
        Sets the pci_slot of this StorageController.
        It shows the pci slot name for the controller.  

        :param pci_slot: The pci_slot of this StorageController.
        :type: str
        """

        self._pci_slot = pci_slot

    @property
    def physical_disk_extensions(self):
        """
        Gets the physical_disk_extensions of this StorageController.
        This object is created to indicate a SCSI controller has physical connectivity to specified physical disk. 

        :return: The physical_disk_extensions of this StorageController.
        :rtype: list[StoragePhysicalDiskExtensionRef]
        """
        return self._physical_disk_extensions

    @physical_disk_extensions.setter
    def physical_disk_extensions(self, physical_disk_extensions):
        """
        Sets the physical_disk_extensions of this StorageController.
        This object is created to indicate a SCSI controller has physical connectivity to specified physical disk. 

        :param physical_disk_extensions: The physical_disk_extensions of this StorageController.
        :type: list[StoragePhysicalDiskExtensionRef]
        """

        self._physical_disk_extensions = physical_disk_extensions

    @property
    def physical_disks(self):
        """
        Gets the physical_disks of this StorageController.
        Physical Disk on a server. 

        :return: The physical_disks of this StorageController.
        :rtype: list[StoragePhysicalDiskRef]
        """
        return self._physical_disks

    @physical_disks.setter
    def physical_disks(self, physical_disks):
        """
        Sets the physical_disks of this StorageController.
        Physical Disk on a server. 

        :param physical_disks: The physical_disks of this StorageController.
        :type: list[StoragePhysicalDiskRef]
        """

        self._physical_disks = physical_disks

    @property
    def presence(self):
        """
        Gets the presence of this StorageController.
        It shows physical presence or absence of the controller on server.  

        :return: The presence of this StorageController.
        :rtype: str
        """
        return self._presence

    @presence.setter
    def presence(self, presence):
        """
        Sets the presence of this StorageController.
        It shows physical presence or absence of the controller on server.  

        :param presence: The presence of this StorageController.
        :type: str
        """

        self._presence = presence

    @property
    def raid_support(self):
        """
        Gets the raid_support of this StorageController.
        It shows the RAID levels supported by controller.  

        :return: The raid_support of this StorageController.
        :rtype: str
        """
        return self._raid_support

    @raid_support.setter
    def raid_support(self, raid_support):
        """
        Sets the raid_support of this StorageController.
        It shows the RAID levels supported by controller.  

        :param raid_support: The raid_support of this StorageController.
        :type: str
        """

        self._raid_support = raid_support

    @property
    def rebuild_rate(self):
        """
        Gets the rebuild_rate of this StorageController.

        :return: The rebuild_rate of this StorageController.
        :rtype: str
        """
        return self._rebuild_rate

    @rebuild_rate.setter
    def rebuild_rate(self, rebuild_rate):
        """
        Sets the rebuild_rate of this StorageController.

        :param rebuild_rate: The rebuild_rate of this StorageController.
        :type: str
        """

        self._rebuild_rate = rebuild_rate

    @property
    def registered_device(self):
        """
        Gets the registered_device of this StorageController.
        The Device to which this Managed Object is associated. 

        :return: The registered_device of this StorageController.
        :rtype: AssetDeviceRegistrationRef
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """
        Sets the registered_device of this StorageController.
        The Device to which this Managed Object is associated. 

        :param registered_device: The registered_device of this StorageController.
        :type: AssetDeviceRegistrationRef
        """

        self._registered_device = registered_device

    @property
    def running_firmware(self):
        """
        Gets the running_firmware of this StorageController.

        :return: The running_firmware of this StorageController.
        :rtype: list[FirmwareRunningFirmwareRef]
        """
        return self._running_firmware

    @running_firmware.setter
    def running_firmware(self, running_firmware):
        """
        Sets the running_firmware of this StorageController.

        :param running_firmware: The running_firmware of this StorageController.
        :type: list[FirmwareRunningFirmwareRef]
        """

        self._running_firmware = running_firmware

    @property
    def self_encrypt_enabled(self):
        """
        Gets the self_encrypt_enabled of this StorageController.

        :return: The self_encrypt_enabled of this StorageController.
        :rtype: str
        """
        return self._self_encrypt_enabled

    @self_encrypt_enabled.setter
    def self_encrypt_enabled(self, self_encrypt_enabled):
        """
        Sets the self_encrypt_enabled of this StorageController.

        :param self_encrypt_enabled: The self_encrypt_enabled of this StorageController.
        :type: str
        """

        self._self_encrypt_enabled = self_encrypt_enabled

    @property
    def type(self):
        """
        Gets the type of this StorageController.
        Controller types are SAS, SATA, PCH, NVME.   

        :return: The type of this StorageController.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this StorageController.
        Controller types are SAS, SATA, PCH, NVME.   

        :param type: The type of this StorageController.
        :type: str
        """

        self._type = type

    @property
    def virtual_drive_extensions(self):
        """
        Gets the virtual_drive_extensions of this StorageController.

        :return: The virtual_drive_extensions of this StorageController.
        :rtype: list[StorageVirtualDriveExtensionRef]
        """
        return self._virtual_drive_extensions

    @virtual_drive_extensions.setter
    def virtual_drive_extensions(self, virtual_drive_extensions):
        """
        Sets the virtual_drive_extensions of this StorageController.

        :param virtual_drive_extensions: The virtual_drive_extensions of this StorageController.
        :type: list[StorageVirtualDriveExtensionRef]
        """

        self._virtual_drive_extensions = virtual_drive_extensions

    @property
    def virtual_drives(self):
        """
        Gets the virtual_drives of this StorageController.
        Storage physical drives are grouped as Drive Group, a drive group then can be partitioned into virtual drives. 

        :return: The virtual_drives of this StorageController.
        :rtype: list[StorageVirtualDriveRef]
        """
        return self._virtual_drives

    @virtual_drives.setter
    def virtual_drives(self, virtual_drives):
        """
        Sets the virtual_drives of this StorageController.
        Storage physical drives are grouped as Drive Group, a drive group then can be partitioned into virtual drives. 

        :param virtual_drives: The virtual_drives of this StorageController.
        :type: list[StorageVirtualDriveRef]
        """

        self._virtual_drives = virtual_drives

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
        if not isinstance(other, StorageController):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
