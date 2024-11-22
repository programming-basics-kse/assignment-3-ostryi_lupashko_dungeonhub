import argparse
import os

from methods import *

def valid_or_create_file(filepath):
    if not os.path.exists(filepath) or not os.path.isfile(filepath):
        raise argparse.ArgumentTypeError(f"File '{filepath}' does not exist.")

    return filepath

def configure_parser(parser):
    parser.add_argument("inputFile", type=valid_or_create_file, help="Path to the input file")

    subparsers = arg_parser.add_subparsers(title="Commands", dest="command", required=True)

    medals_parser = subparsers.add_parser("-medals", help="Some medals stuff")
    medals_parser.add_argument("country", type=str, help="Country code or Team name")
    medals_parser.add_argument("year", type=int, help="Year of olympiad")

    total_parser = subparsers.add_parser("-total", help="Some total stuff")
    total_parser.add_argument("year", type=int, help="Year of olympiad")

    overall_parser = subparsers.add_parser("-overall", help="Some overall stuff")
    overall_parser.add_argument("countries", nargs="+", type=str, help="Countries list")

    subparsers.add_parser("-interactive", help="Some interactive stuff")

    parser.add_argument("-output", type=valid_or_create_file, help="Path to the output file")

arg_parser = argparse.ArgumentParser(description="A CLI tool for analyzing dataset.")
configure_parser(arg_parser)

def main():
    args = arg_parser.parse_args()

    if args.command == "-medals":
        result = process_medals(args.country, args.year)
    elif args.command == "-total":
        result = process_total(args.year)
    elif args.command == "-overall":
        result = process_overall(args.countries)
    elif args.command == "-interactive":
        result = process_interactive()
    else:
        arg_parser.print_help()
        return 0

    print(result)

    if args.output:
        with open(args.output, "w") as f:
            f.write(result)

if __name__ == '__main__':
    main()
