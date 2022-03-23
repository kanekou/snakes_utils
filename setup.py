# (C) 2021-2022 Kohei Kaneshima

# This library is free software; you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation; either version 2.1 of the License, or (at your option) any later version.

# This library is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License along with this library; If not, see <https://www.gnu.org/licenses/>.

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), 'r', encoding='utf-8') as f:
    readme = f.read()

setup(
    name="snakes_utils",
    packages=find_packages(),
    install_requires=['snakes'],
    version="2.0.2",
    license="LGPLv3+",
    author='kanekou',
    author_email='k208580@ie.u-ryukyu.ac.jp',
    url='https://github.com/kanekou/snakes_utils',
    description='Support conversion from SNAKES objects to Built-in Data Types in Python.',
    long_description=readme,
    long_description_content_type="text/markdown",
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
    ],
)
