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

def rotate_dial(dial: list[int], amount: int) -> int:
    start = dial[50]
    count = 0
    full_rotations = abs(amount) // len(dial)
    rest = abs(amount) % len(dial)

    passed_zero_in_partial = False
    if amount > 0: # Rotate Left
        index = amount % len(dial)

        for step in range(1, rest + 1):
            pos = (start + step) % len(dial)
            if pos == 0:
                passed_zero_in_partial = True
    else: # Rotate right
        index = len(dial) - ((-amount) % len(dial))

        for step in range(1, rest + 1):
            pos = (start - step) % len(dial)
            if pos == 0:
                passed_zero_in_partial = True

    dial[:] = dial[index:] + dial[:index]

    count += full_rotations
    if passed_zero_in_partial:
        count += 1
    elif dial[50] == 0:
        count += 1
    return count

def part_1(i: list[str]):
    dial = [i for i in range(100)]

    count = 0
    for instruction in i:
        direction, amount = instruction[0], int(instruction[1:])

        if direction == "R":
            amount = -amount

        rotate_dial(dial, amount)

        if dial[50] == 0:
            count += 1

    print(f"[P1]: The password is: {count}")

def part_2(i: list[str]):
    dial = [i for i in range(100)]

    count = 0
    for instruction in i:
        direction, amount = instruction[0], int(instruction[1:])

        if direction == "R":
            amount = -amount

        count += rotate_dial(dial, amount)

    print(f"[P2]: The password is: {count}")

if __name__ == "__main__":
    inputs = _get_input()
    if not inputs:
        print("Error! Input file is empty!")
        sys.exit()

    part_1(inputs)
    part_2(inputs)

    sys.exit()
