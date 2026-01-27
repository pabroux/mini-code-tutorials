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
print(args.url, args.lines, args.verbose)

