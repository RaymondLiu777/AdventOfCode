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
    shapes = []
    for shape in data[0:-1]:
        shapes.append(list(map(list, shape[1:])))
    present_data = InputParser(data[-1]).format("x", ": ", " ", " ", " ", " ", " ").cast(int).getData()
    presents = []
    for present in present_data:
        presents.append(((present[0], present[1]), tuple(present[2:])))
    # Always fits
    always_fits = 0
    for idx, (size, shapes) in enumerate(presents):
        if(size[0]//3 * size[1]//3 >= sum(shapes)):
            always_fits += 1
            # print(idx, "- always fits")
    return always_fits


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
    