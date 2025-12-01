# 'Advent of code' solution for year 2024 day 7
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

def recursive_equation(equation: list[int], prev_step: int, i: int, ops: list) -> list[int]:
    """Recursively test all possible equations"""

    if i+1 == len(equation):
        return [
            prev_step+equation[i],
            prev_step*equation[i],
            int(str(prev_step) + str(equation[i]))
            ]
    else:
        result = []
        for op in ops:
            result.extend(recursive_equation(equation, op(prev_step, equation[i]), i+1, ops))

        return result

def check_result(lines: list[str], ops: list) -> int:
    """Return the sum of all possible equations"""
    result_sum = 0

    for line in lines:
        line = line.split(": ")

        _eqResult = int(line[0])
        _equation = list(map(int, line[1].split(" ")))
        _eqVariants = recursive_equation(_equation, _equation[0], 1, ops)

        if any([_eqResult == result for result in _eqVariants]):
            result_sum += _eqResult

    return result_sum

if __name__ == "__main__":
    input = get_input()
    if not input:
        print("Error! Input file is empty!")
        sys.exit()

    ops = [lambda x, y: x+y, lambda x, y: x*y]
    result1 = check_result(input, ops)
    print(f"Part 1 solution: {result1}")

    ops = [lambda x, y: x+y, lambda x, y: x*y, lambda x, y: int(str(x) + str(y))]
    result2 = check_result(input, ops)
    print(f"Part 2 solution: {result2}")

    sys.exit()
