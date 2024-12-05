import sys
import pyperclip
sys.path.append('../')
from AoC_helpers import InputParser

def bfs(vertices, node):
    reachable = set()
    queue = [node]
    while len(queue) > 0:
        vertex = queue[0]
        queue = queue[1:]
        if(vertex in reachable):
            continue
        reachable.add(vertex)
        for outgoing in vertices[vertex]["out"]:
            queue.append(outgoing)
    return reachable

def valid(vertices, page_line):
    possible = True
    for i in range(0, len(page_line)):
        for j in range(0, i):
            if page_line[j] in vertices[page_line[i]]["out"]:
                return (False, (i, j))
    return (True,(0,0))

def order_page(vertices, page_line):
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
                if(vertex in vertices[vertex2]["out"]):
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
    vertices = {}
    for first, second in ordering:
        if first not in vertices.keys():
            vertices[first] = {
                "in": set(),
                "out": set()
            }
        if second not in vertices.keys():
            vertices[second] = {
                "in": set(),
                "out": set()
            }
        vertices[first]["out"].add(second)
        vertices[second]["in"].add(first)
    # print(vertices)
    # Create reachable vector
    reachable = {}
    for vertex in vertices.keys():
        reachable[vertex] = bfs(vertices, vertex)
        # print(vertex, reachable[vertex])
    total = 0
    for page_line in pages:
        in_order, error = valid(vertices, page_line)
        # print(page_line, in_order)
        if in_order and part1:
            total += page_line[len(page_line)//2]
        elif not in_order and not part1:
            total += order_page(vertices, page_line)

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
    


    # queue = []
    # for vertex, info in vertices.items():
    #     info["count"] = len(info["out"])
    #     if(len(info["out"]) == 0):
    #         queue.append(vertex)
    # print(queue)
    # visited = {}
    # while len(queue) != 0:
    #     vertex = queue[0]
    #     queue = queue[1:]
    #     if vertex in visited:
    #         continue
    #     for from_vertex in vertices[vertex]["in"]: