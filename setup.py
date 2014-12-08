from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
    name='ckanext-metaconf',
    version=version,
    description="Allows configuring the metadata vocabulary in CKAN.",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Dennis Konrad',
    author_email='mam10hna@studserv.uni-leipzig.de',
    url='',
    license='MIT License',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.metaconf'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
        # Add plugins here, e.g.
    example_metaconf=ckanext.metaconf.plugin:MetaconfPlugin
    ''',
)
