# 'Advent of code' solution for year 2023 day 5
import os
import sys

from time import sleep
                        
global DIR_PATH
DIR_PATH = os.path.dirname(os.path.realpath(__file__))

def get_input():
    input = None
    if os.path.isfile(os.path.join(DIR_PATH, "input.txt")):
        with open(os.path.join(DIR_PATH, "input.txt"), "r") as file:    
            input = file.read().strip().split("\n\n")
        return input
    else:
        print("Error! Input file does not exist!")
        sys.exit()

def part1(input):
    seeds = []
    seeds_transformed = {}

    for i, line in enumerate(input):
        if i == 0: # first line contains the seeds list
            seeds = line.split(":")[1][1:].split(" ")

            for seed in seeds:
                seed = int(seed)
                seeds_transformed[seed] = seed
        else:
            map_lines = line.split("\n")[1:]

            for seed in seeds_transformed.keys():
                temp_seeds_transformed = seeds_transformed.copy()

                for map_range in map_lines:
                    map_range = [int(value) for value in map_range.split(" ")]

                    if seeds_transformed[seed] >= map_range[1] and seeds_transformed[seed] <= map_range[1] + map_range[2]:
                        temp_seeds_transformed[seed] += (map_range[0] - map_range[1])
                    
                seeds_transformed = temp_seeds_transformed

    return min(seeds_transformed.values())

def part2(input) -> int:
    seeds = []
    min_values = []
    
    line = input[0].split(":")[1][1:].split(" ") # first line contains the seeds list
    seeds = [int(value) for value in line]

    for i in range(0, len(seeds), 2):
        ranges = [[seeds[i], seeds[i] + seeds[i+1]]]
        results = []

        for line in input[1:]: # loop through all the maps
            map_lines = line.split("\n")[1:]
            while ranges:
                r = ranges.pop()

                for map_line in map_lines:
                    target, start_range, size = [int(value) for value in map_line.split(" ")]

                    end_range = start_range + size
                    offset = target - start_range

                    if end_range <= r[0] or r[1] <= start_range:
                        continue
                    if r[0] < start_range:
                        ranges.append([r[0], start_range])
                        r[0] = start_range
                    if r[1] > end_range:
                        ranges.append([end_range, r[1]])
                        r[1] = end_range
                    results.append([r[0] + offset, r[1] + offset])
                    break
                else:
                    results.append([r[0], r[1]])
            ranges = results
            results = []
        min_values += ranges

    min_values = [value[0] for value in min_values]
    return min(min_values)

if __name__ == "__main__":
    input = get_input()
    if not input:
        print("Error! Input file is empty!")
        sys.exit()

    result1 = part1(input)
    print("[5.1] Lowest location number: ", result1)
    result2 = part2(input)
    print("[5.2] Lowest location number: ", result2)

    sys.exit()