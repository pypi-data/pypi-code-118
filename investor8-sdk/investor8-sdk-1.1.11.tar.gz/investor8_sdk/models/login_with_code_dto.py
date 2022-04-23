# coding: utf-8

"""
    Investor8.Core

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class LoginWithCodeDto(object):
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
        'req_id': 'str',
        'verification_code': 'str'
    }

    attribute_map = {
        'req_id': 'ReqId',
        'verification_code': 'VerificationCode'
    }

    def __init__(self, req_id=None, verification_code=None):  # noqa: E501
        """LoginWithCodeDto - a model defined in Swagger"""  # noqa: E501
        self._req_id = None
        self._verification_code = None
        self.discriminator = None
        if req_id is not None:
            self.req_id = req_id
        if verification_code is not None:
            self.verification_code = verification_code

    @property
    def req_id(self):
        """Gets the req_id of this LoginWithCodeDto.  # noqa: E501


        :return: The req_id of this LoginWithCodeDto.  # noqa: E501
        :rtype: str
        """
        return self._req_id

    @req_id.setter
    def req_id(self, req_id):
        """Sets the req_id of this LoginWithCodeDto.


        :param req_id: The req_id of this LoginWithCodeDto.  # noqa: E501
        :type: str
        """

        self._req_id = req_id

    @property
    def verification_code(self):
        """Gets the verification_code of this LoginWithCodeDto.  # noqa: E501


        :return: The verification_code of this LoginWithCodeDto.  # noqa: E501
        :rtype: str
        """
        return self._verification_code

    @verification_code.setter
    def verification_code(self, verification_code):
        """Sets the verification_code of this LoginWithCodeDto.


        :param verification_code: The verification_code of this LoginWithCodeDto.  # noqa: E501
        :type: str
        """

        self._verification_code = verification_code

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
        if issubclass(LoginWithCodeDto, dict):
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
        if not isinstance(other, LoginWithCodeDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
