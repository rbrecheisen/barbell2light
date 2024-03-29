#!/usr/bin/env python

"""The setup script."""

import os

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'oauthlib',
    'requests_oauthlib',
    'pydicom',
    'cmd2',
    'pandas',
    'numpy',
    'matplotlib',
    'python-gdcm',
    'pylibjpeg',
    # 'gnureadline',
]

setup_requirements = []

test_requirements = []

setup(
    author="Ralph Brecheisen",
    author_email='ralph.brecheisen@gmail.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Python Boilerplate contains all the boilerplate you need to create a Python package.",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='barbell2light',
    name='barbell2light',
    packages=find_packages(include=['barbell2light', 'barbell2light.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/rbrecheisen/barbell2light',
    version=os.environ['VERSION'],
    zip_safe=False,
)
