from setuptools import setup, find_packages, find_namespace_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="pyrl",
    version="0.0.1",
    description="NNet",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fsperotto/pyrl",
    package_dir={"":"src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)