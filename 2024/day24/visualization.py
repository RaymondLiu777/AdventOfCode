import networkx as nx 
import matplotlib.pyplot as plt 
import sys

sys.path.append('../AoC_Helpers')
from InputParser import InputParser

filename = "input.txt"
starting_bits, gates = InputParser(open(filename).read()).readSections().getData()
starting_bits = InputParser(starting_bits).format(": ").cast(lambda x: x, int).getData()
gates = InputParser(gates).split().getData()
print("digraph G {")
for gate in gates:
    w1, op, w2, _, out = gate
    print("  " + w1 + " -> " + w1 + op + w2)
    print("  " + w2 + " -> " + w1 + op + w2)
    print("  " + w1 + op + w2 + " -> " + out)
print("}")

# z10, kmb, fsh, qts