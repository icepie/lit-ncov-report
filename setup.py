
from os import path as os_path
from setuptools import setup

this_directory = os_path.abspath(os_path.dirname(__file__))

# 读取文件内容


def read_file(filename):
    with open(os_path.join(this_directory, filename), encoding='utf-8') as f:
        long_description = f.read()
    return long_description

# 获取依赖


def read_requirements(filename):
    return [line.strip() for line in read_file(filename).splitlines()
            if not line.startswith('#')]


setup(name='litncov',
      version='0.0.1',
      description='A ncov report library and tool for LIT(Luoyang Institute of Science and Technology)',
      url='http://github.com/icepie/lit-ncov-report',
      author='Tea',
      author_email='icepie.dev@gmail.com',
      license='MIT',
      packages=['litncov'],
      install_requires=read_requirements('requirements.txt'),
      python_requires='>=3.6')
