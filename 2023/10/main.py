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

@dataclass
class Pipe: 
    value: str
    directions: list = None
    neighbours: list = None

    def __init__(self) -> None:
        self.check_directions()

        return      

    def check_directions(self) -> None:
        if self.value == "|":
            self.directions = ["N", "S"]
        elif self.value == "-":
            self.directions = ["E", "W"]
        elif self.value == "L":
            self.directions = ["N", "E"]
        elif self.value == "J":
            self.directions = ["N", "W"]
        elif self.value == "7":
            self.directions = ["S", "W"]
        elif self.value == "F":
            self.directions = ["S", "E"]
        elif self.value == "S":
            self.directions = ["N", "E", "S", "W"]
        
        return 

def checkIfConnected(map, x, y) -> bool:
    pass

def locateLoop(map, start_x, start_y) -> dict:
    loop_dict = {}
    
    

    return loop_dict

def part1(input) -> int:
    steps = 0

    map = [line.split() for line in input]
    loop_map = {}

    for y, row in enumerate(map):
        if "S" in row:
            loop_map = locateLoop(map, y, row.index("S"))

    return steps

if __name__ == "__main__":
    input = get_input()
    if not input:
        print("Error! Input file is empty!")
        sys.exit()

    input = """.....
.S-7.
.|.|.
.L-J.
.....""".strip().splitlines()
                        
    result1 = part1(input)
    print("[10.1] How many steps to get to the furthest point: ", result1)
    
    sys.exit()
