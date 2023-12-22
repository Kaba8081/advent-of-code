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

def part1(input) -> int:
    result = 0

    for mirror in input.split("\n\n"):
        # check horizontal symmetry
        lines = mirror.splitlines()

        for i in range(1, len(lines)):
            symmetric = True
            for j in range(min(i, len(lines)-i)):
                if lines[i-1 - j] == lines[i + j]: continue #print(i, j, "".join(lines[i-1 - j]), " <====> ", "".join(lines[i + j]))
                else:
                    symmetric = False
                    break
            if symmetric: 
                result += i*100
                #print("Horizontal symmetry at row: ", i, f"({i*100})", "\n", mirror)
            
        # check vertical symmetry
        vert_lines = [[row[i] for row in lines] for i in range(len(lines[0]))]
        
        for i in range(1, len(vert_lines)):

            symmetric = True
            for j in range(min(i, len(vert_lines)-i)):
                if vert_lines[i-1 - j] == vert_lines[i + j]: continue #print(i, j, "".join(vert_lines[i-1 - j]), " <====> ", "".join(vert_lines[i + j]))
                else:
                    symmetric = False
                    #print(i, j, "".join(vert_lines[i-1 - j]), " <=//=> ", "".join(vert_lines[i + j]), "!")
                    break
            if symmetric: 
                #print("Vertical symmetry at col: ", i, f"({i})", "\n", mirror)
                result += i

    return result

if __name__ == "__main__":
    input = get_input()
    if not input:
        print("Error! Input file is empty!")
        sys.exit()
    
    result1 = part1(input)
    print("[13.1] Sum of all mirror pattern notes: ", result1)

    sys.exit()
