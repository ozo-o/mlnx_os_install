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