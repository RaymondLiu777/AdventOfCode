import sys
import pyperclip
sys.path.append('../AoC_Helpers')
from InputParser import InputParser
from Grid import Directions, Grid
from TupleOps import TupleOps
# from Graph import Graph


def run(filename: str, part1: bool):
    input = InputParser(open(filename).read().strip()).readGrid().getData()
    grid = Grid(input)
    antennas = {}
    for row in range(grid.rows):
        for col in range(grid.cols):
            antenna = grid.Get((row,col))
            if(antenna == "."):
                continue
            if antenna not in antennas:
                antennas[antenna] = set()
            antennas[antenna].add((row, col))
    antinodes = set()
    for antenna, locations in antennas.items():
        # Every pair of locations creates a line and antinode position
        for location1 in locations:
            for location2 in locations:
                if(location1 == location2):
                    continue
                distance = TupleOps.Subtract(location2, location1)
                if(part1):
                    antinodes.add(TupleOps.Add(location2, distance))
                    antinodes.add(TupleOps.Subtract(location1, distance))
                else:
                    antinode = location2
                    while (grid.InGrid(antinode)):
                        antinodes.add(antinode)
                        antinode = TupleOps.Add(antinode, distance)
                    antinode = location1
                    while (grid.InGrid(antinode)):
                        antinodes.add(antinode)
                        antinode = TupleOps.Subtract(antinode, distance)
    count = 0
    for antinode in antinodes:
        if grid.InGrid(antinode):
            # grid.SetGrid(antinode, "#")
            count += 1
    # grid.print()
    return count


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
    