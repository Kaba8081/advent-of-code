# 'Advent of code' solution for year 2023 day 13
import os
import sys
                        
global DIR_PATH
DIR_PATH = os.path.dirname(os.path.realpath(__file__))

def get_input():
    input = None
    if os.path.isfile(os.path.join(DIR_PATH, "input.txt")):
        with open(os.path.join(DIR_PATH, "input.txt"), "r") as file:    
            input = file.read()
        return input
    else:
        print("Error! Input file does not exist!")
        sys.exit()

#print(i, j, "".join(lines[i-1 - j]), " <====> ", "".join(lines[i + j]))

def part1(input) -> int:
    result = 0

    for mirror in input.split("\n\n"):
        # check horizontal symmetry
        lines = mirror.splitlines()

        for i in range(1, len(lines)):
            symmetric = True

            for j in range(min(i, len(lines)-i)):
                if lines[i-1 - j] == lines[i + j]: continue
                else:
                    symmetric = False
                    break
            if symmetric: 
                result += i*100
            
        # check vertical symmetry
        vert_lines = [[row[i] for row in lines] for i in range(len(lines[0]))]

        for i in range(1, len(vert_lines)):
            symmetric = True

            for j in range(min(i, len(vert_lines)-i)):
                if vert_lines[i-1 - j] == vert_lines[i + j]: continue
                else:
                    symmetric = False
                    break
            if symmetric: 
                result += i

    return result

def checkSymmetry(lines):
    for i in range(1, len(lines)):
        symmetric = True
        smudge_fixed = False

        for j in range(min(i, len(lines)-i)):
            if lines[i-1 - j] == lines[i + j]: continue
            if not smudge_fixed and abs(lines.count("#") - lines.count(".")) == 1:
                smudge_fixed = True
                continue
            else:
                symmetric = False
                break
        if symmetric: 
            return i*100
        
    # check vertical symmetry
    vert_lines = [[row[i] for row in lines] for i in range(len(lines[0]))]

    for i in range(1, len(vert_lines)):
        symmetric = True
        smudge_fixed = False

        for j in range(min(i, len(vert_lines)-i)):
            if vert_lines[i-1 - j] == vert_lines[i + j]: continue
            if not smudge_fixed:
                smudge_fixed = True
                continue
            else:
                symmetric = False
                break
        if symmetric: 
           return i
        
    return 0

def part2(input) -> int:
    result = 0

    for mirror in input.split("\n\n"):
        # check horizontal symmetry
        lines = mirror.splitlines()

        result += checkSymmetry(lines)

    return result

if __name__ == "__main__":
    input = get_input()
    if not input:
        print("Error! Input file is empty!")
        sys.exit()

    input = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""

    result1 = part1(input)
    print("[13.1] Sum of all mirror pattern notes: ", result1)
    result2 = part2(input)
    print("[13.2] Sum of all mirror pattern notes with fixed smuges: ", result2)

    sys.exit()
