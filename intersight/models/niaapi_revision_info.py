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


class NiaapiRevisionInfo(object):
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
        'date_published': 'datetime',
        'revision_comment': 'str',
        'revision_no': 'str'
    }

    attribute_map = {
        'date_published': 'DatePublished',
        'revision_comment': 'RevisionComment',
        'revision_no': 'RevisionNo'
    }

    def __init__(self, date_published=None, revision_comment=None, revision_no=None):
        """
        NiaapiRevisionInfo - a model defined in Swagger
        """

        self._date_published = None
        self._revision_comment = None
        self._revision_no = None

        if date_published is not None:
          self.date_published = date_published
        if revision_comment is not None:
          self.revision_comment = revision_comment
        if revision_no is not None:
          self.revision_no = revision_no

    @property
    def date_published(self):
        """
        Gets the date_published of this NiaapiRevisionInfo.
        The date the revision is made.  

        :return: The date_published of this NiaapiRevisionInfo.
        :rtype: datetime
        """
        return self._date_published

    @date_published.setter
    def date_published(self, date_published):
        """
        Sets the date_published of this NiaapiRevisionInfo.
        The date the revision is made.  

        :param date_published: The date_published of this NiaapiRevisionInfo.
        :type: datetime
        """

        self._date_published = date_published

    @property
    def revision_comment(self):
        """
        Gets the revision_comment of this NiaapiRevisionInfo.
        The changes made in this revision.  

        :return: The revision_comment of this NiaapiRevisionInfo.
        :rtype: str
        """
        return self._revision_comment

    @revision_comment.setter
    def revision_comment(self, revision_comment):
        """
        Sets the revision_comment of this NiaapiRevisionInfo.
        The changes made in this revision.  

        :param revision_comment: The revision_comment of this NiaapiRevisionInfo.
        :type: str
        """

        self._revision_comment = revision_comment

    @property
    def revision_no(self):
        """
        Gets the revision_no of this NiaapiRevisionInfo.
        The Revision No. of this revision.   

        :return: The revision_no of this NiaapiRevisionInfo.
        :rtype: str
        """
        return self._revision_no

    @revision_no.setter
    def revision_no(self, revision_no):
        """
        Sets the revision_no of this NiaapiRevisionInfo.
        The Revision No. of this revision.   

        :param revision_no: The revision_no of this NiaapiRevisionInfo.
        :type: str
        """

        self._revision_no = revision_no

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
        if not isinstance(other, NiaapiRevisionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other