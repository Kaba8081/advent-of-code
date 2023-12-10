# 'Advent of code' solution for year 2023 day 8
import os
import sys
                        
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

def part1(input) -> int:
    instructions = input[0]
    current_pos = "AAA"
    moves = 0
    map = {}

    for line in input[2:]:
        line = line.split(" = ")
        line[1] = line[1].split(", ")

        map[line[0]] = (line[1][0][1:], line[1][1][:-1])
    
    while current_pos != "ZZZ":
        moves += 1
        if instructions[(moves - 1) % len(instructions)] == "L":
            current_pos = map[current_pos][0]
        else:
            current_pos = map[current_pos][1]

    return moves

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return int((a * b) / gcd(a, b))

def part2(input) -> int:
    instructions = input[0]
    current_pos = {}
    required_moves = {}
    map = {}

    for line in input[2:]:
        line = line.split(" = ")
        line[1] = line[1].split(", ")

        map[line[0]] = (line[1][0][1:], line[1][1][:-1])

        if line[0][-1] == "A":
            current_pos[line[0]] = line[0]
    
    for node in current_pos.keys():
        required_moves[node] = 0

        while current_pos[node][-1] != "Z":
            required_moves[node] += 1
            if instructions[(required_moves[node] - 1) % len(instructions)] == "L":
                current_pos[node] = map[current_pos[node]][0]
            else:
                current_pos[node] = map[current_pos[node]][1]

    lcm_of_moves = 1
    for moves in required_moves.values():
        lcm_of_moves = lcm(lcm_of_moves, moves)
        
    return lcm_of_moves

if __name__ == "__main__":
    input = get_input()
    if not input:
        print("Error! Input file is empty!")
        sys.exit()
    
    result1 = part1(input)
    print("[8.1] How many steps are required to reach ZZZ: ", result1)
    result2 = part2(input)
    print("[8.2] How many steps are required to reach nodes xxZ:", result2)
    
    sys.exit()
