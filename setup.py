# -*- coding: utf-8 -*-
"""
This module contains the tool of collective.recipe.sphinxbuilder
"""
import os
from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '0.5.0'

long_description = (
    read('README.txt')
    + '\n' +
    'Detailed Documentation\n'
    '**********************\n'
    + '\n' +
    read('collective', 'recipe', 'sphinxbuilder', 'README.txt')
    + '\n' +
    'Todo list\n' 
    '*********\n'
    + '\n' +
    read('TODO.txt')
    + '\n' +
    'Contributors\n' 
    '************\n'
    + '\n' +
    read('CONTRIBUTORS.txt')
    + '\n' +
    'Change history\n'
    '**************\n'
    + '\n' + 
    read('CHANGES.txt')
    + '\n' +
   'Download\n'
    '********\n'
    )

entry_point = 'collective.recipe.sphinxbuilder:Recipe'
entry_point2 = 'collective.recipe.sphinxbuilder'
entry_points = {"zc.buildout": ["default = %s" % entry_point],
                "collective.recipe.sphinxbuilder": ["default = %s" % entry_point2]}

tests_require=['zope.testing', 'zc.buildout']

setup(name='collective.recipe.sphinxbuilder',
      version=version,
      description="ZC.buildout recipe to generate and build Sphinx-based documentation in the buildout.",
      long_description=long_description,
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        'Framework :: Buildout',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: Zope Public License',
        ],
      keywords='buildout sphinx',
      author='Tarek Ziade',
      author_email='tarek@ziade.org',
      url='http://svn.plone.org/svn/collective/buildout/collective.recipe.sphinxbuilder/trunk',
      license='ZPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.recipe'],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        # -*- Extra requirements: -*-
                        'zc.buildout',
                        'zc.recipe.egg',
                        'docutils',
                        'Sphinx==0.5'
                        ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),
      test_suite = 'collective.recipe.sphinxbuilder.tests.test_docs.test_suite',
      entry_points=entry_points,
      )

