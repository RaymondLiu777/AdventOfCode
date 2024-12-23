import sys
import pyperclip
sys.path.append('../AoC_Helpers')
from InputParser import InputParser
# from Grid import Directions, Grid
# from TupleOps import TupleOps
from Graph import Graph
# from functools import cache
import networkx as nx

def get3Groups(network: Graph):
    groups = set()
    all_nodes = network.graph.keys()
    for node1 in all_nodes:
        for node2 in network.getVertex(node1):
            if(node1 == node2):
                continue
            for node3 in network.getVertex(node2):
                if node3 == node2 or node3 == node1 or node2 == node1:
                    continue
                if network.hasEdge(node1, node2) and network.hasEdge(node1, node3) and network.hasEdge(node2, node3):
                    groups.add(tuple(sorted((node1, node2, node3))))
    return groups

def getLargestGroup(network: Graph):
    network = nx.Graph(network.graph)
    largest = nx.max_weight_clique(network, None)
    return largest[0]


def run(filename: str, part1: bool):
    input = InputParser(open(filename).read()).readLines().format("-").getData()
    network = Graph()
    for node1, node2 in input:
        network.addEdge(node1, node2)
    if(part1):
        groups = get3Groups(network)
        # print(groups)
        print(len(groups))
        count = 0
        for node1, node2, node3 in groups:
            # print(node1, node2, node3)
            if "t" == node1[0] or "t" == node2[0] or "t" == node3[0]:
                count += 1
        return count
    else:
        lanParty = getLargestGroup(network)
        return ",".join(sorted(lanParty))

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
    