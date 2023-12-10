# 'Advent of code' solution for year 2023 day 9
import os
import sys
                        
global DIR_PATH
DIR_PATH = os.path.dirname(os.path.realpath(__file__))

def get_input():
    input = None
    if os.path.isfile(os.path.join(DIR_PATH, "input.txt")):
        with open(os.path.join(DIR_PATH, "input.txt"), "r") as file:    
            input = file.read().strip().splitlines()
        return input
    else:
        print("Error! Input file does not exist!")
        sys.exit()

def findNextDiffs(line) -> list:
    result = []

    for i in range(len(line)-1): # skip last element
        result.append(line[i+1] - line[i])
    
    return result

def findNextValue(lines, back=False) -> int:
    if back:
        lines[-1].insert(0, 0) # first value of last line is always 0
    else:
        lines[-1].append(0) # last value of last line is always 0

    for i in range(len(lines)-1, 0, -1):
        if back:
            lines[i-1].insert(0, lines[i-1][0] - lines[i][0])
        else:
            lines[i-1].append(lines[i][-1] + lines[i-1][-1])

    if back: # part 2
        return lines[0][0]
    else: # part 1
        return lines[0][-1]

def part1(input) -> int:
    final_sum = 0

    for line in input:
        line = line.split()
        line = [int(value) for value in line]
        temp_lines = []

        temp_lines.append(line)
        while len(set(temp_lines[-1])) != 1 or temp_lines[-1][0] != 0:
            temp_lines.append(findNextDiffs(temp_lines[-1].copy()))

        final_sum += findNextValue(temp_lines)

    return final_sum

def part2(input) -> int:
    final_sum = 0

    for line in input:
        line = line.split()
        line = [int(value) for value in line]
        temp_lines = []

        temp_lines.append(line)
        while len(set(temp_lines[-1])) != 1 or temp_lines[-1][0] != 0:
            temp_lines.append(findNextDiffs(temp_lines[-1].copy()))

        final_sum += findNextValue(temp_lines, back=True)

    return final_sum

if __name__ == "__main__":
    input = get_input()
    if not input:
        print("Error! Input file is empty!")
        sys.exit()

    input1 ="""0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45""".strip().splitlines()

    result1 = part1(input)
    print("[8.1] Sum of all extrapolated values:", result1)
    result2 = part2(input)
    print("[8.2] Sum of all backward extrapolated values:", result2)
    
    sys.exit()
