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
    data = InputParser(open(filename).read()).readSections().getData()
    ranges = InputParser(data[0]).format("-").cast(int).getData()
    ingredients = InputParser(data[1]).applyToLines(int).getData()
    fresh = 0
    ranges.sort()
    if(part1):
        for i in ingredients:
            for start, end in ranges:
                if(start <= i and i <= end):
                    fresh += 1
                    break
    else:
        largest_range = 0
        for start, end in ranges:
            if(largest_range > end):
                continue
            if(start > largest_range):
                largest_range = start - 1
            fresh += end - largest_range
            largest_range = end
    return fresh


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
    