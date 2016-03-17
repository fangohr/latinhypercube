# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='latinhypercube',
    version='0.0.1',
    description='Latinhypercube package',
    long_description=readme,
    author='Kenneth Reitz',
    author_email='fangohr@soton.ac.uk',
    url='https://github.com/fangohr/latinhypercube',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

