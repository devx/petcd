# Copyright 2015 Alex Brandt
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

from codecs import open
from setuptools import find_packages
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'petcd', 'information.py'), 'r', encoding = 'utf-8') as fh:
    exec(fh.read(), globals(), locals())

PARAMS = {}

PARAMS['name'] = NAME  # flake8: noqa—provided by exec
PARAMS['version'] = VERSION  # flake8: noqa—provided by exec
PARAMS['description'] = DESCRIPTION  # flake8: noqa—provided by exec

with open(os.path.join(os.path.dirname(__file__), 'README.rst'), 'r', encoding = 'utf-8') as fh:
    PARAMS['long_description'] = fh.read()

PARAMS['url'] = URL  # flake8: noqa—provided by exec
PARAMS['author'] = AUTHOR  # flake8: noqa—provided by exec
PARAMS['author_email'] = AUTHOR_EMAIL  # flake8: noqa—provided by exec
PARAMS['license'] = LICENSE  # flake8: noqa—provided by exec

PARAMS['classifiers'] = [
    'Development Status :: 2 - Pre-Alpha',
    # 'Development Status :: 3 - Alpha',
    # 'Development Status :: 4 - Beta',
    # 'Development Status :: 5 - Production/Stable',
    # 'Development Status :: 6 - Mature',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3 :: Only',
    'Topic :: Database',
    'Topic :: Database :: Front-Ends',
    'Topic :: Software Development :: Libraries',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

PARAMS['keywords'] = [
    'asynchronous',
    'client',
    'etcd',
    'future',
    'futures',
    'tornado',
]

PARAMS['packages'] = find_packages(exclude = ( 'test_*', ))

PARAMS['install_requires'] = [
    'aiohttp',
    'mypy-lang',
]

# ..note::
#     Documentation Requires:
#     * sphinx_rtd_theme

PARAMS['extras_require'] = {}

PARAMS['test_suite'] = 'nose.collector'
PARAMS['tests_require'] = [
    'coverage',
    'nose',
    'torment',
]

PARAMS['data_files'] = [
    ( 'share/doc/{P[name]}-{P[version]}'.format(P = PARAMS), (
        'README.rst',
    )),
]

setup(**PARAMS)
