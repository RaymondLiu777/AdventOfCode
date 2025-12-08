import sys
import pyperclip
import math
# import z3
# import networkx as nx
sys.path.append('../AoC_Helpers')
from InputParser import InputParser
# from Grid import Directions, Grid
from TupleOps import TupleOps
from Graph import Graph
# from functools import cache
# from collections import defaultdict

# Find all nodes in a group
def node_group(graph: Graph, start: tuple[int]):
    q = [start]
    visited = set()
    while len(q) > 0:
        node = q[0]
        q = q[1:]
        if(node in visited):
            continue
        visited.add(node)
        for neighbor in graph.getVertex(node):
            q.append(neighbor)
    return visited
        

def run(filename: str, part1: bool):
    points = InputParser(open(filename).read()).readLines().split(",").cast(int).getData()
    points = list(map(tuple,points))
    # print(points)

    # Create graph of nodes
    graph = Graph()
    for point in points:
        graph.addVertex(tuple(point))

    # Calculate all distances between points
    distances = []
    for idx, point1 in enumerate(points):
        for point2 in points[idx + 1:]:
            diff = TupleOps.Subtract(point1, point2)
            distance  = math.sqrt(sum(map(lambda x: x**2, diff)))
            distances.append((distance, point1, point2))

    # find shortest distances
    distances.sort()
    if part1:

        # Add edges to the graph
        for distance, point1, point2 in distances[0:10 if filename == "sample.txt" else 1000]:
            graph.addEdge(point1, point2)
        # print(distances)

        # find sizes of groups
        group_sizes = []
        visited = set()
        for vertex in graph.graph.keys():
            if vertex not in visited:
                group = node_group(graph, vertex)
                group_sizes.append(len(group))
                visited.update(group)
        group_sizes.sort(reverse=True)
        # print(group_sizes)

        return group_sizes[0] * group_sizes[1] * group_sizes[2]
    else:
        # Add edges to the graph, keep track of the size of an arbitary group
        group = set()
        group.add(points[0])
        for distance, point1, point2 in distances:
            if(point1 in group and point2 in group):
                graph.addEdge(point1, point2)
                continue

            # If a connect is ever made to the group, update nodes in group
            if(point1 in group):
                group.update(node_group(graph, point2))
            elif (point2 in group):
                group.update(node_group(graph, point1))
            graph.addEdge(point1, point2)
            
            # If the group connects all node, we found the connection
            if(len(group) == len(points)):
                return point1[0] * point2[0]
        return -1


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
    