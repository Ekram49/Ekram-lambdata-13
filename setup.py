# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="04082020", # the name that you will install via pip
    version="2.0",
    author="Ekram Ahmed",
    author_email="ekramullahzaki@gmail.com",
    description="Converter",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/Ekram49/Ekram-lambdata-13",
    #keywords="",
    packages=find_packages()
)