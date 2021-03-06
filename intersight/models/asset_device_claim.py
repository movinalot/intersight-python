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


class AssetDeviceClaim(object):
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
        'device': 'AssetDeviceRegistrationRef',
        'device_updates': 'list[AssetConnectionControlMessage]',
        'security_token': 'str',
        'serial_number': 'str'
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
        'device': 'Device',
        'device_updates': 'DeviceUpdates',
        'security_token': 'SecurityToken',
        'serial_number': 'SerialNumber'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, domain_group_moid=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, shared_scope=None, tags=None, version_context=None, account=None, device=None, device_updates=None, security_token=None, serial_number=None):
        """
        AssetDeviceClaim - a model defined in Swagger
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
        self._device = None
        self._device_updates = None
        self._security_token = None
        self._serial_number = None

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
        if device is not None:
          self.device = device
        if device_updates is not None:
          self.device_updates = device_updates
        if security_token is not None:
          self.security_token = security_token
        if serial_number is not None:
          self.serial_number = serial_number

    @property
    def account_moid(self):
        """
        Gets the account_moid of this AssetDeviceClaim.
        The Account ID for this managed object.  

        :return: The account_moid of this AssetDeviceClaim.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this AssetDeviceClaim.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this AssetDeviceClaim.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this AssetDeviceClaim.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this AssetDeviceClaim.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this AssetDeviceClaim.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this AssetDeviceClaim.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this AssetDeviceClaim.
        The time when this managed object was created.  

        :return: The create_time of this AssetDeviceClaim.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this AssetDeviceClaim.
        The time when this managed object was created.  

        :param create_time: The create_time of this AssetDeviceClaim.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def domain_group_moid(self):
        """
        Gets the domain_group_moid of this AssetDeviceClaim.
        The DomainGroup ID for this managed object.  

        :return: The domain_group_moid of this AssetDeviceClaim.
        :rtype: str
        """
        return self._domain_group_moid

    @domain_group_moid.setter
    def domain_group_moid(self, domain_group_moid):
        """
        Sets the domain_group_moid of this AssetDeviceClaim.
        The DomainGroup ID for this managed object.  

        :param domain_group_moid: The domain_group_moid of this AssetDeviceClaim.
        :type: str
        """

        self._domain_group_moid = domain_group_moid

    @property
    def mod_time(self):
        """
        Gets the mod_time of this AssetDeviceClaim.
        The time when this managed object was last modified.  

        :return: The mod_time of this AssetDeviceClaim.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this AssetDeviceClaim.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this AssetDeviceClaim.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this AssetDeviceClaim.
        The unique identifier of this Managed Object instance.  

        :return: The moid of this AssetDeviceClaim.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this AssetDeviceClaim.
        The unique identifier of this Managed Object instance.  

        :param moid: The moid of this AssetDeviceClaim.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this AssetDeviceClaim.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this AssetDeviceClaim.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this AssetDeviceClaim.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this AssetDeviceClaim.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this AssetDeviceClaim.
        The array of owners which represent effective ownership of this object.   

        :return: The owners of this AssetDeviceClaim.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this AssetDeviceClaim.
        The array of owners which represent effective ownership of this object.   

        :param owners: The owners of this AssetDeviceClaim.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this AssetDeviceClaim.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this AssetDeviceClaim.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this AssetDeviceClaim.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this AssetDeviceClaim.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def shared_scope(self):
        """
        Gets the shared_scope of this AssetDeviceClaim.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :return: The shared_scope of this AssetDeviceClaim.
        :rtype: str
        """
        return self._shared_scope

    @shared_scope.setter
    def shared_scope(self, shared_scope):
        """
        Sets the shared_scope of this AssetDeviceClaim.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :param shared_scope: The shared_scope of this AssetDeviceClaim.
        :type: str
        """

        self._shared_scope = shared_scope

    @property
    def tags(self):
        """
        Gets the tags of this AssetDeviceClaim.
        The array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this AssetDeviceClaim.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this AssetDeviceClaim.
        The array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this AssetDeviceClaim.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this AssetDeviceClaim.
        The versioning info for this managed object.   

        :return: The version_context of this AssetDeviceClaim.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this AssetDeviceClaim.
        The versioning info for this managed object.   

        :param version_context: The version_context of this AssetDeviceClaim.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def account(self):
        """
        Gets the account of this AssetDeviceClaim.
        The account of the user that has claimed the device. 

        :return: The account of this AssetDeviceClaim.
        :rtype: IamAccountRef
        """
        return self._account

    @account.setter
    def account(self, account):
        """
        Sets the account of this AssetDeviceClaim.
        The account of the user that has claimed the device. 

        :param account: The account of this AssetDeviceClaim.
        :type: IamAccountRef
        """

        self._account = account

    @property
    def device(self):
        """
        Gets the device of this AssetDeviceClaim.
        A collection of references to the [asset.DeviceRegistration](mo://asset.DeviceRegistration) Managed Object.  When this managed object is deleted, the referenced [asset.DeviceRegistration](mo://asset.DeviceRegistration) MO unsets its reference to this deleted MO. 

        :return: The device of this AssetDeviceClaim.
        :rtype: AssetDeviceRegistrationRef
        """
        return self._device

    @device.setter
    def device(self, device):
        """
        Sets the device of this AssetDeviceClaim.
        A collection of references to the [asset.DeviceRegistration](mo://asset.DeviceRegistration) Managed Object.  When this managed object is deleted, the referenced [asset.DeviceRegistration](mo://asset.DeviceRegistration) MO unsets its reference to this deleted MO. 

        :param device: The device of this AssetDeviceClaim.
        :type: AssetDeviceRegistrationRef
        """

        self._device = device

    @property
    def device_updates(self):
        """
        Gets the device_updates of this AssetDeviceClaim.
        The list of devices that underwent change during the claim process.  

        :return: The device_updates of this AssetDeviceClaim.
        :rtype: list[AssetConnectionControlMessage]
        """
        return self._device_updates

    @device_updates.setter
    def device_updates(self, device_updates):
        """
        Sets the device_updates of this AssetDeviceClaim.
        The list of devices that underwent change during the claim process.  

        :param device_updates: The device_updates of this AssetDeviceClaim.
        :type: list[AssetConnectionControlMessage]
        """

        self._device_updates = device_updates

    @property
    def security_token(self):
        """
        Gets the security_token of this AssetDeviceClaim.
        Obtained from the device connector management UI or API (REST endpoint /connector/SecurityTokens).  

        :return: The security_token of this AssetDeviceClaim.
        :rtype: str
        """
        return self._security_token

    @security_token.setter
    def security_token(self, security_token):
        """
        Sets the security_token of this AssetDeviceClaim.
        Obtained from the device connector management UI or API (REST endpoint /connector/SecurityTokens).  

        :param security_token: The security_token of this AssetDeviceClaim.
        :type: str
        """

        self._security_token = security_token

    @property
    def serial_number(self):
        """
        Gets the serial_number of this AssetDeviceClaim.
        Obtained from the device connector management UI or API (REST endpoint /connector/DeviceIdentifiers).   

        :return: The serial_number of this AssetDeviceClaim.
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """
        Sets the serial_number of this AssetDeviceClaim.
        Obtained from the device connector management UI or API (REST endpoint /connector/DeviceIdentifiers).   

        :param serial_number: The serial_number of this AssetDeviceClaim.
        :type: str
        """

        self._serial_number = serial_number

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
        if not isinstance(other, AssetDeviceClaim):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
