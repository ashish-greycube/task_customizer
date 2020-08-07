# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in task_customizer/__init__.py
from task_customizer import __version__ as version

setup(
	name='task_customizer',
	version=version,
	description='Add Purchase functionality for Task. Similar to Projects.',
	author='GreyCube Technologies',
	author_email='admin@greycube.in',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
