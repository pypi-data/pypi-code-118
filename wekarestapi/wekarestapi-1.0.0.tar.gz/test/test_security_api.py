# coding: utf-8

"""
    @weka-api

    <div>The Weka system supports a RESTful API. This is useful when automating the interaction with the Weka system and when integrating it into your workflows or monitoring systems. The API is accessible at port 14000, via the /api/v2 URL, you can explore it via /api/v2/docs when accessing from the cluster (e.g. https://weka01:14000/api/v2/docs).<div style=\"margin-top: 15px;\">Note: Weka uses 64bit numbers. Please take special care when interacting with the API with different program languages (In JS for example you can use \"json-bigint\")</div></div>  # noqa: E501

    OpenAPI spec version: 3.14
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import wekarestapi
from wekarestapi.api.security_api import SecurityApi  # noqa: E501
from wekarestapi.rest import ApiException


class TestSecurityApi(unittest.TestCase):
    """SecurityApi unit test stubs"""

    def setUp(self):
        self.api = SecurityApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_disable_login_banner(self):
        """Test case for disable_login_banner

        Disable login banner  # noqa: E501
        """
        pass

    def test_enable_login_banner(self):
        """Test case for enable_login_banner

        Enable login banner  # noqa: E501
        """
        pass

    def test_get_login_banner(self):
        """Test case for get_login_banner

        Get the login banner  # noqa: E501
        """
        pass

    def test_get_tokens_expiry(self):
        """Test case for get_tokens_expiry

        Get tokens default expiry time  # noqa: E501
        """
        pass

    def test_get_tokens_expiry_deprecated(self):
        """Test case for get_tokens_expiry_deprecated

        Get tokens default expiry time  # noqa: E501
        """
        pass

    def test_set_ca_cert(self):
        """Test case for set_ca_cert

        Set a CA-Cert for the cluster (Vault)  # noqa: E501
        """
        pass

    def test_set_login_banner(self):
        """Test case for set_login_banner

        Set the login banner  # noqa: E501
        """
        pass

    def test_show_ca_cert(self):
        """Test case for show_ca_cert

        Show the CA-Cert for the cluster (Vault)  # noqa: E501
        """
        pass

    def test_unset_ca_cert(self):
        """Test case for unset_ca_cert

        Unset a CA-Cert for the cluster (Vault)  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
