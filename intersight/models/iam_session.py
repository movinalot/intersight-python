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


class IamSession(object):
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
        'account_permissions': 'list[IamAccountPermissions]',
        'client_ip_address': 'str',
        'expiration': 'datetime',
        'idle_time_expiration': 'datetime',
        'last_login_client': 'str',
        'last_login_time': 'datetime',
        'permission': 'IamPermissionRef',
        'user': 'IamUserRef'
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
        'account_permissions': 'AccountPermissions',
        'client_ip_address': 'ClientIpAddress',
        'expiration': 'Expiration',
        'idle_time_expiration': 'IdleTimeExpiration',
        'last_login_client': 'LastLoginClient',
        'last_login_time': 'LastLoginTime',
        'permission': 'Permission',
        'user': 'User'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, domain_group_moid=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, shared_scope=None, tags=None, version_context=None, account_permissions=None, client_ip_address=None, expiration=None, idle_time_expiration=None, last_login_client=None, last_login_time=None, permission=None, user=None):
        """
        IamSession - a model defined in Swagger
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
        self._account_permissions = None
        self._client_ip_address = None
        self._expiration = None
        self._idle_time_expiration = None
        self._last_login_client = None
        self._last_login_time = None
        self._permission = None
        self._user = None

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
        if account_permissions is not None:
          self.account_permissions = account_permissions
        if client_ip_address is not None:
          self.client_ip_address = client_ip_address
        if expiration is not None:
          self.expiration = expiration
        if idle_time_expiration is not None:
          self.idle_time_expiration = idle_time_expiration
        if last_login_client is not None:
          self.last_login_client = last_login_client
        if last_login_time is not None:
          self.last_login_time = last_login_time
        if permission is not None:
          self.permission = permission
        if user is not None:
          self.user = user

    @property
    def account_moid(self):
        """
        Gets the account_moid of this IamSession.
        The Account ID for this managed object.  

        :return: The account_moid of this IamSession.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this IamSession.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this IamSession.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this IamSession.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this IamSession.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this IamSession.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this IamSession.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this IamSession.
        The time when this managed object was created.  

        :return: The create_time of this IamSession.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this IamSession.
        The time when this managed object was created.  

        :param create_time: The create_time of this IamSession.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def domain_group_moid(self):
        """
        Gets the domain_group_moid of this IamSession.
        The DomainGroup ID for this managed object.  

        :return: The domain_group_moid of this IamSession.
        :rtype: str
        """
        return self._domain_group_moid

    @domain_group_moid.setter
    def domain_group_moid(self, domain_group_moid):
        """
        Sets the domain_group_moid of this IamSession.
        The DomainGroup ID for this managed object.  

        :param domain_group_moid: The domain_group_moid of this IamSession.
        :type: str
        """

        self._domain_group_moid = domain_group_moid

    @property
    def mod_time(self):
        """
        Gets the mod_time of this IamSession.
        The time when this managed object was last modified.  

        :return: The mod_time of this IamSession.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this IamSession.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this IamSession.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this IamSession.
        The unique identifier of this Managed Object instance.  

        :return: The moid of this IamSession.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this IamSession.
        The unique identifier of this Managed Object instance.  

        :param moid: The moid of this IamSession.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this IamSession.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this IamSession.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this IamSession.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this IamSession.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this IamSession.
        The array of owners which represent effective ownership of this object.   

        :return: The owners of this IamSession.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this IamSession.
        The array of owners which represent effective ownership of this object.   

        :param owners: The owners of this IamSession.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this IamSession.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this IamSession.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this IamSession.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this IamSession.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def shared_scope(self):
        """
        Gets the shared_scope of this IamSession.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :return: The shared_scope of this IamSession.
        :rtype: str
        """
        return self._shared_scope

    @shared_scope.setter
    def shared_scope(self, shared_scope):
        """
        Sets the shared_scope of this IamSession.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :param shared_scope: The shared_scope of this IamSession.
        :type: str
        """

        self._shared_scope = shared_scope

    @property
    def tags(self):
        """
        Gets the tags of this IamSession.
        The array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this IamSession.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this IamSession.
        The array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this IamSession.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this IamSession.
        The versioning info for this managed object.   

        :return: The version_context of this IamSession.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this IamSession.
        The versioning info for this managed object.   

        :param version_context: The version_context of this IamSession.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def account_permissions(self):
        """
        Gets the account_permissions of this IamSession.
        The accounts and the permissions within each account which a user can select after authentication. After authentication if user has access to multiple permissions, then user and session object are created in onboarding user account and asked to select one of these permissions.  

        :return: The account_permissions of this IamSession.
        :rtype: list[IamAccountPermissions]
        """
        return self._account_permissions

    @account_permissions.setter
    def account_permissions(self, account_permissions):
        """
        Sets the account_permissions of this IamSession.
        The accounts and the permissions within each account which a user can select after authentication. After authentication if user has access to multiple permissions, then user and session object are created in onboarding user account and asked to select one of these permissions.  

        :param account_permissions: The account_permissions of this IamSession.
        :type: list[IamAccountPermissions]
        """

        self._account_permissions = account_permissions

    @property
    def client_ip_address(self):
        """
        Gets the client_ip_address of this IamSession.
        The user agent IP address from which the session is launched.  

        :return: The client_ip_address of this IamSession.
        :rtype: str
        """
        return self._client_ip_address

    @client_ip_address.setter
    def client_ip_address(self, client_ip_address):
        """
        Sets the client_ip_address of this IamSession.
        The user agent IP address from which the session is launched.  

        :param client_ip_address: The client_ip_address of this IamSession.
        :type: str
        """

        self._client_ip_address = client_ip_address

    @property
    def expiration(self):
        """
        Gets the expiration of this IamSession.
        Expiration time for the session.  

        :return: The expiration of this IamSession.
        :rtype: datetime
        """
        return self._expiration

    @expiration.setter
    def expiration(self, expiration):
        """
        Sets the expiration of this IamSession.
        Expiration time for the session.  

        :param expiration: The expiration of this IamSession.
        :type: datetime
        """

        self._expiration = expiration

    @property
    def idle_time_expiration(self):
        """
        Gets the idle_time_expiration of this IamSession.
        Idle time expiration for the session.  

        :return: The idle_time_expiration of this IamSession.
        :rtype: datetime
        """
        return self._idle_time_expiration

    @idle_time_expiration.setter
    def idle_time_expiration(self, idle_time_expiration):
        """
        Sets the idle_time_expiration of this IamSession.
        Idle time expiration for the session.  

        :param idle_time_expiration: The idle_time_expiration of this IamSession.
        :type: datetime
        """

        self._idle_time_expiration = idle_time_expiration

    @property
    def last_login_client(self):
        """
        Gets the last_login_client of this IamSession.
        The client address from which last login is initiated.  

        :return: The last_login_client of this IamSession.
        :rtype: str
        """
        return self._last_login_client

    @last_login_client.setter
    def last_login_client(self, last_login_client):
        """
        Sets the last_login_client of this IamSession.
        The client address from which last login is initiated.  

        :param last_login_client: The last_login_client of this IamSession.
        :type: str
        """

        self._last_login_client = last_login_client

    @property
    def last_login_time(self):
        """
        Gets the last_login_time of this IamSession.
        The last login time for user.      

        :return: The last_login_time of this IamSession.
        :rtype: datetime
        """
        return self._last_login_time

    @last_login_time.setter
    def last_login_time(self, last_login_time):
        """
        Sets the last_login_time of this IamSession.
        The last login time for user.      

        :param last_login_time: The last_login_time of this IamSession.
        :type: datetime
        """

        self._last_login_time = last_login_time

    @property
    def permission(self):
        """
        Gets the permission of this IamSession.
        Permissions associated with the web session. Permission provides a way to assign roles to a user or user group to perform operations on object hierarchy. 

        :return: The permission of this IamSession.
        :rtype: IamPermissionRef
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """
        Sets the permission of this IamSession.
        Permissions associated with the web session. Permission provides a way to assign roles to a user or user group to perform operations on object hierarchy. 

        :param permission: The permission of this IamSession.
        :type: IamPermissionRef
        """

        self._permission = permission

    @property
    def user(self):
        """
        Gets the user of this IamSession.
        A collection of references to the [iam.User](mo://iam.User) Managed Object.  When this managed object is deleted, the referenced [iam.User](mo://iam.User) MO unsets its reference to this deleted MO. 

        :return: The user of this IamSession.
        :rtype: IamUserRef
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this IamSession.
        A collection of references to the [iam.User](mo://iam.User) Managed Object.  When this managed object is deleted, the referenced [iam.User](mo://iam.User) MO unsets its reference to this deleted MO. 

        :param user: The user of this IamSession.
        :type: IamUserRef
        """

        self._user = user

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
        if not isinstance(other, IamSession):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
