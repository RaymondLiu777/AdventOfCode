import sys
import pyperclip
sys.path.append('../AoC_Helpers')
from InputParser import InputParser
import re
from Grid import Directions, Grid
from TupleOps import TupleOps
# from Graph import Graph
from functools import cache

direction_to_symbol = {
    Directions.N: "^",
    Directions.S: "v",
    Directions.W: "<",
    Directions.E: ">"
}

numpad = {
    "9": (0, 2),
    "8": (0, 1),
    "7": (0, 0),
    "6": (1, 2),
    "5": (1, 1),
    "4": (1, 0),
    "3": (2, 2),
    "2": (2, 1),
    "1": (2, 0),
    "0": (3, 1),
    "A": (3, 2)
}

arrowPad = {
    "A": (0, 2),
    "^": (0, 1),
    "<": (1, 0),
    "v": (1, 1),
    ">": (1, 2) 
}

# Probably a bit excessive
def dfs(current:tuple[int], end:tuple[int], locations, path:str, possible_paths: list):
    if(current == end):
        possible_paths.append(path + "A")
        return
    start_distance = abs(end[1] - current[1]) + abs(end[0] - current[0])
    for direction in Directions.CARDINAL.values():
        next_spot = TupleOps.Add(direction, current)
        if(next_spot not in locations):
            continue
        next_distance = abs(end[1] - next_spot[1]) + abs(end[0] - next_spot[0])
        if next_distance >= start_distance:
            continue
        dfs(next_spot, end, locations, path + direction_to_symbol[direction], possible_paths)

def generateKeypadPath(input:str):
    location = numpad["A"]
    output = [""]
    for button in input:
        destination = numpad[button]
        possibilities = []
        dfs(location, destination, numpad.values(), "", possibilities)
        new_output = []
        for start_path in output:
            for end_path in possibilities:
                new_output.append(start_path + end_path)
        output = new_output
        location = destination
    # print(output)
    return output

def generateArrowPath(input:str):
    location = arrowPad["A"]
    output = [""]
    for button in input:
        destination = arrowPad[button]
        possibilities = []
        dfs(location, destination, arrowPad.values(), "", possibilities)
        new_output = []
        for start_path in output:
            for end_path in possibilities:
                new_output.append(start_path + end_path)
        output = new_output
        location = destination
    return output

@cache
def countShortestPath(input:str, depth:int):
    # print(input, depth)
    if depth == 0:
        return len(input)
    total_size = 0
    start = arrowPad["A"]
    for i in range(len(input)):
        end = arrowPad[input[i]]
        possibilities = []
        dfs(start, end, arrowPad.values(), "", possibilities)
        shortest = -1
        for path in possibilities:
            length = countShortestPath(path, depth - 1)
            if(shortest == -1):
                shortest = length
            shortest = min(shortest, length)
        total_size += shortest
        start = end
    return total_size

def run(filename: str, part1: bool):
    code = InputParser(open(filename).read()).readLines().getData()
    total = 0

    for line in code:
        print(line)

        prefix = int(re.findall(r"-?\d+", line)[0])
        # Figure out possible keypad paths
        paths = set(generateKeypadPath(line))

        # Old part1
        #     # Figure out possible arrow pad paths
        #     for i in range(2):
        #         # print(i)
        #         arrowPadPaths = set()
        #         for path in paths:
        #             arrowPadPaths.update(generateArrowPath(path))
        #         # Prune out longer paths
        #         shortest = -1
        #         for path in arrowPadPaths:
        #             if(shortest == -1):
        #                 shortest = len(path)
        #             shortest = min(len(path), shortest)
        #         paths = set(filter(lambda x: len(x) == shortest, arrowPadPaths))
            
        #     # Find shortest path
        #     shortest = len(paths.pop())
        #     for path in paths:
        #         shortest = min(len(path), shortest)
        #     total += prefix * shortest

        shortest = -1
        for path in paths:
            length = countShortestPath(path, 2 if part1 else 25)
            if(shortest == -1):
                shortest = length
            shortest = min(shortest, length)

        # print(shortest)
        total += prefix * shortest
    return total


if __name__ == "__main__" :
    if len(sys.argv) < 3:
        print("Error, requires two command lines arguments: s/i 1/2")
        exit()
    if sys.argv[2] != '1' and sys.argv[2] != '2':
        print("Error invalid command line args:", sys.argv[1], sys.argv[2])
        exit()

    filename = ""
    if sys.argv[1] == 's':
        filename = "sample.txt"
    elif sys.argv[1] == 'i':
        filename = "input.txt"
    else:
        filename = sys.argv[1]

    part1 = (sys.argv[2] == '1')
    result = run(filename, part1)
    print(result)
    pyperclip.copy(str(result))


#     direction_to_symbol = {
#     Directions.N: "^",
#     Directions.S: "v",
#     Directions.W: "<",
#     Directions.E: ">"
# }

# def dfs(current:tuple[int], end:tuple[int], locations, path:str, possible_paths: list):
#     if(current == end):
#         possible_paths.append(path + "A")
#         return
#     start_distance = abs(end[1] - current[1]) + abs(end[0] - current[0])
#     for direction in Directions.CARDINAL.values():
#         next_spot = TupleOps.Add(direction, current)
#         if(next_spot not in locations):
#             continue
#         next_distance = abs(end[1] - next_spot[1]) + abs(end[0] - next_spot[0])
#         if next_distance >= start_distance:
#             continue
#         dfs(next_spot, end, locations, path + direction_to_symbol[direction], possible_paths)

# def generateKeypadPath(input:str):
#     numpad = {
#         "9": (0, 2),
#         "8": (0, 1),
#         "7": (0, 0),
#         "6": (1, 2),
#         "5": (1, 1),
#         "4": (1, 0),
#         "3": (2, 2),
#         "2": (2, 1),
#         "1": (2, 0),
#         "0": (3, 1),
#         "A": (3, 2)
#     }
#     location = numpad["A"]
#     output = ""
#     for button in input:
#         destination = numpad[button]
#         horizontal_movement = destination[1] - location[1]
#         vertical_movement = destination[0] - location[0]
#         # Prefer going right first
#         if horizontal_movement > 0:
#             output += ">" * horizontal_movement
#         # Prefer going left if not at bottom row
#         if(location != numpad["A"] and location != numpad["0"] and horizontal_movement < 0):
#             output += "<" * -horizontal_movement
#             horizontal_movement = 0
#         # Prefer going up/down after right but before left
#         if vertical_movement < 0:
#             output += "^" * -vertical_movement
#         elif vertical_movement > 0:
#             output += "v" * vertical_movement
#         # Left has least priority
#         if horizontal_movement < 0:
#             output += "<" * -horizontal_movement
#         # Add A button press
#         output += "A"
#         # possibilities = []
#         # dfs(location, destination, locations.values(), "", possibilities)
#         # output.append(possibilities)
#         location = destination
#     print(output)
#     return output

# def generateArrowPath(input:str):
#     arrowPad = {
#         "A": (0, 2),
#         "^": (0, 1),
#         "<": (1, 0),
#         "v": (1, 1),
#         ">": (1, 2) 
#     }
#     location = arrowPad["A"]
#     output = ""
#     for button in input:
#         destination = arrowPad[button]
#         # Handle getting out of < without going up
#         if(location == arrowPad["<"] and location != destination):
#             output += ">"
#             location = arrowPad["v"]

#         horizontal_movement = destination[1] - location[1]
#         vertical_movement = destination[0] - location[0]
#         # Prefer going right first
#         if horizontal_movement > 0:
#             output += ">" * horizontal_movement
#         # Prefer going up/down after right but before left
#         if vertical_movement < 0:
#             output += "^" * -vertical_movement
#         elif vertical_movement > 0:
#             output += "v" * vertical_movement
#         # Left has least priority
#         if horizontal_movement < 0:
#             output += "<" * -horizontal_movement
#         # Add A button press
#         output += "A"
#         location = destination
#     print(output)
#     return output

# def run(filename: str, part1: bool):
#     code = InputParser(open(filename).read()).readLines().getData()
#     total = 0

#     for line in code:
#         prefix = int(re.findall(r"-?\d+", line)[0])
#         keypadPath = generateKeypadPath(line)
#         arrowPadPath = generateArrowPath(keypadPath)
#         arrowPadPath2 = generateArrowPath(arrowPadPath)
#         total += prefix * len(arrowPadPath2)

#     return total