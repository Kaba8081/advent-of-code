# 'Advent of code' solution for year 2023 day 10
import os
import sys

from dataclasses import dataclass

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

def checkDirections(value) -> list: # return an empty list if an empty field is supplied (".")
    if value == "|":
        return ["N", "S"]
    elif value == "-":
        return ["E", "W"]
    elif value == "L":
        return ["N", "E"]
    elif value == "J":
        return ["N", "W"]
    elif value == "7":
        return ["S", "W"]
    elif value == "F":
        return ["S", "E"]
    elif value == "S":
        return ["N", "E", "S", "W"]
        
    return []

def checkIfConnected(dirs1, dirs2, horizontal_diff, vertical_diff) -> bool:
    if "N" in dirs1 and "S" in dirs2 and vertical_diff == -1 and horizontal_diff == 0:
        return True
    elif "S" in dirs1 and "N" in dirs2 and vertical_diff == 1 and horizontal_diff == 0:
        return True
    elif "E" in dirs1 and "W" in dirs2 and vertical_diff == 0 and horizontal_diff == 1:
        return True
    elif "W" in dirs1 and "E" in dirs2 and vertical_diff == 0 and horizontal_diff == -1:
        return True
    else:
        return False

def locateLoop(map, start_x, start_y) -> list: # returns an empty list if no loop is found
    curr_directions = checkDirections(map[start_x][start_y])
    curr_position = [start_x, start_y]
    next_directions = None

    loop_map = [curr_position]
    reverse_directions = {"N": "S", "S": "N", "E": "W", "W": "E"}

    while len(curr_directions) > 0:
        for dir in curr_directions:
            vertical_diff = 0
            horizontal_diff = 0

            if dir == "N":
                vertical_diff = -1
            elif dir == "S":
                vertical_diff = 1
            elif dir == "E":
                horizontal_diff = 1
            elif dir == "W":
                horizontal_diff = -1
            else:
                return [] # selected direction is not valid

            next_directions = checkDirections(map[curr_position[0] + vertical_diff][curr_position[1] + horizontal_diff])
            if next_directions == []: # empty field
                continue
            elif checkIfConnected(curr_directions, next_directions, horizontal_diff, vertical_diff):
                curr_position[0] += vertical_diff
                curr_position[1] += horizontal_diff
                
                next_directions.remove(reverse_directions[dir])
                curr_directions = next_directions
                
                if curr_position == [start_x, start_y]:
                    return loop_map # loop found
                else:
                    loop_map.append(curr_position.copy())
                    break
            else:
                return [] # loop not found

def part1(input) -> int:
    steps = 0

    map = [list(line) for line in input]

    for y, row in enumerate(map):
        for x, value in enumerate(row):
            if value == "S":
                loop_map = locateLoop(map, y, x)

                steps = int(len(loop_map) / 2)
                    

    return steps

"""
Part 2 solved using tlareg's (https://www.reddit.com/u/tlareg/) solution
Pick's theorem (https://en.wikipedia.org/wiki/Pick%27s_theorem):
A = i + b/2 - 1

where A - area of a polygon, i - number of points inside the polygon, b - number of points on the edge of the polygon
b - solution to part 1 * 2
i - solution to part 2
A - Area can be calculated using Sholace formula (https://en.wikipedia.org/wiki/Shoelace_formula):

2A = [(x1 * y2) - (x2 * y1)] +  [(x2 * y3) - (x3 * y2)] + ... + [(xn * y1) - (x1 * yn)]
where (x1, y1), (x2, y2), ... (xn, yn) are the coordinates of the polygon's vertices

i = 2A - b + 2
"""
def part2(input) -> int:
    edges = []

    map = [list(line) for line in input]
    loop_map = []

    for y, row in enumerate(map):
        for x, value in enumerate(row):
            if value == "S":
                loop_map = locateLoop(map, y, x)
                break

    for pipe in loop_map:
        if map[pipe[0]][pipe[1]] in "SLJ7F": # if the pipe is a corner, add it to the edge count
            edges.append((pipe[0], pipe[1]))

    area = 0
    for i in range(len(edges)):
        next_i = (i + 1) % len(edges)
        currentX, currentY = edges[i]
        nextX, nextY = edges[next_i]
        area += currentX * nextY - currentY * nextX
    area = abs(area) / 2
    
    return int(area - len(loop_map)/2) + 1 # points inside the loop

if __name__ == "__main__":
    input = get_input()
    if not input:
        print("Error! Input file is empty!")
        sys.exit()
                        
    result1 = part1(input)
    print("[10.1] How many steps to get to the furthest point: ", result1)
    result2 = part2(input)
    print("[10.2] How many tiles are enclosed by the loop: ", result2)
    
    sys.exit()
