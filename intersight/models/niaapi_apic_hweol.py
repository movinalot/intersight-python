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


class NiaapiApicHweol(object):
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
        'affected_pids': 'str',
        'announcement_date': 'datetime',
        'announcement_date_epoch': 'int',
        'bulletin_no': 'str',
        'description': 'str',
        'endof_new_service_attachment_date': 'datetime',
        'endof_new_service_attachment_date_epoch': 'int',
        'endof_routine_failure_analysis_date': 'datetime',
        'endof_routine_failure_analysis_date_epoch': 'int',
        'endof_sale_date': 'datetime',
        'endof_sale_date_epoch': 'int',
        'endof_security_support': 'datetime',
        'endof_security_support_epoch': 'int',
        'endof_service_contract_renewal_date': 'datetime',
        'endof_service_contract_renewal_date_epoch': 'int',
        'endof_sw_maintenance_date': 'datetime',
        'endof_sw_maintenance_date_epoch': 'int',
        'hardware_eol_url': 'str',
        'headline': 'str',
        'last_dateof_support': 'datetime',
        'last_dateof_support_epoch': 'int',
        'last_ship_date': 'datetime',
        'last_ship_date_epoch': 'int',
        'migration_url': 'str'
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
        'affected_pids': 'AffectedPids',
        'announcement_date': 'AnnouncementDate',
        'announcement_date_epoch': 'AnnouncementDateEpoch',
        'bulletin_no': 'BulletinNo',
        'description': 'Description',
        'endof_new_service_attachment_date': 'EndofNewServiceAttachmentDate',
        'endof_new_service_attachment_date_epoch': 'EndofNewServiceAttachmentDateEpoch',
        'endof_routine_failure_analysis_date': 'EndofRoutineFailureAnalysisDate',
        'endof_routine_failure_analysis_date_epoch': 'EndofRoutineFailureAnalysisDateEpoch',
        'endof_sale_date': 'EndofSaleDate',
        'endof_sale_date_epoch': 'EndofSaleDateEpoch',
        'endof_security_support': 'EndofSecuritySupport',
        'endof_security_support_epoch': 'EndofSecuritySupportEpoch',
        'endof_service_contract_renewal_date': 'EndofServiceContractRenewalDate',
        'endof_service_contract_renewal_date_epoch': 'EndofServiceContractRenewalDateEpoch',
        'endof_sw_maintenance_date': 'EndofSwMaintenanceDate',
        'endof_sw_maintenance_date_epoch': 'EndofSwMaintenanceDateEpoch',
        'hardware_eol_url': 'HardwareEolUrl',
        'headline': 'Headline',
        'last_dateof_support': 'LastDateofSupport',
        'last_dateof_support_epoch': 'LastDateofSupportEpoch',
        'last_ship_date': 'LastShipDate',
        'last_ship_date_epoch': 'LastShipDateEpoch',
        'migration_url': 'MigrationUrl'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, domain_group_moid=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, shared_scope=None, tags=None, version_context=None, affected_pids=None, announcement_date=None, announcement_date_epoch=None, bulletin_no=None, description=None, endof_new_service_attachment_date=None, endof_new_service_attachment_date_epoch=None, endof_routine_failure_analysis_date=None, endof_routine_failure_analysis_date_epoch=None, endof_sale_date=None, endof_sale_date_epoch=None, endof_security_support=None, endof_security_support_epoch=None, endof_service_contract_renewal_date=None, endof_service_contract_renewal_date_epoch=None, endof_sw_maintenance_date=None, endof_sw_maintenance_date_epoch=None, hardware_eol_url=None, headline=None, last_dateof_support=None, last_dateof_support_epoch=None, last_ship_date=None, last_ship_date_epoch=None, migration_url=None):
        """
        NiaapiApicHweol - a model defined in Swagger
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
        self._affected_pids = None
        self._announcement_date = None
        self._announcement_date_epoch = None
        self._bulletin_no = None
        self._description = None
        self._endof_new_service_attachment_date = None
        self._endof_new_service_attachment_date_epoch = None
        self._endof_routine_failure_analysis_date = None
        self._endof_routine_failure_analysis_date_epoch = None
        self._endof_sale_date = None
        self._endof_sale_date_epoch = None
        self._endof_security_support = None
        self._endof_security_support_epoch = None
        self._endof_service_contract_renewal_date = None
        self._endof_service_contract_renewal_date_epoch = None
        self._endof_sw_maintenance_date = None
        self._endof_sw_maintenance_date_epoch = None
        self._hardware_eol_url = None
        self._headline = None
        self._last_dateof_support = None
        self._last_dateof_support_epoch = None
        self._last_ship_date = None
        self._last_ship_date_epoch = None
        self._migration_url = None

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
        if affected_pids is not None:
          self.affected_pids = affected_pids
        if announcement_date is not None:
          self.announcement_date = announcement_date
        if announcement_date_epoch is not None:
          self.announcement_date_epoch = announcement_date_epoch
        if bulletin_no is not None:
          self.bulletin_no = bulletin_no
        if description is not None:
          self.description = description
        if endof_new_service_attachment_date is not None:
          self.endof_new_service_attachment_date = endof_new_service_attachment_date
        if endof_new_service_attachment_date_epoch is not None:
          self.endof_new_service_attachment_date_epoch = endof_new_service_attachment_date_epoch
        if endof_routine_failure_analysis_date is not None:
          self.endof_routine_failure_analysis_date = endof_routine_failure_analysis_date
        if endof_routine_failure_analysis_date_epoch is not None:
          self.endof_routine_failure_analysis_date_epoch = endof_routine_failure_analysis_date_epoch
        if endof_sale_date is not None:
          self.endof_sale_date = endof_sale_date
        if endof_sale_date_epoch is not None:
          self.endof_sale_date_epoch = endof_sale_date_epoch
        if endof_security_support is not None:
          self.endof_security_support = endof_security_support
        if endof_security_support_epoch is not None:
          self.endof_security_support_epoch = endof_security_support_epoch
        if endof_service_contract_renewal_date is not None:
          self.endof_service_contract_renewal_date = endof_service_contract_renewal_date
        if endof_service_contract_renewal_date_epoch is not None:
          self.endof_service_contract_renewal_date_epoch = endof_service_contract_renewal_date_epoch
        if endof_sw_maintenance_date is not None:
          self.endof_sw_maintenance_date = endof_sw_maintenance_date
        if endof_sw_maintenance_date_epoch is not None:
          self.endof_sw_maintenance_date_epoch = endof_sw_maintenance_date_epoch
        if hardware_eol_url is not None:
          self.hardware_eol_url = hardware_eol_url
        if headline is not None:
          self.headline = headline
        if last_dateof_support is not None:
          self.last_dateof_support = last_dateof_support
        if last_dateof_support_epoch is not None:
          self.last_dateof_support_epoch = last_dateof_support_epoch
        if last_ship_date is not None:
          self.last_ship_date = last_ship_date
        if last_ship_date_epoch is not None:
          self.last_ship_date_epoch = last_ship_date_epoch
        if migration_url is not None:
          self.migration_url = migration_url

    @property
    def account_moid(self):
        """
        Gets the account_moid of this NiaapiApicHweol.
        The Account ID for this managed object.  

        :return: The account_moid of this NiaapiApicHweol.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this NiaapiApicHweol.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this NiaapiApicHweol.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this NiaapiApicHweol.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this NiaapiApicHweol.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this NiaapiApicHweol.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this NiaapiApicHweol.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this NiaapiApicHweol.
        The time when this managed object was created.  

        :return: The create_time of this NiaapiApicHweol.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this NiaapiApicHweol.
        The time when this managed object was created.  

        :param create_time: The create_time of this NiaapiApicHweol.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def domain_group_moid(self):
        """
        Gets the domain_group_moid of this NiaapiApicHweol.
        The DomainGroup ID for this managed object.  

        :return: The domain_group_moid of this NiaapiApicHweol.
        :rtype: str
        """
        return self._domain_group_moid

    @domain_group_moid.setter
    def domain_group_moid(self, domain_group_moid):
        """
        Sets the domain_group_moid of this NiaapiApicHweol.
        The DomainGroup ID for this managed object.  

        :param domain_group_moid: The domain_group_moid of this NiaapiApicHweol.
        :type: str
        """

        self._domain_group_moid = domain_group_moid

    @property
    def mod_time(self):
        """
        Gets the mod_time of this NiaapiApicHweol.
        The time when this managed object was last modified.  

        :return: The mod_time of this NiaapiApicHweol.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this NiaapiApicHweol.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this NiaapiApicHweol.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this NiaapiApicHweol.
        The unique identifier of this Managed Object instance.  

        :return: The moid of this NiaapiApicHweol.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this NiaapiApicHweol.
        The unique identifier of this Managed Object instance.  

        :param moid: The moid of this NiaapiApicHweol.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this NiaapiApicHweol.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this NiaapiApicHweol.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this NiaapiApicHweol.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this NiaapiApicHweol.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this NiaapiApicHweol.
        The array of owners which represent effective ownership of this object.   

        :return: The owners of this NiaapiApicHweol.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this NiaapiApicHweol.
        The array of owners which represent effective ownership of this object.   

        :param owners: The owners of this NiaapiApicHweol.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this NiaapiApicHweol.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this NiaapiApicHweol.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this NiaapiApicHweol.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this NiaapiApicHweol.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def shared_scope(self):
        """
        Gets the shared_scope of this NiaapiApicHweol.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :return: The shared_scope of this NiaapiApicHweol.
        :rtype: str
        """
        return self._shared_scope

    @shared_scope.setter
    def shared_scope(self, shared_scope):
        """
        Sets the shared_scope of this NiaapiApicHweol.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :param shared_scope: The shared_scope of this NiaapiApicHweol.
        :type: str
        """

        self._shared_scope = shared_scope

    @property
    def tags(self):
        """
        Gets the tags of this NiaapiApicHweol.
        The array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this NiaapiApicHweol.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this NiaapiApicHweol.
        The array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this NiaapiApicHweol.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this NiaapiApicHweol.
        The versioning info for this managed object.   

        :return: The version_context of this NiaapiApicHweol.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this NiaapiApicHweol.
        The versioning info for this managed object.   

        :param version_context: The version_context of this NiaapiApicHweol.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def affected_pids(self):
        """
        Gets the affected_pids of this NiaapiApicHweol.
        String contains the PID of hardwares affected by this notice, seperated by comma.  

        :return: The affected_pids of this NiaapiApicHweol.
        :rtype: str
        """
        return self._affected_pids

    @affected_pids.setter
    def affected_pids(self, affected_pids):
        """
        Sets the affected_pids of this NiaapiApicHweol.
        String contains the PID of hardwares affected by this notice, seperated by comma.  

        :param affected_pids: The affected_pids of this NiaapiApicHweol.
        :type: str
        """

        self._affected_pids = affected_pids

    @property
    def announcement_date(self):
        """
        Gets the announcement_date of this NiaapiApicHweol.
        When this notice is announced.  

        :return: The announcement_date of this NiaapiApicHweol.
        :rtype: datetime
        """
        return self._announcement_date

    @announcement_date.setter
    def announcement_date(self, announcement_date):
        """
        Sets the announcement_date of this NiaapiApicHweol.
        When this notice is announced.  

        :param announcement_date: The announcement_date of this NiaapiApicHweol.
        :type: datetime
        """

        self._announcement_date = announcement_date

    @property
    def announcement_date_epoch(self):
        """
        Gets the announcement_date_epoch of this NiaapiApicHweol.
        Epoch time of Announcement Date.  

        :return: The announcement_date_epoch of this NiaapiApicHweol.
        :rtype: int
        """
        return self._announcement_date_epoch

    @announcement_date_epoch.setter
    def announcement_date_epoch(self, announcement_date_epoch):
        """
        Sets the announcement_date_epoch of this NiaapiApicHweol.
        Epoch time of Announcement Date.  

        :param announcement_date_epoch: The announcement_date_epoch of this NiaapiApicHweol.
        :type: int
        """

        self._announcement_date_epoch = announcement_date_epoch

    @property
    def bulletin_no(self):
        """
        Gets the bulletin_no of this NiaapiApicHweol.
        The bulletinno of this hardware end of life notice.  

        :return: The bulletin_no of this NiaapiApicHweol.
        :rtype: str
        """
        return self._bulletin_no

    @bulletin_no.setter
    def bulletin_no(self, bulletin_no):
        """
        Sets the bulletin_no of this NiaapiApicHweol.
        The bulletinno of this hardware end of life notice.  

        :param bulletin_no: The bulletin_no of this NiaapiApicHweol.
        :type: str
        """

        self._bulletin_no = bulletin_no

    @property
    def description(self):
        """
        Gets the description of this NiaapiApicHweol.
        The description of this hardware end of life notice.  

        :return: The description of this NiaapiApicHweol.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this NiaapiApicHweol.
        The description of this hardware end of life notice.  

        :param description: The description of this NiaapiApicHweol.
        :type: str
        """

        self._description = description

    @property
    def endof_new_service_attachment_date(self):
        """
        Gets the endof_new_service_attachment_date of this NiaapiApicHweol.
        Date time of end of new services attachment  .  

        :return: The endof_new_service_attachment_date of this NiaapiApicHweol.
        :rtype: datetime
        """
        return self._endof_new_service_attachment_date

    @endof_new_service_attachment_date.setter
    def endof_new_service_attachment_date(self, endof_new_service_attachment_date):
        """
        Sets the endof_new_service_attachment_date of this NiaapiApicHweol.
        Date time of end of new services attachment  .  

        :param endof_new_service_attachment_date: The endof_new_service_attachment_date of this NiaapiApicHweol.
        :type: datetime
        """

        self._endof_new_service_attachment_date = endof_new_service_attachment_date

    @property
    def endof_new_service_attachment_date_epoch(self):
        """
        Gets the endof_new_service_attachment_date_epoch of this NiaapiApicHweol.
        Epoch time of New service attachment Date .  

        :return: The endof_new_service_attachment_date_epoch of this NiaapiApicHweol.
        :rtype: int
        """
        return self._endof_new_service_attachment_date_epoch

    @endof_new_service_attachment_date_epoch.setter
    def endof_new_service_attachment_date_epoch(self, endof_new_service_attachment_date_epoch):
        """
        Sets the endof_new_service_attachment_date_epoch of this NiaapiApicHweol.
        Epoch time of New service attachment Date .  

        :param endof_new_service_attachment_date_epoch: The endof_new_service_attachment_date_epoch of this NiaapiApicHweol.
        :type: int
        """

        self._endof_new_service_attachment_date_epoch = endof_new_service_attachment_date_epoch

    @property
    def endof_routine_failure_analysis_date(self):
        """
        Gets the endof_routine_failure_analysis_date of this NiaapiApicHweol.
        Date time of end of routinefailure analysis.  

        :return: The endof_routine_failure_analysis_date of this NiaapiApicHweol.
        :rtype: datetime
        """
        return self._endof_routine_failure_analysis_date

    @endof_routine_failure_analysis_date.setter
    def endof_routine_failure_analysis_date(self, endof_routine_failure_analysis_date):
        """
        Sets the endof_routine_failure_analysis_date of this NiaapiApicHweol.
        Date time of end of routinefailure analysis.  

        :param endof_routine_failure_analysis_date: The endof_routine_failure_analysis_date of this NiaapiApicHweol.
        :type: datetime
        """

        self._endof_routine_failure_analysis_date = endof_routine_failure_analysis_date

    @property
    def endof_routine_failure_analysis_date_epoch(self):
        """
        Gets the endof_routine_failure_analysis_date_epoch of this NiaapiApicHweol.
        Epoch time of End of Routine Failure Analysis Date.  

        :return: The endof_routine_failure_analysis_date_epoch of this NiaapiApicHweol.
        :rtype: int
        """
        return self._endof_routine_failure_analysis_date_epoch

    @endof_routine_failure_analysis_date_epoch.setter
    def endof_routine_failure_analysis_date_epoch(self, endof_routine_failure_analysis_date_epoch):
        """
        Sets the endof_routine_failure_analysis_date_epoch of this NiaapiApicHweol.
        Epoch time of End of Routine Failure Analysis Date.  

        :param endof_routine_failure_analysis_date_epoch: The endof_routine_failure_analysis_date_epoch of this NiaapiApicHweol.
        :type: int
        """

        self._endof_routine_failure_analysis_date_epoch = endof_routine_failure_analysis_date_epoch

    @property
    def endof_sale_date(self):
        """
        Gets the endof_sale_date of this NiaapiApicHweol.
        When this hardware will end sale.  

        :return: The endof_sale_date of this NiaapiApicHweol.
        :rtype: datetime
        """
        return self._endof_sale_date

    @endof_sale_date.setter
    def endof_sale_date(self, endof_sale_date):
        """
        Sets the endof_sale_date of this NiaapiApicHweol.
        When this hardware will end sale.  

        :param endof_sale_date: The endof_sale_date of this NiaapiApicHweol.
        :type: datetime
        """

        self._endof_sale_date = endof_sale_date

    @property
    def endof_sale_date_epoch(self):
        """
        Gets the endof_sale_date_epoch of this NiaapiApicHweol.
        Epoch time of End of Sale Date.  

        :return: The endof_sale_date_epoch of this NiaapiApicHweol.
        :rtype: int
        """
        return self._endof_sale_date_epoch

    @endof_sale_date_epoch.setter
    def endof_sale_date_epoch(self, endof_sale_date_epoch):
        """
        Sets the endof_sale_date_epoch of this NiaapiApicHweol.
        Epoch time of End of Sale Date.  

        :param endof_sale_date_epoch: The endof_sale_date_epoch of this NiaapiApicHweol.
        :type: int
        """

        self._endof_sale_date_epoch = endof_sale_date_epoch

    @property
    def endof_security_support(self):
        """
        Gets the endof_security_support of this NiaapiApicHweol.
        Date time of end of security support .  

        :return: The endof_security_support of this NiaapiApicHweol.
        :rtype: datetime
        """
        return self._endof_security_support

    @endof_security_support.setter
    def endof_security_support(self, endof_security_support):
        """
        Sets the endof_security_support of this NiaapiApicHweol.
        Date time of end of security support .  

        :param endof_security_support: The endof_security_support of this NiaapiApicHweol.
        :type: datetime
        """

        self._endof_security_support = endof_security_support

    @property
    def endof_security_support_epoch(self):
        """
        Gets the endof_security_support_epoch of this NiaapiApicHweol.
        Epoch time of End of Security Support Date .  

        :return: The endof_security_support_epoch of this NiaapiApicHweol.
        :rtype: int
        """
        return self._endof_security_support_epoch

    @endof_security_support_epoch.setter
    def endof_security_support_epoch(self, endof_security_support_epoch):
        """
        Sets the endof_security_support_epoch of this NiaapiApicHweol.
        Epoch time of End of Security Support Date .  

        :param endof_security_support_epoch: The endof_security_support_epoch of this NiaapiApicHweol.
        :type: int
        """

        self._endof_security_support_epoch = endof_security_support_epoch

    @property
    def endof_service_contract_renewal_date(self):
        """
        Gets the endof_service_contract_renewal_date of this NiaapiApicHweol.
        Date time of end of service contract renew .  

        :return: The endof_service_contract_renewal_date of this NiaapiApicHweol.
        :rtype: datetime
        """
        return self._endof_service_contract_renewal_date

    @endof_service_contract_renewal_date.setter
    def endof_service_contract_renewal_date(self, endof_service_contract_renewal_date):
        """
        Sets the endof_service_contract_renewal_date of this NiaapiApicHweol.
        Date time of end of service contract renew .  

        :param endof_service_contract_renewal_date: The endof_service_contract_renewal_date of this NiaapiApicHweol.
        :type: datetime
        """

        self._endof_service_contract_renewal_date = endof_service_contract_renewal_date

    @property
    def endof_service_contract_renewal_date_epoch(self):
        """
        Gets the endof_service_contract_renewal_date_epoch of this NiaapiApicHweol.
        Epoch time of End of Renewal service contract.  

        :return: The endof_service_contract_renewal_date_epoch of this NiaapiApicHweol.
        :rtype: int
        """
        return self._endof_service_contract_renewal_date_epoch

    @endof_service_contract_renewal_date_epoch.setter
    def endof_service_contract_renewal_date_epoch(self, endof_service_contract_renewal_date_epoch):
        """
        Sets the endof_service_contract_renewal_date_epoch of this NiaapiApicHweol.
        Epoch time of End of Renewal service contract.  

        :param endof_service_contract_renewal_date_epoch: The endof_service_contract_renewal_date_epoch of this NiaapiApicHweol.
        :type: int
        """

        self._endof_service_contract_renewal_date_epoch = endof_service_contract_renewal_date_epoch

    @property
    def endof_sw_maintenance_date(self):
        """
        Gets the endof_sw_maintenance_date of this NiaapiApicHweol.
        The date of end of maintainance.  

        :return: The endof_sw_maintenance_date of this NiaapiApicHweol.
        :rtype: datetime
        """
        return self._endof_sw_maintenance_date

    @endof_sw_maintenance_date.setter
    def endof_sw_maintenance_date(self, endof_sw_maintenance_date):
        """
        Sets the endof_sw_maintenance_date of this NiaapiApicHweol.
        The date of end of maintainance.  

        :param endof_sw_maintenance_date: The endof_sw_maintenance_date of this NiaapiApicHweol.
        :type: datetime
        """

        self._endof_sw_maintenance_date = endof_sw_maintenance_date

    @property
    def endof_sw_maintenance_date_epoch(self):
        """
        Gets the endof_sw_maintenance_date_epoch of this NiaapiApicHweol.
        Epoch time of End of maintenance Date.  

        :return: The endof_sw_maintenance_date_epoch of this NiaapiApicHweol.
        :rtype: int
        """
        return self._endof_sw_maintenance_date_epoch

    @endof_sw_maintenance_date_epoch.setter
    def endof_sw_maintenance_date_epoch(self, endof_sw_maintenance_date_epoch):
        """
        Sets the endof_sw_maintenance_date_epoch of this NiaapiApicHweol.
        Epoch time of End of maintenance Date.  

        :param endof_sw_maintenance_date_epoch: The endof_sw_maintenance_date_epoch of this NiaapiApicHweol.
        :type: int
        """

        self._endof_sw_maintenance_date_epoch = endof_sw_maintenance_date_epoch

    @property
    def hardware_eol_url(self):
        """
        Gets the hardware_eol_url of this NiaapiApicHweol.
        Hardware end of sale URL link to the notice webpage.  

        :return: The hardware_eol_url of this NiaapiApicHweol.
        :rtype: str
        """
        return self._hardware_eol_url

    @hardware_eol_url.setter
    def hardware_eol_url(self, hardware_eol_url):
        """
        Sets the hardware_eol_url of this NiaapiApicHweol.
        Hardware end of sale URL link to the notice webpage.  

        :param hardware_eol_url: The hardware_eol_url of this NiaapiApicHweol.
        :type: str
        """

        self._hardware_eol_url = hardware_eol_url

    @property
    def headline(self):
        """
        Gets the headline of this NiaapiApicHweol.
        The title of this hardware end of life notice.  

        :return: The headline of this NiaapiApicHweol.
        :rtype: str
        """
        return self._headline

    @headline.setter
    def headline(self, headline):
        """
        Sets the headline of this NiaapiApicHweol.
        The title of this hardware end of life notice.  

        :param headline: The headline of this NiaapiApicHweol.
        :type: str
        """

        self._headline = headline

    @property
    def last_dateof_support(self):
        """
        Gets the last_dateof_support of this NiaapiApicHweol.
        Date time of end of support .  

        :return: The last_dateof_support of this NiaapiApicHweol.
        :rtype: datetime
        """
        return self._last_dateof_support

    @last_dateof_support.setter
    def last_dateof_support(self, last_dateof_support):
        """
        Sets the last_dateof_support of this NiaapiApicHweol.
        Date time of end of support .  

        :param last_dateof_support: The last_dateof_support of this NiaapiApicHweol.
        :type: datetime
        """

        self._last_dateof_support = last_dateof_support

    @property
    def last_dateof_support_epoch(self):
        """
        Gets the last_dateof_support_epoch of this NiaapiApicHweol.
        Epoch time of last date of support .  

        :return: The last_dateof_support_epoch of this NiaapiApicHweol.
        :rtype: int
        """
        return self._last_dateof_support_epoch

    @last_dateof_support_epoch.setter
    def last_dateof_support_epoch(self, last_dateof_support_epoch):
        """
        Sets the last_dateof_support_epoch of this NiaapiApicHweol.
        Epoch time of last date of support .  

        :param last_dateof_support_epoch: The last_dateof_support_epoch of this NiaapiApicHweol.
        :type: int
        """

        self._last_dateof_support_epoch = last_dateof_support_epoch

    @property
    def last_ship_date(self):
        """
        Gets the last_ship_date of this NiaapiApicHweol.
        Date time of Lastship Date.  

        :return: The last_ship_date of this NiaapiApicHweol.
        :rtype: datetime
        """
        return self._last_ship_date

    @last_ship_date.setter
    def last_ship_date(self, last_ship_date):
        """
        Sets the last_ship_date of this NiaapiApicHweol.
        Date time of Lastship Date.  

        :param last_ship_date: The last_ship_date of this NiaapiApicHweol.
        :type: datetime
        """

        self._last_ship_date = last_ship_date

    @property
    def last_ship_date_epoch(self):
        """
        Gets the last_ship_date_epoch of this NiaapiApicHweol.
        Epoch time of last ship Date.  

        :return: The last_ship_date_epoch of this NiaapiApicHweol.
        :rtype: int
        """
        return self._last_ship_date_epoch

    @last_ship_date_epoch.setter
    def last_ship_date_epoch(self, last_ship_date_epoch):
        """
        Sets the last_ship_date_epoch of this NiaapiApicHweol.
        Epoch time of last ship Date.  

        :param last_ship_date_epoch: The last_ship_date_epoch of this NiaapiApicHweol.
        :type: int
        """

        self._last_ship_date_epoch = last_ship_date_epoch

    @property
    def migration_url(self):
        """
        Gets the migration_url of this NiaapiApicHweol.
        The URL of this migration notice.   

        :return: The migration_url of this NiaapiApicHweol.
        :rtype: str
        """
        return self._migration_url

    @migration_url.setter
    def migration_url(self, migration_url):
        """
        Sets the migration_url of this NiaapiApicHweol.
        The URL of this migration notice.   

        :param migration_url: The migration_url of this NiaapiApicHweol.
        :type: str
        """

        self._migration_url = migration_url

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
        if not isinstance(other, NiaapiApicHweol):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
