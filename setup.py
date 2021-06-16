#!/usr/bin/env python
from setuptools import setup

install_requires = [
    'netmiko>=3.4.0',
    'setuptools_rust==0.12.1'
]

general_scripts = [
    'main.py'
]

console_scripts = [
    'mlnxos = main:main'
]

version_string = "1.0.1"

setup(name="mlnxos",
      version=version_string,
      packages=[
          "switch",
      ],
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ],
      scripts=general_scripts,
      install_requires=install_requires,
      entry_points={'console_scripts': console_scripts},
      use_2to3=False,
      zip_safe=False,
      )

# from setuptools import setup, find_packages
#
# with open('README.md') as readme_file:
#     README = readme_file.read()
#
#
# install_requires = [
#     'netmiko>=3.4.0',
#     'setuptools_rust==0.12.1'
# ]
#
# setup_args = dict(
#     name='mlnxos',
#     version='0.1',
#     description='Useful tool to install mellanox-os',
#     long_description_content_type="text/markdown",
#     long_description=README,
#     license='MIT',
#     packages=find_packages(),
#     author='Oz Ohayon',
#     author_email='ozo@nvidia.com',
#     keywords=['mlnxos', 'mellanox'],
#     url='https://github.com/ozo-o/mlnx_os_install.git',
#     download_url='https://pypi.org/project/elastictools/',
#     install_requires=install_requires,
# )
#
#
# if __name__ == '__main__':
#     setup(**setup_args)


