# 'Advent of code' solution for year 2025 day 4
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

def check_surroundings(map: list[str], x: int, y: int) -> int:
    # returns how many haybales surround the given coord
    result = 0

    for i in range(-1, 2):
        y2 = y + i
        
        for j in range(-1, 2):
            x2 = x + j

            if x2 < 0 or y2 < 0 or x2 >= len(map[0]) or y2 >= len(map):
                continue
            if i == 0 and j == 0:
                continue
            if map[y2][x2] == "@":
                result += 1
    
    return result

def remove_haybale(map: list[str], x: int, y: int) -> bool:
    # returns true if a haybale at the given location was removed
    count = 0

    for i in range(-1, 2):
        y2 = y + i
        
        for j in range(-1, 2):
            x2 = x + j

            if x2 < 0 or y2 < 0 or x2 >= len(map[0]) or y2 >= len(map):
                continue
            elif i == 0 and j == 0:
                continue
            elif map[y2][x2] == "x":
                continue
            elif map[y2][x2] == "@":
                count += 1
    
    if count < 4 and map[y][x] == '@':
        map[y] = map[y][:x] + 'x' + map[y][x+1:]
        return True
    return False

def part_1(i: list[str]):
    result = 0

    for y, line in enumerate(i):
        for x, value in enumerate(line):
            if value == "." or value == 'x':
                continue
            elif check_surroundings(i, x, y) < 4:
                result += 1

    print(f"[P1] Rolls accessed by forklifts: {result}")

def part_2(i: list[str]):
    result = 0

    prev_count = -1
    curr_count = 0
    while prev_count != curr_count:
        for y, line in enumerate(i):
            for x, value in enumerate(line):
                if value == ".":
                    continue
                elif remove_haybale(i, x, y):
                    result += 1

        prev_count = int(curr_count)
        curr_count = int(result)

    print(f"[P2] Rolls accessed by forklifts: {result}")

if __name__ == "__main__":
    inputs = _get_input()
    if not inputs:
        print("Error! Input file is empty!")
        sys.exit()

    part_1(inputs)
    part_2(inputs)

    sys.exit()
