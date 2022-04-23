#!/usr/bin/env python

"""Tests for `json2xml` package."""


import unittest
from collections import OrderedDict
from pyexpat import ExpatError

import pytest
import xmltodict
import json

from json2xml import json2xml
from json2xml.dicttoxml import dicttoxml
from json2xml.utils import InvalidDataError, readfromjson, readfromstring, readfromurl, \
    JSONReadError, StringReadError, URLReadError


class TestJson2xml(unittest.TestCase):
    """Tests for `json2xml` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_read_from_json(self):
        """Test something."""
        data = readfromjson("examples/bigexample.json")
        if type(data) == 'list':
            # it's json array, so we just take the first element and check it's type
            assert type(data[0]) is dict
        else:
            data = readfromjson("examples/licht.json")
            assert type(data) is dict

    def test_read_from_invalid_json(self):
        """Test something."""
        with pytest.raises(JSONReadError) as pytest_wrapped_e:
            readfromjson("examples/licht_wrong.json")
        assert pytest_wrapped_e.type == JSONReadError

    def test_read_from_url(self):
        data = readfromurl("https://coderwall.com/vinitcool76.json")
        assert type(data) is dict

    def test_read_from_wrong_url(self):
        with pytest.raises(URLReadError) as pytest_wrapped_e:
            readfromurl("https://coderwall.com/vinitcool76.jsoni")
        assert pytest_wrapped_e.type == URLReadError

    def test_read_from_jsonstring(self):
        data = readfromstring(
            '{"login":"mojombo","id":1,"avatar_url":"https://avatars0.githubusercontent.com/u/1?v=4"}'
        )
        assert type(data) is dict

    def test_read_from_invalid_jsonstring(self):
        with pytest.raises(StringReadError) as pytest_wrapped_e:
            readfromstring(
                '{"login":"mojombo","id":1,"avatar_url":"https://avatars0.githubusercontent.com/u/1?v=4"'
            )
        assert pytest_wrapped_e.type == StringReadError

    def test_json_to_xml_conversion(self):
        data = readfromstring(
            '{"login":"mojombo","id":1,"avatar_url":"https://avatars0.githubusercontent.com/u/1?v=4"}'
        )
        xmldata = json2xml.Json2xml(data).to_xml()
        dict_from_xml = xmltodict.parse(xmldata)
        assert type(dict_from_xml["all"]) == OrderedDict

    def test_custom_wrapper_and_indent(self):
        data = readfromstring(
            '{"login":"mojombo","id":1,"avatar_url":"https://avatars0.githubusercontent.com/u/1?v=4"}'
        )
        xmldata = json2xml.Json2xml(data, wrapper="test", pretty=False).to_xml()
        old_dict = xmltodict.parse(xmldata)
        # test must be present, snce it is the wrpper
        assert "test" in old_dict.keys()
        # reverse test, say a wrapper called ramdom won't be present
        assert "random" not in old_dict.keys()

    def test_no_wrapper(self):
        data = readfromstring(
            '{"login":"mojombo","id":1,"avatar_url":"https://avatars0.githubusercontent.com/u/1?v=4"}'
        )
        xmldata = json2xml.Json2xml(data, root=False, pretty=False).to_xml()
        assert xmldata.startswith(b'<login type="str">mojombo</login>')
        self.assertRaises(ExpatError, xmltodict.parse, xmldata)

    def test_item_wrap(self):
        data = readfromstring(
            '{"my_items":[{"my_item":{"id":1} },{"my_item":{"id":2} }],"my_str_items":["a","b"]}'
        )
        xmldata = json2xml.Json2xml(data, pretty=False).to_xml()
        old_dict = xmltodict.parse(xmldata)
        # item must be present within my_items
        print(xmldata)
        assert "item" in old_dict['all']['my_items']
        assert "item" in old_dict['all']['my_str_items']

    def test_no_item_wrap(self):
        data = readfromstring(
            '{"my_items":[{"my_item":{"id":1} },{"my_item":{"id":2} }],"my_str_items":["a","b"]}'
        )
        xmldata = json2xml.Json2xml(data, pretty=False, item_wrap=False).to_xml()
        old_dict = xmltodict.parse(xmldata)
        # my_item must be present within my_items
        print(xmldata)
        assert "my_item" in old_dict['all']['my_items']
        assert "my_str_items" in old_dict['all']

    def test_empty_array(self):
        data = readfromstring(
            '{"empty_list":[]}'
        )
        xmldata = json2xml.Json2xml(data, pretty=False).to_xml()
        old_dict = xmltodict.parse(xmldata)
        print(xmldata)
        # item empty_list be present within all
        assert "empty_list" in old_dict['all']

    def test_attrs(self):
        data = readfromstring(
            '{"my_string":"a","my_int":1,"my_float":1.1,"my_bool":true,"my_null":null,"empty_list":[],"empty_dict":{}}'
        )
        xmldata = json2xml.Json2xml(data, pretty=False).to_xml()
        old_dict = xmltodict.parse(xmldata)
        print(xmldata)
        # test all attrs
        assert "str" == old_dict['all']['my_string']['@type']
        assert "int" == old_dict['all']['my_int']['@type']
        assert "float" == old_dict['all']['my_float']['@type']
        assert "bool" == old_dict['all']['my_bool']['@type']
        assert "null" == old_dict['all']['my_null']['@type']
        assert "list" == old_dict['all']['empty_list']['@type']
        assert "dict" == old_dict['all']['empty_dict']['@type']

    def test_dicttoxml_bug(self):
        input_dict = {
            'response': {
                'results': {
                    'user': [{
                        'name': 'Ezequiel', 'age': '33', 'city': 'San Isidro'
                        }, {
                        'name': 'Belén', 'age': '30', 'city': 'San Isidro'}]}}}

        xmldata = json2xml.Json2xml(
            json.dumps(input_dict), wrapper='response', pretty=False, attr_type=False, item_wrap=False
            ).to_xml()

        old_dict = xmltodict.parse(xmldata)
        assert 'response' in old_dict.keys()

    def test_dict2xml_no_root(self):
        payload = {'mock': 'payload'}
        result = dicttoxml(payload, attr_type=False, root=False)
        assert b'<mock>payload</mock>' == result

    def test_dict2xml_with_root(self):
        payload = {'mock': 'payload'}
        result = dicttoxml(payload, attr_type=False)
        assert b'<?xml version="1.0" encoding="UTF-8" ?><root><mock>payload</mock></root>' == result

    def test_dict2xml_with_custom_root(self):
        payload = {'mock': 'payload'}
        result = dicttoxml(payload, attr_type=False, custom_root="element")
        assert b'<?xml version="1.0" encoding="UTF-8" ?><element><mock>payload</mock></element>' == result

    def test_bad_data(self):
        data = b"!\0a8f"
        decoded = data.decode("utf-8")
        with pytest.raises(InvalidDataError) as pytest_wrapped_e:
            json2xml.Json2xml(decoded).to_xml()
        assert pytest_wrapped_e.type == InvalidDataError

    def test_read_boolean_data_from_json(self):
        """Test correct return for boolean types."""
        data = readfromjson("examples/booleanjson.json")
        result = json2xml.Json2xml(data).to_xml()
        print(result)
        dict_from_xml = xmltodict.parse(result)
        print(dict_from_xml)
        assert dict_from_xml["all"]["boolean"]["#text"] != 'True'
        assert dict_from_xml["all"]["boolean"]["#text"] == 'true'
        assert dict_from_xml["all"]["boolean_dict_list"]["item"][0]["boolean_dict"]["boolean"]["#text"] == 'true'
        assert dict_from_xml["all"]["boolean_dict_list"]["item"][1]["boolean_dict"]["boolean"]["#text"] == 'false'
        assert dict_from_xml["all"]["boolean_list"]["item"][0]["#text"] == 'true'
        assert dict_from_xml["all"]["boolean_list"]["item"][1]["#text"] == 'false'

    def test_read_boolean_data_from_json2(self):
        """Test correct return for boolean types."""
        data = readfromjson("examples/booleanjson2.json")
        result = json2xml.Json2xml(data).to_xml()
        print(result)
        dict_from_xml = xmltodict.parse(result)
        print(dict_from_xml)
        assert dict_from_xml["all"]["boolean_list"]["item"][0]["#text"] != 'True'
        assert dict_from_xml["all"]["boolean_list"]["item"][0]["#text"] == 'true'
        assert dict_from_xml["all"]["boolean_list"]["item"][1]["#text"] == 'false'
        assert dict_from_xml["all"]["number_array"]["item"][0]["#text"] == '1'
        assert dict_from_xml["all"]["number_array"]["item"][1]["#text"] == '2'
        assert dict_from_xml["all"]["number_array"]["item"][2]["#text"] == '3'
        assert dict_from_xml["all"]["string_array"]["item"][0]["#text"] == 'a'
        assert dict_from_xml["all"]["string_array"]["item"][1]["#text"] == 'b'
        assert dict_from_xml["all"]["string_array"]["item"][2]["#text"] == 'c'

    def test_dict2xml_with_namespaces(self):
        data = {'ns1:node1': 'data in namespace 1', 'ns2:node2': 'data in namespace 2'}
        namespaces = {'ns1': 'http://www.google.de/ns1', 'ns2': 'http://www.google.de/ns2'}
        result = dicttoxml(data, attr_type=False, xml_namespaces=namespaces)
        print(result)
        assert b'<?xml version="1.0" encoding="UTF-8" ?>' \
               b'<root xmlns:ns1="http://www.google.de/ns1" xmlns:ns2="http://www.google.de/ns2">' \
               b'<ns1:node1>data in namespace 1</ns1:node1>' \
               b'<ns2:node2>data in namespace 2</ns2:node2>' \
               b'</root>' == result

    def test_dict2xml_with_flat(self):
        data = {'flat_list@flat': [1, 2, 3], 'non_flat_list': [4, 5, 6]}
        result = dicttoxml(data, attr_type=False)
        print(result)
        assert b'<?xml version="1.0" encoding="UTF-8" ?>' \
               b'<root><item>1</item><item>2</item><item>3</item>' \
               b'<non_flat_list><item>4</item><item>5</item><item>6</item></non_flat_list>' \
               b'</root>' == result

    def test_dict2xml_with_val_and_custom_attr(self):
        # in order to use @attr in non-dict objects, we need to lift into a dict and combine with @val as key
        data = {'list1': [1, 2, 3], 'list2': {'@attrs': {'myattr1': 'myval1', 'myattr2': 'myval2'}, '@val': [4, 5, 6]}}
        result = dicttoxml(data, attr_type=False)
        print(result)
        assert b'<?xml version="1.0" encoding="UTF-8" ?>' \
               b'<root><list1><item>1</item><item>2</item><item>3</item></list1>' \
               b'<list2 myattr1="myval1" myattr2="myval2"><item>4</item><item>5</item><item>6</item></list2>' \
               b'</root>' == result
