# PySentry

This tutorial explains how to make your Python project more secure.

## What?

Written in Rust ⚡, PySentry is a tool that audits Python projects for known security vulnerabilities by analyzing dependency files and cross-referencing them against multiple vulnerability databases Multiple sources (PyPA Advisory Database, PyPI JSON API and OSV.dev).
it can analyze multiple file formats: `uv.lock`, `poetry.lock`, `Pipfile.lock`, `pylock.toml`, `pyproject.toml` as well as `requirements.txt`.

## How to use the tutorial?

- CLI

## Requirements

- [uv](https://docs.astral.sh/uv/)

## Usage

To check whether a project has vulnerabilities, run the following:
```zsh
uvx pysentry-rs --compact .
```

When executed in the current directory, this command makes PySentry analyze the existing `uv.lock` file. If any vulnerabilities are found—for example, in the werkzeug package (version 3.1.3)—PySentry will not only report them but also suggest possible fixes.

> [!TIP]
> Add PySentry in your [pre-commit](https://pre-commit.com) or your CI/CD pipeline.

## Resources

- [PySentry](https://pysentry.com)
