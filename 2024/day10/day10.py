import sys
import pyperclip
sys.path.append('../AoC_Helpers')
from InputParser import InputParser
from Grid import Directions, Grid
from TupleOps import TupleOps
# from Graph import Graph

def findPaths(grid: Grid, location: tuple):
    if(not grid.InGrid(location)):
        return []
    current_height = grid.Get(location)
    if(current_height == 9):
        return [location]
    else:
        total_peaks = []
        for dir in Directions.CARDINAL.values():
            next_location = TupleOps.Add(location, dir)
            if(grid.InGrid(next_location) and grid.Get(next_location) == current_height + 1):
                total_peaks = [*total_peaks, *findPaths(grid, next_location)]
        return total_peaks

def run(filename: str, part1: bool):
    input = InputParser(open(filename).read().strip()).readGrid().modifyData(int).getData()
    grid = Grid(input)
    paths = 0
    for row in range(grid.rows):
        for col in range(grid.cols):
            if(grid.Get((row, col)) == 0):
                all_peaks = findPaths(grid, (row, col))
                paths += len(set(all_peaks)) if part1 else len(all_peaks)
                # print((row, col), all_peaks)
    return paths


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
    