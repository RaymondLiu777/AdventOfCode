import sys
import pyperclip
sys.path.append('../AoC_Helpers')
from InputParser import InputParser
from Grid import Directions, Grid
from TupleOps import TupleOps
# from Graph import Graph

def run_simulation(grid: Grid, location: tuple, loop_detection=True):
    visited = {}
    directions = [Directions.N, Directions.E, Directions.S, Directions.W]
    direction_index = 0
    while(True):
        # Cycle Detection
        if(loop_detection and location in visited and directions[direction_index] in visited[location]):
            return True

        # Location tracking
        if(location not in visited):
            visited[location] = {directions[direction_index]}
        else:
            visited[location].add(directions[direction_index])

        next_location = TupleOps.Add(location, directions[direction_index])
        # Off the grid
        if(not grid.InGrid(next_location)):
            break
        # Doesn't hit wall
        if(grid.Get(next_location) != "#"):
            location = next_location
        # Hits wall
        else:
            direction_index = (direction_index + 1) % len(directions)
    return False if loop_detection else visited

def run(filename: str, part1: bool):
    grid = InputParser(open(filename).read().strip()).readGrid().getData()
    grid = Grid(grid)
    location = (-1, -1)
    for row in range(grid.rows):
        for col in range(grid.cols):
            if(grid.Get((row, col)) == "^"):
                location = (row, col)
    visited = run_simulation(grid, location, loop_detection=False)
    if(part1):
        return len(visited)
    # Brute force cycles :/
    loops = 0
    for obstacle in visited.keys():
        original = grid.SetGrid(obstacle, "#")
        if run_simulation(grid, location):
            loops += 1
        grid.SetGrid(obstacle, original)
    return loops

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

# Unused code for clever cycle detection
def extend_backwards(grid: Grid, location: tuple, directions: list, direction_index: int, visited: set):
    while(grid.InGrid(location) and grid.Get(location) != "#"):
        left_direction = directions[(direction_index-1) % len(directions)]
        left_block = TupleOps.Add(location, left_direction)
        if(grid.InGrid(left_block) and grid.Get(left_block) == "#"):
            extend_backwards(grid, location, directions, (direction_index-1) % len(directions), visited)
        if(location not in visited):
            visited[location] = {directions[direction_index]}
        else:
            visited[location].add(directions[direction_index])
        location = TupleOps.Add(location, directions[(direction_index + 2) % len(directions)])
        if(location in visited and directions[direction_index] in visited[location]):
            break