import sys
import pyperclip
sys.path.append('../AoC_Helpers')
from InputParser import InputParser
# from Grid import Directions, Grid
# from TupleOps import TupleOps
# from Graph import Graph
from functools import cache

# Implementation for part 1
def naive_impl(input):
    last_row = input
    next_row = []
    for i in range(25):
        for stone in last_row:
            if(stone == 0):
                next_row.append(1)
            elif(len(str(stone)) % 2 == 1):
                next_row.append(stone*2024)
            else:
                stone_str = str(stone)
                stone_len = len(stone_str)
                next_row.append(int(stone_str[0:stone_len//2]))
                next_row.append(int(stone_str[stone_len//2:]))
        # print(next_row)
        last_row = next_row
        next_row = []
    return len(last_row)

# Implementation for part 2
@cache
def num_stones(stone: int, time_left:int):
    if(time_left == 0):
        return 1
    else:
        if(stone == 0):
            return num_stones(1, time_left - 1)
        elif(len(str(stone)) % 2 == 1):
            return num_stones(stone*2024, time_left-1)
        else:
            stone_str = str(stone)
            stone_len = len(stone_str)
            stone1 = int(stone_str[0:stone_len//2])
            stone2 = int(stone_str[stone_len//2:])
            return num_stones(stone1, time_left-1) + num_stones(stone2, time_left-1)
        
def run(filename: str, part1: bool):
    input = InputParser(open(filename).read()).readLines().split().modifyData(int).getData()[0]
    print (input)
    total_stones = 0
    for stone in input:
        total_stones += num_stones(stone, 25 if part1 else 75)
    return total_stones
    
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

