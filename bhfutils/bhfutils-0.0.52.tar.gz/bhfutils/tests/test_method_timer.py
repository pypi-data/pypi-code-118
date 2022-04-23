'''
Offline utility tests
'''
import sys
import time
from os import path
from unittest import TestCase

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from scutils.method_timer import MethodTimer


class TestMethodTimer(TestCase):

    def test_under(self):
        @MethodTimer.timeout(1, False)
        def method():
            time.sleep(0.5)
            return True
        result = method()
        self.assertTrue(result)

    def test_over(self):
        @MethodTimer.timeout(1, "STUFF")
        def method():
            time.sleep(1.5)
            return True
        result = method()
        self.assertEqual(result, "STUFF")

    def test_params(self):
        @MethodTimer.timeout(1, "STUFF2")
        def method(param1, param2, param3):
            time.sleep(1.5)
            return True
        result = method(True, "Stuff", ['item'])
        self.assertEqual(result, "STUFF2")
