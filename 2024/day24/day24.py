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
from collections import defaultdict


def run(filename: str, part1: bool):
    starting_bits, gates = InputParser(open(filename).read()).readSections().getData()
    starting_bits = InputParser(starting_bits).format(": ").cast(lambda x: x, int).getData()
    gates = InputParser(gates).split().getData()
    # print(starting_bits, gates)
    wire_state = defaultdict(lambda: -1)
    for wire, start_value in starting_bits:
        wire_state[wire] = start_value
    gates = set(map(tuple, gates))
    # print(wire_state, gates)
    if(part1):
        while(len(gates) > 0):
            unfinished = set()
            for gate in gates:
                w1, op, w2, _, out = gate
                if(wire_state[w1] != -1 and wire_state[w2] != -1):
                    w1_state = True if wire_state[w1] == 1 else False
                    w2_state = True if wire_state[w2] == 1 else False
                    if(op == "AND"):
                        out_state = w1_state and w2_state
                    elif(op == "OR"):
                        out_state = w1_state or w2_state
                    elif(op == "XOR"):
                        out_state = (w1_state and not w2_state) or (not w1_state and w2_state)
                    else:
                        raise Exception()
                    wire_state[out] = 1 if out_state else 0
                else:
                    unfinished.add(gate)
            gates = unfinished
        wires = list(sorted(filter(lambda x: x[0][0] == "z", wire_state.items())))
        wires.reverse()
        zNum = 0
        for wire, value in wires:
            zNum *= 2
            zNum += value
        print(wires)
        return zNum
    else:
        # Part2 is more complex, first use the visualizer to get the DOT languague version of the graph
        # Visualize graph in a DOT graph generator
        # Find the carry bit from x00, y00 add set it in c (in "cry")
        # Use this to find problems at different adders and figure out which gates needs to be swap
        swaps = {"abc": "cba", "cba": "abc"}
        gate_map = dict(map(lambda x: (x[0:3], x[4] if x[4] not in swaps else swaps[x[4]]), gates))
        for key, val in list(gate_map.items()):
            gate_map[(key[2], key[1], key[0])] = val
        c = "cry"
        for i in range(1, 45):
            num = str(i) if i >= 10 else "0" + str(i)
            print(num)
            x = "x" + num
            y = "y" + num
            xyAnd = gate_map[(x, "AND", y)]
            xyXor = gate_map[(x, "XOR", y)] #intermediate (i1)
            ciXor = gate_map[(c, "XOR", xyXor)] #Should be z01
            if(ciXor != "z" + num):
                print("Incorrect z output", num)
                raise Exception()
            ciAnd = gate_map[(c, "AND", xyXor)]
            # There should be a OR with ciAND and xyAND for the next carry bit
            if((xyAnd, "OR", ciAnd) not in gate_map):
                print("Error with OR to create next carry")
                raise Exception()
            c = gate_map[(xyAnd, "OR", ciAnd)]
        print("Everything okay")
        return ",".join(sorted(swaps.keys()))
        


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
    