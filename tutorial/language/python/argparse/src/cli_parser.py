"""
argparse — build rich CLIs with zero dependencies.

Try it:
    python cli_parser.py Alice --shout --repeat 3
    python cli_parser.py Alice -sr 2
    python cli_parser.py --version
    python cli_parser.py --help
"""

import argparse


# Create the parser
parser = argparse.ArgumentParser(
    prog="greeter",
    description="A minimal argparse tutorial.",
    # ↳ auto-appends "(default: …)" to every help string
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
)

# Attach arguments
# ↳ Positional — mandatory, no dash prefix
parser.add_argument("name")
# ↳ Boolean flag — False by default, True when passed
parser.add_argument("-s", "--shout", action="store_true")
# ↳ type= converts the raw string and doubles as a validator (raise ArgumentTypeError to reject).
#   Works with builtins (int, float) or custom functions like positive_int below.
#   metavar= controls the placeholder shown in --help (e.g. "-r N" instead of "-r POSITIVE_INT").
def positive_int(value: str) -> int:
    n = int(value)
    if n <= 0:
        raise argparse.ArgumentTypeError(f"{value} must be > 0")
    return n

parser.add_argument(
    "-r",
    "--repeat",
    type=positive_int,
    default=1,
    metavar="N",
    help="Times to repeat",
)
# ↳ prints "greeter 1.0.0" and exits immediately
parser.add_argument("-V", "--version", action="version", version="%(prog)s 1.0.0")

# Parse and use
if __name__ == "__main__":
    args = parser.parse_args()
    msg = f"Hello, {args.name}!"
    for _ in range(args.repeat):
        print(msg.upper() if args.shout else msg)
