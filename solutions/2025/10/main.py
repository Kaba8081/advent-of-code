# 'Advent of code' solution for year 2025 day 10
import os
import sys
from itertools import product
from ortools.sat.python import cp_model

DIR_PATH = os.path.dirname(os.path.realpath(__file__))

# pylint: disable=consider-using-enumerate

def _get_input():
    content = None
    if os.path.isfile(os.path.join(DIR_PATH, "input.txt")):
        with open(os.path.join(DIR_PATH, "input.txt"), "r", encoding="utf-8") as file:
            content = file.read().strip().splitlines()
        return content
    else:
        print("Error! Input file does not exist!")
        sys.exit()

def interpret_input(i: list[str]) -> list[tuple[str, list[tuple[int]], list[int]]]:
    new_input = []
    for line in i:
        line = line.split(" ")

        lights = line[0][1:-1]

        req = line[-1][1:-1].split(",")
        req = [int(v) for v in req]

        str_moves = line[1:-1]
        moves = []
        for v in str_moves:
            new_v = v[1:-1].split(",")
            moves.append(tuple(int(value) for value in new_v))

        new_input.append((lights, moves, req))
    return new_input

def part_1(str_i: list[str]):
    i = interpret_input(str_i)
    result = 0

    for line in i:
        lights = line[0]
        lights = [1 if i=="#" else 0 for i in lights]
        moves = line[1]

        # rows stored as a integer bitmasks
        a_mtrx = [0]*len(lights)
        for j, move in enumerate(moves):
            for i in move:
                a_mtrx[i] ^= (1 << j)

        d = []
        for i in range(len(lights)):
            d.append((False ^ bool(lights[i])) & 1)

        rows = [ [a_mtrx[i], d[i]] for i in range(len(lights))]

        where = [-1]*len(moves)
        row_ptr = 0

        for col in range(len(moves)):
            sel = -1
            for r in range(row_ptr, len(lights)):
                if (rows[r][0] >> col) & 1:
                    sel = r
                    break
            if sel == -1:
                continue

            rows[row_ptr], rows[sel] = rows[sel], rows[row_ptr]
            where[col] = row_ptr
            pivot_mask, pivot_rhs = rows[row_ptr]

            for r in range(len(lights)):
                if r != row_ptr and ((rows[r][0] >> col) & 1):
                    rows[r][0] ^= pivot_mask
                    rows[r][1] ^= pivot_rhs
            row_ptr += 1
            if row_ptr >= len(lights):
                break

        # check if valid
        for r in range(row_ptr, len(lights)):
            if rows[r][0] == 0 and rows[r][1] == 1:
                print("NOT VALID")
                print(lights, moves, rows)
                return

        free_vars = [c for c,v in enumerate(where) if v == -1]

        best_weight = float("inf")
        for bits in product((0,1), repeat=len(free_vars)):
            x = [0]*len(moves)

            for idx, val in enumerate(bits):
                x[ free_vars[idx] ] = val

            for col in range(len(moves)):
                v = where[col]
                if v != -1:
                    mask, rhs = rows[v][0], rows[v][1]
                    s = rhs
                    m = mask & ~(1 << col)
                    while m:
                        lowbit = m & -m
                        j = lowbit.bit_length() - 1
                        s ^= x[j]
                        m ^= lowbit
                    x[col] = s

            weight = sum(x)
            if weight < best_weight:
                best_weight = weight

        result += best_weight
    print(f"[P1] Fewest button presses {result}")

def part_2(str_i: list[str]):
    i = interpret_input(str_i)
    result = 0

    for line in i:
        lights = line[0]
        lights = [1 if i=="#" else 0 for i in lights]
        moves = []
        for move in line[1]:
            tmp = []
            for i in range(len(lights)):
                if i in move:
                    tmp.append(1)
                else:
                    tmp.append(0)
            moves.append(tmp)

        required = line[2]

        model = cp_model.CpModel()
        x = [model.NewIntVar(0, 1000, f'x{i}') for i in range(len(moves))]

        for j in range(len(lights)):
            model.Add(sum(x[i]*moves[i][j] for i in range(len(moves))) == required[j])

        model.Minimize(sum(x))

        solver = cp_model.CpSolver()
        status = solver.Solve(model)

        if status == cp_model.OPTIMAL:
            solution = [solver.Value(var) for var in x]
            result += sum(solution)
        else:
            print(f"Something went wrong when solving:\n{moves}\n{required}")

    print(f"[P2] Fewest button presses {result}")

if __name__ == "__main__":
    inputs = _get_input()
    if not inputs:
        print("Error! Input file is empty!")
        sys.exit()

    part_1(inputs)
    part_2(inputs)

    sys.exit()
