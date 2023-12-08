# 'Advent of code' solution for year 2023 day 5
import os
import sys
                        
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

if __name__ == "__main__":
    input = get_input()
    if not input:
        print("Error! Input file is empty!")
        sys.exit()
    
    input1 = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4""".strip().split("\n\n")

    result1 = part1(input)
    print("[5.1] Lowest location number: ", result1)

    result2 = part2(input)
    print("[5.2] Lowest location number: ", result2)

    input("Press any key to continue...")
    
    sys.exit()