# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup

version = '1.0'

long_description = (
    open('README.rst').read()
    + '\n' +
    open('CONTRIBUTORS.rst').read()
    + '\n' +
    open('CHANGES.rst').read()
)

setup(name='plonesocial.messaging',
      version=version,
      description='Exchange private messages among Plone users',
      long_description=long_description,
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Web Environment',
          'Framework :: Plone :: 4.2',
          'Framework :: Plone :: 4.3',
          'Framework :: Plone',
          'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      keywords='plone socbiz social messages',
      author='',
      author_email='',
      url='https://github.com/cosent/plonesocial.messaging',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['plonesocial', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'plone.api',
          'plone.app.jquerytools',
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
