"""
Quart-Motor
-------------
Async MongoDB support for Quart applications.
Quart-Motor is pip-installable:
    $ pip install Quart-Motor

Source code is hosted on `GitHub <https://github.com/marirs/quart-motor>`_.
Contributions are welcome!
"""

from setuptools import find_packages, setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name="Quart-Motor",
    version='2.4.1',
    url="https://www.github.com/quart-motor/",
    download_url="https://www.github.com/quart-motor/tags",
    license="BSD",
    author="Sriram G",
    author_email="marirs@gmail.com",
    description="Motor support for Quart applications",
    long_description=long_description,
    long_description_content_type='text/markdown',
    zip_safe=False,
    packages=find_packages(),
    install_requires=[
        "PyMongo>=3.10",
        "Quart>=0.12.0",
        "motor>=2.1.0",
        "six",
    ],
    classifiers=[
        "Environment :: Web Environment",
        "Development Status :: 5 - Production/Stable",
        "Natural Language :: English",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Unix",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    python_requires='>=3.6',
)