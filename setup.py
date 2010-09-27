from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='Loquacious Snake',
      version=version,
      description="Loquacious interface to write end-to-end tests",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='testing tests BDD TDD loquacious fluent',
      author='Nicholas Lemay',
      author_email='nlemay@pyxis-tech.com',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False
    ,
      install_requires=[
        'setuptools',
        'selenium',
        'mock'
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
