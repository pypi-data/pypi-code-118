# Copyright (c) 2022 The Razo Community
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from __future__ import with_statement
from setuptools import setup
from razo import vers
six_classifiers = [
    "Development Status :: 4 - Beta",
    "Programming Language :: Python :: 3",
    "Intended Audience :: End Users/Desktop",
    "License :: OSI Approved :: MIT License",
    "Topic :: Utilities",
]

    
with open("README.rst", "r") as fp:
    six_long_description = fp.read()

setup(name="razo",
      version=vers[0],
      author="Fred Dumb",
      author_email="vmuonline@126.com",
      url="https://github.com/fredongit/razo",
      tests_require=["pytest"],
      packages=['razo','langpack'],
      description="Run command system in Python",
      long_description=six_long_description,
      license="MIT",
      classifiers=six_classifiers,
      python_requires=">=3.6",
      )
