# -*- coding: utf-8 -*-
"""
This module contains the tool of cirb.novacwaws
"""
import os
from setuptools import setup, find_packages

version = '1.4.3.dev0'

tests_require = ['zope.testing']

setup(name='cirbpolicy.novac',
      version=version,
      description="",
      long_description=\
          open("README.txt").read() + "\n" + \
          open("CHANGES.txt").read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        'Framework :: Plone',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        ],
      keywords='',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['cirbpolicy', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        # -*- Extra requirements: -*-
                        'Products.LinguaPlone>4',
                        'plone.app.registry',
                        #'cirb.cas',
                        'Products.CAS4PAS',
                        'cirb.urbis',
                        'cirb.novac',
#                        'plonetheme.urbanisme',
#                        'plonetheme.novac',
                        'cirb.footersitemap',
                        'Products.Collage',
                        'Products.PloneFormGen',
                        'webcouturier.dropdownmenu',
                        'collective.recaptcha',
                        'collective.easyslider',
                        ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),
      test_suite='cirbpolicy.novac.tests.test_docs.test_suite',
      entry_points="""
      # -*- entry_points -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
