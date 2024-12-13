import sys
import pyperclip
sys.path.append('../AoC_Helpers')
from InputParser import InputParser
# from Grid import Directions, Grid
from TupleOps import TupleOps
# from Graph import Graph
# from functools import cache

from z3 import Int, Solver, sat


def run(filename: str, part1: bool):
    input = InputParser(open(filename).read()).readSections().findNumbers().getData()
    tokens = 0
    for buttonA, buttonB, prize in input:
        if not part1:
            prize = TupleOps.Add(prize, (10000000000000, 10000000000000))
        # print(buttonA, buttonB, prize)
        a = Int('a')
        b = Int('b')
        s = Solver()
        s.add(a >= 0, b >= 0)
        if part1:
            s.add(a <= 100, b <= 100)
        s.add(buttonA[0] * a + buttonB[0] * b == prize[0])
        s.add(buttonA[1] * a + buttonB[1] * b == prize[1])  
        if(s.check() == sat):
            tokens += s.model()[a].as_long() * 3 + s.model()[b].as_long()
    return tokens


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
