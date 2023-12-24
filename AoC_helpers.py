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

def Get2DLocation(grid, location):
    return grid[location[0]][location[1]]

def InGrid(grid_rows, grid_cols, location):
    return location[0] >= 0 and location[1] >= 0 and location[0] < grid_rows and location[1] < grid_cols

def NextLocation(location, offset):
    return tuple(map(lambda i, j: i + j, location, offset))