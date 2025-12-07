# 'Advent of code' solution for year 2025 day 7
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
    result = 0
    curr = set()

    curr.add(i[0].find("S"))
    for line_i, line in enumerate(i[1:], 1):
        new_curr = set()
        for index in curr:
            if line[index] == '^':
                if index-1 >= 0 and line[index-1] == ".": # split left
                    line = line[:index-1] + "|" + line[index:]
                    new_curr.add(index-1)
                if index+1 <= len(line) and line[index+1] == ".": # split right
                    line = line[:index+1] + "|" + line[index+2:]
                    new_curr.add(index+1)
                result+=1
            elif i[line_i][index] == ".":
                line = line[:index] + "|" + line[index+1:]
                new_curr.add(index)
        curr = new_curr
        i[line_i] = line

        # print("\n".join(i), "\n")

    print(f"[P1] Beam was split {result} times")

def part_2(i: list[str]):
    found: dict[tuple[int, int], int] = {}
    splitters: dict[int, list[int]] = {}

    for y, line in enumerate(i):
        for x, val in enumerate(line):
            if val == "^":
                if x not in splitters:
                    splitters[x] = []
                splitters[x].append(y)

    def rec(x: int, y: int) -> int:
        if (x,y) in found:
            return found[(x,y)]

        split: int | None = None
        if x in splitters and y < max(splitters[x]):
            for sy in splitters[x]:
                if sy > y:
                    split = sy
                    break

        if split is None:
            return 1

        l = rec(x-1, split)
        r = rec(x+1, split)

        found[(x,y)] = l + r
        return l + r

    result = rec(i[0].find("S"), 0)
    print(f"[P2] Beam was split {result} times")

if __name__ == "__main__":
    inputs = _get_input()
    if not inputs:
        print("Error! Input file is empty!")
        sys.exit()

    part_1(inputs.copy())
    part_2(inputs.copy())

    sys.exit()
