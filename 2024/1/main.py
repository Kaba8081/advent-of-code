# 'Advent of code' solution for year 2024 day 1
import os
import sys
  
global DIR_PATH
DIR_PATH = os.path.dirname(os.path.realpath(__file__))

def get_ids(input: list[str]) -> (list[int], list[int]):
    """Returns two lists of ids from input"""
    ids_1 = []
    ids_2 = []

    for line in input:
        ids = line.split("   ")
        ids_1.append(int(ids[0]))
        ids_2.append(int(ids[1]))

    return ids_1, ids_2

def get_distance(input: list[str]) -> int:
    """Returns a total distance between two lists of ids"""
    total_distance = 0
    ids_1, ids_2 = get_ids(input)

    ids_1.sort()
    ids_2.sort()

    total_distance = sum([abs(id1 - id2) for id1, id2 in zip(ids_1, ids_2)])

    return total_distance

def get_similarity(input: list[str]) -> int:
    """Returns a similarity between two lists of ids"""
    similarity = 0
    ids_1, ids_2 = get_ids(input)

    for id_1 in ids_1:
        similarity += id_1 * ids_2.count(id)

    return similarity

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

    result1 = get_distance(input)
    print("Part 1: ", result1)

    result2 = get_similarity(input)
    print("Part 2: ", result2)

    sys.exit()
