import sys
import pyperclip
sys.path.append('../')
import AoC_helpers
from pyvis.network import Network

def visualize(wires):
    net = Network()
    net.add_nodes(list(wires.keys()))
    for key, connections in wires.items():
        for connection in connections:
            net.add_edge(key, connection)
    net.show("graph.html", notebook=False)

def run(filename: str, part1: bool):
    wires = {}
    for line in open(filename):
        component, connections = line.strip().split(":")
        if(component not in wires):
            wires[component] = []
        for connection in connections.split():
            if(connection not in wires):
                wires[connection] = []
            wires[component].append(connection)
            wires[connection].append(component)
    # Step 1 Visualize
    visualize(wires)
    # Step 2 put the three cuts here
    break_connections = [("pzl", "hfx"), ("bvb", "cmg"), ("jqt", "nvd")]
    for node1, node2 in break_connections:
        wires[node1].remove(node2)
        wires[node2].remove(node1)
    total = 1
    for start in break_connections[0]:
        queue = [start]
        visited = set()
        while(len(queue) > 0):
            node = queue[0]
            queue = queue[1:]
            if(node in visited):
                continue
            visited.add(node)
            for connection in wires[node]:
                queue.append(connection)
        total *= len(visited)
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
    
