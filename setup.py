#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# Our version ALWAYS matches the version of Wagtail we support
# If Wagtail has a new release, we branch, tag, then update this setting after the tag.
version = "2.4"

if sys.argv[-1] == "tag":
    os.system('git tag -a %s -m "version %s"' % (version, version))
    os.system("git push --tags")
    sys.exit()

with open("README.rst") as readme_file:
    long_description = readme_file.read()

setup(
    name="cookiecutter-django-wagtail",
    version=version,
    description="A Cookiecutter template for creating Wagtail projects quickly.",
    long_description=long_description,
    author="Jean Zombie",
    author_email="kappa_camus@tutanota.com",
    url="https://github.com/Jean-Zombie/cookiecutter-django-wagtail.git",
    packages=[],
    license="BSD",
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Framework :: Django :: 2.0",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development",
    ],
    keywords=(
        "cookiecutter, Python, projects, project templates, django, "
        "skeleton, scaffolding, project directory, setup.py, wagtail, cms"
    ),
)
