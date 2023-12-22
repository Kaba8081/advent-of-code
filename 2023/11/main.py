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

def findEmptySpaceBetween(empty_spaces, planet1, planet2) -> int:
    result = 0

    # find empty collumns between planets
    for x in range(*sorted((planet1[0], planet2[0]))):
        if x in empty_spaces[1]:
            result += 1
    
    # find empty rows between planets
    for y in range(*sorted((planet1[1], planet2[1]))):
        if y in empty_spaces[0]:
            result += 1
    
    return result

def methodWithoutExpanding(input, expand_amount) -> int:
    dist_sum = 0

    galaxy = [list(row) for row in input]
    planets = {} # id: [x, y]
    spaces = [[], []] # [[y1, y2, ...], [x1, x2, ...]]

    for y in range(len(galaxy)):
        for x in range(len(galaxy[y])):
            if galaxy[y][x] == "#":
                planets[len(planets.keys())] = [x, y]

    # find empty collumns between planets
    for x in range(0, len(galaxy)):
        empty = True
        for y in range(len(galaxy[x])):
            if galaxy[y][x] != ".":
                empty = False
                break
        if empty:
            spaces[1].append(x)
    
    # find empty rows between planets
    for y in range(0, len(galaxy)):
        empty = True
        for x in range(len(galaxy[y])):
            if galaxy[y][x] != ".":
                empty = False
                break
        if empty:
            spaces[0].append(y)

    for i in range(len(planets.keys())):
        for j in range(len(planets.keys())):
            if i > j: continue
            else:
                empty_space = findEmptySpaceBetween(spaces, planets[i], planets[j])
                dist_sum += abs(planets[i][0] - planets[j][0]) + abs(planets[i][1] - planets[j][1]) + empty_space * expand_amount - empty_space

    return dist_sum

def part1WithoutExpanding(input) -> int:
    return methodWithoutExpanding(input, 2)

def part2(input) -> int:
    return methodWithoutExpanding(input, 1000000)

if __name__ == "__main__":
    input = get_input()
    if not input:
        print("Error! Input file is empty!")
        sys.exit()

    result1 = part1(input)
    print("[11.1] Sum of all lenghts between planets: ", result1)
    result1 = part1WithoutExpanding(input)
    print("[11.1] Sum of all lenghts between planets (using a method without expanding galaxies): ", result1)
    result2 = part2(input)
    print("[11.2] Sum of all lenghts between planets in the much older galaxy: ", result2)
    
    sys.exit()
