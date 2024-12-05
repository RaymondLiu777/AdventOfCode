import sys
import pyperclip
sys.path.append('../AoC_Helpers')
from InputParser import InputParser
from Graph import Graph

def valid(graph: Graph, page_line: list[int]):
    for i in range(0, len(page_line)):
        for j in range(0, i):
            if graph.hasEdge(page_line[i], page_line[j]):
                return False
    return True

def order_page(graph: Graph, page_line: list[int]):
    vertex_set = set(page_line)
    order = []
    while len(vertex_set) > 0:
        # Find vertex with nothing going into it
        found_valid = False
        for vertex in vertex_set:
            valid = True
            for vertex2 in vertex_set:
                if(vertex == vertex2):
                    continue
                if(graph.hasEdge(vertex, vertex2)):
                    valid = False
                    break
            if(valid):
                order.append(vertex)
                vertex_set.remove(vertex)
                found_valid = True
                break
        if not found_valid:
            print("Can't find ordering for ", page_line)
            return 0
    # print(page_line, order)
    return order[len(order)//2]


def run(filename: str, part1: bool):
    input = InputParser(open(filename).read().strip()).readSections().getData()
    ordering = InputParser(input[0]).split("|").modifyData(int).getData()
    pages = InputParser(input[1]).split(",").modifyData(int).getData()
    # Build graph
    graph = Graph(directed=True)
    for first, second in ordering:
        graph.addEdge(first, second)
    # graph.print()
    total = 0
    for page_line in pages:
        in_order = valid(graph, page_line)
        # print(page_line, in_order)
        if in_order and part1:
            total += page_line[len(page_line)//2]
        elif not in_order and not part1:
            total += order_page(graph, page_line)
    return total


if __name__ == "__main__" :
    if len(sys.argv) < 3:
        print("Error, requires two command lines arguments: s/i 1/2")
        exit()
    if (sys.argv[1] != 's' and sys.argv[1] != 'i') or (sys.argv[2] != '1' and sys.argv[2] != '2'):
        print("Error invalid command line args:", sys.argv[1], sys.argv[2])
        exit()

    filename = ""
    if sys.argv[1] == 's':
        filename = "sample.txt"
    elif sys.argv[1] == 'i':
        filename = "input.txt"

    part1 = (sys.argv[2] == '1')
    result = run(filename, part1)
    print(result)
    pyperclip.copy(str(result))
