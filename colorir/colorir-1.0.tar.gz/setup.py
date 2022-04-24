import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE/"README.rst").read_text()

setup(
    name="colorir",
    version="1.0",
    packages=["colorir"],
    url="https://github.com/aleferna12/colorir",
    license="MIT",
    author="aleferna",
    author_email="alexandrepchfernandes@gmail.com",
    description="A python package for easy management of colors and palettes.",
    long_description=README,
    long_description_content_type="text/x-rst",
    project_urls={"Documentation": "https://colorir.readthedocs.io/en/latest/"},
    include_package_data=True
)