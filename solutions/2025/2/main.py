# 'Advent of code' solution for year 2025 day 2
import os
import sys

DIR_PATH = os.path.dirname(os.path.realpath(__file__))

def _get_input():
    content = None
    if os.path.isfile(os.path.join(DIR_PATH, "input.txt")):
        with open(os.path.join(DIR_PATH, "input.txt"), "r", encoding="utf-8") as file:
            content = file.read().strip().split(',')
        return content
    else:
        print("Error! Input file does not exist!")
        sys.exit()

def part_1(i: list[str]):
    result = 0

    for rang in i:
        rang = rang.split('-')
        start, end = int(rang[0]), int(rang[1])

        mid = 0
        for num in range(start, end+1, 1):
            num = str(num)
            if len(num) == 1:
                continue

            mid = len(num) // 2

            if num[:mid] == num[mid:]:
                result += int(num)

    print(f"[P1]: All invalid ID's summed: {result}")

def part_2(i: list[str]):
    result = 0

    for rang in i:
        rang = rang.split('-')
        start, end = int(rang[0]), int(rang[1])

        for num in range(start, end+1, 1):
            num = str(num)
            curr = []

            for i in num:
                curr.append(i)

                if len(curr) > len(num) // 2:
                    break
                elif len(num) % len(curr) == 0 and len(num) // len(curr) == num.count("".join(curr)):
                    result += int(num)
                    break

    print(f"[P2]: All invalid ID's summed: {result}")

if __name__ == "__main__":
    inputs = _get_input()
    if not inputs:
        print("Error! Input file is empty!")
        sys.exit()

    part_1(inputs)
    part_2(inputs)

    sys.exit()
