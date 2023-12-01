# Advent of code solution for year 2023 day 1
import sys

input = None

test_input1 = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet""".strip().splitlines()

test_input2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen""".strip().splitlines()

with open("input.txt","r") as file:
    input = file.read().strip().splitlines()

if not input:
    print("Error! Input file is empty!")
    sys.exit()

global numeric_values, text_values
numeric_values = "1,2,3,4,5,6,7,8,9".split(",")
text_values = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

# day 1 part 1
def part1(input):
    calibration_sum = 0

    for line in input:
        calibration = ""
        line = line.lower()

        for character in line: # numeric values
            calibration += character if character in numeric_values else ""

        calibration_sum += int(calibration[0] + calibration[-1])

    return calibration_sum

# day 1 part 2
def part2(input):
    calibration_sum = 0

    for line in input:
        line = line.lower()

        lowest_number = [99, None]
        highest_number = [-1, None]

        for index, character in enumerate(line): # numeric values
            if character in numeric_values:
                if lowest_number[0] > index:
                    lowest_number = [index, character]

                if highest_number[0] < index:
                    highest_number = [index, character]
        
        for text_value in text_values.keys(): # text values
            curr_line = f"{line}"
            index = curr_line.find(text_value)
            while index != -1:
                if lowest_number[0] > index:
                    lowest_number = [index, text_values[text_value]]

                if highest_number[0] < index:
                    highest_number = [index, text_values[text_value]]

                curr_line = curr_line.replace(text_value, "x" * len(text_value), 1) # replace the found occurence with x's
                index = curr_line.find(text_value)
        
        calibration_sum += int(str(lowest_number[1]) + str(highest_number[1]))

    return calibration_sum

if __name__ == "__main__":
    result1 = part1(input)
    print(f"[1.1] Sum of all calibration values: {result1}")

    result2 = part2(input)
    print(f"[1.2] Sum of all calibration values: {result2}")

    sys.exit()


