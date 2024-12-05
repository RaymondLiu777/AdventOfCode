from TupleOps import TupleOps

class Directions:

    U = (0, 1)
    D = (0, -1)
    L = (-1, 0)
    R = (1, 0)
    UR = (1, 1)
    UL = (-1, 1)
    DR = (1, -1)
    DL = (-1, -1) 

    # Useful constants
    CARDINAL = {
        "U": U, "D": D, "L": L, "R": R
    }

    DIAGONAL = { 
        "UR": UR, "UL": UL, "DR": DR, "DL": DL 
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

    def InGrid(self, location):
        return location[0] >= 0 and location[1] >= 0 and location[0] < len(self.grid) and location[1] < len(self.grid[location[0]])