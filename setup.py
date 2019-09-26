import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cpselect",
    version="1.0.3",
    author="adal02",
    author_email="adal02.py@gmail.com",
    description="Does what cpselect does in MATLAB.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/adal02/phg-cpselect",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 4 - Beta"
    ],
    install_requires=["matplotlib", "Pillow", "PyQt5"],
    include_package_data=True,
)