# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup

version = '1.0'

long_description = (
    open('README.rst').read()
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.rst').read()
)

setup(name='plonesocial.messaging',
      version=version,
      description='',
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          'Environment :: Web Environment',
          'Framework :: Plone',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.6',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      keywords='',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='gpl',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['plonesocial', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'plone.api',
          'Products.CMFCore',
          'Products.CMFPlone >=4.3',
          'Products.GenericSetup',
          'setuptools',
          'zope.component',
          'zope.event',
          'zope.i18nmessageid',
          'zope.interface',
          'zope.schema',
      ],
      extras_require={
          'test': [
              'plone.app.testing[robot] >=4.2.2',
              'plone.testing',
          ],
      },
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=['PasteScript'],
      paster_plugins=['templer.localcommands'],
      )
