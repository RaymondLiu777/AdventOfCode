import sys
import pyperclip
# import z3
# import networkx as nx
sys.path.append('../AoC_Helpers')
from InputParser import InputParser
from Grid import Directions, Grid
from TupleOps import TupleOps
# from Graph import Graph
# from functools import cache
# from collections import defaultdict


def run(filename: str, part1: bool):
    data = InputParser(open(filename).read()).readGrid().getData()
    grid = Grid(data)
    total = 0
    while True:
        movable = []
        # Check for movable items
        for location in grid:
            if(grid.Get(location) != "@"):
                continue
            count = 0
            for offset in Directions.ALL.values():
                adjacent = TupleOps.Add(location, offset)
                if(grid.InGrid(adjacent) and grid.Get(adjacent) == "@"):
                    count += 1
            if(count < 4):
                movable.append(location)
        # Remove movable items
        for location in movable:
            grid.SetGrid(location, "X")
        total += len(movable)
        if(part1):
            break
        if(len(movable) == 0):
            break
        movable.clear()
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
    