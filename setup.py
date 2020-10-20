from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="testds", # the name that you will install via pip
    version="1.0",
    author="Carlo Lucido",
    author_email="c.jose.lucido@gmail.com",
    description="test implementation on machine",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/CJLucido/testds",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)