import sys
import pyperclip
sys.path.append('../AoC_Helpers')
from InputParser import InputParser
from Grid import Directions, Grid
from TupleOps import TupleOps
# from Graph import Graph
# from functools import cache

def bfs(location, locations, cheat_distance):
    # print("Start")
    queue = [(location, cheat_distance)]
    while len(queue) > 0:
        location, distance_left = queue[0]
        # print(location, distance_left)
        queue = queue[1:]
        if(location in locations):
            continue
        if(distance_left < 0):
            continue
        locations.add(location)
        for direction in Directions.CARDINAL.values():
            queue.append((TupleOps.Add(location, direction), distance_left - 1))

def cheats(location, path, cheat_distance):
    skip_distance = 100
    possible_locations = set()
    bfs(location, possible_locations, cheat_distance)
    skips = set()
    for skip in possible_locations:
        skip_time =  abs(location[0] - skip[0]) + abs(location[1] - skip[1])
        if(skip in path.keys() and path[skip] >= path[location] + skip_distance + skip_time):
            skips.add(skip)
    return len(skips)

def run(filename: str, part1: bool):
    input = InputParser(open(filename).read()).readGrid().getData()
    grid = Grid(input)
    start = (-1, -1)
    end = (-1, -1)
    for location in grid:
        if(grid.Get(location) == "S"):
            start = location
        if(grid.Get(location) == "E"):
            end = location
    visited = set()
    prev = {}
    queue = [start]
    while len(queue) > 0:
        top = queue[0]
        queue = queue[1:]
        if top in visited:
            continue
        visited.add(top)
        for direction in Directions.CARDINAL.values():
            next_location = TupleOps.Add(top, direction)
            if(grid.Get(next_location) != "#" and next_location not in visited):
                prev[next_location] = top
                queue.append(next_location)
    path = [end]
    temp = end
    while temp != start:
        temp = prev[temp]
        path.append(temp)
    path.reverse()
    path = dict(zip(path, range(len(path))))
    # print(path)
    valid_skips = 0
    
    for location in path.keys():
        valid_skips += cheats(location, path, 2 if part1 else 20)
    return valid_skips


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
    

    # 877365 - going through end
    # 877354 - no going through end
    # 1000685 - no going through end 20
    # 1000697 - 20 going through end