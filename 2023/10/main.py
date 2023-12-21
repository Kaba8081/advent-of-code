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

if __name__ == "__main__":
    input = get_input()
    if not input:
        print("Error! Input file is empty!")
        sys.exit()

#     input = """..F7.
# .FJ|.
# SJ.L7
# |F--J
# LJ...""".strip().splitlines()
                        
    result1 = part1(input)
    print("[10.1] How many steps to get to the furthest point: ", result1)
    
    sys.exit()
