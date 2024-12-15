import sys
import pyperclip
sys.path.append('../AoC_Helpers')
from InputParser import InputParser
from Grid import Directions, Grid
from TupleOps import TupleOps
# from Graph import Graph
# from functools import cache


def run(filename: str, part1: bool):
    grid, moves = open(filename).read().split("\n\n")
    grid = grid.replace("#", "##")
    grid = grid.replace("O", "[]")
    grid = grid.replace(".", "..")
    grid = grid.replace("@", "@.")
    grid = Grid(InputParser(grid).readGrid().getData())
    moves = list(moves.strip())
    moves = filter(lambda x: x != "\n", moves)
    robot = (-1, -1)
    boxes = set()
    for location in grid:
        if(grid.Get(location) == "@"):
            robot = location
            grid.SetGrid(location, ".")
        if(grid.Get(location) == "["):
            boxes.add(location)
            grid.SetGrid(location, ".")
        if(grid.Get(location) == "]"):
            grid.SetGrid(location, ".")

    arrow_to_dir = {
        "^": Directions.N,
        "v": Directions.S,
        ">": Directions.E,
        "<": Directions.W,
    }
    moves = list(map(lambda x: arrow_to_dir[x], moves))
    # grid.print()
    # print(moves)
    # print(boxes)
    for move in moves:
        next_location = TupleOps.Add(robot, move)
        if(next_location in boxes or TupleOps.Add(next_location, (0, -1)) in boxes):
            locations_to_check = [next_location]
            boxes_to_move = set()
            wall_found = False
            # Search for all boxes that might get moved
            while len(locations_to_check) > 0:
                potential_box = locations_to_check[0]
                locations_to_check = locations_to_check[1:]
                # Check location/location to the right for a box
                if(grid.Get(potential_box) == "#"):
                    wall_found = True
                    break
                if(potential_box in boxes or TupleOps.Add(potential_box, (0, -1)) in boxes):
                    box = potential_box if potential_box in boxes else TupleOps.Add(potential_box, (0, -1))
                    boxes_to_move.add(box)
                    if(move == Directions.W):
                        locations_to_check.append(TupleOps.Add(box, move))
                    elif(move == Directions.E):
                        locations_to_check.append(TupleOps.Add(box, TupleOps.Multiply(move, 2)))
                    else:
                        locations_to_check.append(TupleOps.Add(box, move))
                        locations_to_check.append(TupleOps.Add(box, (0, 1), move))
            if(wall_found):
                # Pushes some box into a wall (do nothing)
                continue
            else:
                # Move all boxes
                for box in boxes_to_move:
                    boxes.remove(box)
                for box in boxes_to_move:
                    boxes.add(TupleOps.Add(box, move))
                robot = next_location
        elif(grid.Get(next_location) == "."):
            robot = next_location
            continue
        elif(grid.Get(next_location) == "#"):
            continue
        else:
            print(grid.Get(next_location), next_location)
            raise Exception("unrecongized symbol")
    for box in boxes:
        grid.SetGrid(box, "[")
        grid.SetGrid(TupleOps.Add(box, (0, 1)), "]")
    grid.SetGrid(robot, "@")
    grid.print()
    gps = 0
    for location in grid:
        if(grid.Get(location) == "["):
            gps += 100 * location[0] + location[1]

    return gps


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
    

# grid, moves = open(filename).read().split("\n\n")
#     grid = Grid(InputParser(grid).readGrid().getData())
#     moves = list(moves.strip())
#     moves = filter(lambda x: x != "\n", moves)
#     robot = (-1, -1)
#     for location in grid:
#         if(grid.Get(location) == "@"):
#             robot = location
#             grid.SetGrid(location, ".")
#     arrow_to_dir = {
#         "^": Directions.N,
#         "v": Directions.S,
#         ">": Directions.E,
#         "<": Directions.W,
#     }
#     moves = list(map(lambda x: arrow_to_dir[x], moves))
#     # grid.print()
#     # print(moves)
#     for move in moves:
#         next_location = TupleOps.Add(robot, move)
#         if(grid.Get(next_location) == "."):
#             robot = next_location
#             continue
#         elif(grid.Get(next_location) == "#"):
#             continue
#         elif(grid.Get(next_location) == "O"):
#             next_next_location = next_location
#             while(grid.Get(next_next_location) == "O"):
#                 next_next_location = TupleOps.Add(next_next_location, move)
#             if(grid.Get(next_next_location) == "#"):
#                 continue
#             elif(grid.Get(next_next_location) == "."):
#                 grid.SetGrid(next_next_location, "O")
#                 grid.SetGrid(next_location, ".")
#                 robot = next_location
#         else:
#             print(grid.Get(next_location), next_location)
#             raise Exception("unrecongized symbol")
#     grid.SetGrid(robot, "@")
#     grid.print()
#     gps = 0
#     for location in grid:
#         if(grid.Get(location) == "O"):
#             gps += 100 * location[0] + location[1]

#     return gps