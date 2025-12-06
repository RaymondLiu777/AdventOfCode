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
    if part1:
        return normal_math(filename)
    else:
        return abnormal_math(filename)

def normal_math(filename):
    data = InputParser(open(filename).read()).readLines().split().getData()
    numbers = InputParser(data[0:-1]).cast(int).getData()
    operations = data[-1]
    total = 0
    for idx, op in enumerate(operations):
        col_total = 0 if op == "+" else 1
        for line in numbers:
            if(op == "+"):
                col_total += line[idx]
            elif(op == "*"):
                col_total *= line[idx]
        total += col_total
    print(numbers, operations)
    return total

def abnormal_math(filename):
    data = InputParser(open(filename).read()).readLines().getData()
    number_lines = data[0:-1]
    operation_line = data[-1]

    # Parse out offsets from the operations
    spacing = []
    operations = []
    start = 0
    for idx, char in enumerate(operation_line):
        if(char == "*" or char == "+"):
            operations.append(char)
            spacing.append(idx - start - 1)
            start = idx
    spacing = spacing[1:]
    longest_line = max(map(len, number_lines))
    spacing.append(longest_line - start)
    print(operations, spacing)

    # Parse out numbers using offsets
    numbers = []
    for line in number_lines:
        number_row = []
        for offset in spacing:
            number_row.append(line[0:offset])
            line = line[offset + 1:]
        numbers.append(number_row)
    print(numbers)
   
    # Do math
    total = 0
    for idx, op in enumerate(operations):
        col_total = 0 if op == "+" else 1
        for col in range(spacing[idx]):
            number = 0
            for line in numbers:
                if(line[idx][col] != " "):
                    number = number * 10 + int(line[idx][col])
            if(op == "+"):
                col_total += number
            elif(op == "*"):
                col_total *= number
        total += col_total
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
    