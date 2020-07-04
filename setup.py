"""
Quart-Motor
-------------
Async MongoDB support for Quart applications.
Quart-Motor is pip-installable:
    $ pip install Quart-Motor

Source code is hosted on `GitHub <https://github.com/marirs/quart-motor>`_.
Contributions are welcome!
"""

from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name="Quart-Motor",
    version='2.4.0',
    url="https://www.github.com/quart-motor/",
    download_url="https://www.github.com/quart-motor/tags",
    license="BSD",
    author="Sriram G",
    author_email="marirs@gmail.com",
    description="Motor support for Quart applications",
    long_description=long_description,
    long_description_content_type='text/markdown',
    zip_safe=False,
    platforms="any",
    packages=['quart_motor'],
    install_requires=[
        "Quart>=0.12.0",
        "motor>=2.1.0"
        "PyMongo>=3.10.1",
        "six",
    ],
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    python_requires='>=3.6',
)