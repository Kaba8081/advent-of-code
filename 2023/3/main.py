# 'Advent of code' solution for year 2022 day 3
import os
import sys

from string import punctuation

global DIR_PATH
DIR_PATH = os.path.dirname(os.path.realpath(__file__))

# universal functions
def get_input():
    input = None
    if os.path.isfile(os.path.join(DIR_PATH, "input.txt")):
        with open(os.path.join(DIR_PATH, "input.txt"), "r") as file:    
            input = file.read().strip().splitlines()
        return input
    else:
        print("Error! Input file does not exist!")
        sys.exit()

def check_side(line, index, step):
    number = ""
    numeric = [str(i) for i in range(10)]

    if step == -1: # check left
        for i in range(index-1, -1, -1):
            if line[i] in numeric:
                number = line[i] + number
            else:
                break
    elif step == 1: # check right
        for i in range(index+1, len(line), 1):
            if line[i] in numeric:
                number += line[i]
            else:
                break
    
    return number

# part 1 functions
def sum_nearby(input, input_index, line_index):
    part_sum = 0
    numeric = [str(i) for i in range(10)]

    # check if middle is a number
    if input[input_index][line_index] in numeric:
        # left + middle + right
        number = ""
        number += check_side(input[input_index], line_index, -1) # left side
        number += input[input_index][line_index] 
        number += check_side(input[input_index], line_index, 1) # right side
        part_sum = int(number)
    else: # check left and right
        if input[input_index][line_index-1] in numeric: # left side is a number
            # left + number
            number = ""
            number += check_side(input[input_index], line_index-1, -1) # left side
            number += input[input_index][line_index-1]
            part_sum += int(number)
        if input[input_index][line_index+1] in numeric: # right side is a number
            # number + right
            number = ""
            number += input[input_index][line_index+1]
            number += check_side(input[input_index], line_index+1, 1) # right side
            part_sum += int(number)
    
    return part_sum

def part1(input):
    part_sum = 0
    symbols = list(punctuation)
    symbols.remove(".") # remove dot from symbols

    for i, line in enumerate(input):
        for j, symbol in enumerate(line):
            if symbol in symbols: # check only symbols
                # select line above
                if i > 0:
                    part_sum += sum_nearby(input, i-1, j)
                
                # select same line
                part_sum += sum_nearby(input, i, j)
                
                # select line below
                if i < len(input)-1:
                    part_sum += sum_nearby(input, i+1, j)
                    
    return part_sum

# part 2 functions
def find_nearby(input, input_index, line_index):
    found_nums = []
    numeric = [str(i) for i in range(10)]

    # check if middle is a number
    if input[input_index][line_index] in numeric:
        # left + middle + right
        number = ""
        number += check_side(input[input_index], line_index, -1) # left side
        number += input[input_index][line_index] 
        number += check_side(input[input_index], line_index, 1) # right side
        found_nums.append(int(number))
    else: # check left and right
        if input[input_index][line_index-1] in numeric: # left side is a number
            # left + number
            number = ""
            number += check_side(input[input_index], line_index-1, -1) # left side
            number += input[input_index][line_index-1]
            found_nums.append(int(number))
        if input[input_index][line_index+1] in numeric: # right side is a number
            # number + right
            number = ""
            number += input[input_index][line_index+1]
            number += check_side(input[input_index], line_index+1, 1) # right side
            found_nums.append(int(number))
    
    return found_nums

def part2(input):
    ratio_sum = 0

    for i, line in enumerate(input):
        for j, symbol in enumerate(line):
            nearby_nums = []

            if symbol == "*": # check only gears
                # select line above
                if i > 0:
                    nearby_nums += find_nearby(input, i-1, j)
                
                # select same line
                nearby_nums += find_nearby(input, i, j)
                
                # select line below
                if i < len(input)-1:
                    nearby_nums += find_nearby(input, i+1, j)

                ratio_sum += nearby_nums[0] * nearby_nums[1] if len(nearby_nums) == 2 else 0

    return ratio_sum

if __name__ == "__main__":
    input = get_input()

    if not input:
        print("Error! Input file is empty!")
        sys.exit()
                        
    result1 = part1(input)
    print("[1.1] Sum of all engine part numbers: ", result1)
    result2 = part2(input)
    print("[1.2] Sum of all gear ratios: ", result2)
    
    sys.exit()
