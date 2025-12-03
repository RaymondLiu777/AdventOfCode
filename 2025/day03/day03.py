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
    data = InputParser(open(filename).read()).readLines().getData()
    total = 0
    length = 2 if part1 else 12
    for battery in data:
        start = 0
        voltage = 0
        battery = list(map(int,battery))
        for i in range(length):
            highestV = max(battery[start : len(battery) - (length - 1 - i)])
            bestIndex = battery.index(highestV, start, len(battery) - (length - 1 - i))
            voltage = voltage * 10 + highestV
            start = bestIndex + 1
        total += voltage
        # print(voltage)
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
    