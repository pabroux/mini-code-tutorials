# Python `argparse`

This tutorial shows how to build a command-line interface using Python's built-in [`argparse`](https://docs.python.org/3/library/argparse.html) module — no third-party library needed.

## What?

`argparse` is Python's standard library module for parsing command-line arguments. It handles positional arguments, optional flags, type conversion, validation, and auto-generated `--help` output:
```
$ python cli_parser.py --help
usage: greeter [-h] [-s] [-r N] [-V] name

A minimal argparse tutorial.

positional arguments:
  name

options:
  -h, --help            show this help message and exit
  -s, --shout
  -r N, --repeat N      Times to repeat (default: 1)
  -V, --version         show program's version number and exit
```
Most Python CLI tools start with `argparse`. Libraries like [click](https://click.palletsprojects.com) and [typer](https://typer.tiangolo.com) add convenience, but `argparse` covers the fundamentals with zero dependencies — and ships with every Python installation.

## How to use the tutorial?

- Script

## Requirements

- Python >=`3.11`

## Installation

If you have [mise](https://mise.jdx.dev), install Python in one step:
```zsh
mise install
```

## Usage

Everything is well explained in the [`cli_parser.py`](https://github.com/pabroux/mini-code-tutorials/blob/master/tutorial/language/python/argparse/src/cli_parser.py) script, in the `src` folder.

To test, run the script directly:
```zsh
python src/cli_parser.py Alice --shout --repeat 3
python src/cli_parser.py Alice -sr 2
python src/cli_parser.py --version
python src/cli_parser.py --help
```

## Resources

- [`argparse` documentation](https://docs.python.org/3/library/argparse.html) by Python
- [`argparse` tutorial](https://docs.python.org/3/howto/argparse.html) by Python
- [click](https://click.palletsprojects.com) — a popular third-party alternative
