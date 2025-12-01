# 'Advent of code' solution for year 2024 day 4
import os
import sys
import re

global DIR_PATH
DIR_PATH = os.path.dirname(os.path.realpath(__file__))

def search_for_word(lines: list[str], word: str, pos: tuple[int, int]) -> int:
    """Find all possible combinations of the given word 
    in the given list of lines at the given position"""
    word_count = 0
    x, y = pos

    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue

            i = 0
            while (0 <= x + i * dx < len(lines)
                   and 0 <= y + i * dy < len(lines[0])
                   and i < len(word)):
                if not lines[x + i * dx][y + i * dy] == word[i] or i >= len(word):
                    break
                if i == len(word) - 1:
                    word_count += 1
                    break
                i += 1

    return word_count

def part1(lines: list[str]) -> int:
    word = "XMAS"
    word_count = 0
    indexes = [(i, m.start()) for i, line in enumerate(lines) for m in re.finditer(word[0], line)]
    for index in indexes:
        word_count += search_for_word(lines, word, index)

    return word_count

def check_xmas(lines: list[str], pos: tuple[int, int]) -> int:
    """Find diagonal pattern 'MAS' in the given list of lines at the given position"""
    x, y = pos

    # Edge of the grid definetly doesn't contain the pattern
    if x == 0 or y == 0 or x == len(lines) - 1 or y == len(lines[0]) - 1:
        return 0

    letters = {"M", "S"}

    if ({lines[x - 1][y - 1], lines[x + 1][y + 1]} == letters
        and {lines[x - 1][y + 1], lines[x + 1][y - 1]} == letters):
        return 1

    return 0

def part2(lines: list[str]) -> int:
    word_count = 0
    indexes = [(i, m.start()) for i, line in enumerate(lines) for m in re.finditer("A", line)]

    for index in indexes:
        word_count += check_xmas(lines, index)
    return word_count

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

    result1 = part1(input)
    print(f"Part 1: {result1}")
    result2 = part2(input)
    print(f"Part 2: {result2}")

    sys.exit()
