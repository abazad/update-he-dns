# encoding: utf-8

from __future__ import absolute_import, print_function

from setuptools import setup


__version__ = '0.1'
__author__ = 'Dmitry Orlov <me@mosquito.su>'


setup(name='update-he-dns',
      version=__version__,
      author=__author__,
      author_email='me@mosquito.su',
      license="MIT",
      description="Simple DYNDNS updater for dns.he.net",
      platforms="all",
      url="http://github.com/mosquito/update-he-dns",
      classifiers=[
          'Environment :: Console',
          'Programming Language :: Python',
      ],
      long_description=open('README.rst').read(),
      py_modules=["updatehedns"],
      entry_points = {
        'console_scripts': [
          'update-he-dns = updatehedns:main',
        ],
      },
      requires=['Python (>2.6)']
      )
