import sys
import pyperclip
sys.path.append('../AoC_Helpers')
from InputParser import InputParser
from Grid import Directions, Grid
from TupleOps import TupleOps
# from Graph import Graph
# from functools import cache

directions = [Directions.N, Directions.E, Directions.S, Directions.W]

def forwardStep(grid:Grid, location:tuple, direction_index:tuple, visited):
    # Check for right turn
    forward = TupleOps.Add(location, directions[direction_index])
    forwardRight = TupleOps.Add(forward, directions[(direction_index + 1) % 4])
    if forwardRight not in visited :
        return (forwardRight, (direction_index + 1) % 4)
    elif forward not in visited:
        return (forward, direction_index)
    else:
        return (location, (direction_index - 1) % 4)

def searchRegion(grid:Grid, start:tuple, visited:set):
    queue = [start]
    area = 0 
    perimeter = 0
    patch = grid.Get(start)
    sides = set()
    newly_visited = set()
    while len(queue) > 0:
        top = queue[0]
        queue = queue[1:]
        if top in visited:
            continue
        if not grid.InGrid(top):
            continue
        if patch != grid.Get(top):
            continue
        visited.add(top)
        newly_visited.add(top)
        area += 1
        for direction in Directions.CARDINAL.values():
            if not grid.InGrid(TupleOps.Add(top, direction)) or patch != grid.Get(top, direction):
                perimeter += 1
                sides.add(TupleOps.Add(top, direction))
            queue.append(TupleOps.Add(top, direction))
    # print(patch, sides)
    walls = 0
    while len(sides) > 0:
        start = sides.pop()
        start_direction = -1
        for idx, dir in enumerate(directions):
            neighbor = TupleOps.Add(start, dir)
            if(neighbor in newly_visited):
                start_direction = (idx - 1) % 4
        # print(start, start_direction)
        location = start
        direction = start_direction
        while(True):
            location, next_direction = forwardStep(grid, location, direction, newly_visited)
            if direction != next_direction:
                walls += 1
            if location in sides:
                sides.remove(location)
            direction = next_direction
            if(location == start and direction == start_direction):
                break
            # print(location, direction)
    return (area, perimeter, walls)

def run(filename: str, part1: bool):
    input = InputParser(open(filename).read()).readGrid().getData()
    grid = Grid(input)
    regions = []
    visited = set()
    for location in grid:
        if location not in visited:
            regions.append(searchRegion(grid, location, visited))
    total = 0
    for region in regions:
        total += region[0] * (region[1] if part1 else region[2])
    return total


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
    

    # def forwardStep(grid:Grid, location:tuple, direction_index:tuple, patch):
    # # Check for right turn
    # forward = TupleOps.Add(location, directions[direction_index])
    # forwardRight = TupleOps.Add(forward, directions[(direction_index + 1) % 4])
    # forwardPatch = grid.Get(forward) if grid.InGrid(forward) else None
    # forwardRightPatch = grid.Get(forwardRight) if grid.InGrid(forwardRight) else None
    # if forwardRightPatch != patch and forwardPatch != patch:
    #     return (forwardRight, (direction_index + 1) % 4)
    # elif forwardPatch != patch:
    #     return (forward, direction_index)
    # else:
    #     return (location, (direction_index - 1) % 4)

    # 805984
    # 805900