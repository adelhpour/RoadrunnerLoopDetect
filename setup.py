from setuptools import setup
from setuptools import find_packages

MAJOR = 0
MINOR = 0
MICRO = 1

version = f'{MAJOR}.{MINOR}.{MICRO}'

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="roadrunnerloopdetect",
    version=version,
    author="Adel Heydarabadipour",
    author_email="adelhp@uw.edu",
    description="Find the loops presented in the Jacobin matrix of Roadrunner using LoopDetect",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/adelhpour/RoadRunnerLoopDetect",
    project_urls={
        "Bug Tracker": "https://github.com/adelhpour/RoadRunnerLoopDetect/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["roadrunner", "loopdetect"],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.8"
)
