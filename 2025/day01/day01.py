import sys
import pyperclip
# import z3
# import networkx as nx
sys.path.append('../AoC_Helpers')
from InputParser import InputParser
# from Grid import Directions, Grid
# from TupleOps import TupleOps
# from Graph import Graph
# from functools import cache
# from collections import defaultdict


def run(filename: str, part1: bool):
    data = InputParser(open(filename).read().strip()).readLines().applyToLines(lambda x: (x[0], int(x[1:]))).getData()
    # print(data)
    location = 50
    count = 0
    for direction, amount in data:
        if(direction == "L"):
            amount *= -1
        original_location = location
        location += amount
        if not part1:
            # print(location, location // 100)
            # Check if it when positive or negative
            if location >= 100:
                count += location // 100
                # If location is a perfect multiple of 100, reduce count by one, it will be counted below
                if location % 100 == 0:
                    count -= 1
            if location < 0:
                count += -(location // 100)
                # If location was 0, subtrack the count by one if it goes negative
                if original_location == 0:
                    count -= 1
        location = location % 100
        if location == 0:
            count += 1
        # print(direction + str(amount), location, count)
        print(location)
    return count


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
    