import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "renovosolutions.aws-cdk-renovo-s3-bucket",
    "version": "1.0.107",
    "description": "An AWS CDK construct library for creating S3 buckets with desirable defaults.",
    "license": "Apache-2.0",
    "url": "https://github.com/RenovoSolutions/cdk-library-renovo-s3-bucket.git",
    "long_description_content_type": "text/markdown",
    "author": "Renovo Solutions<webmaster+cdk@renovo1.com>",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/RenovoSolutions/cdk-library-renovo-s3-bucket.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "renovo_s3_bucket",
        "renovo_s3_bucket._jsii"
    ],
    "package_data": {
        "renovo_s3_bucket._jsii": [
            "cdk-library-renovo-s3-bucket@1.0.107.jsii.tgz"
        ],
        "renovo_s3_bucket": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "aws-cdk.aws-s3>=1.153.0, <2.0.0",
        "aws-cdk.core>=1.153.0, <2.0.0",
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
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
