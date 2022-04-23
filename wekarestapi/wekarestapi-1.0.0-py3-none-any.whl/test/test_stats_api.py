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
from wekarestapi.api.stats_api import StatsApi  # noqa: E501
from wekarestapi.rest import ApiException


class TestStatsApi(unittest.TestCase):
    """StatsApi unit test stubs"""

    def setUp(self):
        self.api = StatsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_real_time_stats(self):
        """Test case for get_real_time_stats

        Get real time stats  # noqa: E501
        """
        pass

    def test_get_stats(self):
        """Test case for get_stats

        Get stats  # noqa: E501
        """
        pass

    def test_get_stats_description(self):
        """Test case for get_stats_description

        Get stats description  # noqa: E501
        """
        pass

    def test_get_stats_disk_usage(self):
        """Test case for get_stats_disk_usage

        Get stats retention and estimated disk usage  # noqa: E501
        """
        pass

    def test_get_stats_retention(self):
        """Test case for get_stats_retention

        Set stats retention  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
