# This file is placed in the Public Domain.
#
# http://genocide.rtfd.io - EM_T04_OTP-CR-117_19

import os

from setuptools import setup

def read():
    return open("README.rst", "r").read()

def uploadlist(dir):
    upl = []
    for file in os.listdir(dir):
        if not file or file.startswith('.'):
            continue
        d = dir + os.sep + file
        if os.path.isdir(d):   
            upl.extend(uploadlist(d))
        else:
            if file.endswith(".pyc") or file.startswith("__pycache"):
                continue
            upl.append(d)
    return upl

setup(
    name='genocide',
    version='58',
    url='https://github.com/bthate/genocide',
    author='Bart Thate',
    author_email='bthate67@gmail.com', 
    description="Prosector. Reconsider. OTP-CR-117/19.",
    long_description=read(),
    license='Public Domain',
    packages=["genocide"],
    zip_safe=False,
    install_requires=["libobj", "librun", "libexc"],
    include_package_data=True,
    data_files=[
                ("share/genocide", uploadlist("files")),
                ("man/man1", ["files/genocide.1.gz"]),
                ("share/doc/genocide", uploadlist("docs")),
                ("share/doc/genocide/jpg", uploadlist("docs/jpg")),
                ("share/doc/genocide/pdf", uploadlist("docs/pdf")),
                ("share/doc/genocide/_templates", uploadlist("docs/_templates")),
               ],
    scripts=["bin/genocide"],
    classifiers=['Development Status :: 3 - Alpha',
                 'License :: Public Domain',
                 'Operating System :: Unix',
                 'Programming Language :: Python',
                 'Topic :: Utilities'
                ]
)
 