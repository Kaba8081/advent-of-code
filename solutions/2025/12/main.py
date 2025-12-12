# 'Advent of code' solution for year 2025 day 12
import os
import sys

DIR_PATH = os.path.dirname(os.path.realpath(__file__))

def _get_input():
    content = None
    if os.path.isfile(os.path.join(DIR_PATH, "input.txt")):
        with open(os.path.join(DIR_PATH, "input.txt"), "r", encoding="utf-8") as file:
            content = file.read().strip()
        return content
    else:
        print("Error! Input file does not exist!")
        sys.exit()

def interpret_input(str_i: list[str]) -> tuple[
    dict[int, list[str]],
    list[tuple[ tuple[int, int], list[int] ]]
]:
    str_i = str_i.split("\n\n")

    str_pieces = str_i[:-1]
    pieces: dict[int, list[str]] = {}
    for piece in str_pieces:
        piece = piece.split("\n")

        id = piece[0][0]
        mtrx = piece[1:]

        pieces[int(id)] = mtrx

    str_grids = str_i[-1].split("\n")
    grids: list[tuple[ tuple[int, int], list[int] ]] = []
    for row in str_grids:
        row = row.split(" ")
        w, h = (int(v) for v in row[0][:-1].split("x"))
        req = [int(v) for v in row[1:]]

        grids.append(( (w, h), req ))

    return pieces, grids 

def part_1(str_i: list[str]):
    pieces, grids = interpret_input(str_i)
    result = 0

    for grid in grids:
        free_space = grid[0][0] * grid[0][1]
        taken_space = 0
        for i, shape_count in enumerate(grid[1]):
            for line in pieces[i]:
                taken_space += line.count("#") * shape_count
        
        if taken_space <= free_space:
            result += 1

    print(f"[P1] ys {result}")

def part_2(i: list[str]):
    return

if __name__ == "__main__":
    inputs = _get_input()
    if not inputs:
        print("Error! Input file is empty!")
        sys.exit()

    part_1(inputs)
    part_2(inputs)

    sys.exit()
