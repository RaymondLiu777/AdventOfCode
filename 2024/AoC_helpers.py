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
        newlocation = TupleOps.Add(location, *argv)
        return self.grid[newlocation[0]][newlocation[1]]

    def InGrid(self, location):
        return location[0] >= 0 and location[1] >= 0 and location[0] < len(self.grid) and location[1] < len(self.grid[location[0]])

class TupleOps:
    def Add(tup1, *argv):
        value = tup1
        for arg in argv:
            value = tuple(map(lambda i, j: i + j, value, arg))
        return value

    def Multiply(tup1, multiple):
        return tuple(map(lambda i: i * multiple, tup1))

def parseLine(string: str, *arg):
    string = string.strip()
    result = []
    start = 0
    for split in arg:
        location = string.find(split, start)
        if(location != start):
            result.append(string[start:location])
        start = location + len(split)
    if(start != len(string)):
        result.append(string[start:])
    return tuple(result)



