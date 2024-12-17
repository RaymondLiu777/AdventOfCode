import sys
import pyperclip
sys.path.append('../AoC_Helpers')
from InputParser import InputParser
# from Grid import Directions, Grid
# from TupleOps import TupleOps
# from Graph import Graph
# from functools import cache

def runCode(A, B, C, code):
    ip = 0
    output = []
    while ip < len(code):
        instruction = code[ip]
        # Get combo op
        literal = code[ip+1]
        combo = literal
        if(combo == 4):
            combo = A
        elif(combo == 5):
            combo = B
        elif(combo == 6):
            combo = C
        # elif(combo == 7):
        #     raise Exception("Unknown combo operand")
        # Run instructions
        if(instruction == 0):
            A = A // (2 ** combo)
        elif(instruction == 1):
            B = B ^ literal
        elif(instruction == 2):
            B = combo % 8
        elif(instruction == 3):
            if(A != 0):
                ip = literal
                continue
        elif(instruction == 4):
            B = B ^ C
        elif(instruction == 5):
            # if(combo % 8 != code[len(output)]):
            #     return -1
            output.append(combo % 8)
        elif(instruction == 6):
            B = A // (2 ** combo)
        elif(instruction == 7):
            C = A // (2 ** combo)
        else:
            raise Exception("Unknown operation")
        # print(instruction, literal, A, B, C)
        # input()
        ip += 2
    # if(len(output) != len(code)):
    #     return -1
    return tuple(output)


# Observe that the code takes A, performs some operations to produce a output value and then shifts A by 3 (removing last 3 bits)
# Thus we can build the number by guessing 3 bits at a time, for every three bits we can see if it matches the end of the expected output
# If it does, then these three bits are a possible value for the start of A, so we shift then over by 3 and try guessing 3 more bits
# Use backtracking since there may be dead ends where a number appears generate the start but becomes impossible? <- Not sure if necessary
def backTracking(B, C, code):
    queue = [0]
    visited = set()
    while len(queue) > 0:
        top = queue.pop()
        if(top in visited):
            continue
        visited.add(top)
        # print(top, queue)
        # input()
        new_vals = []
        # Note that we must check the numbers from smallest to biggest (on the chance we find the correct number), 
        # however they are reversed before being appended to the queue so that the smallest numbers are at the "front" of the queue (end of the list)
        for i in range(8):
            new_A = top * 8 + i
            output = runCode(new_A, B, C, code)
            if(output == code):
                return new_A
            if(len(output) > len(code)):
                continue
            if(code[-1 * len(output):] == output):
                new_vals.append(new_A)
        new_vals.reverse()
        queue = queue + new_vals
    return -1



def run(filename: str, part1: bool):
    registers, code = InputParser(open(filename).read()).readSections().findNumbers().getData()
    # print(registers, code)
    A = registers[0][0]
    B = registers[1][0]
    C = registers[2][0]
    code = code[0]
    if(part1):
        output = runCode(A, B, C, code)
        return ','.join(map(str,output))
    else:
        return backTracking(B, C, code)

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
