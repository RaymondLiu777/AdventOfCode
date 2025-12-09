import sys
import pyperclip
# import z3
# import networkx as nx
sys.path.append('../AoC_Helpers')
from InputParser import InputParser
from Grid import Directions, Grid
from TupleOps import TupleOps
# from Graph import Graph
# from functools import cache
# from collections import defaultdict

# Create an axis mapping where each square is a location or a range (condense squares without points on them)
def create_axis_mapping(values):
    axis_values = set()
    for location in values:
        axis_values.add(location)
    axis_values = list(axis_values)
    axis_values.sort()
    axis_ranges = [(axis_values[0]-1, axis_values[0])]
    for idx, value in enumerate(axis_values[0:-1]):
        axis_ranges.append(value)
        axis_ranges.append((value, axis_values[idx+1]))
    axis_ranges.append(axis_values[-1])
    axis_ranges.append((axis_values[-1], axis_values[-1]+1))
    return {val: idx for idx, val in enumerate(axis_ranges)}

# Flood fill outside, then fill inside
def floodfill(grid: Grid, start: tuple[int]):
    # Floodfill
    q = [start]
    while len(q) > 0:
        point = q[0]
        q = q[1:]
        if(not grid.InGrid(point)):
            continue
        if(grid.Get(point) == 1 or grid.Get(point) == -1):
            continue
        grid.SetGrid(point, -1)
        for offset in Directions.CARDINAL.values():
            adjacent = TupleOps.Add(point, offset)
            q.append(adjacent)
    # grid.print()
    # Reverse inside/outside fill
    for location in grid:
            if(grid.Get(location) == 0):
                grid.SetGrid(location, 1)
            elif(grid.Get(location) == -1):
                grid.SetGrid(location, 0)

# Check if a rectangle is fully covered
def validSquare(grid, x_axis, y_axis, point1, point2):
    x_start = x_axis[min(point1[0], point2[0])]
    x_end = x_axis[max(point1[0], point2[0])]
    y_start = y_axis[min(point1[1], point2[1])]
    y_end = y_axis[max(point1[1], point2[1])]
    for x in range(x_start, x_end+1):
        for y in range(y_start, y_end + 1):
            if(grid.Get((x,y)) != 1):
                return False
    return True

def run(filename: str, part1: bool):
    data = InputParser(open(filename).read()).readLines().split(",").cast(int).getData()
    points = list(map(tuple, data))
    if part1:
        areas = []
        for idx, point1 in enumerate(points):
            for point2 in points[idx + 1:]:
                area = (abs(point2[0] - point1[0]) + 1) * (abs(point2[1] - point1[1]) + 1)
                areas.append((area, point1, point2))
        areas.sort(reverse=True)
        # print(areas)
        return areas[0][0]
    else:
        # Create a grid, except compress x/y to only values on the points
        x_axis = create_axis_mapping(map(lambda x: x[0], points))
        y_axis = create_axis_mapping(map(lambda x: x[1], points))
        # print(x_axis, y_axis)
        # Draw line on grid
        grid = Grid([[0 for i in range(len(x_axis))] for j in range(len(y_axis))])
        for idx, point1 in enumerate(points):
            point2 = points[(idx + 1) % len(points)]
            # Check if x changes or y changes
            if(point1[0] != point2[0] and point1[1] != point2[1]):
                print("Error with points", point1, point2)
                return -1
            if(point1[0] != point2[0]):
                # X changes
                y = y_axis[point1[1]]
                x_start = x_axis[min(point1[0], point2[0])]
                x_end = x_axis[max(point1[0], point2[0])]
                for x in range(x_start, x_end + 1):
                    grid.SetGrid((x,y), 1)
            elif(point1[1] != point2[1]):
                # Y changes
                x = x_axis[point1[0]]
                y_start = y_axis[min(point1[1], point2[1])]
                y_end = y_axis[max(point1[1], point2[1])]
                for y in range(y_start, y_end + 1):
                    grid.SetGrid((x,y), 1)
        # grid.print()
        floodfill(grid, (0, 0))
        # grid.print()
        # Check possible rectangles
        areas = []
        for idx, point1 in enumerate(points):
            for point2 in points[idx + 1:]:
                if(validSquare(grid, x_axis, y_axis, point1, point2)):
                    area = (abs(point2[0] - point1[0]) + 1) * (abs(point2[1] - point1[1]) + 1)
                    areas.append((area, point1, point2))
        areas.sort(reverse=True)
        # print(areas)
        return areas[0][0]



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
    