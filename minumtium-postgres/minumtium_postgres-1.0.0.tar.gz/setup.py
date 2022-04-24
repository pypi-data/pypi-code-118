import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="minumtium_postgres",
    version="1.0.0",
    author="Danilo Guimaraes (danodic)",
    author_email="danilo@danodic.dev",
    description="A postgres database adapter for the minumtium library.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    install_requires=['sqlalchemy', 'pg8000', 'minumtium', 'pydantic'],
    python_requires=">=3.6",
)
