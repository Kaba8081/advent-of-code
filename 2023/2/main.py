# 'Advent of code' solution for year 2023 day 2
import os
import sys
     
dir_path = os.path.dirname(os.path.realpath(__file__))
input = None

with open(os.path.join(dir_path, "input.txt"), "r") as file:    
    input = file.read().strip().splitlines()
if not input:
    print("Error! Input file is empty!")
    sys.exit()

test_input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""".strip().splitlines()

def part1(input):
    id_sum = 0
    games_dict = {}
    max_possible = {"r":12, "g":13, "b":14}

    for line in input:
        line = line.split(":")
        line[1] = line[1][1:] # remove space at the beginning
        game_id = int(line[0].split(" ")[1])
        rgb_value = [0,0,0] # max shown value of each color

        game_subset = line[1].split("; ")
        for subset in game_subset:
            subset = subset.split(", ")

            for value in subset:
                value = value.split(" ")
                if value[1] == "red" and rgb_value[0] < int(value[0]):
                    rgb_value[0] = int(value[0])
                elif value[1] == "green" and rgb_value[1] < int(value[0]):
                    rgb_value[1] = int(value[0])
                elif value[1] == "blue" and rgb_value[2] < int(value[0]):
                    rgb_value[2] = int(value[0])

        games_dict[game_id] = {"r":rgb_value[0], "g":rgb_value[1], "b":rgb_value[2]} 

    for game_id in games_dict.keys():
        if games_dict[game_id]["r"] > max_possible["r"]:
            continue
        if games_dict[game_id]["g"] > max_possible["g"]:
            continue
        if games_dict[game_id]["b"] > max_possible["b"]:
            continue

        id_sum += game_id

    return id_sum

def part2(input):
    power_sum = 0
    games_dict = {}

    for line in input:
        line = line.split(":")
        line[1] = line[1][1:] # remove space at the beginning
        game_id = int(line[0].split(" ")[1])
        rgb_value = [0,0,0] # max shown value of each color

        game_subset = line[1].split("; ")
        for subset in game_subset:
            subset = subset.split(", ")

            for value in subset:
                value = value.split(" ")
                if value[1] == "red" and rgb_value[0] < int(value[0]):
                    rgb_value[0] = int(value[0])
                elif value[1] == "green" and rgb_value[1] < int(value[0]):
                    rgb_value[1] = int(value[0])
                elif value[1] == "blue" and rgb_value[2] < int(value[0]):
                    rgb_value[2] = int(value[0])

        games_dict[game_id] = {"r":rgb_value[0], "g":rgb_value[1], "b":rgb_value[2]} 

    for game_id in games_dict.keys():
        temp_sum = games_dict[game_id]['r']
        temp_sum *= games_dict[game_id]['g']
        temp_sum *= games_dict[game_id]['b']

        power_sum += temp_sum

    return power_sum

if __name__ == "__main__":
    result1 = part1(input)
    print(f"[1.1] Sum of all possible games ID's: {result1}")
    result2 = part2(input)
    print(f"[1.2] Sum of the power of the games: {result2}")

    sys.exit()