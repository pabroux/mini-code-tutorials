import argparse

# Create the parser
parser = argparse.ArgumentParser(
    prog='programName',
    description='Description of the program',
    epilog='Text at the end of the help',
)

# Attach arguments
# ↳ Positional one
parser.add_argument('url')
# ↳ Optional one taking a value and casting it to int
parser.add_argument('-l',
                    '--lines',
                    help='Number of lines to fetch',
                    type=int)
# ↳ Optional one with a default value 
parser.add_argument('-v',
                    '--verbose',
                    help='Verbose mode',
                    action='store_true'
                    )

# Preview the help
parser.print_help()

# Parse the arguments
args = parser.parse_args()

"""
argparse — no click needed.

    python cli_parser.py greet Alice --shout --repeat 3
    python cli_parser.py download https://ex.com -o out.html --quiet
    python cli_parser.py -vvv greet Bob
"""

import argparse


# -- Custom type: any callable(str) -> value works --------------------------
def positive_int(value: str) -> int:
    n = int(value)
    if n <= 0:
        raise argparse.ArgumentTypeError(f"{value} must be > 0")
    return n


# -- Root parser with global flags -----------------------------------------
parser = argparse.ArgumentParser(
    prog="mycli",
    description="A compact argparse tutorial.",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
)
parser.add_argument("-V", "--version", action="version", version="%(prog)s 1.0.0")
parser.add_argument(
    "-v", "--verbose", action="count", default=0, help="-v info, -vv debug, -vvv trace"
)

# -- Subcommands (the click-killer) ----------------------------------------
sub = parser.add_subparsers(dest="command", required=True, title="commands")

# greet
g = sub.add_parser("greet", help="Say hello")
g.add_argument("name")  # positional
g.add_argument("-s", "--shout", action="store_true")  # boolean flag
g.add_argument(
    "-r",
    "--repeat",
    type=positive_int,
    default=1,  # custom type
    metavar="N",
    help="Times to repeat",
)

# download
d = sub.add_parser("download", help="Fetch a URL")
d.add_argument("url")
d.add_argument("-o", "--output", default="-", help="File or stdout")
d.add_argument("-m", "--method", choices=["GET", "POST", "HEAD"], default="GET")
d.add_argument("--retries", type=int, default=3)
# mutually exclusive: can't use both
mx = d.add_mutually_exclusive_group()
mx.add_argument("--quiet", action="store_true", help="Suppress output")
mx.add_argument("--debug", action="store_true", help="Debug traces")

# stats — nargs and append
s = sub.add_parser("stats", help="Compute stats on a file")
s.add_argument("file")
s.add_argument(
    "-c",
    "--columns",
    nargs="+",
    metavar="COL",  # 1..N values
    help="Columns to include",
)
s.add_argument("-f", "--format", choices=["table", "json", "csv"], default="table")
s.add_argument(
    "--range",
    nargs=2,
    type=int,
    metavar=("MIN", "MAX"),
    help="Filter rows by value range",
)
s.add_argument(
    "--tag",
    action="append",
    default=[],  # repeatable flag
    help="Add a tag (repeatable: --tag a --tag b)",
)


# -- Dispatch ---------------------------------------------------------------
def greet(a):
    msg = f"Hello, {a.name}!"
    for _ in range(a.repeat):
        print(msg.upper() if a.shout else msg)


def download(a):
    print(f"[{a.method}] {a.url} -> {a.output}  (retries={a.retries})")
    if a.quiet:
        print("  (quiet)")
    if a.debug:
        print("  (debug)")


def stats(a):
    print(f"{a.file} as {a.format}")
    if a.columns:
        print(f"  columns: {a.columns}")
    if a.range:
        print(f"  range:   {a.range[0]}–{a.range[1]}")
    if a.tag:
        print(f"  tags:    {a.tag}")


if __name__ == "__main__":
    args = parser.parse_args()
    if args.verbose:
        print(f"[v={args.verbose}] {args}")
    {"greet": greet, "download": download, "stats": stats}[args.command](args)

print(args.url, args.lines, args.verbose)

