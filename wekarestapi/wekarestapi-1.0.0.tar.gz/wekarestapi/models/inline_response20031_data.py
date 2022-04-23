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

class InlineResponse20031Data(object):
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
        'group': 'str',
        'host_id': 'str',
        'ip': 'str',
        'port': 'str',
        'uid': 'str'
    }

    attribute_map = {
        'group': 'group',
        'host_id': 'host_id',
        'ip': 'ip',
        'port': 'port',
        'uid': 'uid'
    }

    def __init__(self, group=None, host_id=None, ip=None, port=None, uid=None):  # noqa: E501
        """InlineResponse20031Data - a model defined in Swagger"""  # noqa: E501
        self._group = None
        self._host_id = None
        self._ip = None
        self._port = None
        self._uid = None
        self.discriminator = None
        if group is not None:
            self.group = group
        if host_id is not None:
            self.host_id = host_id
        if ip is not None:
            self.ip = ip
        if port is not None:
            self.port = port
        if uid is not None:
            self.uid = uid

    @property
    def group(self):
        """Gets the group of this InlineResponse20031Data.  # noqa: E501


        :return: The group of this InlineResponse20031Data.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this InlineResponse20031Data.


        :param group: The group of this InlineResponse20031Data.  # noqa: E501
        :type: str
        """

        self._group = group

    @property
    def host_id(self):
        """Gets the host_id of this InlineResponse20031Data.  # noqa: E501


        :return: The host_id of this InlineResponse20031Data.  # noqa: E501
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this InlineResponse20031Data.


        :param host_id: The host_id of this InlineResponse20031Data.  # noqa: E501
        :type: str
        """

        self._host_id = host_id

    @property
    def ip(self):
        """Gets the ip of this InlineResponse20031Data.  # noqa: E501


        :return: The ip of this InlineResponse20031Data.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this InlineResponse20031Data.


        :param ip: The ip of this InlineResponse20031Data.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def port(self):
        """Gets the port of this InlineResponse20031Data.  # noqa: E501


        :return: The port of this InlineResponse20031Data.  # noqa: E501
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this InlineResponse20031Data.


        :param port: The port of this InlineResponse20031Data.  # noqa: E501
        :type: str
        """

        self._port = port

    @property
    def uid(self):
        """Gets the uid of this InlineResponse20031Data.  # noqa: E501


        :return: The uid of this InlineResponse20031Data.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this InlineResponse20031Data.


        :param uid: The uid of this InlineResponse20031Data.  # noqa: E501
        :type: str
        """

        self._uid = uid

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
        if issubclass(InlineResponse20031Data, dict):
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
        if not isinstance(other, InlineResponse20031Data):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
