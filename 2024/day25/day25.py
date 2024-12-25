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
    schematics = InputParser(open(filename).read()).readSections().getData()
    lock_sizes = set()
    key_sizes = set()
    for schematic in schematics:
        isLock = True if schematic[0] == "#" * 5 else False
        sizes = []
        # Count from top
        for i in range(5):
            num = 0
            while(num < 5 and schematic[num + 1][i] == ("#" if isLock else ".")):
                num += 1
            sizes.append(num if isLock else 5-num)
        if isLock:
            lock_sizes.add(tuple(sizes))
        else:
            key_sizes.add(tuple(sizes))
    # print(lock_sizes, key_sizes)
    fits = 0
    for lock in lock_sizes:
        for key in key_sizes:
            can_fit = True
            for i in range(5):
                if(lock[i] + key[i] > 5):
                    can_fit = False
            fits += 1 if can_fit else 0
    return fits


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
    