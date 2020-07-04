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

setup(
    name="Quart-Motor",
    url="https://www.github.com/quart-motor/",
    download_url="https://www.github.com/quart-motor/tags",
    license="BSD",
    author="Sriram G",
    author_email="marirs@gmail.com",
    description="Motor support for Quart applications",
    long_description=__doc__,
    zip_safe=False,
    platforms="any",
    packages=find_packages(),
    install_requires=[
        "Quart>=0.12.0",
        "motor>=2.1.0"
        "PyMongo>=3.10.1",
        "six",
    ],
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Quart",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    python_requires='>=3.6',
)