# coding: utf-8

"""
    Intersight REST API

    This is Intersight REST API 

    OpenAPI spec version: 1.0.9-228
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class HyperflexLocalCredentialPolicy(object):
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
        'mod_time': 'datetime',
        'moid': 'str',
        'object_type': 'str',
        'owners': 'list[str]',
        'parent': 'MoBaseMoRef',
        'tags': 'list[MoTag]',
        'version_context': 'MoVersionContext',
        'description': 'str',
        'name': 'str',
        'cluster_profiles': 'list[HyperflexClusterProfileRef]',
        'factory_hypervisor_password': 'bool',
        'hxdp_root_pwd': 'str',
        'hypervisor_admin': 'str',
        'hypervisor_admin_pwd': 'str',
        'is_hxdp_root_pwd_set': 'bool',
        'is_hypervisor_admin_pwd_set': 'bool',
        'organization': 'IamAccountRef'
    }

    attribute_map = {
        'account_moid': 'AccountMoid',
        'ancestors': 'Ancestors',
        'create_time': 'CreateTime',
        'mod_time': 'ModTime',
        'moid': 'Moid',
        'object_type': 'ObjectType',
        'owners': 'Owners',
        'parent': 'Parent',
        'tags': 'Tags',
        'version_context': 'VersionContext',
        'description': 'Description',
        'name': 'Name',
        'cluster_profiles': 'ClusterProfiles',
        'factory_hypervisor_password': 'FactoryHypervisorPassword',
        'hxdp_root_pwd': 'HxdpRootPwd',
        'hypervisor_admin': 'HypervisorAdmin',
        'hypervisor_admin_pwd': 'HypervisorAdminPwd',
        'is_hxdp_root_pwd_set': 'IsHxdpRootPwdSet',
        'is_hypervisor_admin_pwd_set': 'IsHypervisorAdminPwdSet',
        'organization': 'Organization'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, version_context=None, description=None, name=None, cluster_profiles=None, factory_hypervisor_password=None, hxdp_root_pwd=None, hypervisor_admin=None, hypervisor_admin_pwd=None, is_hxdp_root_pwd_set=None, is_hypervisor_admin_pwd_set=None, organization=None):
        """
        HyperflexLocalCredentialPolicy - a model defined in Swagger
        """

        self._account_moid = None
        self._ancestors = None
        self._create_time = None
        self._mod_time = None
        self._moid = None
        self._object_type = None
        self._owners = None
        self._parent = None
        self._tags = None
        self._version_context = None
        self._description = None
        self._name = None
        self._cluster_profiles = None
        self._factory_hypervisor_password = None
        self._hxdp_root_pwd = None
        self._hypervisor_admin = None
        self._hypervisor_admin_pwd = None
        self._is_hxdp_root_pwd_set = None
        self._is_hypervisor_admin_pwd_set = None
        self._organization = None

        if account_moid is not None:
          self.account_moid = account_moid
        if ancestors is not None:
          self.ancestors = ancestors
        if create_time is not None:
          self.create_time = create_time
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
        if tags is not None:
          self.tags = tags
        if version_context is not None:
          self.version_context = version_context
        if description is not None:
          self.description = description
        if name is not None:
          self.name = name
        if cluster_profiles is not None:
          self.cluster_profiles = cluster_profiles
        if factory_hypervisor_password is not None:
          self.factory_hypervisor_password = factory_hypervisor_password
        if hxdp_root_pwd is not None:
          self.hxdp_root_pwd = hxdp_root_pwd
        if hypervisor_admin is not None:
          self.hypervisor_admin = hypervisor_admin
        if hypervisor_admin_pwd is not None:
          self.hypervisor_admin_pwd = hypervisor_admin_pwd
        if is_hxdp_root_pwd_set is not None:
          self.is_hxdp_root_pwd_set = is_hxdp_root_pwd_set
        if is_hypervisor_admin_pwd_set is not None:
          self.is_hypervisor_admin_pwd_set = is_hypervisor_admin_pwd_set
        if organization is not None:
          self.organization = organization

    @property
    def account_moid(self):
        """
        Gets the account_moid of this HyperflexLocalCredentialPolicy.
        The Account ID for this managed object.  

        :return: The account_moid of this HyperflexLocalCredentialPolicy.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this HyperflexLocalCredentialPolicy.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this HyperflexLocalCredentialPolicy.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this HyperflexLocalCredentialPolicy.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this HyperflexLocalCredentialPolicy.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this HyperflexLocalCredentialPolicy.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this HyperflexLocalCredentialPolicy.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this HyperflexLocalCredentialPolicy.
        The time when this managed object was created.  

        :return: The create_time of this HyperflexLocalCredentialPolicy.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this HyperflexLocalCredentialPolicy.
        The time when this managed object was created.  

        :param create_time: The create_time of this HyperflexLocalCredentialPolicy.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this HyperflexLocalCredentialPolicy.
        The time when this managed object was last modified.  

        :return: The mod_time of this HyperflexLocalCredentialPolicy.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this HyperflexLocalCredentialPolicy.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this HyperflexLocalCredentialPolicy.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this HyperflexLocalCredentialPolicy.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this HyperflexLocalCredentialPolicy.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this HyperflexLocalCredentialPolicy.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this HyperflexLocalCredentialPolicy.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this HyperflexLocalCredentialPolicy.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this HyperflexLocalCredentialPolicy.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this HyperflexLocalCredentialPolicy.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this HyperflexLocalCredentialPolicy.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this HyperflexLocalCredentialPolicy.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this HyperflexLocalCredentialPolicy.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this HyperflexLocalCredentialPolicy.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this HyperflexLocalCredentialPolicy.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this HyperflexLocalCredentialPolicy.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this HyperflexLocalCredentialPolicy.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this HyperflexLocalCredentialPolicy.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this HyperflexLocalCredentialPolicy.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this HyperflexLocalCredentialPolicy.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this HyperflexLocalCredentialPolicy.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this HyperflexLocalCredentialPolicy.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this HyperflexLocalCredentialPolicy.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this HyperflexLocalCredentialPolicy.
        The versioning info for this managed object   

        :return: The version_context of this HyperflexLocalCredentialPolicy.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this HyperflexLocalCredentialPolicy.
        The versioning info for this managed object   

        :param version_context: The version_context of this HyperflexLocalCredentialPolicy.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def description(self):
        """
        Gets the description of this HyperflexLocalCredentialPolicy.
        Description of the policy.  

        :return: The description of this HyperflexLocalCredentialPolicy.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this HyperflexLocalCredentialPolicy.
        Description of the policy.  

        :param description: The description of this HyperflexLocalCredentialPolicy.
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """
        Gets the name of this HyperflexLocalCredentialPolicy.
        Name of the policy.   

        :return: The name of this HyperflexLocalCredentialPolicy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this HyperflexLocalCredentialPolicy.
        Name of the policy.   

        :param name: The name of this HyperflexLocalCredentialPolicy.
        :type: str
        """

        self._name = name

    @property
    def cluster_profiles(self):
        """
        Gets the cluster_profiles of this HyperflexLocalCredentialPolicy.
        List of cluster profiles using this policy 

        :return: The cluster_profiles of this HyperflexLocalCredentialPolicy.
        :rtype: list[HyperflexClusterProfileRef]
        """
        return self._cluster_profiles

    @cluster_profiles.setter
    def cluster_profiles(self, cluster_profiles):
        """
        Sets the cluster_profiles of this HyperflexLocalCredentialPolicy.
        List of cluster profiles using this policy 

        :param cluster_profiles: The cluster_profiles of this HyperflexLocalCredentialPolicy.
        :type: list[HyperflexClusterProfileRef]
        """

        self._cluster_profiles = cluster_profiles

    @property
    def factory_hypervisor_password(self):
        """
        Gets the factory_hypervisor_password of this HyperflexLocalCredentialPolicy.
        Indicates if Hypervisor password is the factory set default password. For HyperFlex Data Platform versions 3.0 or higher, enable this if the default password was not changed on the Hypervisor. It is required to supply a new custom Hypervisor password that will be applied to the Hypervisor during deployment. For HyperFlex Data Platform versions prior to 3.0 release, this setting has no effect and the default password will be used for initial install. The Hypervisor password should be changed after deployment.  

        :return: The factory_hypervisor_password of this HyperflexLocalCredentialPolicy.
        :rtype: bool
        """
        return self._factory_hypervisor_password

    @factory_hypervisor_password.setter
    def factory_hypervisor_password(self, factory_hypervisor_password):
        """
        Sets the factory_hypervisor_password of this HyperflexLocalCredentialPolicy.
        Indicates if Hypervisor password is the factory set default password. For HyperFlex Data Platform versions 3.0 or higher, enable this if the default password was not changed on the Hypervisor. It is required to supply a new custom Hypervisor password that will be applied to the Hypervisor during deployment. For HyperFlex Data Platform versions prior to 3.0 release, this setting has no effect and the default password will be used for initial install. The Hypervisor password should be changed after deployment.  

        :param factory_hypervisor_password: The factory_hypervisor_password of this HyperflexLocalCredentialPolicy.
        :type: bool
        """

        self._factory_hypervisor_password = factory_hypervisor_password

    @property
    def hxdp_root_pwd(self):
        """
        Gets the hxdp_root_pwd of this HyperflexLocalCredentialPolicy.
        HyperFlex storage controller VM password must contain a minimum of 10 characters, with at least 1 lowercase, 1 uppercase, 1 numeric, and 1 of these special characters - !@#$%^&*  

        :return: The hxdp_root_pwd of this HyperflexLocalCredentialPolicy.
        :rtype: str
        """
        return self._hxdp_root_pwd

    @hxdp_root_pwd.setter
    def hxdp_root_pwd(self, hxdp_root_pwd):
        """
        Sets the hxdp_root_pwd of this HyperflexLocalCredentialPolicy.
        HyperFlex storage controller VM password must contain a minimum of 10 characters, with at least 1 lowercase, 1 uppercase, 1 numeric, and 1 of these special characters - !@#$%^&*  

        :param hxdp_root_pwd: The hxdp_root_pwd of this HyperflexLocalCredentialPolicy.
        :type: str
        """

        self._hxdp_root_pwd = hxdp_root_pwd

    @property
    def hypervisor_admin(self):
        """
        Gets the hypervisor_admin of this HyperflexLocalCredentialPolicy.
        Hypervisor administrator username must contain only alphanumeric characters. Use the root account for ESXi deployments.  

        :return: The hypervisor_admin of this HyperflexLocalCredentialPolicy.
        :rtype: str
        """
        return self._hypervisor_admin

    @hypervisor_admin.setter
    def hypervisor_admin(self, hypervisor_admin):
        """
        Sets the hypervisor_admin of this HyperflexLocalCredentialPolicy.
        Hypervisor administrator username must contain only alphanumeric characters. Use the root account for ESXi deployments.  

        :param hypervisor_admin: The hypervisor_admin of this HyperflexLocalCredentialPolicy.
        :type: str
        """

        self._hypervisor_admin = hypervisor_admin

    @property
    def hypervisor_admin_pwd(self):
        """
        Gets the hypervisor_admin_pwd of this HyperflexLocalCredentialPolicy.
        Specifies the ESXi root password. For HyperFlex Data Platform 3.0 or later, if the factory default password was not manually changed, you must set a new custom password. If the password was manually changed, you must not enable the factory default password property and provide the current hypervisor password. Note - All HyperFlex nodes require the same hypervisor password for installation. For HyperFlex Data Platform prior to 3.0, use the default password \"Cisco123\" for newly manufactured HyperFlex servers. A custom password should only be entered if hypervisor credentials were manually changed prior to deployment.  

        :return: The hypervisor_admin_pwd of this HyperflexLocalCredentialPolicy.
        :rtype: str
        """
        return self._hypervisor_admin_pwd

    @hypervisor_admin_pwd.setter
    def hypervisor_admin_pwd(self, hypervisor_admin_pwd):
        """
        Sets the hypervisor_admin_pwd of this HyperflexLocalCredentialPolicy.
        Specifies the ESXi root password. For HyperFlex Data Platform 3.0 or later, if the factory default password was not manually changed, you must set a new custom password. If the password was manually changed, you must not enable the factory default password property and provide the current hypervisor password. Note - All HyperFlex nodes require the same hypervisor password for installation. For HyperFlex Data Platform prior to 3.0, use the default password \"Cisco123\" for newly manufactured HyperFlex servers. A custom password should only be entered if hypervisor credentials were manually changed prior to deployment.  

        :param hypervisor_admin_pwd: The hypervisor_admin_pwd of this HyperflexLocalCredentialPolicy.
        :type: str
        """

        self._hypervisor_admin_pwd = hypervisor_admin_pwd

    @property
    def is_hxdp_root_pwd_set(self):
        """
        Gets the is_hxdp_root_pwd_set of this HyperflexLocalCredentialPolicy.

        :return: The is_hxdp_root_pwd_set of this HyperflexLocalCredentialPolicy.
        :rtype: bool
        """
        return self._is_hxdp_root_pwd_set

    @is_hxdp_root_pwd_set.setter
    def is_hxdp_root_pwd_set(self, is_hxdp_root_pwd_set):
        """
        Sets the is_hxdp_root_pwd_set of this HyperflexLocalCredentialPolicy.

        :param is_hxdp_root_pwd_set: The is_hxdp_root_pwd_set of this HyperflexLocalCredentialPolicy.
        :type: bool
        """

        self._is_hxdp_root_pwd_set = is_hxdp_root_pwd_set

    @property
    def is_hypervisor_admin_pwd_set(self):
        """
        Gets the is_hypervisor_admin_pwd_set of this HyperflexLocalCredentialPolicy.

        :return: The is_hypervisor_admin_pwd_set of this HyperflexLocalCredentialPolicy.
        :rtype: bool
        """
        return self._is_hypervisor_admin_pwd_set

    @is_hypervisor_admin_pwd_set.setter
    def is_hypervisor_admin_pwd_set(self, is_hypervisor_admin_pwd_set):
        """
        Sets the is_hypervisor_admin_pwd_set of this HyperflexLocalCredentialPolicy.

        :param is_hypervisor_admin_pwd_set: The is_hypervisor_admin_pwd_set of this HyperflexLocalCredentialPolicy.
        :type: bool
        """

        self._is_hypervisor_admin_pwd_set = is_hypervisor_admin_pwd_set

    @property
    def organization(self):
        """
        Gets the organization of this HyperflexLocalCredentialPolicy.
        Organization 

        :return: The organization of this HyperflexLocalCredentialPolicy.
        :rtype: IamAccountRef
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """
        Sets the organization of this HyperflexLocalCredentialPolicy.
        Organization 

        :param organization: The organization of this HyperflexLocalCredentialPolicy.
        :type: IamAccountRef
        """

        self._organization = organization

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
        if not isinstance(other, HyperflexLocalCredentialPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
