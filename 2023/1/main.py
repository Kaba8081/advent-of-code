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

calibration_sum = 0

numeric_values = "1,2,3,4,5,6,7,8,9,0".split(",")
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
    "zero": 0
}

for line in test_input2:
    curr_line = line
    print(curr_line)
    calibration = ""

    for character in curr_line: # numeric values
        calibration += character if character in numeric_values else ""

    for text_value in text_values.keys():
        word = ""
        for char in curr_line:
            word += char
            if len(word) <= 5: # 'eight' is the longest word (5 letters)
                if word == text_value: # check the word for any of the text values
                    calibration += str(text_values[text_value])
                elif char in numeric_values: # check if the char is a number
                    word = "" 
                    calibration += char
                    curr_line = curr_line.replace(char, "", 1)
            else:
                word = word[-1]

    calibration_sum += int(calibration[0] + calibration[-1])

print(f"Sum of all calibration values: {calibration_sum}")


