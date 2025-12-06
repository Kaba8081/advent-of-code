# 'Advent of code' solution for year 2025 day 6
import os
import sys
import re

DIR_PATH = os.path.dirname(os.path.realpath(__file__))

def _get_input():
    content = None
    if os.path.isfile(os.path.join(DIR_PATH, "input.txt")):
        with open(os.path.join(DIR_PATH, "input.txt"), "r", encoding="utf-8") as file:
            content = file.read().splitlines()
        return content
    else:
        print("Error! Input file does not exist!")
        sys.exit()

def operation(result: int, num: str, op: str) -> int:
    x = int(num)
    match op:
        case "+":
            result += x
        case "*":
            result *= x

    return result

def part_1(i: list[str]):
    result = 0
    operations = i[-1].replace(' ', '')

    clean = []
    for line_i in range(0, len(i)-1):
        clean.append(re.sub(r'\s+', ' ', i[line_i]).strip().split(' '))

    for x in range(0, len(clean[0])):
        col_res = int(clean[0][x])
        for y in range(1, len(clean)):
            col_res = operation(col_res, clean[y][x], operations[x])

        result += col_res

    print(f"[P1] Grand total: {result}")

def part_2(i: list[str]):
    result = 0

    nums = []
    for col in range(len(i[0])-1, -1, -1):
        num = ""
        op = None

        for row in range(0, len(i)):
            if i[row][col] == '+' or i[row][col] == '*':
                op = i[row][col]
            elif i[row][col] != ' ':
                num += i[row][col]

        if op:
            nums.append(int(num))
            if op == '+':
                result += sum(nums)
            else:
                tmp = nums[0]
                for idx in range(1, len(nums)):
                    tmp *= nums[idx]
                result += tmp
            nums = []
        elif num.strip():
            nums.append(int(num))

    print(f"[P2] Grand total using Cephalopod math: {result}")

if __name__ == "__main__":
    inputs = _get_input()
    if not inputs:
        print("Error! Input file is empty!")
        sys.exit()

    part_1(inputs)
    part_2(inputs)

    sys.exit()
