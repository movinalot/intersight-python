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


class ServerConfigImport(object):
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
        'organization': 'IamAccountRef',
        'policy_prefix': 'str',
        'policy_types': 'list[str]',
        'profile_name': 'str',
        'server': 'ComputeRackUnitRef',
        'server_profile': 'ServerProfileRef'
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
        'organization': 'Organization',
        'policy_prefix': 'PolicyPrefix',
        'policy_types': 'PolicyTypes',
        'profile_name': 'ProfileName',
        'server': 'Server',
        'server_profile': 'ServerProfile'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, domain_group_moid=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, shared_scope=None, tags=None, version_context=None, description=None, organization=None, policy_prefix=None, policy_types=None, profile_name=None, server=None, server_profile=None):
        """
        ServerConfigImport - a model defined in Swagger
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
        self._organization = None
        self._policy_prefix = None
        self._policy_types = None
        self._profile_name = None
        self._server = None
        self._server_profile = None

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
        if organization is not None:
          self.organization = organization
        if policy_prefix is not None:
          self.policy_prefix = policy_prefix
        if policy_types is not None:
          self.policy_types = policy_types
        if profile_name is not None:
          self.profile_name = profile_name
        if server is not None:
          self.server = server
        if server_profile is not None:
          self.server_profile = server_profile

    @property
    def account_moid(self):
        """
        Gets the account_moid of this ServerConfigImport.
        The Account ID for this managed object.  

        :return: The account_moid of this ServerConfigImport.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this ServerConfigImport.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this ServerConfigImport.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this ServerConfigImport.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this ServerConfigImport.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this ServerConfigImport.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this ServerConfigImport.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this ServerConfigImport.
        The time when this managed object was created.  

        :return: The create_time of this ServerConfigImport.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this ServerConfigImport.
        The time when this managed object was created.  

        :param create_time: The create_time of this ServerConfigImport.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def domain_group_moid(self):
        """
        Gets the domain_group_moid of this ServerConfigImport.
        The DomainGroup ID for this managed object.  

        :return: The domain_group_moid of this ServerConfigImport.
        :rtype: str
        """
        return self._domain_group_moid

    @domain_group_moid.setter
    def domain_group_moid(self, domain_group_moid):
        """
        Sets the domain_group_moid of this ServerConfigImport.
        The DomainGroup ID for this managed object.  

        :param domain_group_moid: The domain_group_moid of this ServerConfigImport.
        :type: str
        """

        self._domain_group_moid = domain_group_moid

    @property
    def mod_time(self):
        """
        Gets the mod_time of this ServerConfigImport.
        The time when this managed object was last modified.  

        :return: The mod_time of this ServerConfigImport.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this ServerConfigImport.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this ServerConfigImport.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this ServerConfigImport.
        The unique identifier of this Managed Object instance.  

        :return: The moid of this ServerConfigImport.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this ServerConfigImport.
        The unique identifier of this Managed Object instance.  

        :param moid: The moid of this ServerConfigImport.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this ServerConfigImport.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this ServerConfigImport.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this ServerConfigImport.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this ServerConfigImport.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this ServerConfigImport.
        The array of owners which represent effective ownership of this object.   

        :return: The owners of this ServerConfigImport.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this ServerConfigImport.
        The array of owners which represent effective ownership of this object.   

        :param owners: The owners of this ServerConfigImport.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this ServerConfigImport.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this ServerConfigImport.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this ServerConfigImport.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this ServerConfigImport.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def shared_scope(self):
        """
        Gets the shared_scope of this ServerConfigImport.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :return: The shared_scope of this ServerConfigImport.
        :rtype: str
        """
        return self._shared_scope

    @shared_scope.setter
    def shared_scope(self, shared_scope):
        """
        Sets the shared_scope of this ServerConfigImport.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :param shared_scope: The shared_scope of this ServerConfigImport.
        :type: str
        """

        self._shared_scope = shared_scope

    @property
    def tags(self):
        """
        Gets the tags of this ServerConfigImport.
        The array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this ServerConfigImport.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this ServerConfigImport.
        The array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this ServerConfigImport.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this ServerConfigImport.
        The versioning info for this managed object.   

        :return: The version_context of this ServerConfigImport.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this ServerConfigImport.
        The versioning info for this managed object.   

        :param version_context: The version_context of this ServerConfigImport.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def description(self):
        """
        Gets the description of this ServerConfigImport.
        Description of the imported profile.  

        :return: The description of this ServerConfigImport.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ServerConfigImport.
        Description of the imported profile.  

        :param description: The description of this ServerConfigImport.
        :type: str
        """

        self._description = description

    @property
    def organization(self):
        """
        Gets the organization of this ServerConfigImport.
        Relationship to the Organization that owns the Managed Object. 

        :return: The organization of this ServerConfigImport.
        :rtype: IamAccountRef
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """
        Sets the organization of this ServerConfigImport.
        Relationship to the Organization that owns the Managed Object. 

        :param organization: The organization of this ServerConfigImport.
        :type: IamAccountRef
        """

        self._organization = organization

    @property
    def policy_prefix(self):
        """
        Gets the policy_prefix of this ServerConfigImport.
        Policy prefix for the policies of the imported server profile.  

        :return: The policy_prefix of this ServerConfigImport.
        :rtype: str
        """
        return self._policy_prefix

    @policy_prefix.setter
    def policy_prefix(self, policy_prefix):
        """
        Sets the policy_prefix of this ServerConfigImport.
        Policy prefix for the policies of the imported server profile.  

        :param policy_prefix: The policy_prefix of this ServerConfigImport.
        :type: str
        """

        self._policy_prefix = policy_prefix

    @property
    def policy_types(self):
        """
        Gets the policy_types of this ServerConfigImport.
        Types of the policies to be imported for the imported server profile.  

        :return: The policy_types of this ServerConfigImport.
        :rtype: list[str]
        """
        return self._policy_types

    @policy_types.setter
    def policy_types(self, policy_types):
        """
        Sets the policy_types of this ServerConfigImport.
        Types of the policies to be imported for the imported server profile.  

        :param policy_types: The policy_types of this ServerConfigImport.
        :type: list[str]
        """

        self._policy_types = policy_types

    @property
    def profile_name(self):
        """
        Gets the profile_name of this ServerConfigImport.
        Profile name for the imported server profile.   

        :return: The profile_name of this ServerConfigImport.
        :rtype: str
        """
        return self._profile_name

    @profile_name.setter
    def profile_name(self, profile_name):
        """
        Sets the profile_name of this ServerConfigImport.
        Profile name for the imported server profile.   

        :param profile_name: The profile_name of this ServerConfigImport.
        :type: str
        """

        self._profile_name = profile_name

    @property
    def server(self):
        """
        Gets the server of this ServerConfigImport.
        The physical server on which import action will be triggered. 

        :return: The server of this ServerConfigImport.
        :rtype: ComputeRackUnitRef
        """
        return self._server

    @server.setter
    def server(self, server):
        """
        Sets the server of this ServerConfigImport.
        The physical server on which import action will be triggered. 

        :param server: The server of this ServerConfigImport.
        :type: ComputeRackUnitRef
        """

        self._server = server

    @property
    def server_profile(self):
        """
        Gets the server_profile of this ServerConfigImport.
        The server profile which will be generated upon successful import. 

        :return: The server_profile of this ServerConfigImport.
        :rtype: ServerProfileRef
        """
        return self._server_profile

    @server_profile.setter
    def server_profile(self, server_profile):
        """
        Sets the server_profile of this ServerConfigImport.
        The server profile which will be generated upon successful import. 

        :param server_profile: The server_profile of this ServerConfigImport.
        :type: ServerProfileRef
        """

        self._server_profile = server_profile

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
        if not isinstance(other, ServerConfigImport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
