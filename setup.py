#!/usr/bin/env python3
from codecs import open
from os import path
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))


setup(
    name="pyfreshintellivent",
    version="0.1.0",
    description="Manage Fresh Intellivent Sky bathroom ventilation fan",
    author="Ståle Storø Hauknes",
    author_email="walnut-caprice.04@icloud.com",
    url="https://github.com/LaStrada/pyfreshintellivent",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    install_requires=[
        "bleak"
    ],
    zip_safe=True,
    keywords="ble, ventilation, fresh, intellivent,sky",
)
