# 'Advent of code' solution for year 2024 day 5
import os
import sys
                        
global DIR_PATH
DIR_PATH = os.path.dirname(os.path.realpath(__file__))

def isUpdateCorrect(page_ordering: list[(int, int)], update: list[int]) -> tuple[bool, list[int]]:
    """Check if the given update is correct
    :param page_ordering: list of dependencies
    :param update: list of pages
    :return: True if the update is correct, False otherwise,
    :return: list of pages in correct order
    """
    _dependencies = {} # page -> dependencies
    _print_order = []
    fixed_update = update.copy()
    isCorrect = True

    for dependency in page_ordering:
        # both pages need to be in the update
        if not dependency[0] in update or not dependency[1] in update:
            continue
        if dependency[1] not in _dependencies:
            _dependencies[dependency[1]] = [dependency[0]]
        elif dependency[0] not in _dependencies[dependency[1]]:
            _dependencies[dependency[1]].append(dependency[0])

    for page in update:
        # page has no dependencies
        if not page in _dependencies.keys():
            _print_order.append(page)
            continue

        # page was rendered before all dependencies
        for dependency in _dependencies[page]:
            if dependency not in _print_order:
                isCorrect = False
                fixed_update.remove(page)
                fixed_update.insert(fixed_update.index(dependency) + 1, page)

        _print_order.append(page)
        
    return isCorrect, fixed_update

def part1(page_ordering: list[(int, int)], updates: list[(int, int)]) -> int:
    """Find all correct udpates and sum the middle pages"""
    page_sum = 0

    for update in updates:
        if isUpdateCorrect(page_ordering, update)[0]:
            _len = len(update)
            page_sum += update[_len // 2]

    return page_sum

def part2(page_ordering: list[(int, int)], updates: list[(int, int)]) -> int:
    """Correct invalid udpates and sum the middle pages"""
    page_sum = 0


    for update in updates:
        correct, fixed = isUpdateCorrect(page_ordering, update)
        if correct:
            continue

        while not correct:
            correct, fixed = isUpdateCorrect(page_ordering, fixed)
        _len = len(fixed)
        page_sum += fixed[_len // 2]

    return page_sum

def get_input():
    input = None
    if os.path.isfile(os.path.join(DIR_PATH, "input.txt")):
        with open(os.path.join(DIR_PATH, "input.txt"), "r") as file:    
            input = file.read().strip().split("\n\n")
        return input
    else:
        print("Error! Input file does not exist!")
        sys.exit()
                        
if __name__ == "__main__":
    input = get_input()
    if not input:
        print("Error! Input file is empty!")
        sys.exit()

    # parse input
    page_ordering = input[0].split("\n")
    page_ordering = [[int(num) for num in dependeny.split("|")] for dependeny in page_ordering]
    updates = input[1].split("\n")
    updates = [[int(num) for num in update.split(",")] for update in updates]
      
    result1 = part1(page_ordering, updates)
    print(f"Part 1: {result1}")
    result2 = part2(page_ordering, updates)
    print(f"Part 2: {result2}")
    
    sys.exit()
