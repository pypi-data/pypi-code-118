# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['scm_config']

package_data = \
{'': ['*']}

install_requires = \
['colorama>=0.4.4,<0.5.0',
 'deepdiff>=5.7.0,<6.0.0',
 'dynaconf>=3.1.5,<4.0.0',
 'ordered-set>=4.0.2,<5.0.0',
 'pytest>=7.0.1,<8.0.0',
 'typer>=0.4.1,<0.5.0',
 'wheel>=0.37.1,<0.38.0']

entry_points = \
{'console_scripts': ['scm = scm_config.main:main_cli']}

setup_kwargs = {
    'name': 'scm-config',
    'version': '0.2.2',
    'description': 'self configuration management written in Python',
    'long_description': '# SCM\nSelf Managed Configuration Management(SCM) is a simple command line app for configuration management, written in python.\n> Designed to run only on ubuntu operating system\n\nThis tool, currently supports only three resources \n* service\n* directory\n* file \n\n\n# Resource Detailed information \n## Service \nService resource is useful for installing and managing packages from the linux repository, \n> Note that currently this tool is designed to support only on Ubuntu Operating System\n\n***Name parameter in the below section is a list format, meaning it can take multiple values and the actions and other parameters are applied to each name resource accordingly**\n### Example \n```\n[service.setup]\nname = ["apache2"] \naction= ["install", "enable"]\n```\nIn the above example, "service" is the resource and "setup" is the service identifier. \n* name  -> Name of the service that is to be installed on the ubuntu system \n* action -> Action to be done on the listed service, currently these are only supported \n> ["install", "enable", "disable"]\n\n```\n[service.ops]\nname = ["apache2"]\naction =["restart"]\n```\nIn the above example, "service" is the resource and "ops" is the service identifier. once the service is installed and service operations can be done using this tool. \n* name  -> Name of the service that is to be installed on the ubuntu system \n* action -> Action to be done on the listed service, currently these are only supported \n> ["stop", "start", "restart", "reload", "disable", "enable"]\n\n## Directory\nDirectory resource is useful for installing and managing the metadata directories on the system, \n> Note that currently this resource is tested only on Ubuntu Operating System, but can run on any Linux Operating System\n\n### Example \n```\n# Modify the directory permissions \n[directory.list]\nname = ["/etc/apache"] \nparams = {\'owner\'=\'root\',\'group\'=\'root\',\'mode\'= \'0755\'}\naction = [\'create\']\nnotifies = "@format {this.service.ops}"\n```\nIn the above example, "directory" is the resource and "list" is the service identifier. \n* name  -> Name of the directory where the metadata needs modification including creation of the directory using the action method\n* params -> parameter to support the directory operations, currently [\'owner\', \'group\' and \'mode\'] are supported in the list \n* action -> Action to be done on the listed service, currently for directories only [\'create\'] is supported\n* notifies -> Parameter to notify any other resource in the same recipe file, In example, notifies the service ops resources, that would restart the apache2 service based on the modifications \n> ["install", "enable", "disable"]\n\n### Example \n```\n# Modify the input content of the file \n[file.conf]\nname = ["/var/www/customers/public_html/index.php"]\naction = ["create"]\noverride ="true"\ncontent  = ["This is the test file"]\nparams = {\'owner\'= \'root\',\'group\'= \'root\',\'mode\' = \'0755\'}\nnotifies = "@format {this.service.ops}"\n\n```\nIn the above example, "file" is the resource and "conf" is the service identifier. \n* name  -> Name of the file where the content need to be added or appended based on the configuration requirement\n* action -> Action to be done on the listed service, currently for file only [\'create\'] is supported\n* override -> This parameter will override if there is any existing file, default it will append the content to the file \n* content -> Input content for the file provide in the form the double quotes. For simplicity ,large content is not tested with the current version of the code. \n* params -> parameter to support the file operations, currently [\'owner\', \'group\' and \'mode\'] are supported in the list \n* notifies -> Parameter to notify any other resource in the same recipe file, In example, notifies the service ops resources, that would restart the apache2 service based on the modifications \n> ["install", "enable", "disable"]\n\n# Complete overview of the example file \n\n```toml\n# Service setup for the apache instance \n[service.setup]\nname = ["apache2"] \naction= ["install", "enable"]\n\n# Service restart for the apache instance \n[service.ops]\nname = ["apache2"]\naction =["restart"]\n\n\n# Modify the directory permissions \n[directory.list]\nname = ["/etc/apache"] \nparams = {\'owner\'=\'root\',\'group\'=\'root\',\'mode\'= \'0755\'}\naction = [\'create\']\nnotifies = "@format {this.service.ops}"\n\n# Modify the input content of the file \n[file.conf]\nname = ["/var/www/customers/public_html/index.php"]\naction = ["create"]\ncontent  = ["This is the test file"]\nparams = {\'owner\'= \'root\',\'group\'= \'root\',\'mode\' = \'0755\'}\nnotifies = "@format {this.service.ops}"\n```\n# Installation and Usage # \n\n## Manual clone\n```bash\n  $ git clone https://github.com/Sai-Repalle/scm_project\n  $ cd scm_project\n  $ python3 -m venv venv \n  $ source venv/bin/activate\n  $ pip install -r requirements.txt \n```\n## Usage\n```bash\nUsage: scm [OPTIONS] COMMAND [ARGS]...\nOptions:\n  -v, --version         Display\\\'s the application version\n  --install-completion  Install completion for the current shell.\n  --show-completion     Show completion for the current shell, to copy it or\n                        customize the installation.\n  --help                Show this message and exit.\n\nCommands:\n  create\n  diff\n  info\n  init\n  push\n  validate\n\n```\n## initialization\ninit command is used for initialization and helpful to create the respective directories, also this command is useful for expanding future versions of the scm tool\n\n`init <keyword>`\nTo start with the tool, initialize the tool without any parameters, this would set the configuration files required for tool to work\n```bash\n$ scm init python\n```\n### output \n```bash\nscm init   \nroot@machine:~/scm# python3 -m scm init\n[INFO][04-22-2022 06:08:13]::Reading the Json configuration /root/scm/scm/settings/settings.json\n[INFO][04-22-2022 06:08:13]::creating directory CONFIG_DIR\n[INFO][04-22-2022 06:08:13]::creating directory CONFIG_HASH_DIR\n[INFO][04-22-2022 06:08:13]::creating files CONFIG_DEF_FILE\n[INFO][04-22-2022 06:08:13]::creating files CONFIG_HASH_FILE\n\n```\n## create\n`create <name>`\n```bash\n$ scm init --receipe_name <receipe_name>\n```\nBelow example, will create a receipe called "apache" and `apache.toml` file is created in the config directory located at the root directory of the scm \n### output \n```bash\nroot@machine:~/scm# python3 -m scm create --receipe apache\n[INFO][04-22-2022 06:09:56]::Reading the Json configuration /root/scm/scm/settings/settings.json\n[INFO][04-22-2022 06:09:56]::creating directory CONFIG_DIR\n[INFO][04-22-2022 06:09:56]::CONFIG_DIR directory already exists\n[INFO][04-22-2022 06:09:56]::creating directory CONFIG_HASH_DIR\n[INFO][04-22-2022 06:09:56]::CONFIG_HASH_DIR directory already exists\n[INFO][04-22-2022 06:09:56]::creating files CONFIG_DEF_FILE\n[INFO][04-22-2022 06:09:56]::creating files CONFIG_HASH_FIL\n```\n\n\n## info\n`info --receipe_name <name>`\n```bash\n$ scm info --receipe_name <receipe_name>\n```\n```bash \n\n```\n## validate\n`validate <name>`\n```bash\n$ scm validate --receipe_name <receipe_name>\n```\n\n## push\n`push <name>`\n```bash\n$ scm push --receipe_name <receipe_name>\n```\n\n## clean\n`clean <name>`\n```bash\n$ scm clean --receipe_name <receipe_name>\n```',
    'author': 'Sai Repalle',
    'author_email': 'n.repalle85@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Sai-Repalle/scm_project',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
