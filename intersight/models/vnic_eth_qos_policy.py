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


class VnicEthQosPolicy(object):
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
        'mtu': 'int',
        'organization': 'IamAccountRef',
        'rate_limit': 'int',
        'trust_host_cos': 'bool'
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
        'mtu': 'Mtu',
        'organization': 'Organization',
        'rate_limit': 'RateLimit',
        'trust_host_cos': 'TrustHostCos'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, domain_group_moid=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, shared_scope=None, tags=None, version_context=None, description=None, name=None, cos=None, mtu=None, organization=None, rate_limit=None, trust_host_cos=None):
        """
        VnicEthQosPolicy - a model defined in Swagger
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
        self._mtu = None
        self._organization = None
        self._rate_limit = None
        self._trust_host_cos = None

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
        if mtu is not None:
          self.mtu = mtu
        if organization is not None:
          self.organization = organization
        if rate_limit is not None:
          self.rate_limit = rate_limit
        if trust_host_cos is not None:
          self.trust_host_cos = trust_host_cos

    @property
    def account_moid(self):
        """
        Gets the account_moid of this VnicEthQosPolicy.
        The Account ID for this managed object.  

        :return: The account_moid of this VnicEthQosPolicy.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this VnicEthQosPolicy.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this VnicEthQosPolicy.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this VnicEthQosPolicy.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this VnicEthQosPolicy.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this VnicEthQosPolicy.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this VnicEthQosPolicy.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this VnicEthQosPolicy.
        The time when this managed object was created.  

        :return: The create_time of this VnicEthQosPolicy.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this VnicEthQosPolicy.
        The time when this managed object was created.  

        :param create_time: The create_time of this VnicEthQosPolicy.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def domain_group_moid(self):
        """
        Gets the domain_group_moid of this VnicEthQosPolicy.
        The DomainGroup ID for this managed object.  

        :return: The domain_group_moid of this VnicEthQosPolicy.
        :rtype: str
        """
        return self._domain_group_moid

    @domain_group_moid.setter
    def domain_group_moid(self, domain_group_moid):
        """
        Sets the domain_group_moid of this VnicEthQosPolicy.
        The DomainGroup ID for this managed object.  

        :param domain_group_moid: The domain_group_moid of this VnicEthQosPolicy.
        :type: str
        """

        self._domain_group_moid = domain_group_moid

    @property
    def mod_time(self):
        """
        Gets the mod_time of this VnicEthQosPolicy.
        The time when this managed object was last modified.  

        :return: The mod_time of this VnicEthQosPolicy.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this VnicEthQosPolicy.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this VnicEthQosPolicy.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this VnicEthQosPolicy.
        The unique identifier of this Managed Object instance.  

        :return: The moid of this VnicEthQosPolicy.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this VnicEthQosPolicy.
        The unique identifier of this Managed Object instance.  

        :param moid: The moid of this VnicEthQosPolicy.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this VnicEthQosPolicy.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this VnicEthQosPolicy.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this VnicEthQosPolicy.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this VnicEthQosPolicy.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this VnicEthQosPolicy.
        The array of owners which represent effective ownership of this object.   

        :return: The owners of this VnicEthQosPolicy.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this VnicEthQosPolicy.
        The array of owners which represent effective ownership of this object.   

        :param owners: The owners of this VnicEthQosPolicy.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this VnicEthQosPolicy.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this VnicEthQosPolicy.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this VnicEthQosPolicy.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this VnicEthQosPolicy.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def shared_scope(self):
        """
        Gets the shared_scope of this VnicEthQosPolicy.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :return: The shared_scope of this VnicEthQosPolicy.
        :rtype: str
        """
        return self._shared_scope

    @shared_scope.setter
    def shared_scope(self, shared_scope):
        """
        Sets the shared_scope of this VnicEthQosPolicy.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :param shared_scope: The shared_scope of this VnicEthQosPolicy.
        :type: str
        """

        self._shared_scope = shared_scope

    @property
    def tags(self):
        """
        Gets the tags of this VnicEthQosPolicy.
        The array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this VnicEthQosPolicy.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this VnicEthQosPolicy.
        The array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this VnicEthQosPolicy.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this VnicEthQosPolicy.
        The versioning info for this managed object.   

        :return: The version_context of this VnicEthQosPolicy.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this VnicEthQosPolicy.
        The versioning info for this managed object.   

        :param version_context: The version_context of this VnicEthQosPolicy.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def description(self):
        """
        Gets the description of this VnicEthQosPolicy.
        Description of the policy.  

        :return: The description of this VnicEthQosPolicy.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this VnicEthQosPolicy.
        Description of the policy.  

        :param description: The description of this VnicEthQosPolicy.
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """
        Gets the name of this VnicEthQosPolicy.
        Name of the concrete policy.   

        :return: The name of this VnicEthQosPolicy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this VnicEthQosPolicy.
        Name of the concrete policy.   

        :param name: The name of this VnicEthQosPolicy.
        :type: str
        """

        self._name = name

    @property
    def cos(self):
        """
        Gets the cos of this VnicEthQosPolicy.
        Class of Service to be associated to the traffic on the virtual interface.  

        :return: The cos of this VnicEthQosPolicy.
        :rtype: int
        """
        return self._cos

    @cos.setter
    def cos(self, cos):
        """
        Sets the cos of this VnicEthQosPolicy.
        Class of Service to be associated to the traffic on the virtual interface.  

        :param cos: The cos of this VnicEthQosPolicy.
        :type: int
        """

        self._cos = cos

    @property
    def mtu(self):
        """
        Gets the mtu of this VnicEthQosPolicy.
        The Maximum Transmission Unit (MTU) or packet size that the virtual interface accepts.  

        :return: The mtu of this VnicEthQosPolicy.
        :rtype: int
        """
        return self._mtu

    @mtu.setter
    def mtu(self, mtu):
        """
        Sets the mtu of this VnicEthQosPolicy.
        The Maximum Transmission Unit (MTU) or packet size that the virtual interface accepts.  

        :param mtu: The mtu of this VnicEthQosPolicy.
        :type: int
        """

        self._mtu = mtu

    @property
    def organization(self):
        """
        Gets the organization of this VnicEthQosPolicy.
        Relationship to the Organization that owns the Managed Object. 

        :return: The organization of this VnicEthQosPolicy.
        :rtype: IamAccountRef
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """
        Sets the organization of this VnicEthQosPolicy.
        Relationship to the Organization that owns the Managed Object. 

        :param organization: The organization of this VnicEthQosPolicy.
        :type: IamAccountRef
        """

        self._organization = organization

    @property
    def rate_limit(self):
        """
        Gets the rate_limit of this VnicEthQosPolicy.
        The value in Mbps (0-40000) to use for limiting the data rate on the virtual interface. Setting this to zero will turn rate limiting off.  

        :return: The rate_limit of this VnicEthQosPolicy.
        :rtype: int
        """
        return self._rate_limit

    @rate_limit.setter
    def rate_limit(self, rate_limit):
        """
        Sets the rate_limit of this VnicEthQosPolicy.
        The value in Mbps (0-40000) to use for limiting the data rate on the virtual interface. Setting this to zero will turn rate limiting off.  

        :param rate_limit: The rate_limit of this VnicEthQosPolicy.
        :type: int
        """

        self._rate_limit = rate_limit

    @property
    def trust_host_cos(self):
        """
        Gets the trust_host_cos of this VnicEthQosPolicy.
        Enables usage of the Class of Service provided by the operating system.   

        :return: The trust_host_cos of this VnicEthQosPolicy.
        :rtype: bool
        """
        return self._trust_host_cos

    @trust_host_cos.setter
    def trust_host_cos(self, trust_host_cos):
        """
        Sets the trust_host_cos of this VnicEthQosPolicy.
        Enables usage of the Class of Service provided by the operating system.   

        :param trust_host_cos: The trust_host_cos of this VnicEthQosPolicy.
        :type: bool
        """

        self._trust_host_cos = trust_host_cos

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
        if not isinstance(other, VnicEthQosPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
