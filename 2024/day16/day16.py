import sys
import pyperclip
import heapq
from collections import defaultdict
sys.path.append('../AoC_Helpers')
from InputParser import InputParser
from Grid import Directions, Grid
from TupleOps import TupleOps
# from Graph import Graph
# from functools import cache



def run(filename: str, part1: bool):
    input = InputParser(open(filename).read()).readGrid().getData()
    grid = Grid(input)
    previous = defaultdict(lambda: {
                "priority": -1,
                "prev": []
            })
    start = (-1, -1)
    end = (-1, -1)
    for location in grid:
        if(grid.Get(location) == "S"):
            start = location
        if(grid.Get(location) == "E"):
            end = location
    directions = [Directions.N, Directions.E, Directions.S, Directions.W]
    visited = set()
    pq = [(0, start, 1)]
    final_priority = -1
    end_direction = -1
    while len(pq) > 0:
        priority, location, direction_index = heapq.heappop(pq)
        if((location, direction_index) in visited):
            continue
        # print(location, priority, directions[direction_index])
        if(grid.Get(location) == "E"):
            if(final_priority == -1):
                final_priority = priority
                previous[(location, direction_index)]["priority"] = priority
                end_direction = direction_index
            continue
        if(grid.Get(location) == "#"):
            continue
        visited.add((location, direction_index))
        if(previous[(location, direction_index)]["priority"] == -1):
            previous[(location, direction_index)]["priority"] = priority
        else:
            previous[(location, direction_index)]["priority"] = min(priority, previous[(location, direction_index)]["priority"])
        # print(location, priority, directions[direction_index])
        # Go forward
        next_location = TupleOps.Add(location, directions[direction_index])
        previous[(next_location, direction_index)]["prev"].append(((location, direction_index), priority + 1))
        heapq.heappush(pq, (priority + 1, TupleOps.Add(location, directions[direction_index]), direction_index))
        # Turn Left/Right
        right = (direction_index + 1) % 4
        previous[(location, right)]["prev"].append(((location, direction_index), priority + 1000))
        heapq.heappush(pq, (priority + 1000, location, right))
        left = (direction_index - 1) % 4
        previous[(location, left)]["prev"].append(((location, direction_index), priority + 1000))
        heapq.heappush(pq, (priority + 1000, location, left))
    # BFS from start to end
    on_path = set()
    queue = [(end, end_direction)]
    # print(previous)
    while len(queue) > 0:
        info = queue[0]
        queue = queue[1:]
        on_path.add(info[0])
        node = previous[info]
        # print(location, node)
        for prev, priority in node["prev"]:
            if(node["priority"] == priority):
                queue.append(prev)
    return final_priority if part1 else len(on_path)


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
