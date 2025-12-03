# 'Advent of code' solution for year {year} day {day}
import os
import sys

DIR_PATH = os.path.dirname(os.path.realpath(__file__))

def _get_input():
    content = None
    if os.path.isfile(os.path.join(DIR_PATH, "input.txt")):
        with open(os.path.join(DIR_PATH, "input.txt"), "r", encoding="utf-8") as file:
            content = file.read().strip().splitlines()
        return content
    else:
        print("Error! Input file does not exist!")
        sys.exit()

def part_1(i: list[str]):
    result = 0

    for bt_pack in i:
        max_num: int = 0
        second_max: int = 0

        for index, batt in enumerate(bt_pack):
            if index != len(bt_pack)-1 and int(batt) > max_num:
                max_num = int(batt)
                second_max = 0
            elif int(batt) > second_max:
                second_max = int(batt)

        result += max_num*10 + second_max

    print(f"[P1]: Sum of all joltages: {result}")

def part_2(i: list[str]):
    result = 0
    required_batts = 12

    for bt_pack in i:
        to_remove = len(bt_pack) - required_batts

        value = ""
        for batt in bt_pack:
            while (to_remove > 0
                    and len(value) > 0
                    and int(value[-1]) < int(batt)):
                to_remove -= 1
                value = value[:-1]

            value += batt

        result += int(value[:12])

    print(f"[P2]: Sum of all joltages: {result}")

if __name__ == "__main__":
    inputs = _get_input()
    if not inputs:
        print("Error! Input file is empty!")
        sys.exit()

    part_1(inputs)
    part_2(inputs)

    sys.exit()
