# 'Advent of code' solution for year 2024 day 3
import os
import sys
import re

global DIR_PATH
DIR_PATH = os.path.dirname(os.path.realpath(__file__))

def find_instructions(input):
    results = re.findall(r"mul\(\d+,\s*\d+\)|do\(\)|don't\(\)", input)

    return results

def execute_instruction(instruction):
    instruction = instruction.replace("mul(", "").replace(")", "")
    values = instruction.split(",")

    return int(values[0]) * int(values[1])

def get_input():
    input = None
    if os.path.isfile(os.path.join(DIR_PATH, "input.txt")):
        with open(os.path.join(DIR_PATH, "input.txt"), "r") as file:    
            input = file.read().replace('\n', '').strip()
        return input
    else:
        print("Error! Input file does not exist!")
        sys.exit()

if __name__ == "__main__":
    input = get_input()
    if not input:
        print("Error! Input file is empty!")
        sys.exit()

    instructions = find_instructions(input)

    # Part 1
    result = 0
    for instruction in instructions:
        if instruction.startswith("mul("):
            result += execute_instruction(instruction)
    print("Part 1: ", result)

    # Part 2
    active = True
    result = 0
    for instruction in instructions:
        if instruction == "do()":
            active = True
        elif instruction == "don't()":
            active = False
        elif active and instruction.startswith("mul("):
            result += execute_instruction(instruction)
    print("Part 2: ", result)

    sys.exit()
