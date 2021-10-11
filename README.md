# random-file-dataset-generator

## Description:

Simple script for generating a sample dataset of randomly scribed files suitable for data quality management and system tests.

Components such as file count limits, filepaths, test file contents, and naming conventions are alterable, however, default settings for the script rely on a filepath containing a directory called 'data'.

## Requirements:

- Python 3.0 +

## Usage:

```sh
git clone https://github.com/christopher-christofi/random-file-dataset-generator
```

Build the directory that will contain the generated test files and initiate the generator script.

```sh
mkdir data && python random-file-dataset-generator/file_gen.py
```

A text document containing all the unique random identifiers that pair with each randomly generated test file is also created, 'codes.txt'