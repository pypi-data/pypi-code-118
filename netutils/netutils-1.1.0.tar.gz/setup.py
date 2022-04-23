# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['netutils', 'netutils.config']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'netutils',
    'version': '1.1.0',
    'description': 'Common helper functions useful in network automation.',
    'long_description': '# netutils\n\nA Python library that is a collection of objects for common network automation tasks.\n\nThis library intends to keep the following tenets:\n\n* Must not be any dependencies required to run the library.\n  * May be some optional dependencies, to be managed by the user in opt in fashion.\n* Shall prefer functions over classes.\n* Shall prefer a folder and file structure that is flat.\n* Shall leverage docstrings as the primary documentation mechanism.\n  * Must provide examples in every public function.\n* Shall retain a high test coverage.\n\n# Function Groupings\n\nFunctions are grouped with like functions, such as IP or MAC address based functions. Included to date are groupings of:\n\n* Bandwidth - Provides the ability to convert between various bandwidth values.\n* Banner - Provides the ability to normalize the various banner delimiters.\n* BGP ASN - Provides the ability to convert BGP ASN from integer to dot notation.\n* Configuration\n  * Cleaning - Provides the ability to remove or replace lines based on regex matches.\n  * Compliance - Provides the ability to compare two configurations to sanely understand the differences.\n  * Parsing - Provides the ability to parse configuration for the minor differences that are there.\n* DNS - Provides the ability to work with DNS, such as validating that a FQDN is resolvable.\n* Interface - Provides the ability to work with interface names, expanding, abbreviating, and spliting the names.\n* IP Address - Provides the ability to work with IP addresses, primarily exposing Python `ipaddress` functionality.\n* Library Mapper - Provides mappings in expected vendor names between Netmiko, NAPALM, pyntc, ntc-templates, pyats, and scrapli.\n* MAC Address - Provides the ability to work with MAC addresses such as validating or converting to integer.\n* Password - Provides the ability to compare and encrypt common password schemas such as type5 and type7 Cisco passwords.\n* Ping - Provides the ability to ping, currently only tcp ping.\n* Protocol Mapper - Provides a mapping for protocol names to numbers and vice versa.\n* Route - Provides the ability to provide a list of routes and an IP Address and return the longest prefix matched route.\n* Time -Provides the ability to convert between integer time and string times.\n* VLANs - Provide the ability to convert configuration into lists or lists into configuration.\n\n# Installation\n\nOption 1: Install from PyPI.\n\n```bash\n$ pip install netutils\n```\n\nOption 2: Install from a GitHub branch, such as develop as shown below.\n\n```bash\n$ pip install git+https://github.com/networktocode/netutils.git@develop\n```\n\n# Examples\n\nWhile all functions come with examples in the docstrings, for quick reference of the types of problems this library intends to\nsolve the following examples are provided.\n\nThe following function will help in deploying list of VLANs and match the configuration style in a standard IOS-like configurations.\n\n```python\n>>> from netutils.vlan import vlanlist_to_config\n>>>\n>>> vlan_cfg = vlanlist_to_config([1, 2, 3, 5, 6, 1000, 1002, 1004, 1006, 1008, 1010, 1012, 1014, 1016, 1018])\n>>>\n>>> vlan_cfg\n["1-3,5,6,1000,1002,1004,1006,1008,1010,1012,1014", "1016,1018"]\n>>>\n>>> for index, line in enumerate(vlan_cfg):\n...     if index == 0:\n...         print(f"  switchport trunk allowed vlan {line}")\n...     else:\n...         print(f"  switchport trunk allowed vlan add {line}")\n...\n  switchport trunk allowed vlan 1-3,5,6,1000,1002,1004,1006,1008,1010,1012,1014\n  switchport trunk allowed vlan add 1016,1018\n>>>\n```\n\nYou may want to compare a known password with a given encrypted password. This can help in verifying if the\npasswords are as expected for compliance reasons.\n\n```python\n>>> from netutils.password import compare_type5\n>>>\n>>> compare_type5("cisco","$1$nTc1$Z28sUTcWfXlvVe2x.3XAa.")\nTrue\n>>>\n>>> compare_type5("not_cisco","$1$nTc1$Z28sUTcWfXlvVe2x.3XAa.")\nFalse\n>>>\n```\n\nOften times interfaces will come in various different shortened names, and it is helpful to normalize them.\n\n```python\n>>> from netutils.interface import canonical_interface_name\n>>>\n>>> canonical_interface_name("Gi1/0/1")\n\'GigabitEthernet1/0/1\'\n>>>\n>>> canonical_interface_name("Eth1")\n\'Ethernet1\'\n>>>\n```\n\nThese are just some examples of the many functions provided by this library.\n\n# Attribution\n\nThe library was built to be a centralized place for common network automation code to be accessed. While in most cases it is\ndifficult, if not impossible to understand the origin of code, the following intends to describe the known motivation for where\ncode was derived from and in the few cases where actual code was directly taken from. Except where noted, all code is believed to\nbe unattributable, from @itdependsnetworks, or from another Network to Code employee. If this is in fact an error, please open an\nissue, and the proper attribution will be provided. Any errors were not done out of malice, but rather the natural developer\nworkflow of pulling snippets of code from existing locations such as StackOverflow and Github over months and years of development.\nAs an example it is nearly impossible to understand the original author of Cisco type7 encryption/decryption in the sea of\navailable code, and remains unattributable though clearly originally developed prior to this library being created.\n\nInfluencers\n* [Netmiko](https://github.com/ktbyers/netmiko)\n* [NAPALM](https://github.com/napalm-automation/napalm)\n* [Ansible](https://github.com/ansible/ansible)\n* [IPCal](https://github.com/ammyblabla/ipcal)\n* [StackOverflow](https://stackoverflow.com/)\n* [Python 3 Docs](https://docs.python.org/3/library/)\n\nIn many instances variables and function names were reused, but the code was built from scratch to avoid any potential licensing\nissues. Functions that were known to be rewritten and their known origin.\n\n| Function | Origin |\n| -------- | ------ |\n| asn_to_int | NAPALM |\n| is_ip | IPCal |\n| ip_to_bin | IPCal |\n| get_usable_range | IPCal |\n| encrypt_type7 | unknown |\n| decrypt_type7 | unknown |\n| vlan_to_list | Ansible |\n| sanitize_config | NAPALM |\n\nRelevant PR\'s\n* https://github.com/napalm-automation/napalm/pull/493\n* https://github.com/ansible/ansible/pull/39901\n* https://github.com/ansible/ansible/pull/26566\n\nIn building out the time conversion, the regex patterns are based on NAPALM implementation with their consent.\n\n# Contributing\n\nPull requests are welcomed and automatically built and tested against multiple versions of Python through TravisCI.\nExcept for unit tests, testing is only supported on Python 3.7.\n\nThe project is packaged with a light development environment based on `docker-compose` to help with the local development of the project and to run tests within TravisCI.\n\nThe project is following Network to Code software development guidelines and are leveraging the following:\n- Black, Pylint, Bandit, flake8, and pydocstyle for Python linting and formatting.\n- pytest, coverage, and unittest for unit tests.\n\nThere are a number of things that are required in order to have a successful PR.\n\n- All new functions must contain at least 1 example in their docstrings.\n- Docstrings must conform to the google docstring [convention](https://google.github.io/styleguide/pyguide.html#381-docstrings).\n- Unit test for newly added functions are required.\n- If applicable, tests related to config parsing and compliuance must be added.\n- Update the jinja2 filter (netutils.utils.jinja2_convenience_function) for any new functions (see below for details).\n- If you create a new file in the `netutils` folder, you must create a new folder and `index.rst` in the docs folder (see below for details).\n- Your PR must not introduce any required dependencies. You can introduce optional or development dependencies.\n\n## Adding to the jinja2 filter function\n\nTo add a new function to the jinja2 filter, add a new entry to the `_JINJA2_FUNCTION_MAPPINGS` located in the `utils.py` file. When adding an entry, the key corresponds with the name to call the function and the value to the path to find the function.\n\n## Adding docs for a new python file\n\nIf adding a new python file, the docs must be updated to account for the new file.\n\n1. Create a new folder in `docs/source/netutils` matching the name of your new file.\n2. Create an `index.rst` file in that folder.\n3. Add the following to the newly created file.\n\n```python\n#############################\n# ENTER THE TITLE OF THE PAGE\n##############################\n\n.. automodule:: netutils.newfile\n    :members:\n```\n\n## CLI Helper Commands\n\nThe project features a CLI helper based on [invoke](http://www.pyinvoke.org/) to help setup the development environment. The commands are listed below in 3 categories:\n- `dev environment`\n- `utility`\n- `testing`\n\nEach command can be executed with `invoke <command>`. Each command also has its own help `invoke <command> --help`\n\n### Local dev environment\n\n```\n  build              Build all docker images.\n  clean              Remove the project specific image.\n  rebuild            Clean the Docker image and then rebuild without using cache.\n```\n\n### Utility\n\n```\n  clean-docs         Removes the build directory and all of its contents.\n  check-pypi-version Verify if the version specified already exists on PyPI.\n  cli                Enter the image to perform troubleshooting or dev work.\n  html               Creates html docs using sphinx-build command.\n```\n\n### Testing\n\n```\n  bandit             Run bandit to validate basic static code security analysis.\n  black              Run black to check that Python files adhere to its style standards.\n  coverage           Run the coverage report against pytest.\n  flake8             Run flake8 to check that Python files adhere to its style standards.\n  pylint             Run pylint code analysis.\n  pydocstyle         Run pydocstyle to validate docstring formatting adheres to NTC defined standards.\n  pytest             Run pytest for the specified name and Python version.\n  tests              Run all tests for the specified name and Python version.\n  yamllint           Run yamllint to validate formatting adheres to NTC defined YAML standards.\n```\n\n## Questions\n\nPlease see [the documentation](https://netutils.readthedocs.io/) for detailed documentation on how to use netutils. For any additional questions or\ncomments, feel free to swing by the [Network to Code slack channel](https://networktocode.slack.com/) (channel #networktocode).\nSign up [here](http://slack.networktocode.com/)\n\n',
    'author': 'Network to Code, LLC',
    'author_email': 'opensource@networktocode.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://netutils.readthedocs.io',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
