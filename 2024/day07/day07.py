import sys
import pyperclip
sys.path.append('../AoC_Helpers')
from InputParser import InputParser
# from Grid import Directions, Grid
# from TupleOps import TupleOps
# from Graph import Graph


def all_possibilities(goal: int, values: list[int], part1: bool):
    if len(values) == 1:
        return goal == values[0]
    elif(values[0] > goal):
        return False
    else:
        add = all_possibilities(goal, (values[0] + values[1], *values[2:]), part1)
        mul = all_possibilities(goal, (values[0] * values[1], *values[2:]), part1)
        concat = all_possibilities(goal, (int(str(values[0]) + str(values[1])), *values[2:]), part1) if not part1 else False
        return add or mul or concat

def run(filename: str, part1: bool):
    input = InputParser(open(filename).read().strip()).readLines().split(":").modifyData(int, lambda x: x.split()).getData()
    total = 0
    for goal, values in input:
        values = tuple(map(int, values))
        possible = all_possibilities(goal, values, part1)
        if possible:
            total += goal
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
    