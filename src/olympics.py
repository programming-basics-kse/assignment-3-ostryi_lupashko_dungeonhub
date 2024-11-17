import argparse
import os

from methods import *

def valid_or_create_file(filepath):
    directory = os.path.dirname(filepath)

    # TODO: create dir if not exists
    if directory and os.path.exists(directory):
        raise argparse.ArgumentTypeError(f"Directory '{directory}' does not exist.")

    if not os.path.isfile(filepath):
        try:
            with open(filepath, "r") as f:
                pass

            print(f"File '{filepath}' created.")
        except Exception as e:
            raise argparse.ArgumentTypeError(f"Could not create file '{filepath}': {e}")

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

if __name__ == '__main__':
    args = arg_parser.parse_args()

    if args.command == "-medals":
        process_medals(args.country, args.year)
    elif args.command == "-total":
        process_total(args.year)
    elif args.command == "-overall":
        process_overall(args.countries)
    elif args.command == "-interactive":
        process_interactive()
    else:
        arg_parser.print_help()
