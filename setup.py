#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

extras_require = {
    'test': ['pytest', 'pytest-cov', 'mypy', 'flake8']}

setup(
    author="Nick Frederick Settje",
    author_email='nsettje@alumni.stanford.edu',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Type-safe error handling for Python.",
    install_requires=[],
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='errs',
    name='errs',
    packages=find_packages(include=['errs']),
    test_suite='tests',
    extras_require=extras_require,
    url='https://github.com/nicksettje/errs',
    version='0.1.1',
    zip_safe=False,
)
