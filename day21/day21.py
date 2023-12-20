import sys
import pyperclip
sys.path.append('../')
import AoC_helpers

def bfs(grid, start, limit, start_even, get_first_squares):
    grid_rows = len(grid)
    grid_cols = len(grid[0])
    visited = [[-1] * grid_cols for i in range(grid_rows)]
    visited[start[0]][start[1]] = 0
    queue = [start]
    first_squares = {
        "N": (-1, -1),
        "E": (-1, -1),
        "S": (-1, -1),
        "W": (-1, -1),
    }
    while(len(queue) > 0):
        location = queue[0]
        queue = queue[1:]
        distance = visited[location[0]][location[1]]
        if(distance >= limit):
            continue
        for direction in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            next_location = tuple(map(lambda i, j: i + j, location, direction))
            if(next_location[0] < 0 or next_location[1] < 0 or next_location[0] >= grid_rows or next_location[1] >= grid_cols):
                # Find first squares in each direction
                if(get_first_squares):
                    if(next_location[0] < 0):
                        if(first_squares["N"] == (-1, -1)):
                            first_squares["N"] = next_location
                    if(next_location[1] < 0):
                        if(first_squares["W"] == (-1, -1)):
                            first_squares["W"] = next_location
                    if(next_location[0] >= grid_rows):
                        if(first_squares["S"] == (-1, -1)):
                            first_squares["S"] = next_location
                    if(next_location[1] >= grid_cols):
                        if(first_squares["E"] == (-1, -1)):
                            first_squares["E"] = next_location
                continue
            if(visited[next_location[0]][next_location[1]] != -1):
                continue
            if(grid[next_location[0]][next_location[1]] == "#"):
                continue
            visited[next_location[0]][next_location[1]] = distance + 1
            queue.append(next_location)
    evens = 0
    odds = 0
    for row in visited:
        for status in row:
            if(status % 2 == 0):
                evens += 1
            else:
                odds += 1
    if get_first_squares:
        return evens, odds, first_squares
    else:
        return evens, odds


def run(filename: str, part1: bool):
    steps = 64
    grid = [[char for char in line.strip()] for line in open(filename).readlines()]
    grid_rows = len(grid)
    grid_cols = len(grid[0])
    start = (-1, -1)
    for row in range(grid_rows):
        for col in range(grid_cols):
            if(grid[row][col] == "S"):
                start = (row, col)
                grid[row][col] = "."
    evens, odds = bfs(grid, start, steps, True, False)
    return evens


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
    