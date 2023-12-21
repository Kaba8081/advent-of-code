# 'Advent of code' solution for year 2023 day 11
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

def expandGalaxy(galaxy) -> list:
    new_galaxy = galaxy.copy()
    new_galaxy = [list(row) for row in new_galaxy]

    offset = 0
    for y in range(len(galaxy)): # expand empty rows
        empty = True
        for x in range(len(galaxy[y])):
            if galaxy[y][x] != ".":
                empty = False
                continue

        if empty:
            new_galaxy.insert(y+offset, list("." * len(galaxy[y])))
            offset += 1

    offset = 0
    for x in range(len(new_galaxy[0])): # expand empty columns
        empty = True
        for y in range(len(galaxy)):
            if galaxy[y][x] != ".":
                empty = False
                continue
        
        if empty:
            for y in range(len(new_galaxy)):
                new_galaxy[y].insert(x+offset, ".")
            offset += 1

    return new_galaxy

def part1(input) -> int:
    dist_sum = 0

    galaxy = [list(row) for row in input]
    galaxy = expandGalaxy(input)

    planets = {} # id: [x, y]

    for y in range(len(galaxy)):
        for x in range(len(galaxy[y])):
            if galaxy[y][x] == "#":
                planets[len(planets.keys())] = [x, y]

    counted = []
    for i in range(len(planets.keys())):
        for j in range(len(planets.keys())):
            if i == j or i in counted:
                continue
            else:
                dist_sum += abs(planets[i][0] - planets[j][0]) + abs(planets[i][1] - planets[j][1])

        counted.append(i)

    return int(dist_sum/2)

if __name__ == "__main__":
    input = get_input()
    if not input:
        print("Error! Input file is empty!")
        sys.exit()

    result1 = part1(input)
    print("[11.1] Sum of all lenghts between planets: ", result1)
    
    sys.exit()
