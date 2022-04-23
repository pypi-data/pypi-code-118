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
from wekarestapi.models.inline_response2008 import InlineResponse2008  # noqa: E501
from wekarestapi.rest import ApiException


class TestInlineResponse2008(unittest.TestCase):
    """InlineResponse2008 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testInlineResponse2008(self):
        """Test InlineResponse2008"""
        # FIXME: construct object with mandatory attributes with example values
        # model = wekarestapi.models.inline_response2008.InlineResponse2008()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
