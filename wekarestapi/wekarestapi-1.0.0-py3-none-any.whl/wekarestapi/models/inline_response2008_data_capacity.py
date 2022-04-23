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

class InlineResponse2008DataCapacity(object):
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
        'total_bytes': 'float',
        'hot_spare_bytes': 'float',
        'unprovisioned_bytes': 'float'
    }

    attribute_map = {
        'total_bytes': 'total_bytes',
        'hot_spare_bytes': 'hot_spare_bytes',
        'unprovisioned_bytes': 'unprovisioned_bytes'
    }

    def __init__(self, total_bytes=None, hot_spare_bytes=None, unprovisioned_bytes=None):  # noqa: E501
        """InlineResponse2008DataCapacity - a model defined in Swagger"""  # noqa: E501
        self._total_bytes = None
        self._hot_spare_bytes = None
        self._unprovisioned_bytes = None
        self.discriminator = None
        if total_bytes is not None:
            self.total_bytes = total_bytes
        if hot_spare_bytes is not None:
            self.hot_spare_bytes = hot_spare_bytes
        if unprovisioned_bytes is not None:
            self.unprovisioned_bytes = unprovisioned_bytes

    @property
    def total_bytes(self):
        """Gets the total_bytes of this InlineResponse2008DataCapacity.  # noqa: E501


        :return: The total_bytes of this InlineResponse2008DataCapacity.  # noqa: E501
        :rtype: float
        """
        return self._total_bytes

    @total_bytes.setter
    def total_bytes(self, total_bytes):
        """Sets the total_bytes of this InlineResponse2008DataCapacity.


        :param total_bytes: The total_bytes of this InlineResponse2008DataCapacity.  # noqa: E501
        :type: float
        """

        self._total_bytes = total_bytes

    @property
    def hot_spare_bytes(self):
        """Gets the hot_spare_bytes of this InlineResponse2008DataCapacity.  # noqa: E501


        :return: The hot_spare_bytes of this InlineResponse2008DataCapacity.  # noqa: E501
        :rtype: float
        """
        return self._hot_spare_bytes

    @hot_spare_bytes.setter
    def hot_spare_bytes(self, hot_spare_bytes):
        """Sets the hot_spare_bytes of this InlineResponse2008DataCapacity.


        :param hot_spare_bytes: The hot_spare_bytes of this InlineResponse2008DataCapacity.  # noqa: E501
        :type: float
        """

        self._hot_spare_bytes = hot_spare_bytes

    @property
    def unprovisioned_bytes(self):
        """Gets the unprovisioned_bytes of this InlineResponse2008DataCapacity.  # noqa: E501


        :return: The unprovisioned_bytes of this InlineResponse2008DataCapacity.  # noqa: E501
        :rtype: float
        """
        return self._unprovisioned_bytes

    @unprovisioned_bytes.setter
    def unprovisioned_bytes(self, unprovisioned_bytes):
        """Sets the unprovisioned_bytes of this InlineResponse2008DataCapacity.


        :param unprovisioned_bytes: The unprovisioned_bytes of this InlineResponse2008DataCapacity.  # noqa: E501
        :type: float
        """

        self._unprovisioned_bytes = unprovisioned_bytes

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
        if issubclass(InlineResponse2008DataCapacity, dict):
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
        if not isinstance(other, InlineResponse2008DataCapacity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
