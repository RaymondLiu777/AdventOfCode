import sys
import pyperclip
sys.path.append('../')
import AoC_helpers

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
    visited = [[-1] * grid_cols for i in range(grid_rows)]
    visited[start[0]][start[1]] = 0
    queue = [start]
    while(len(queue) > 0):
        location = queue[0]
        queue = queue[1:]
        distance = visited[location[0]][location[1]]
        if(distance >= steps):
            continue
        for direction in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            next_location = tuple(map(lambda i, j: i + j, location, direction))
            if(next_location[0] < 0 or next_location[1] < 0 or next_location[0] >= grid_rows or next_location[1] >= grid_cols):
                print("Out of bounds:", next_location, distance + 1)
                continue
            if(visited[next_location[0]][next_location[1]] != -1):
                continue
            if(grid[next_location[0]][next_location[1]] == "#"):
                continue
            visited[next_location[0]][next_location[1]] = distance + 1
            queue.append(next_location)
    total = 0

    for row in visited:
        for status in row:
            if(status % 2 == steps % 2):
                total += 1
        # print(row)
    return total


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
    