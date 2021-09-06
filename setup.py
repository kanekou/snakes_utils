# Copyright (c) 2021 Kohei Kaneshima (kanekou)
# This software is released under the MIT License, see LICENSE.txt.

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), 'r', encoding='utf-8') as f:
    readme = f.read()

setup(
    name="snakes_utils",
    packages=find_packages(),
    install_requires=['snakes'],
    version="1.0.0",
    license="MIT",
    author='kanekou',
    author_email='k208580@ie.u-ryukyu.ac.jp',
    url='https://github.com/kanekou/snakes_utils',
    description='Support converting snakes to data structures.',
    long_description=readme,
    long_description_content_type="text/markdown",
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
    ],
)
