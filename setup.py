from os import path as os_path
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="litncov",
    version="2.1.1",
    description="A ncov report library and tool for LIT(Luoyang Institute of Science and Technology)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://github.com/icepie/lit-ncov-report",
    author="Tea",
    author_email="icepie.dev@gmail.com",
    license="MIT",
    packages=["litncov"],
    install_requires=["rich", "requests", "gb2260", "pytz"],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "litncov = litncov.main:main",
        ],
    },
)
