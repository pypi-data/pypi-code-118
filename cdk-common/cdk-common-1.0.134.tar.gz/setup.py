import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "cdk-common",
    "version": "1.0.134",
    "description": "Common AWS CDK librarys.",
    "license": "Apache-2.0",
    "url": "https://github.com/neilkuan/cdk-common.git",
    "long_description_content_type": "text/markdown",
    "author": "Neil Kuan<guan840912@gmail.com>",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/neilkuan/cdk-common.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "cdk_common",
        "cdk_common._jsii"
    ],
    "package_data": {
        "cdk_common._jsii": [
            "cdk-common@1.0.134.jsii.tgz"
        ],
        "cdk_common": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "aws-cdk.aws-iam>=1.134.0, <2.0.0",
        "aws-cdk.aws-lambda>=1.134.0, <2.0.0",
        "aws-cdk.aws-s3>=1.134.0, <2.0.0",
        "aws-cdk.core>=1.134.0, <2.0.0",
        "constructs>=3.2.27, <4.0.0",
        "jsii>=1.57.0, <2.0.0",
        "publication>=0.0.3"
    ],
    "classifiers": [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Typing :: Typed",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
