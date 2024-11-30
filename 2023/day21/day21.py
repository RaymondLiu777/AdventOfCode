import sys
import pyperclip
sys.path.append('../')
import AoC_helpers
import functools

grid = []

@functools.lru_cache
def bfs(start, limit, start_even, get_first_squares):
    # print(start, limit, start_even, get_first_squares)
    grid_rows = len(grid)
    grid_cols = len(grid[0])
    visited = [[-1] * grid_cols for i in range(grid_rows)]
    visited[start[0]][start[1]] = 0
    queue = [start]
    first_squares = {
        "N": ((-1, -1), -1),
        "E": ((-1, -1), -1),
        "S": ((-1, -1), -1),
        "W": ((-1, -1), -1),
    }
    while(len(queue) > 0):
        location = queue[0]
        queue = queue[1:]
        distance = visited[location[0]][location[1]]
        if(limit != -1 and distance >= limit):
            continue
        for direction in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            next_location = tuple(map(lambda i, j: i + j, location, direction))
            if(next_location[0] < 0 or next_location[1] < 0 or next_location[0] >= grid_rows or next_location[1] >= grid_cols):
                # Find first squares in each direction
                if(get_first_squares):
                    if(next_location[0] < 0):
                        if(first_squares["N"] == ((-1, -1), -1)):
                            first_squares["N"] = (next_location, distance + 1)
                    if(next_location[1] < 0):
                        if(first_squares["W"] == ((-1, -1), -1)):
                            first_squares["W"] = (next_location, distance + 1)
                    if(next_location[0] >= grid_rows):
                        if(first_squares["S"] == ((-1, -1), -1)):
                            first_squares["S"] = (next_location, distance + 1)
                    if(next_location[1] >= grid_cols):
                        if(first_squares["E"] == ((-1, -1), -1)):
                            first_squares["E"] = (next_location, distance + 1)
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
            if(status == -1):
                continue
            if(status % 2 == 0):
                evens += 1
            else:
                odds += 1
    # Debug print graph
    # for row in visited:
    #     for status in row:
    #         if(status == -1):
    #             print(".", end="")
    #             continue
    #         if(status % 2 == 0):
    #             print("O", end="")
    #         else:
    #             print("X", end="")
    #     print()
    if not start_even:
        evens, odds = odds, evens
    # print(evens)
    if get_first_squares:
        return evens, odds, first_squares
    else:
        return evens, odds


def run(filename: str, part1: bool):
    global grid
    grid = [[char for char in line.strip()] for line in open(filename).readlines()]
    grid_rows = len(grid)
    grid_cols = len(grid[0])
    start = (-1, -1)
    for row in range(grid_rows):
        for col in range(grid_cols):
            if(grid[row][col] == "S"):
                start = (row, col)
                grid[row][col] = "."
    # Calculate initial information
    steps = 64 if part1 else 26501365
    evens, odds, first_squares = bfs(start, steps, True, True)
    if(part1):
        return evens
    # print(evens, odds, first_squares)
    # Go all directions
    for direction, offset in [("N", (-1, 0)), ("W", (0, -1)), ("S", (1, 0)), ("E", (0, 1))]: # , ("W", (0, -1)), ("S", (1, 0)), ("E", (0, 1))
        on_even = False
        distance_left = steps - first_squares[direction][1]
        start = first_squares[direction][0]
        start = (start[0] + (grid_rows * -offset[0]) , start[1] + (grid_cols * -offset[1]))
        while True:
            edge = grid_rows + grid_cols + 2 > distance_left
            on_even = not on_even
            new_evens, new_odds, new_first_squares = bfs(start, distance_left if edge else -1, on_even, True)
            evens += new_evens
            odds += new_odds
            # Calculate new start square
            start = new_first_squares[direction][0]
            start = (start[0] + (grid_rows * -offset[0]) , start[1] + (grid_cols * -offset[1]))
            # Find remaining distance
            if(new_first_squares[direction][0] == (-1, -1)):
                distance_left = -1
            else:
                distance_left -= new_first_squares[direction][1]
            if(distance_left < 0):
                break
    print(evens, odds)
    # Go every other square
    corner_distances = {
        "NW": min(first_squares["N"][1] + first_squares["N"][0][1] + 1, first_squares["W"][1] + first_squares["W"][0][0] + 1),
        "NE": min(first_squares["N"][1] + (grid_cols - first_squares["N"][0][1]), first_squares["E"][1] + first_squares["E"][0][0] + 1),
        "SW": min(first_squares["S"][1] + first_squares["S"][0][1] + 1, first_squares["W"][1] + (grid_rows - first_squares["W"][0][0])),
        "SE": min(first_squares["S"][1] + (grid_cols - first_squares["S"][0][1]),  first_squares["E"][1] + (grid_rows - first_squares["E"][0][0])),
    }
    print(corner_distances)
    for direction, start in [("NW", (0, 0)), ("NE", (0, grid_cols - 1)), ("SW", (grid_rows - 1, 0)), ("SE", (grid_rows - 1, grid_cols - 1))]:
        print(direction)
        distance_left = steps - corner_distances[direction]
        if(distance_left < 0):
            continue
        on_even = True
        while True:
            distance_left_row = distance_left
            whole_squares = int((distance_left_row - (grid_rows + grid_cols)) / grid_rows)
            if(whole_squares == -1):
                whole_squares = 0
            if(whole_squares % 2 == 1):
                whole_squares -= 1
            distance_left_row -= whole_squares * grid_cols
            new_evens, new_odds = bfs(start, -1, True, False)
            evens += new_evens * int(whole_squares/2)
            odds += new_odds * int(whole_squares/2)
            new_evens, new_odds = bfs(start, -1, False, False)
            evens += new_evens * int(whole_squares/2)
            odds += new_odds * int(whole_squares/2)
            on_even_row = on_even
            while True:
                edge = grid_rows + grid_cols + 2 > distance_left_row
                new_evens, new_odds = bfs(start, distance_left_row if edge else -1, on_even_row, False)
                evens += new_evens
                odds += new_odds
                distance_left_row -= grid_rows
                on_even_row = not on_even_row
                if(distance_left_row < 0):
                    break
            distance_left -= grid_cols
            on_even = not on_even
            if(distance_left < 0):
                break
    return odds

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