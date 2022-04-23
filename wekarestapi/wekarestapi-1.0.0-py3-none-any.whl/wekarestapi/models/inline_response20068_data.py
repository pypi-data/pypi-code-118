# coding: utf-8

"""
    @weka-api

    <div>The Weka system supports a RESTful API. This is useful when automating the interaction with the Weka system and when integrating it into your workflows or monitoring systems. The API is accessible at port 14000, via the /api/v2 URL, you can explore it via /api/v2/docs when accessing from the cluster (e.g. https://weka01:14000/api/v2/docs).<div style=\"margin-top: 15px;\">Note: Weka uses 64bit numbers. Please take special care when interacting with the API with different program languages (In JS for example you can use \"json-bigint\")</div></div>  # noqa: E501

    OpenAPI spec version: 3.12.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InlineResponse20068Data(object):
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
        'resend_secs': 'float',
        'result': 'InlineResponse20068DataResult',
        'completed': 'bool'
    }

    attribute_map = {
        'resend_secs': 'resend_secs',
        'result': 'result',
        'completed': 'completed'
    }

    def __init__(self, resend_secs=None, result=None, completed=None):  # noqa: E501
        """InlineResponse20068Data - a model defined in Swagger"""  # noqa: E501
        self._resend_secs = None
        self._result = None
        self._completed = None
        self.discriminator = None
        if resend_secs is not None:
            self.resend_secs = resend_secs
        if result is not None:
            self.result = result
        if completed is not None:
            self.completed = completed

    @property
    def resend_secs(self):
        """Gets the resend_secs of this InlineResponse20068Data.  # noqa: E501


        :return: The resend_secs of this InlineResponse20068Data.  # noqa: E501
        :rtype: float
        """
        return self._resend_secs

    @resend_secs.setter
    def resend_secs(self, resend_secs):
        """Sets the resend_secs of this InlineResponse20068Data.


        :param resend_secs: The resend_secs of this InlineResponse20068Data.  # noqa: E501
        :type: float
        """

        self._resend_secs = resend_secs

    @property
    def result(self):
        """Gets the result of this InlineResponse20068Data.  # noqa: E501


        :return: The result of this InlineResponse20068Data.  # noqa: E501
        :rtype: InlineResponse20068DataResult
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this InlineResponse20068Data.


        :param result: The result of this InlineResponse20068Data.  # noqa: E501
        :type: InlineResponse20068DataResult
        """

        self._result = result

    @property
    def completed(self):
        """Gets the completed of this InlineResponse20068Data.  # noqa: E501


        :return: The completed of this InlineResponse20068Data.  # noqa: E501
        :rtype: bool
        """
        return self._completed

    @completed.setter
    def completed(self, completed):
        """Sets the completed of this InlineResponse20068Data.


        :param completed: The completed of this InlineResponse20068Data.  # noqa: E501
        :type: bool
        """

        self._completed = completed

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
        if issubclass(InlineResponse20068Data, dict):
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
        if not isinstance(other, InlineResponse20068Data):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
