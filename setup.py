# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="assignment_1_1", # the name that you will install via pip
    version="1.1",
    author="Ekram Ahmed",
    author_email="ekramullahzaki@gmail.com",
    description="Multiplies by 100",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/Ekram49/Ekram-lambdata-13",
    #keywords="",
    packages=find_packages()
)