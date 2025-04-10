from setuptools import setup, find_packages

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="widevine_keys",
    version="1.0.0",
    packages=find_packages(),
    install_requires=required,
    include_package_data=True,
)
