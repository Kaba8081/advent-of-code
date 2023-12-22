# 'Advent of code' solution for year 2023 day 12
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

def checkResult(result, records) -> bool:
    damaged_records = []
    on_streak = False
    streak = 0

    for value in result:
        if value == "#":
            if not on_streak:
                on_streak = True
                streak = 1
            else:
                on_streak = True
                streak += 1
        else:
            if streak != 0: damaged_records.append(int(streak))
            on_streak = False
            streak = 0
    if streak != 0: damaged_records.append(int(streak))
    
    if records == damaged_records: return True
    else: return False

def part1(input) -> int:
    final_sum = 0

    for line in input:
        line = line.split(" ")

        records = line[1].split(",")
        records = [int(value) for value in records]

        curr_spring = 0
        curr_index = 0
        for i in range(len(line)):
            temp_line = list(line[0])
            for i, value in enumerate(line[0]):
                if value == "#":
                    curr_spring += 1
                elif value == "?":
                    if curr_spring < records[curr_index]:
                        temp_line[i] = "#"
                        curr_spring += 1

                    elif curr_spring == records[curr_index]:
                        temp_line[i] = "."

                        curr_index += 1
                        curr_spring = 0
                else:
                    if curr_spring == records[curr_index]:
                        curr_index += 1
                    curr_spring = 0
            if checkResult(temp_line, records):
                final_sum += 1
    return final_sum
if __name__ == "__main__":
    input = get_input()
    if not input:
        print("Error! Input file is empty!")
        sys.exit()
                        
    input = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1""".strip().splitlines()
    
    result1 = part1(input)
    print("[12.1] Sum of possible spring arrangements: ", result1)
    
    sys.exit()
