from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="fff",
    description="file & folder formulator",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="null",
    url="https://github.com/admiraltoad/fff",
    project_urls={
        "Issues": "https://github.com/admiraltoad/fff/issues",
        "CI": "https://github.com/admiraltoad/fff/actions",
        "Changelog": "https://github.com/admiraltoad/fff/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["fff"],
    entry_points="""
        [console_scripts]
        fff=fff.cli:cli
    """,
    install_requires=["click"],
    extras_require={
        "test": ["pytest"]
    },
    python_requires=">=3.7",
)
