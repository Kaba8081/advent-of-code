# 'Advent of code' solution for year 2022 day 4
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
    points = 0
    my_nums = []
    
    for line in input:
        temp_points = 0
        
        # line[0] - list of winning numbers
        # line[1] - list of scratchcard numbers
        line = line.split('|')
        line[0] = line[0].split(":")[1].split(" ")
        line[1] = line[1].split(" ")
        
        for my_num in line[1]:
            if my_num != '':
                if my_num in line[0]:
                    if temp_points == 0:
                        temp_points = 1
                    else:
                        temp_points *= 2
        
        points += temp_points

    return points

if __name__ == "__main__":
    input = get_input()

#     input = """
# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".strip().splitlines()

    if not input:
        print("Error! Input file is empty!")
        sys.exit()
                        
    # your code goes here

    result1 = part1(input)
    print("[4.1] Total scratchcards points: ", result1)

    sys.exit()
