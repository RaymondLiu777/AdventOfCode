import sys
import pyperclip
sys.path.append('../AoC_Helpers')
from InputParser import InputParser
# from Grid import Directions, Grid
# from TupleOps import TupleOps
# from Graph import Graph
# from functools import cache

def findLocations(robots, size, seconds):
    
    final_locations = []
    for px, py, vx, vy in robots:
        final_location_x = (px + vx * seconds) % size[0]
        final_location_y = (py + vy * seconds) % size[1]
        final_locations.append((final_location_x, final_location_y))
    return final_locations

def drawRobots(final_locations, size):
    locations = set(final_locations)
    for j in range(size[1]):
        for i in range(size[0]):
            if (i, j) in locations:
                print("0", end="")
            else:
                print(".", end="")
        print()

def run(filename: str, part1: bool):
    # size = (11, 7)
    size = (101, 103)
    robots = InputParser(open(filename).read()).readLines().findNumbers().getData()
    if(part1):
        final_locations = findLocations(robots, size, 100)
        q1 = 0
        q2 = 0
        q3 = 0
        q4 = 0
        for location in final_locations:
            if(location[0] < (size[0]-1)/2 and location[1] < (size[1]-1)/2):
                # print("q1", location)
                q1 += 1
            if(location[0] > (size[0]-1)/2 and location[1] < (size[1]-1)/2):
                q2 += 1
            if(location[0] < (size[0]-1)/2 and location[1] > (size[1]-1)/2):
                q3 += 1
            if(location[0] > (size[0]-1)/2 and location[1] > (size[1]-1)/2):
                q4 += 1
        # print(final_locations)
        # print(q1, q2, q3, q4)
        return q1 * q2 * q3 * q4
    else:
        i = 0
        while(True):
            val = input()
            i += int(val) if val != "" else 1
            final_locations = findLocations(robots, size, i)
            while(len(set(final_locations)) != len(robots)):
                i += 1
                final_locations = findLocations(robots, size, i)
            print(i)
            drawRobots(final_locations, size)

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
    