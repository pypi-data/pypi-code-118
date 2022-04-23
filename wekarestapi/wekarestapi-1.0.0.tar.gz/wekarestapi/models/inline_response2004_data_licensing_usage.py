# coding: utf-8

"""
    @weka-api

    <div>The Weka system supports a RESTful API. This is useful when automating the interaction with the Weka system and when integrating it into your workflows or monitoring systems. The API is accessible at port 14000, via the /api/v2 URL, you can explore it via /api/v2/docs when accessing from the cluster (e.g. https://weka01:14000/api/v2/docs).<div style=\"margin-top: 15px;\">Note: Weka uses 64bit numbers. Please take special care when interacting with the API with different program languages (In JS for example you can use \"json-bigint\")</div></div>  # noqa: E501

    OpenAPI spec version: 3.14
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InlineResponse2004DataLicensingUsage(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'drive_capacity_gb': 'float',
        'obs_capacity_gb': 'float',
        'usable_capacity_gb': 'float'
    }

    attribute_map = {
        'drive_capacity_gb': 'drive_capacity_gb',
        'obs_capacity_gb': 'obs_capacity_gb',
        'usable_capacity_gb': 'usable_capacity_gb'
    }

    def __init__(self, drive_capacity_gb=None, obs_capacity_gb=None, usable_capacity_gb=None):  # noqa: E501
        """InlineResponse2004DataLicensingUsage - a model defined in Swagger"""  # noqa: E501
        self._drive_capacity_gb = None
        self._obs_capacity_gb = None
        self._usable_capacity_gb = None
        self.discriminator = None
        if drive_capacity_gb is not None:
            self.drive_capacity_gb = drive_capacity_gb
        if obs_capacity_gb is not None:
            self.obs_capacity_gb = obs_capacity_gb
        if usable_capacity_gb is not None:
            self.usable_capacity_gb = usable_capacity_gb

    @property
    def drive_capacity_gb(self):
        """Gets the drive_capacity_gb of this InlineResponse2004DataLicensingUsage.  # noqa: E501


        :return: The drive_capacity_gb of this InlineResponse2004DataLicensingUsage.  # noqa: E501
        :rtype: float
        """
        return self._drive_capacity_gb

    @drive_capacity_gb.setter
    def drive_capacity_gb(self, drive_capacity_gb):
        """Sets the drive_capacity_gb of this InlineResponse2004DataLicensingUsage.


        :param drive_capacity_gb: The drive_capacity_gb of this InlineResponse2004DataLicensingUsage.  # noqa: E501
        :type: float
        """

        self._drive_capacity_gb = drive_capacity_gb

    @property
    def obs_capacity_gb(self):
        """Gets the obs_capacity_gb of this InlineResponse2004DataLicensingUsage.  # noqa: E501


        :return: The obs_capacity_gb of this InlineResponse2004DataLicensingUsage.  # noqa: E501
        :rtype: float
        """
        return self._obs_capacity_gb

    @obs_capacity_gb.setter
    def obs_capacity_gb(self, obs_capacity_gb):
        """Sets the obs_capacity_gb of this InlineResponse2004DataLicensingUsage.


        :param obs_capacity_gb: The obs_capacity_gb of this InlineResponse2004DataLicensingUsage.  # noqa: E501
        :type: float
        """

        self._obs_capacity_gb = obs_capacity_gb

    @property
    def usable_capacity_gb(self):
        """Gets the usable_capacity_gb of this InlineResponse2004DataLicensingUsage.  # noqa: E501


        :return: The usable_capacity_gb of this InlineResponse2004DataLicensingUsage.  # noqa: E501
        :rtype: float
        """
        return self._usable_capacity_gb

    @usable_capacity_gb.setter
    def usable_capacity_gb(self, usable_capacity_gb):
        """Sets the usable_capacity_gb of this InlineResponse2004DataLicensingUsage.


        :param usable_capacity_gb: The usable_capacity_gb of this InlineResponse2004DataLicensingUsage.  # noqa: E501
        :type: float
        """

        self._usable_capacity_gb = usable_capacity_gb

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(InlineResponse2004DataLicensingUsage, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse2004DataLicensingUsage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
