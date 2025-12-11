import sys
import pyperclip
# import z3
# import networkx as nx
sys.path.append('../AoC_Helpers')
from InputParser import InputParser
# from Grid import Directions, Grid
# from TupleOps import TupleOps
# from Graph import Graph
from functools import lru_cache
# from collections import defaultdict

wires = {}

def count_paths(node):
    if node == "out":
        return 1
    total = 0
    for next in wires[node]:
        total += count_paths(next)
    return total

@lru_cache(maxsize=1000)
def count_paths2(node, visited):
    if node == "out":
        if (all(visited)):
            return 1
        else:
            return 0
    visited = list(visited)
    if node == "fft":
        visited[0] = True
    if node == "dac":
        visited[1] = True
    visited = tuple(visited)
    total = 0
    for next in wires[node]:
        total += count_paths2(next, visited)
    return total

def run(filename: str, part1: bool):
    data = InputParser(open(filename).read()).readLines().split().getData()
    global wires
    wires = {x[0][0:-1]: tuple(x[1:]) for x in data}
    # print(data)
    if part1:
        return count_paths("you")
    else:
        return count_paths2("svr", (False, False))


if __name__ == "__main__" :
    if len(sys.argv) < 3:
        print("Error, requires two command lines arguments: s/i 1/2")
        exit()
    if sys.argv[2] != '1' and sys.argv[2] != '2':
        print("Error invalid command line args:", sys.argv[1], sys.argv[2])
        exit()

    filename = ""
    if sys.argv[1] == 's':
        if(sys.argv[2] == "1"):
            filename = "sample.txt"
        else:
            filename = "sample2.txt"
    elif sys.argv[1] == 'i':
        filename = "input.txt"
    else:
        filename = sys.argv[1]

    part1 = (sys.argv[2] == '1')
    result = run(filename, part1)
    print(result)
    pyperclip.copy(str(result))
    