"""Minimal setup file for tasks project."""

from setuptools import setup, find_packages

setup(
    name='food_delivery',
    version='0.1.0',
    license='proprietary',
    description='takeaway ordering service',

    author='Matt Oliver',

    packages=find_packages(),
    package_data={'data': ['*.json']},
    
    # install_requires=['click==7.1.2', 'tinydb==3.15.1', 'six'],
    # extras_require={'mongo': 'pymongo'},

    # entry_points={
    #     'console_scripts': [
    #         'tasks = tasks.cli:tasks_cli',
    #     ]
    # },
)
