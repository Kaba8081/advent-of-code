# 'Advent of code' solution for year {year} day {day}
import os
import sys

DIR_PATH = os.path.dirname(os.path.realpath(__file__))

def _get_input():
    content = None
    if os.path.isfile(os.path.join(DIR_PATH, "input.txt")):
        with open(os.path.join(DIR_PATH, "input.txt"), "r", encoding="utf-8") as file:
            content = file.read().strip().splitlines()
        return content
    else:
        print("Error! Input file does not exist!")
        sys.exit()

def part_1(i: list[str]):
    lines = i.copy()
    ranges = []
    result = 0

    index = 0
    while lines[index] != '':
        start, end = lines[index].split('-')
        ranges.append((int(start), int(end)))
        index += 1

    for idx in range(index+1, len(lines)):
        value = int(lines[idx])
        for r in ranges:
            if value > r[0] and value < r[1]:
                result += 1
                break

    print(f"[P1] Fresh ingridients: {result}")

def part_2(i: list[str]):
    ranges = []
    for line in i:
        if line == '':
            break
        start, end = line.split('-')
        ranges.append((int(start), int(end)))

    ranges.sort(key=lambda x: x[0])
    result = 0
    curr_range = ranges[0]
    for index in range(1, len(ranges)):
        start, end = ranges[index]
        if start > curr_range[1] + 1:
            result += curr_range[1] - curr_range[0] + 1
            curr_range = (start, end)
        else:
            curr_range = (curr_range[0], max(curr_range[1], end))
    result += curr_range[1] - curr_range[0] + 1

    print(f"[P2] Fresh ingridient count: {result}")

if __name__ == "__main__":
    inputs = _get_input()
    if not inputs:
        print("Error! Input file is empty!")
        sys.exit()

    part_1(inputs)
    part_2(inputs)

    sys.exit()
