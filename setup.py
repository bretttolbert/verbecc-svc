#!/usr/bin/python

import os
from setuptools import setup, find_packages

package = 'verb_conjugate_fr'
setup_dir = os.path.dirname(os.path.abspath(__file__))
version_file = os.path.join(setup_dir, package, 'VERSION')

with open(version_file) as version_file:
    version = version_file.read().strip()

requirements = (
    open(os.path.join(setup_dir,'requirements.txt')).read().splitlines()
    )
required = [line for line in requirements if not line.startswith('-')]

setup(name=package,
      version=version,
      description='description',
      url='https://github.com/bretttolbert/' + package.replace('_', '-'),
      author='Brett Tolbert',
      author_email='bretttolbert@gmail.com',
      packages=find_packages(),
      install_requires=[required],
      include_package_data=True,
      entry_points = {
          'console_scripts': ['confr=verb_conjugate_fr.cli:main']
      }
      )