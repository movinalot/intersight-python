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


class VnicFcAdapterPolicy(object):
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
        'error_detection_timeout': 'int',
        'error_recovery_settings': 'VnicFcErrorRecoverySettings',
        'flogi_settings': 'VnicFlogiSettings',
        'interrupt_settings': 'VnicFcInterruptSettings',
        'io_throttle_count': 'int',
        'lun_count': 'int',
        'lun_queue_depth': 'int',
        'organization': 'IamAccountRef',
        'plogi_settings': 'VnicPlogiSettings',
        'resource_allocation_timeout': 'int',
        'rx_queue_settings': 'VnicFcQueueSettings',
        'scsi_queue_settings': 'VnicScsiQueueSettings',
        'tx_queue_settings': 'VnicFcQueueSettings'
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
        'error_detection_timeout': 'ErrorDetectionTimeout',
        'error_recovery_settings': 'ErrorRecoverySettings',
        'flogi_settings': 'FlogiSettings',
        'interrupt_settings': 'InterruptSettings',
        'io_throttle_count': 'IoThrottleCount',
        'lun_count': 'LunCount',
        'lun_queue_depth': 'LunQueueDepth',
        'organization': 'Organization',
        'plogi_settings': 'PlogiSettings',
        'resource_allocation_timeout': 'ResourceAllocationTimeout',
        'rx_queue_settings': 'RxQueueSettings',
        'scsi_queue_settings': 'ScsiQueueSettings',
        'tx_queue_settings': 'TxQueueSettings'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, domain_group_moid=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, shared_scope=None, tags=None, version_context=None, description=None, name=None, error_detection_timeout=None, error_recovery_settings=None, flogi_settings=None, interrupt_settings=None, io_throttle_count=None, lun_count=None, lun_queue_depth=None, organization=None, plogi_settings=None, resource_allocation_timeout=None, rx_queue_settings=None, scsi_queue_settings=None, tx_queue_settings=None):
        """
        VnicFcAdapterPolicy - a model defined in Swagger
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
        self._error_detection_timeout = None
        self._error_recovery_settings = None
        self._flogi_settings = None
        self._interrupt_settings = None
        self._io_throttle_count = None
        self._lun_count = None
        self._lun_queue_depth = None
        self._organization = None
        self._plogi_settings = None
        self._resource_allocation_timeout = None
        self._rx_queue_settings = None
        self._scsi_queue_settings = None
        self._tx_queue_settings = None

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
        if error_detection_timeout is not None:
          self.error_detection_timeout = error_detection_timeout
        if error_recovery_settings is not None:
          self.error_recovery_settings = error_recovery_settings
        if flogi_settings is not None:
          self.flogi_settings = flogi_settings
        if interrupt_settings is not None:
          self.interrupt_settings = interrupt_settings
        if io_throttle_count is not None:
          self.io_throttle_count = io_throttle_count
        if lun_count is not None:
          self.lun_count = lun_count
        if lun_queue_depth is not None:
          self.lun_queue_depth = lun_queue_depth
        if organization is not None:
          self.organization = organization
        if plogi_settings is not None:
          self.plogi_settings = plogi_settings
        if resource_allocation_timeout is not None:
          self.resource_allocation_timeout = resource_allocation_timeout
        if rx_queue_settings is not None:
          self.rx_queue_settings = rx_queue_settings
        if scsi_queue_settings is not None:
          self.scsi_queue_settings = scsi_queue_settings
        if tx_queue_settings is not None:
          self.tx_queue_settings = tx_queue_settings

    @property
    def account_moid(self):
        """
        Gets the account_moid of this VnicFcAdapterPolicy.
        The Account ID for this managed object.  

        :return: The account_moid of this VnicFcAdapterPolicy.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this VnicFcAdapterPolicy.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this VnicFcAdapterPolicy.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this VnicFcAdapterPolicy.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this VnicFcAdapterPolicy.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this VnicFcAdapterPolicy.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this VnicFcAdapterPolicy.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this VnicFcAdapterPolicy.
        The time when this managed object was created.  

        :return: The create_time of this VnicFcAdapterPolicy.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this VnicFcAdapterPolicy.
        The time when this managed object was created.  

        :param create_time: The create_time of this VnicFcAdapterPolicy.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def domain_group_moid(self):
        """
        Gets the domain_group_moid of this VnicFcAdapterPolicy.
        The DomainGroup ID for this managed object.  

        :return: The domain_group_moid of this VnicFcAdapterPolicy.
        :rtype: str
        """
        return self._domain_group_moid

    @domain_group_moid.setter
    def domain_group_moid(self, domain_group_moid):
        """
        Sets the domain_group_moid of this VnicFcAdapterPolicy.
        The DomainGroup ID for this managed object.  

        :param domain_group_moid: The domain_group_moid of this VnicFcAdapterPolicy.
        :type: str
        """

        self._domain_group_moid = domain_group_moid

    @property
    def mod_time(self):
        """
        Gets the mod_time of this VnicFcAdapterPolicy.
        The time when this managed object was last modified.  

        :return: The mod_time of this VnicFcAdapterPolicy.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this VnicFcAdapterPolicy.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this VnicFcAdapterPolicy.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this VnicFcAdapterPolicy.
        The unique identifier of this Managed Object instance.  

        :return: The moid of this VnicFcAdapterPolicy.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this VnicFcAdapterPolicy.
        The unique identifier of this Managed Object instance.  

        :param moid: The moid of this VnicFcAdapterPolicy.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this VnicFcAdapterPolicy.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this VnicFcAdapterPolicy.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this VnicFcAdapterPolicy.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this VnicFcAdapterPolicy.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this VnicFcAdapterPolicy.
        The array of owners which represent effective ownership of this object.   

        :return: The owners of this VnicFcAdapterPolicy.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this VnicFcAdapterPolicy.
        The array of owners which represent effective ownership of this object.   

        :param owners: The owners of this VnicFcAdapterPolicy.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this VnicFcAdapterPolicy.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this VnicFcAdapterPolicy.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this VnicFcAdapterPolicy.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this VnicFcAdapterPolicy.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def shared_scope(self):
        """
        Gets the shared_scope of this VnicFcAdapterPolicy.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :return: The shared_scope of this VnicFcAdapterPolicy.
        :rtype: str
        """
        return self._shared_scope

    @shared_scope.setter
    def shared_scope(self, shared_scope):
        """
        Sets the shared_scope of this VnicFcAdapterPolicy.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :param shared_scope: The shared_scope of this VnicFcAdapterPolicy.
        :type: str
        """

        self._shared_scope = shared_scope

    @property
    def tags(self):
        """
        Gets the tags of this VnicFcAdapterPolicy.
        The array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this VnicFcAdapterPolicy.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this VnicFcAdapterPolicy.
        The array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this VnicFcAdapterPolicy.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this VnicFcAdapterPolicy.
        The versioning info for this managed object.   

        :return: The version_context of this VnicFcAdapterPolicy.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this VnicFcAdapterPolicy.
        The versioning info for this managed object.   

        :param version_context: The version_context of this VnicFcAdapterPolicy.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def description(self):
        """
        Gets the description of this VnicFcAdapterPolicy.
        Description of the policy.  

        :return: The description of this VnicFcAdapterPolicy.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this VnicFcAdapterPolicy.
        Description of the policy.  

        :param description: The description of this VnicFcAdapterPolicy.
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """
        Gets the name of this VnicFcAdapterPolicy.
        Name of the concrete policy.   

        :return: The name of this VnicFcAdapterPolicy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this VnicFcAdapterPolicy.
        Name of the concrete policy.   

        :param name: The name of this VnicFcAdapterPolicy.
        :type: str
        """

        self._name = name

    @property
    def error_detection_timeout(self):
        """
        Gets the error_detection_timeout of this VnicFcAdapterPolicy.
        Error Detection Timeout, also referred to as EDTOV, is the number of milliseconds to wait before the system assumes that an error has occurred.  

        :return: The error_detection_timeout of this VnicFcAdapterPolicy.
        :rtype: int
        """
        return self._error_detection_timeout

    @error_detection_timeout.setter
    def error_detection_timeout(self, error_detection_timeout):
        """
        Sets the error_detection_timeout of this VnicFcAdapterPolicy.
        Error Detection Timeout, also referred to as EDTOV, is the number of milliseconds to wait before the system assumes that an error has occurred.  

        :param error_detection_timeout: The error_detection_timeout of this VnicFcAdapterPolicy.
        :type: int
        """

        self._error_detection_timeout = error_detection_timeout

    @property
    def error_recovery_settings(self):
        """
        Gets the error_recovery_settings of this VnicFcAdapterPolicy.
        Fibre Channel Error Recovery Settings.  

        :return: The error_recovery_settings of this VnicFcAdapterPolicy.
        :rtype: VnicFcErrorRecoverySettings
        """
        return self._error_recovery_settings

    @error_recovery_settings.setter
    def error_recovery_settings(self, error_recovery_settings):
        """
        Sets the error_recovery_settings of this VnicFcAdapterPolicy.
        Fibre Channel Error Recovery Settings.  

        :param error_recovery_settings: The error_recovery_settings of this VnicFcAdapterPolicy.
        :type: VnicFcErrorRecoverySettings
        """

        self._error_recovery_settings = error_recovery_settings

    @property
    def flogi_settings(self):
        """
        Gets the flogi_settings of this VnicFcAdapterPolicy.
        Fibre Channel Flogi Settings.  

        :return: The flogi_settings of this VnicFcAdapterPolicy.
        :rtype: VnicFlogiSettings
        """
        return self._flogi_settings

    @flogi_settings.setter
    def flogi_settings(self, flogi_settings):
        """
        Sets the flogi_settings of this VnicFcAdapterPolicy.
        Fibre Channel Flogi Settings.  

        :param flogi_settings: The flogi_settings of this VnicFcAdapterPolicy.
        :type: VnicFlogiSettings
        """

        self._flogi_settings = flogi_settings

    @property
    def interrupt_settings(self):
        """
        Gets the interrupt_settings of this VnicFcAdapterPolicy.
        Interrupt Settings for the virtual fibre channel interface.  

        :return: The interrupt_settings of this VnicFcAdapterPolicy.
        :rtype: VnicFcInterruptSettings
        """
        return self._interrupt_settings

    @interrupt_settings.setter
    def interrupt_settings(self, interrupt_settings):
        """
        Sets the interrupt_settings of this VnicFcAdapterPolicy.
        Interrupt Settings for the virtual fibre channel interface.  

        :param interrupt_settings: The interrupt_settings of this VnicFcAdapterPolicy.
        :type: VnicFcInterruptSettings
        """

        self._interrupt_settings = interrupt_settings

    @property
    def io_throttle_count(self):
        """
        Gets the io_throttle_count of this VnicFcAdapterPolicy.
        The maximum number of data or control I/O operations that can be pending for the virtual interface at one time. If this value is exceeded, the additional I/O operations wait in the queue until the number of pending I/O operations decreases and the additional operations can be processed.  

        :return: The io_throttle_count of this VnicFcAdapterPolicy.
        :rtype: int
        """
        return self._io_throttle_count

    @io_throttle_count.setter
    def io_throttle_count(self, io_throttle_count):
        """
        Sets the io_throttle_count of this VnicFcAdapterPolicy.
        The maximum number of data or control I/O operations that can be pending for the virtual interface at one time. If this value is exceeded, the additional I/O operations wait in the queue until the number of pending I/O operations decreases and the additional operations can be processed.  

        :param io_throttle_count: The io_throttle_count of this VnicFcAdapterPolicy.
        :type: int
        """

        self._io_throttle_count = io_throttle_count

    @property
    def lun_count(self):
        """
        Gets the lun_count of this VnicFcAdapterPolicy.
        The maximum number of LUNs that the Fibre Channel driver will export or show. The maximum number of LUNs is usually controlled by the operating system running on the server.  

        :return: The lun_count of this VnicFcAdapterPolicy.
        :rtype: int
        """
        return self._lun_count

    @lun_count.setter
    def lun_count(self, lun_count):
        """
        Sets the lun_count of this VnicFcAdapterPolicy.
        The maximum number of LUNs that the Fibre Channel driver will export or show. The maximum number of LUNs is usually controlled by the operating system running on the server.  

        :param lun_count: The lun_count of this VnicFcAdapterPolicy.
        :type: int
        """

        self._lun_count = lun_count

    @property
    def lun_queue_depth(self):
        """
        Gets the lun_queue_depth of this VnicFcAdapterPolicy.
        The number of commands that the HBA can send and receive in a single transmission per LUN.  

        :return: The lun_queue_depth of this VnicFcAdapterPolicy.
        :rtype: int
        """
        return self._lun_queue_depth

    @lun_queue_depth.setter
    def lun_queue_depth(self, lun_queue_depth):
        """
        Sets the lun_queue_depth of this VnicFcAdapterPolicy.
        The number of commands that the HBA can send and receive in a single transmission per LUN.  

        :param lun_queue_depth: The lun_queue_depth of this VnicFcAdapterPolicy.
        :type: int
        """

        self._lun_queue_depth = lun_queue_depth

    @property
    def organization(self):
        """
        Gets the organization of this VnicFcAdapterPolicy.
        Relationship to the Organization that owns the Managed Object. 

        :return: The organization of this VnicFcAdapterPolicy.
        :rtype: IamAccountRef
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """
        Sets the organization of this VnicFcAdapterPolicy.
        Relationship to the Organization that owns the Managed Object. 

        :param organization: The organization of this VnicFcAdapterPolicy.
        :type: IamAccountRef
        """

        self._organization = organization

    @property
    def plogi_settings(self):
        """
        Gets the plogi_settings of this VnicFcAdapterPolicy.
        Fibre Channel Plogi Settings.  

        :return: The plogi_settings of this VnicFcAdapterPolicy.
        :rtype: VnicPlogiSettings
        """
        return self._plogi_settings

    @plogi_settings.setter
    def plogi_settings(self, plogi_settings):
        """
        Sets the plogi_settings of this VnicFcAdapterPolicy.
        Fibre Channel Plogi Settings.  

        :param plogi_settings: The plogi_settings of this VnicFcAdapterPolicy.
        :type: VnicPlogiSettings
        """

        self._plogi_settings = plogi_settings

    @property
    def resource_allocation_timeout(self):
        """
        Gets the resource_allocation_timeout of this VnicFcAdapterPolicy.
        Resource Allocation Timeout, also referred to as RATOV, is the number of milliseconds to wait before the system assumes that a resource cannot be properly allocated.  

        :return: The resource_allocation_timeout of this VnicFcAdapterPolicy.
        :rtype: int
        """
        return self._resource_allocation_timeout

    @resource_allocation_timeout.setter
    def resource_allocation_timeout(self, resource_allocation_timeout):
        """
        Sets the resource_allocation_timeout of this VnicFcAdapterPolicy.
        Resource Allocation Timeout, also referred to as RATOV, is the number of milliseconds to wait before the system assumes that a resource cannot be properly allocated.  

        :param resource_allocation_timeout: The resource_allocation_timeout of this VnicFcAdapterPolicy.
        :type: int
        """

        self._resource_allocation_timeout = resource_allocation_timeout

    @property
    def rx_queue_settings(self):
        """
        Gets the rx_queue_settings of this VnicFcAdapterPolicy.
        Fibre Channel Receive Queue Settings.  

        :return: The rx_queue_settings of this VnicFcAdapterPolicy.
        :rtype: VnicFcQueueSettings
        """
        return self._rx_queue_settings

    @rx_queue_settings.setter
    def rx_queue_settings(self, rx_queue_settings):
        """
        Sets the rx_queue_settings of this VnicFcAdapterPolicy.
        Fibre Channel Receive Queue Settings.  

        :param rx_queue_settings: The rx_queue_settings of this VnicFcAdapterPolicy.
        :type: VnicFcQueueSettings
        """

        self._rx_queue_settings = rx_queue_settings

    @property
    def scsi_queue_settings(self):
        """
        Gets the scsi_queue_settings of this VnicFcAdapterPolicy.
        SCSI Input/Output Queue Settings.  

        :return: The scsi_queue_settings of this VnicFcAdapterPolicy.
        :rtype: VnicScsiQueueSettings
        """
        return self._scsi_queue_settings

    @scsi_queue_settings.setter
    def scsi_queue_settings(self, scsi_queue_settings):
        """
        Sets the scsi_queue_settings of this VnicFcAdapterPolicy.
        SCSI Input/Output Queue Settings.  

        :param scsi_queue_settings: The scsi_queue_settings of this VnicFcAdapterPolicy.
        :type: VnicScsiQueueSettings
        """

        self._scsi_queue_settings = scsi_queue_settings

    @property
    def tx_queue_settings(self):
        """
        Gets the tx_queue_settings of this VnicFcAdapterPolicy.
        Fibre Channel Transmit Queue Settings.   

        :return: The tx_queue_settings of this VnicFcAdapterPolicy.
        :rtype: VnicFcQueueSettings
        """
        return self._tx_queue_settings

    @tx_queue_settings.setter
    def tx_queue_settings(self, tx_queue_settings):
        """
        Sets the tx_queue_settings of this VnicFcAdapterPolicy.
        Fibre Channel Transmit Queue Settings.   

        :param tx_queue_settings: The tx_queue_settings of this VnicFcAdapterPolicy.
        :type: VnicFcQueueSettings
        """

        self._tx_queue_settings = tx_queue_settings

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
        if not isinstance(other, VnicFcAdapterPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
