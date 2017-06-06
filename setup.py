#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

setup(
    name='django-debug-permissions',
    version='1.0.0',
    description="Get a list of all user permissions available in the Django system",
    long_description=readme,
    author="Tim Kamanin",
    author_email='tim@timonweb.com',
    url='https://github.com/timonweb/django-debug-permissions',
    packages=['debug_permissions'],
    include_package_data=True,
    package_data={'': ['README.md']},
    install_requires=[
        'Django'
    ],
    license="BSD license",
    zip_safe=False,
    keywords=[
        'django', 'debug', 'permissions', 'development', 'cli'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ]
)
