from setuptools import find_packages
from setuptools import setup

setup (
    name="datakit",
    version="v1.0.0",
    description="""
A fast, CLI-first dataset profiling tool for quickly understanding CSV files.
""",
    author="Jonathon Chew",
    author_email="jonchew626@hotmail.com",
    url="https://github.com/jonathon-chew/datakit",
    package_dir={"": "src"},
    packages=find_packages(exclude=("tests*")),
)
