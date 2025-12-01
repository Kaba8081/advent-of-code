# 'Advent of code' solution for year 2024 day 6
import os
import sys
from typing import Literal
                        
global DIR_PATH
DIR_PATH = os.path.dirname(os.path.realpath(__file__))

def guard_step(puzzle_map: list[list[str]], pos: tuple[int, int], direction: Literal["N", "E", "S", "W"]) -> tuple[Literal["N", "E", "S", "W"], tuple[int, int]]:
    """Return the next direction and position of the guard
    @param: map: list[list[str]] - the map of the puzzle
    @param: pos: tuple[int, int] - the current position of the guard
    @param: direction: str - the current direction of the guard
    @return: tuple[str, tuple[int, int]] - the next direction and position of the guard
    """
    
    _vec2 = (0,0) # movement vector
    next_direction = direction # next direction if the guard hits a wall

    match direction:
        case "N":
            _vec2 = (-1, 0)
            next_direction = "E"
        case "E":
            _vec2 = (0, 1)
            next_direction = "S"
        case "S":
            _vec2 = (1, 0)
            next_direction = "W"
        case "W":
            _vec2 = (0, -1)
            next_direction = "N"
    
    _new_pos = (pos[0] + _vec2[0], pos[1] + _vec2[1])

    if 0 > _new_pos[0] or _new_pos[0] >= len(puzzle_map) or 0 > _new_pos[1] or _new_pos[1] >= len(puzzle_map[0]):
        return direction, _new_pos
    elif puzzle_map[_new_pos[0]][_new_pos[1]] == "#":
        return next_direction, pos

    return direction, _new_pos

def predict_path(puzzle_map: list[list[str]], start: tuple[int, int]) -> list[list[bool]]:
    """Return the full path the guard will traverse"""
    direction = "N"
    x, y = start

    # initialize the guard path
    path = [[False for _ in range(len(puzzle_map[0]))] for _ in range(len(puzzle_map))]
    path[x][y] = True

    # while the guard is inside the map
    while True:
        direction, new_pos = guard_step(puzzle_map, (x, y), direction)
        x, y = new_pos
        if not (x >= 0 and x < len(puzzle_map) and y >= 0 and y < len(puzzle_map[0])):
            break
        path[x][y] = True

    return path

def part1(puzzle_map: list[list[str]]) -> int:
    """Return a sum of distinct points visited by the guard"""
    start = None
    for x in range(len(puzzle_map)):
        for y in range(len(puzzle_map[x])):
            if puzzle_map[x][y] == "^":
                start = (x, y)
                break
    
    if not start:
        print("Start position not found!")
        start = (0,0)

    path = predict_path(puzzle_map, start)

    return sum([row.count(True) for row in path])

def part2(puzzle_map: list[list[str]]) -> int:
    """Return the number of loops,
    that can be created by placing a single block"""
    _loops = 0

    start = None
    for x in range(len(puzzle_map)):
        for y in range(len(puzzle_map[x])):
            if puzzle_map[x][y] == "^":
                start = (x, y)
                break
    
    if not start:
        print("Start position not found!")
        start = (0,0)
    
    pos = start
    directions =[("N", start)] # list[ (direction, turning point) ]

    # while the guard is inside the map
    while True:
        n_direction, pos = guard_step(puzzle_map, (x, y), directions[-1])
        if n_direction != directions[-1][0]:
            directions.append((n_direction, pos))
        
        # if the guard is outside the map - break
        if not (pos[0] >= 0 and pos[0] < len(puzzle_map) and pos[1] >= 0 and pos[1] < len(puzzle_map[0])):
            break
        
        # if the guard is inside the map and the last 3 directions are different
        # if the guard is on the same x or y
        # as in the 3rd last turning point
        # and if the next tile is not a wall
        if (len(set(directions[-3:])) == 3
            and (directions[-3][1][0] == x or directions[-3][1][1] == y)):
                _loops += 1
    
    return _loops

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
