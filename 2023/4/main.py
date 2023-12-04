# 'Advent of code' solution for year 2022 day 4
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

def check_winnings(win_nums, my_nums):
    result = []

    for number in my_nums:
        if number != '' and number in win_nums:
                result.append(number)
    
    return len(result)

def part1(input):
    points = 0
    my_nums = []
    
    for line in input:
        temp_points = 0
        
        # line[0] - list of winning numbers
        # line[1] - list of scratchcard numbers
        line = line.split('|')
        line[0] = line[0].split(":")[1].split(" ")
        line[1] = line[1].split(" ")

        cards_won = check_winnings(line[0], line[1])

        temp_points = 2 ** (cards_won-1) if cards_won > 0 else 0
        
        points += temp_points

    return points

def part2(input):
    scratchcards = {}

    for line in input:
        card_number = int(line.split(":")[0].split(" ")[-1])

        if card_number in scratchcards.keys():
            scratchcards[card_number] += 1
        else:
            scratchcards[card_number] = 1

        # line[0] - list of winning numbers
        # line[1] - list of scratchcard numbers
        line = line.split('|')
        line[0] = line[0].split(":")[1].split(" ")
        line[1] = line[1].split(" ")

        cards_won = check_winnings(line[0], line[1])
        for num in range(cards_won):
            num = num + 1

            if card_number + num in scratchcards.keys():
                scratchcards[card_number + num] += scratchcards[card_number]
            else:
                scratchcards[card_number + num] = scratchcards[card_number]
        
    return sum(scratchcards.values())

if __name__ == "__main__":
    input = get_input()

#     input = """
# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".strip().splitlines()

    if not input:
        print("Error! Input file is empty!")
        sys.exit()
                        
    # your code goes here

    result1 = part1(input)
    print("[4.1] Total scratchcards points: ", result1)
    result2 = part2(input)
    print("[4.2] Total scratchcards amount: ", result2)

    sys.exit()
