# 'Advent of code' solution for year 2025 day 11
import os
import sys
from functools import lru_cache

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

def interpret_input(i: list[str]) -> dict[str, list[str]]:
    node_dict = {}

    for line in i:
        line = line.split(":")
        node = line[0]
        conns = line[1][1:].split(" ")

        node_dict[node] = conns

    return node_dict

def part_1(str_i: list[str]):
    i = interpret_input(str_i)

    def rec(node: str, traversed_nodes: set) -> int:
        if node in traversed_nodes:
            return 0
        elif node == "out":
            return 1
        
        result = 0
        traversed_nodes.add(node)

        for child_node in i[node]:
            result += rec(child_node, traversed_nodes.copy())
        
        return result

    print(f"[P1]: 'you' -> 'out' Path count: {rec("you", set())}")

def part_2(str_i: list[str]):
    i = interpret_input(str_i)
    i['out'] = []

    @lru_cache(maxsize=None)
    def rec(node: str, counter: int) -> int:
        counter = counter | (node == 'dac') << 1 | (node == 'fft') 

        if node == "out" and counter == 0x3:
            return 1

        return sum([rec(child, counter) for child in i[node]])
    
    result = rec("svr", 0)
    print(f"[P2]: 'svr' -> 'out' Path count: {result}")

if __name__ == "__main__":
    inputs = _get_input()
    if not inputs:
        print("Error! Input file is empty!")
        sys.exit()

    part_1(inputs)
    part_2(inputs)

    sys.exit()
