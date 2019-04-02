import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="phg-cpselect-adal02",
    version="0.0.2",
    author="adal02r",
    author_email="adal02.py@gmail.com",
    description="Does what cpselect does in MATLAB.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/adal02/phg-cpselect",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)