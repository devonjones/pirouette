#!/usr/bin/env python
from setuptools import find_packages, setup

setup(
	name="pirouette",
	version="0.1.1",
	url = "https://github.com/devonjones/pirouette",
	author="Devon Jones",
	author_email="devon.jones@gmail.com",
	license = "Apache",
	scripts = ["bin/pirouette"],
	packages=find_packages(),
	install_requires=["sh", "timeout", "PYYaml"],
	description = "Program for rotating ip address",
)
