# encoding: utf-8
from __future__ import unicode_literals

import os
import sys

from shutil import rmtree

from setuptools import setup, Command


NAME = "anti_useragent"
DESCRIPTION = "fake chrome, firefox, opera browser header anti useragent"
URL = "https://github.com/ihandmine/anti-useragent"
AUTHOR = "handmine"
AUTHOR_EMAIL = "handmine@outlook.com"
VERSION = "1.0.5"
LICENSE = "MIT"
REQUIRES_PYTHON = ">=3.7.0"


def list_dir(dir):
    result = [dir]
    for file in os.listdir(dir):
        if os.path.isdir(os.path.join(dir, file)):
            result.extend(list_dir(os.path.join(dir, file)))
    return result


here = os.path.abspath(os.path.dirname(__file__))
with open(f"{here}/README.md", encoding='utf-8') as f:
    long_description = f.read()


class UploadCommand(Command):
    """Support setup.py upload."""

    description = "Build and publish the package."
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print("\033[1m{0}\033[0m".format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status("Removing previous builds...")
            rmtree(os.path.join(here, "dist"))
        except OSError:
            pass

        self.status("Building Source and Wheel distribution...")
        os.system("{0} setup.py sdist bdist_wheel".format(sys.executable))

        self.status("Uploading the package to PyPI via Twine...")
        os.system("twine upload dist/*")

        sys.exit()



setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    url=URL,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license=LICENSE,
    packages=list_dir(NAME),
    package_dir={NAME: NAME},
    python_requires=REQUIRES_PYTHON,
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'loguru',
    ],
    keywords=[
        'user', 'agent', 'user agent', 'useragent',
        'fake', 'fake useragent', 'fake user agent',
        'anti', 'anti useragent'
    ],
    cmdclass={"upload": UploadCommand},
)
