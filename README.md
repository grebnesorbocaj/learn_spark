# Learning Spark

Note: this repository (via `poetry new learn_spark`) comes with the file `README.rst`, using the restructured text format for documentation. Seems cool, maybe I'll learn it later (maybe not).

## Index

- [Setup](#setup)
- [Formatting and Dependency Management Inspiration](#inspiration)

## Setup

#### .env

The .env-template should be renamed to .env and the contents should be altered to fit the locations of data in your personal computer.

.env values are referenced in `learn_spark/config.py` which is referenced in applications rather than hardcoded filepaths.

#### hooks/

I added a pre-commit hook which will run `poetry run black $file` on python files staged for commits. To use this in your repo, run `cp pre-commit.template ../.git/hooks/pre-commit && chmod +x ../.git/hooks/pre-commit` from the /hooks/ directory. Hopefully that works.

#### Apache Spark

Installed via brew... `brew install apache-spark`

```shell
$ brew info apache-spark
apache-spark: stable 3.0.1, HEAD
Engine for large-scale data processing
https://spark.apache.org/
/usr/local/Cellar/apache-spark/3.0.1 (1,191 files, 237.4MB) *
  Built from source on 2021-02-16 at 19:58:56
From: https://github.com/Homebrew/homebrew-core/blob/HEAD/Formula/apache-spark.rb
License: Apache-2.0
==> Dependencies
Required: openjdk@11 ✔
==> Options
--HEAD
        Install HEAD version
==> Analytics
install: 3,766 (30 days), 10,465 (90 days), 56,721 (365 days)
install-on-request: 3,760 (30 days), 10,435 (90 days), 55,755 (365 days)
build-error: 0 (30 days)
```

Note that I had issues with INFO continuing to be displayed in logs, making for very verbose logging. To fix:

```shell
export SPARK_HOME=/usr/local/Cellar/apache-spark/3.0.1/libexec
```

And in SPARK_HOME, cd to the `conf/` directory. Do the following and inside `log4j.properties` change INFO to ERROR at the log4j.rootCategory line.

```shell
cp log4j.properties.template log4j.properties
```

#### Java

I don't remember how I installed this...(I also have java14 installed but 11 is my default)

```shell
$ java --version
openjdk 11.0.2 2019-01-15
OpenJDK Runtime Environment 18.9 (build 11.0.2+9)
OpenJDK 64-Bit Server VM 18.9 (build 11.0.2+9, mixed mode)
```

#### Poetry

[Poetry Installation Guide, via python-poetry.org](https://python-poetry.org/docs/#installation)

```shell
$ poetry --version
Poetry version 1.1.4
```

#### Python

Version of python via virtualenv... I think

```shell
$ python --version
Python 3.7.3
```

## Inspiration

Yaadi is a P.O.S. but I he told me to reference [his repo](https://github.com/Ydot19/taming-pyspark) for the same course and tbh it's kinda sexy. 

- Poetry for dependency management 
  - coming from development in a Conda environment this is a breath of fresh air
- Python Black for code formatting
  - looks like Yaadi doesn't even format with this often but it's nice and succint
- Python-Dotenv and Config.py
  - using a dotenv file is good practice something I should get used to
