# Author: Kenta Nakamura <c60evaporator@gmail.com>
# Copyright (c) 2020-2021 Kenta Nakamura
# License: BSD 3 clause

from setuptools import setup
import seaborn_analyzer

DESCRIPTION = "seaborn-analyzer: data visualization of regression, classification and distribution"
NAME = 'seaborn-analyzer'
AUTHOR = 'Kenta Nakamura'
AUTHOR_EMAIL = 'c60evaporator@gmail.com'
URL = 'https://github.com/c60evaporator/seaborn-analyzer'
LICENSE = 'BSD 3-Clause'
DOWNLOAD_URL = 'https://github.com/c60evaporator/seaborn-analyzer'
VERSION = seaborn_analyzer.__version__
PYTHON_REQUIRES = ">=3.6"

INSTALL_REQUIRES = [
    'matplotlib>=3.3.4',
    'seaborn>=0.11.0',
    'numpy >=1.20.3',
    'pandas>=1.2.4',
    'matplotlib>=3.3.4',
    'scipy>=1.6.3',
    'scikit-learn>=0.24.2',
]

EXTRAS_REQUIRE = {
    'tutorial': [
        'mlxtend>=0.18.0',
        'xgboost>=1.4.2',
    ]
}

PACKAGES = [
    'seaborn_analyzer'
]

CLASSIFIERS = [
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: BSD License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3 :: Only',
    'Topic :: Scientific/Engineering',
    'Topic :: Scientific/Engineering :: Visualization',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'Topic :: Multimedia :: Graphics',
    'Framework :: Matplotlib',
]

with open('README.rst', 'r') as fp:
    readme = fp.read()
with open('CONTACT.txt', 'r') as fp:
    contacts = fp.read()
long_description = readme + '\n\n' + contacts

setup(name=NAME,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      maintainer=AUTHOR,
      maintainer_email=AUTHOR_EMAIL,
      description=DESCRIPTION,
      long_description=long_description,
      license=LICENSE,
      url=URL,
      version=VERSION,
      download_url=DOWNLOAD_URL,
      python_requires=PYTHON_REQUIRES,
      install_requires=INSTALL_REQUIRES,
      extras_require=EXTRAS_REQUIRE,
      packages=PACKAGES,
      classifiers=CLASSIFIERS
    )