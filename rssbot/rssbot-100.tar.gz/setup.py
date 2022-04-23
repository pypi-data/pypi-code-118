# This file is placed in the Public Domain.


from setuptools import setup


def read():
    return open("README.rst", "r").read()


setup(
    name="rssbot",
    version="100",
    url="https://github.com/bthate/rssbot",
    author="Bart Thate",
    author_email="bthate67@gmail.com",
    description="rss feed fetcher for irc channels.",
    long_description=read(),
    license="Public Domain",
    install_requires=["libobj", "librun", "libexc", "feedparser"],
    packages=["rssbot"],
    scripts=["bin/rssbot", "bin/rsscmd", "bin/rssctl"],
    include_package_data=True,
    data_files=[
                ("share/rssbot", ["files/rssbot.service"]),
               ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: Public Domain",
        "Operating System :: Unix",
        "Programming Language :: Python",
        "Topic :: Utilities",
    ],
)
