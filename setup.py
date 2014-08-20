#!/usr/bin/env python

import sys
import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

setup(name='abspath',
      version='0.1.0',
      description='get the absolute paths of files on the command line',
      long_description=README,
      author='Arne Neumann',
      author_email='abspath.programming@arne.cl',
      url='https://github.com/arne-cl/abspath',
      scripts=['abspath'],
      license='3-Clause BSD',
)


