# fff

[![PyPI](https://img.shields.io/pypi/v/fff.svg)](https://pypi.org/project/fff/)
[![Changelog](https://img.shields.io/github/v/release/admiraltoad/fff?include_prereleases&label=changelog)](https://github.com/admiraltoad/fff/releases)
[![Tests](https://github.com/admiraltoad/fff/workflows/Test/badge.svg)](https://github.com/admiraltoad/fff/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/admiraltoad/fff/blob/master/LICENSE)

file & folder formulator

## Installation

Install this tool using `pip`:

    pip install fff

## Usage

For help, run:

    fff --help

You can also use:

    python -m fff --help

## Development

To contribute to this tool, first checkout the code. Then create a new virtual environment:

    cd fff
    python -m venv venv
    source venv/bin/activate

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest
