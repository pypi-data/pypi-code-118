import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="paymob",
    version="1.0.0",
    author="Paymob",
    author_email="menessy@paymob.com",
    description="Paymob FLASH SDK",	
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PaymobAccept/paymob-python",
    project_urls={
        "Documentation": "https://docs.paymob.com",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
          'requests',
      ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
