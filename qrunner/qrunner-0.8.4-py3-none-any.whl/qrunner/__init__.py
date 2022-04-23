# coding=utf-8
from qrunner.running.runner import main
from qrunner.case import TestCase, Page, H5Page
from qrunner.core.h5.driver import H5Driver
from qrunner.decorate import *
from qrunner.utils.log import logger
from qrunner.utils.decorate import *
from qrunner.utils.mock import mock, mock_en
from time import sleep


__version__ = "0.8.4"
__description__ = "全栈自动化测试框架"

