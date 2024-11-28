import argparse
import os

from methods import *


def valid_file(filepath):
    if not os.path.exists(filepath) or not os.path.isfile(filepath):
        raise argparse.ArgumentTypeError(f"File '{filepath}' does not exist.")

    return filepath

def validate_top_args(args):
    valid_letters = {"M", "F"}
    valid_numbers = {"1", "2", "3", "4"}

    letters = [arg for arg in args if arg.isalpha()]
    numbers = [arg for arg in args if arg.isdigit()]

    if not letters or not numbers:
        raise argparse.ArgumentTypeError("You must specify at least one letter (M or F) and one number (1, 2, 3, 4).")

    if len(letters) + len(numbers) != len(args):
        invalid_args = set(args) - set(letters) - set(numbers)
        raise argparse.ArgumentTypeError(
            f"Invalid arguments: {', '.join(invalid_args)}. Allowed numbers are 1, 2, 3, 4.")

    if len(letters) > 2 or len(numbers) > 2:
        raise argparse.ArgumentTypeError("You can only specify 'M', 'F' or 'M F' and two numbers '3 4'.")

    if letters[0] not in valid_letters or numbers[0] not in valid_numbers:
        raise argparse.ArgumentTypeError("You must specify only acceptable prarams (M F for letters and 1 2 3 4 for numbers)")

    if len(letters) > 1 and letters[1] not in valid_letters:
        raise argparse.ArgumentTypeError(
            "You must specify only acceptable prarams (M F for letters and 1 2 3 4 for numbers)")

    if len(numbers) > 1 and numbers[1] not in valid_numbers:
        raise argparse.ArgumentTypeError(
            "You must specify only acceptable prarams (M F for letters and 1 2 3 4 for numbers)")

    return args

def configure_parser(parser):
    parser.add_argument("inputFile", type=valid_file, help="Path to the input file")

    subparsers = arg_parser.add_subparsers(title="Commands", dest="command", required=True)

    medals_parser = subparsers.add_parser("medals", help="Some medals stuff")
    medals_parser.add_argument("country", type=str, help="Country code or Team name")
    medals_parser.add_argument("year", type=int, help="Year of olympiad")
    medals_parser.add_argument("--output", type=valid_file, help="Path to the output file")

    total_parser = subparsers.add_parser("total", help="Some total stuff")
    total_parser.add_argument("year", type=int, help="Year of olympiad")
    total_parser.add_argument("--output", type=valid_file, help="Path to the output file")

    overall_parser = subparsers.add_parser("overall", help="Some overall stuff")
    overall_parser.add_argument("countries", nargs="+", type=str, help="Countries list")
    overall_parser.add_argument("--output", type=valid_file, help="Path to the output file")

    top_parser = subparsers.add_parser("top", help="Top player with gender and age")
    top_parser.add_argument(
        "top",
        nargs="+",
        help="Specify the top arguments (e.g., --top M F 1 2 or --top M 3)",
    )
    top_parser.add_argument("--output", type=valid_file, help="Path to the output file")

    interactive_parser = subparsers.add_parser("interactive", help="Some interactive stuff")
    interactive_parser.add_argument("--output", type=valid_file, help="Path to the output file")

    args = parser.parse_args()
    if args.command == "top":
        try:

            validate_top_args(args.top)
        except argparse.ArgumentTypeError as e:
            parser.error(str(e))


arg_parser = argparse.ArgumentParser(description="A CLI tool for analyzing dataset.")
configure_parser(arg_parser)

def main():
    args = arg_parser.parse_args()

    if args.command == "medals":
        result = process_medals(args.inputFile, args.country, str(args.year))
    elif args.command == "total":
        result = process_total(args.inputFile, str(args.year))
    elif args.command == "overall":
        result = process_overall(args.inputFile, args.countries)
    elif args.command == "interactive":
        result = process_interactive(args.inputFile)
    elif args.command == "top":  # Check this
        top_args = args.top

        who = [False, False]
        category = [0, 0]

        if top_args[1] in ["M", "F"]:
            who = [True, True]
        elif top_args[0] == "M":
            who[0] = True
        else:
            who[1] = True

        if len(top_args) == 2:
            category[0] = top_args[1]
        elif len(top_args) == 3:
            if top_args[1] not in ["M", "F"]:
                category[0] = top_args[1]
                category[1] = top_args[2]
        else:
            category = [top_args[2], top_args[3]]

        result = process_top(args.inputFile, who, category)
    else:
        print(args.command)
        arg_parser.print_help()
        return 0

    if not result:
        result = "No data found"

    result = "\n================\n" + result + "\n================\n"

    print(result)

    if args.output:
        with open(args.output, "w") as f:
            f.write(result)

if __name__ == '__main__':
    main()
