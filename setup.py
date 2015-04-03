# -*- coding: utf-8 -*-
"""Installer for the collective.contact.membrane package."""

from setuptools import find_packages
from setuptools import setup


long_description = (
    open('README.rst').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.rst').read()
    + '\n' +
    open('CHANGES.rst').read()
    + '\n')


setup(
    name='collective.contact.membrane',
    version='1.0.3.dev0',
    description="Membrane integration for collective.contact content types",
    long_description=long_description,
    # Get more from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ],
    keywords='contact, membrane',
    author='Cédric Messiant',
    author_email='cedricmessiant@ecreall.com',
    url='http://pypi.python.org/pypi/collective.contact.membrane',
    license='GPL',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['collective', 'collective.contact'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'collective.contact.core>1.1',
        'dexterity.membrane<=1.0',
        'ecreall.helpers.upgrade',
        'plone.directives.form', # non declared dependency of dexterity.membrane 1.0, can be removed after upgrading dexterity.membrane if dexterity.membrane doesn't depend on it anymore.
        'five.grok',
        'plone.api',
        'setuptools',
    ],
    extras_require={
        'test': [
            'ecreall.helpers.testing',
            'plone.app.testing',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
