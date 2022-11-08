from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in family_details/__init__.py
from family_details import __version__ as version

setup(
	name="family_details",
	version=version,
	description="for entering family details",
	author="muhammad mp",
	author_email="mammuz77@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
