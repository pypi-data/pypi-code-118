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

class UidLimitsBody(object):
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
        'ssd_quota': 'float',
        'total_quota': 'float'
    }

    attribute_map = {
        'ssd_quota': 'ssd_quota',
        'total_quota': 'total_quota'
    }

    def __init__(self, ssd_quota=None, total_quota=None):  # noqa: E501
        """UidLimitsBody - a model defined in Swagger"""  # noqa: E501
        self._ssd_quota = None
        self._total_quota = None
        self.discriminator = None
        if ssd_quota is not None:
            self.ssd_quota = ssd_quota
        if total_quota is not None:
            self.total_quota = total_quota

    @property
    def ssd_quota(self):
        """Gets the ssd_quota of this UidLimitsBody.  # noqa: E501

        SSD quota (format - capacity in decimal or binary units - 11B, 1KB, 1MB, 1GB, 1TB, 1PB, 1EB, 1KiB, 1MiB, 1GiB, 1TiB, 1PiB, 1EiB)  # noqa: E501

        :return: The ssd_quota of this UidLimitsBody.  # noqa: E501
        :rtype: float
        """
        return self._ssd_quota

    @ssd_quota.setter
    def ssd_quota(self, ssd_quota):
        """Sets the ssd_quota of this UidLimitsBody.

        SSD quota (format - capacity in decimal or binary units - 11B, 1KB, 1MB, 1GB, 1TB, 1PB, 1EB, 1KiB, 1MiB, 1GiB, 1TiB, 1PiB, 1EiB)  # noqa: E501

        :param ssd_quota: The ssd_quota of this UidLimitsBody.  # noqa: E501
        :type: float
        """

        self._ssd_quota = ssd_quota

    @property
    def total_quota(self):
        """Gets the total_quota of this UidLimitsBody.  # noqa: E501

        Total quota (format - capacity in decimal or binary units - 11B, 1KB, 1MB, 1GB, 1TB, 1PB, 1EB, 1KiB, 1MiB, 1GiB, 1TiB, 1PiB, 1EiB)  # noqa: E501

        :return: The total_quota of this UidLimitsBody.  # noqa: E501
        :rtype: float
        """
        return self._total_quota

    @total_quota.setter
    def total_quota(self, total_quota):
        """Sets the total_quota of this UidLimitsBody.

        Total quota (format - capacity in decimal or binary units - 11B, 1KB, 1MB, 1GB, 1TB, 1PB, 1EB, 1KiB, 1MiB, 1GiB, 1TiB, 1PiB, 1EiB)  # noqa: E501

        :param total_quota: The total_quota of this UidLimitsBody.  # noqa: E501
        :type: float
        """

        self._total_quota = total_quota

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
        if issubclass(UidLimitsBody, dict):
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
        if not isinstance(other, UidLimitsBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
