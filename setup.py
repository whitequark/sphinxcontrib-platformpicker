from setuptools import setup, find_packages


with open("README.rst") as f:
    long_desc = f.read()


setup(
    name="sphinxcontrib-platformpicker",
    version="1.0",
    author="whitequark",
    author_email="whitequark@whitequark.org",
    license="MIT",
    description="Platform picker extension for Sphinx",
    long_description=long_desc,
    zip_safe=False,
    packages=find_packages(),
    namespace_packages=["sphinxcontrib"],
    install_requires=["Sphinx>=2.0"],
    project_urls={
        "Documentation": "https://sphinxcontrib-platformpicker.readthedocs.io/",
        "Source Code": "https://github.com/whitequark/sphinxcontrib-platformpicker",
        "Bug Tracker": "https://github.com/whitequark/sphinxcontrib-platformpicker/issues",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Documentation",
        "Topic :: Utilities",
    ],
)
