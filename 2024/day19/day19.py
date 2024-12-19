import sys
import pyperclip
sys.path.append('../AoC_Helpers')
from InputParser import InputParser
# from Grid import Directions, Grid
# from TupleOps import TupleOps
# from Graph import Graph
from functools import cache

towels = set()

@cache
def makeTowel(pattern):
    if(pattern == ""):
        return 1
    possibilities = 0
    for towel in towels:
        if towel == pattern[0:len(towel)]:
            possibilities += makeTowel(pattern[len(towel):])
    return possibilities

def run(filename: str, part1: bool):
    global towels
    towels, patterns = InputParser(open(filename).read()).readSections().getData()
    towels = set(towels[0].split(", "))
    # print(towels, patterns)
    possibilities = 0
    for pattern in patterns:
        if part1:
            if(makeTowel(pattern) != 0):
                possibilities += 1
        else:
            possibilities += makeTowel(pattern)
    return possibilities


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
    