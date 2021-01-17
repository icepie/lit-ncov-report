
from os import path as os_path
from setuptools import setup

setup(name='litncov',
      version='0.1.0',
      description='A ncov report library and tool for LIT(Luoyang Institute of Science and Technology)',
      url='http://github.com/icepie/lit-ncov-report',
      author='Tea',
      author_email='icepie.dev@gmail.com',
      license='MIT',
      packages=['litncov'],
      install_requires=['click', 'requests', 'gb2260'],
      python_requires='>=3.6',
      entry_points={
          'console_scripts': [
              'litncov = litncov.main:main',
          ],
      }
      )
