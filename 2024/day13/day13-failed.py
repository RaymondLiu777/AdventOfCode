import sys
import pyperclip
sys.path.append('../AoC_Helpers')
from InputParser import InputParser
# from Grid import Directions, Grid
from TupleOps import TupleOps
# from Graph import Graph
# from functools import cache

import scipy.optimize

def run(filename: str, part1: bool):
    input = InputParser(open(filename).read()).readSections().getData()
    tokens = 0
    for section in input:
        buttonA = tuple(map(int, InputParser.parseLine(section[0], "Button A: X+", ", Y+")))
        buttonB = tuple(map(int, InputParser.parseLine(section[1], "Button B: X+", ", Y+")))
        prize = tuple(map(int, InputParser.parseLine(section[2], "Prize: X=", ", Y=")))
        if not part1:
            prize = TupleOps.Add(prize, (10000000000000, 10000000000000))
        # print(buttonA, buttonB, prize)
        c = [3, 1]
        a_eq = [[buttonA[0], buttonB[0]], [buttonA[1], buttonB[1]]]
        b_eq = [prize[0], prize[1]]
        x0_bounds = (0, 100) if part1 else (0, None)
        x1_bounds = (0, 100) if part1 else (0, None)
        res = scipy.optimize.linprog(
            c, A_eq=a_eq, b_eq=b_eq, bounds=(x0_bounds, x1_bounds),
            integrality=[1, 1])
        # print(res)
        if(res.success):
            tokens += res.x[0] * 3 + res.x[1]
            # print(res.x)
        # print(res.x, res.success)
        if(res.status != 0 and res.status != 2):
            print(res.status)
        # return
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

