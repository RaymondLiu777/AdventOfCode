import sys
import pyperclip
# import z3
# import networkx as nx
sys.path.append('../AoC_Helpers')
from InputParser import InputParser
from Grid import Directions, Grid
# from TupleOps import TupleOps
# from Graph import Graph
# from functools import cache
# from collections import defaultdict
from collections import Counter


def run(filename: str, part1: bool):
    data = InputParser(open(filename).read()).readGrid().getData()
    grid = Grid(data)
    s_row, s_col = grid.GetLocation("S")
    splits = 0
    cols = Counter()
    cols[s_col] = 1
    for row in range(s_row + 1, grid.rows):
        next_cols = Counter()
        for col, amount in cols.items():
            if(grid.Get((row, col)) == "^"):
                next_cols[col-1] += amount
                next_cols[col+1] += amount
                splits += 1
            else:
                next_cols[col] += amount
        cols = next_cols
    return splits if part1 else cols.total()


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
    