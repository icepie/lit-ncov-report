
from os import path as os_path
from setuptools import setup

setup(name='litncov',
      version='0.0.3',
      description='A ncov report library and tool for LIT(Luoyang Institute of Science and Technology)',
      url='http://github.com/icepie/lit-ncov-report',
      author='Tea',
      author_email='icepie.dev@gmail.com',
      license='MIT',
      packages=['litncov'],
      install_requires=['requests', 'gb2260'],
      python_requires='>=3.6')
