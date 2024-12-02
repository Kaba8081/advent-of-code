# 'Advent of code' solution for year 2024 day 2
import os
import sys

global DIR_PATH
DIR_PATH = os.path.dirname(os.path.realpath(__file__))

def isSafe(report: list[int]) -> bool:
    """Check if the report is safe or not"""
    if not (sorted(report) == report or sorted(report,reverse=True) == report):
        return False

    for i in range(len(report)-1):
        if abs(report[i] - report[i+1]) > 3:
            return False
        elif report[i] == report[i+1]:
            return False

    return True

def isSafePart2(report: list[int]) -> bool:
    """Check if the report is safe or not"""
    safe = False
    for i in range(len(report)):
        temp_report = report[:i] + report[i+1:]
        if isSafe(temp_report):
            safe = True

    return safe

def countSafeReports(puzzle_input: list[str], part: 1 | 2) -> int:
    count = 0
    for line in puzzle_input:
        report = list(map(int, line.split(" ")))
        if part==1 and isSafe(report):
            count += 1
        elif part==2 and isSafePart2(report):
            count += 1

    return count

def get_input():
    input = None
    if os.path.isfile(os.path.join(DIR_PATH, "input.txt")):
        with open(os.path.join(DIR_PATH, "input.txt"), "r") as file:    
            input = file.read().strip().splitlines()
        return input
    else:
        print("Error! Input file does not exist!")
        sys.exit()

if __name__ == "__main__":
    input = get_input()
    if not input:
        print("Error! Input file is empty!")
        sys.exit()

    result1 = countSafeReports(input, 1)
    print(f"Result 1: {result1}")

    result2 = countSafeReports(input, 2)
    print(f"Result 2: {result2}")

    sys.exit()
