# 'Advent of code' solution for year 2022 day 6
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

def part1(input):
    time_line = input[0].split(":")[1].strip().split(' ')
    time_line = [int(value) for value in time_line if value != '']
    
    distance_line = input[1].split(":")[1].strip().split(' ')
    distance_line = [int(value) for value in distance_line if value != '']

    data = (time_line, distance_line)
    result = 1

    for i, race_time in enumerate(data[0]):
        possible_ways = 0

        for speed in range(1,race_time-1):
            distance = speed * (race_time-speed)
            
            if distance > data[1][i]:
                possible_ways += 1
        
        result *= (possible_ways if possible_ways > 0 else 1)
    
    return result

def part2(input):
    race_time = int(input[0].split(":")[1].strip().replace(' ', ''))
    top_distance = int(input[1].split(":")[1].strip().replace(' ', ''))
    possible_ways = 0

    for speed in range(1, race_time-1):
        distance = speed * (race_time-speed)
        
        if distance > top_distance:
            possible_ways += 1
    
    return possible_ways

if __name__ == "__main__":
    input = get_input()
    if not input:
        print("Error! Input file is empty!")
        sys.exit()

    result1 = part1(input)
    print("[6.1] Multiplied winnable solutions:", result1)
    result2 = part2(input)
    print("[6.2] Possible ways:", result2)
    
    sys.exit()
