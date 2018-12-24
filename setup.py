#!/usr/bin/env python

import os
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

class PyTest(TestCommand):

    # pytestのオプションを指定する際は--pytest-args='{options}'を使用する
    user_options = [
        ('pytest-args=', 'a', 'Arguments for pytest'),
    ]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_target = []
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

# setup.py内でpytestのimportが必要
setup_requires=[
    'pytest'
]
install_requires=[
    'requests',
]
tests_require=[
    'pytest-timeout',
    'pytest'
]

setup(
    name='acktodo',
    version='0.0.1',
    description='Ack''s TODO App',
    long_description="",
    author='Kenneth Reitz',
    author_email='me@kennethreitz.com',
    url='https://github.com/acksobae/acktodo',
    license=license,
    packages=['acktodo.domain', 'acktodo.gui', 'acktodo.infra'],
    test_suite = 'sample_test.suite',
    cmdclass={'test': PyTest},
)