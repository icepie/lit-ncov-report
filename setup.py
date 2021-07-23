#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="litncov",
    version="2.2.1",
    description="A ncov report library and tool for LIT(Luoyang Institute of Science and Technology)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://github.com/icepie/lit-ncov-report",
    author="Tea",
    author_email="icepie.dev@gmail.com",
    license="MIT",
    packages=["litncov"],
    install_requires=["rich", "requests", "pytz"],
    keywords=["lit", "ncov", "report", "11070"],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "litncov = litncov.main:main",
        ],
    },
)
