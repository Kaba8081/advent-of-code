# 'Advent of code' solution for year 2022 day 1
import os
import sys

from string import punctuation

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

def check_left(line, y):
    number = ""
    numeric = [str(i) for i in range(10)]

    for i in range(y-1, -1, -1):
        if line[i] in numeric:
            number = line[i] + number
        else:
            break
    
    return number

def check_right(line, y):
    number = ""
    numeric = [str(i) for i in range(10)]

    for i in range(y+1, len(line), 1):
        if line[i] in numeric:
            number += line[i]
        else:
            break

    return number

def part1(input):
    part_sum = 0
    last_part_sum = 0
    symbols = list(punctuation)
    symbols.remove(".")
    numeric = [str(i) for i in range(10)]

    for input_i, line in enumerate(input):
        
        for line_i, symbol in enumerate(line):
            if symbol in symbols:
                
                # line above
                if input_i > 0:
                    if input[input_i-1][line_i] in numeric: # number directly to above the symbol -> left + number + right
                        number = check_left(input[input_i-1], line_i)
                        number += input[input_i-1][line_i]
                        number += check_right(input[input_i-1], line_i)
                        part_sum += int(number) if number else 0
                    else:
                        if input[input_i-1][line_i-1] in numeric: # top left corner -> left + number
                            number = check_left(input[input_i-1], line_i-1)
                            number += input[input_i-1][line_i-1]
                            part_sum += int(number) if number else 0
                        if input[input_i-1][line_i+1] in numeric: # top right corner -> number + right
                            number = input[input_i-1][line_i+1]
                            number += check_right(input[input_i-1], line_i+1)
                            part_sum += int(number) if number else 0

                # same line
                if input[input_i][line_i-1] in numeric: # left + number
                    number = check_left(line, line_i)
                    part_sum += int(number) if number else 0
                if input[input_i][line_i+1] in numeric: # number + right
                    number = check_right(line, line_i)
                    part_sum += int(number) if number else 0
                
                # line below
                if input_i < len(input)-1:
                    # directly below
                    if input[input_i+1][line_i] in numeric: # left + number + right
                        number = check_left(input[input_i+1], line_i)
                        number += input[input_i+1][line_i]
                        number += check_right(input[input_i+1], line_i)
                        part_sum += int(number) if number else 0
                    else:
                        if input[input_i+1][line_i-1] in numeric: # bottom left corner -> left + number
                            number = check_left(input[input_i+1], line_i-1)
                            number += input[input_i+1][line_i-1]
                            part_sum += int(number) if number else 0
                        if input[input_i+1][line_i+1] in numeric: # bottom right corner -> number + right
                            number = input[input_i+1][line_i+1]
                            number += check_right(input[input_i+1], line_i+1)
                            part_sum += int(number) if number else 0

                print(input[input_i-1] if input_i > 0 else "")
                print(line)
                print(input[input_i+1] if input_i < len(input) else "")
                print(part_sum - last_part_sum)
                print("position:", input_i, line_i)
                print("-"*20)
                last_part_sum = part_sum

    print(part_sum) 

    return part_sum

if __name__ == "__main__":
    input = get_input()

#     input = """467..114.. 
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..""".strip().splitlines() # test input

    if not input:
        print("Error! Input file is empty!")
        sys.exit()
                        
    result1 = part1(input)
    print("[1.1] Sum of all engine part numbers: ", result1)
    
    sys.exit()
