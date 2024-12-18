import sys
import pyperclip
sys.path.append('../AoC_Helpers')
from InputParser import InputParser
from Grid import Directions, Grid
from TupleOps import TupleOps
# from Graph import Graph
# from functools import cache

def findPath(corrupted, sample):
    start = (0, 0)
    queue = [start]
    size = (7, 7) if sample else (71, 71)
    goal = TupleOps.Add(size, (-1, -1))
    visited = set()
    prev = {}
    foundPath = False
    while len(queue) > 0:
        top = queue[0]
        queue = queue[1:]
        if(top in visited):
            continue
        visited.add(top)
        if top == goal:
            foundPath = True
            break
        for direction in Directions.CARDINAL.values():
            next_spot = TupleOps.Add(top, direction)
            if(next_spot[0] < 0 or next_spot[1] < 0 or next_spot[0] >= size[0] or next_spot[1] >= size[1]):
                continue
            if(next_spot in corrupted):
                continue
            if(next_spot in prev.keys()):
                continue
            prev[next_spot] = top
            queue.append(next_spot)
    if(foundPath == False):
        return set()
    location = goal
    path = [goal]
    while(location != start):
        location = prev[location]
        path.append(location)
    return set(path)

def run(filename: str, part1: bool, sample: bool):
    input = InputParser(open(filename).read()).readLines().findNumbers().getData()
    if(part1):
        return len(findPath(set(input[0:12]) if sample else set(input[0:1024]), sample)) - 1
    # Part 2
    i = 0
    while(True):
        # Add a tile that might block the path
        i += 1
        path = findPath(set(input[0:i]), sample)
        if(len(path) == 0):
            return ','.join(map(str,input[i - 1]))
        # Don't run pathfinding again if old path is valid
        while input[i] not in path:
            i += 1 
       
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
    result = run(filename, part1, filename.find("sample") != -1)
    print(result)
    pyperclip.copy(str(result))
    