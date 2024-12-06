from TupleOps import TupleOps

class Directions:

    N = (-1, 0)
    S = (1, 0)
    E = (0, 1)
    W = (0, -1)
    NW = TupleOps.Add(N, W)
    NE = TupleOps.Add(N, E)
    SW = TupleOps.Add(S, W)
    SE = TupleOps.Add(S, E)

    # Useful constants
    CARDINAL = {
        "N": N, "E": E, "S": S, "W": W
    }

    DIAGONAL = { 
        "NE": NE, "SE": SE, "SW": SW, "NW": NW
    }

    ALL = { **CARDINAL, **DIAGONAL }


class Grid:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
    
    def Get(self, location, *argv):
        new_location = TupleOps.Add(location, *argv)
        if not self.InGrid(new_location):
            print("Error invalid location", location, argv)
            raise Exception("Error invalid location")
        return self.grid[new_location[0]][new_location[1]]

    def SetGrid(self, location, value):
        if not self.InGrid(location):
            print("Error invalid location", location)
            raise Exception("Error invalid location")
        old_value = self.grid[location[0]][location[1]]
        self.grid[location[0]][location[1]] = value
        return old_value

    def InGrid(self, location):
        return location[0] >= 0 and location[1] >= 0 and location[0] < len(self.grid) and location[1] < len(self.grid[location[0]])

    def print(self):
        for line in self.grid:
            for char in line:
                print(char, end="")
            print()