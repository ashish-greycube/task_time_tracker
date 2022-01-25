from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in task_time_tracker/__init__.py
from task_time_tracker import __version__ as version

setup(
	name="task_time_tracker",
	version=version,
	description="Customization for tracking task based on time",
	author="GreyCube Technologies",
	author_email="admin@greycube.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
