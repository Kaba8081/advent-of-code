from datetime import datetime
from pathlib import Path
import argparse

from core.advent_of_code import AdventOfCode

def main():
    parser = argparse.ArgumentParser(description="Advent of Code Helper CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Grabbing input
    grab_parser = subparsers.add_parser("grab", help="Download input for a day")
    grab_parser.add_argument("-y", "--year", type=int, default=datetime.now().year)
    grab_parser.add_argument("-d", "--day", type=int, default=datetime.now().day)
    grab_parser.add_argument(
        "-t", 
        "--template", 
        action="store_true",
        help="Create a 'main.py' file alongside the downloaded input file"
    )

    # Running the solution
    run_parser = subparsers.add_parser("run", help="Run solution for a day")
    run_parser.add_argument("-y", "--year", type=int, default=datetime.now().year)
    run_parser.add_argument("-d", "--day", type=int, default=datetime.now().day)
    run_parser.add_argument(
        "-p",
        "--profile",
        action="store_true",
        help="Profile execution time and memory"
    )

    args = parser.parse_args()
    path = Path(__file__).resolve().parent
    aoc = AdventOfCode(path)

    if args.command == "grab":
        aoc.grab_input(args.year, args.day, args.template)
    elif args.command == "run":
        aoc.run_solution(args.year, args.day, args.profile)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
