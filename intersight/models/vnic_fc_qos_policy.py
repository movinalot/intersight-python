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


class VnicFcQosPolicy(object):
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
        'cos': 'int',
        'max_data_field_size': 'int',
        'organization': 'IamAccountRef',
        'rate_limit': 'int'
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
        'cos': 'Cos',
        'max_data_field_size': 'MaxDataFieldSize',
        'organization': 'Organization',
        'rate_limit': 'RateLimit'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, domain_group_moid=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, shared_scope=None, tags=None, version_context=None, description=None, name=None, cos=None, max_data_field_size=None, organization=None, rate_limit=None):
        """
        VnicFcQosPolicy - a model defined in Swagger
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
        self._cos = None
        self._max_data_field_size = None
        self._organization = None
        self._rate_limit = None

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
        if cos is not None:
          self.cos = cos
        if max_data_field_size is not None:
          self.max_data_field_size = max_data_field_size
        if organization is not None:
          self.organization = organization
        if rate_limit is not None:
          self.rate_limit = rate_limit

    @property
    def account_moid(self):
        """
        Gets the account_moid of this VnicFcQosPolicy.
        The Account ID for this managed object.  

        :return: The account_moid of this VnicFcQosPolicy.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this VnicFcQosPolicy.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this VnicFcQosPolicy.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this VnicFcQosPolicy.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this VnicFcQosPolicy.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this VnicFcQosPolicy.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this VnicFcQosPolicy.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this VnicFcQosPolicy.
        The time when this managed object was created.  

        :return: The create_time of this VnicFcQosPolicy.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this VnicFcQosPolicy.
        The time when this managed object was created.  

        :param create_time: The create_time of this VnicFcQosPolicy.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def domain_group_moid(self):
        """
        Gets the domain_group_moid of this VnicFcQosPolicy.
        The DomainGroup ID for this managed object.  

        :return: The domain_group_moid of this VnicFcQosPolicy.
        :rtype: str
        """
        return self._domain_group_moid

    @domain_group_moid.setter
    def domain_group_moid(self, domain_group_moid):
        """
        Sets the domain_group_moid of this VnicFcQosPolicy.
        The DomainGroup ID for this managed object.  

        :param domain_group_moid: The domain_group_moid of this VnicFcQosPolicy.
        :type: str
        """

        self._domain_group_moid = domain_group_moid

    @property
    def mod_time(self):
        """
        Gets the mod_time of this VnicFcQosPolicy.
        The time when this managed object was last modified.  

        :return: The mod_time of this VnicFcQosPolicy.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this VnicFcQosPolicy.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this VnicFcQosPolicy.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this VnicFcQosPolicy.
        The unique identifier of this Managed Object instance.  

        :return: The moid of this VnicFcQosPolicy.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this VnicFcQosPolicy.
        The unique identifier of this Managed Object instance.  

        :param moid: The moid of this VnicFcQosPolicy.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this VnicFcQosPolicy.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this VnicFcQosPolicy.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this VnicFcQosPolicy.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this VnicFcQosPolicy.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this VnicFcQosPolicy.
        The array of owners which represent effective ownership of this object.   

        :return: The owners of this VnicFcQosPolicy.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this VnicFcQosPolicy.
        The array of owners which represent effective ownership of this object.   

        :param owners: The owners of this VnicFcQosPolicy.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this VnicFcQosPolicy.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this VnicFcQosPolicy.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this VnicFcQosPolicy.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this VnicFcQosPolicy.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def shared_scope(self):
        """
        Gets the shared_scope of this VnicFcQosPolicy.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :return: The shared_scope of this VnicFcQosPolicy.
        :rtype: str
        """
        return self._shared_scope

    @shared_scope.setter
    def shared_scope(self, shared_scope):
        """
        Sets the shared_scope of this VnicFcQosPolicy.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :param shared_scope: The shared_scope of this VnicFcQosPolicy.
        :type: str
        """

        self._shared_scope = shared_scope

    @property
    def tags(self):
        """
        Gets the tags of this VnicFcQosPolicy.
        The array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this VnicFcQosPolicy.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this VnicFcQosPolicy.
        The array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this VnicFcQosPolicy.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this VnicFcQosPolicy.
        The versioning info for this managed object.   

        :return: The version_context of this VnicFcQosPolicy.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this VnicFcQosPolicy.
        The versioning info for this managed object.   

        :param version_context: The version_context of this VnicFcQosPolicy.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def description(self):
        """
        Gets the description of this VnicFcQosPolicy.
        Description of the policy.  

        :return: The description of this VnicFcQosPolicy.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this VnicFcQosPolicy.
        Description of the policy.  

        :param description: The description of this VnicFcQosPolicy.
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """
        Gets the name of this VnicFcQosPolicy.
        Name of the concrete policy.   

        :return: The name of this VnicFcQosPolicy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this VnicFcQosPolicy.
        Name of the concrete policy.   

        :param name: The name of this VnicFcQosPolicy.
        :type: str
        """

        self._name = name

    @property
    def cos(self):
        """
        Gets the cos of this VnicFcQosPolicy.
        Class of Service to be associated to the traffic on the virtual interface.  

        :return: The cos of this VnicFcQosPolicy.
        :rtype: int
        """
        return self._cos

    @cos.setter
    def cos(self, cos):
        """
        Sets the cos of this VnicFcQosPolicy.
        Class of Service to be associated to the traffic on the virtual interface.  

        :param cos: The cos of this VnicFcQosPolicy.
        :type: int
        """

        self._cos = cos

    @property
    def max_data_field_size(self):
        """
        Gets the max_data_field_size of this VnicFcQosPolicy.
        The maximum size of the Fibre Channel frame payload bytes that the virtual interface supports.  

        :return: The max_data_field_size of this VnicFcQosPolicy.
        :rtype: int
        """
        return self._max_data_field_size

    @max_data_field_size.setter
    def max_data_field_size(self, max_data_field_size):
        """
        Sets the max_data_field_size of this VnicFcQosPolicy.
        The maximum size of the Fibre Channel frame payload bytes that the virtual interface supports.  

        :param max_data_field_size: The max_data_field_size of this VnicFcQosPolicy.
        :type: int
        """

        self._max_data_field_size = max_data_field_size

    @property
    def organization(self):
        """
        Gets the organization of this VnicFcQosPolicy.
        Relationship to the Organization that owns the Managed Object. 

        :return: The organization of this VnicFcQosPolicy.
        :rtype: IamAccountRef
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """
        Sets the organization of this VnicFcQosPolicy.
        Relationship to the Organization that owns the Managed Object. 

        :param organization: The organization of this VnicFcQosPolicy.
        :type: IamAccountRef
        """

        self._organization = organization

    @property
    def rate_limit(self):
        """
        Gets the rate_limit of this VnicFcQosPolicy.
        The value in Mbps to use for limiting the data rate on the virtual interface. Setting this to zero will turn rate limiting off.   

        :return: The rate_limit of this VnicFcQosPolicy.
        :rtype: int
        """
        return self._rate_limit

    @rate_limit.setter
    def rate_limit(self, rate_limit):
        """
        Sets the rate_limit of this VnicFcQosPolicy.
        The value in Mbps to use for limiting the data rate on the virtual interface. Setting this to zero will turn rate limiting off.   

        :param rate_limit: The rate_limit of this VnicFcQosPolicy.
        :type: int
        """

        self._rate_limit = rate_limit

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
        if not isinstance(other, VnicFcQosPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
