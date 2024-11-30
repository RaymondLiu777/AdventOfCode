import sys
import pyperclip
sys.path.append('./')
sys.path.append('../')
import AoC_helpers
import functools

intersections = {
    (0,1): {
        "To": [],
        # "From": []
    }
}

node_ids = {}

@functools.lru_cache
def dfs(start, end, visited):
    if(start == end):
        return 0
    max_distance = -1
    for destination, distance, path_id in intersections[start]["To"]:
        node_id = node_ids[destination]
        if(visited[node_id]):
            continue
        new_visited = list(visited)
        new_visited[node_id] = True
        distance_to_end = dfs(destination, end, tuple(new_visited))
        if(distance_to_end != -1):
            max_distance = max(max_distance, distance_to_end + distance)
    return max_distance


def run(filename: str, part1: bool):
    directions = {
        "U": (-1, 0),
        "D": (1, 0),
        "L": (0, -1),
        "R": (0, 1)
    }
    opposite_directions = {
        "U": "D",
        "D": "U",
        "L": "R",
        "R": "L"
    }
    impossible_step = [("U", "v"), ("R", "<"), ("D", "^"), ("L", ">")]
    slopes = {
        "v": "D",
        ">": "R",
        "<": "L",
        "^": "U"
    }
    grid = [[char for char in row.strip()] for row in open(filename)] if part1 else [["." if char in slopes.keys() else char for char in row.strip()] for row in open(filename)]
    grid_rows = len(grid)
    grid_cols = len(grid[0])
    for row in range(grid_rows):
        for col in range(grid_cols):
            print(grid[row][col], end="")
        print()
    entrance = (0, 1)
    end = (grid_rows - 1, grid_cols - 2)
    path_id = 0
    queue = [(entrance, "D")]
    searched = set()
    while len(queue) > 0:
        start, last_direction = queue[0]
        location = start
        queue = queue[1:]
        if((start, last_direction) in searched):
            continue
        searched.add((start, last_direction))
        next_directions = []
        distance_travelled = 0
        while(True):
            next_directions.clear()
            # Move
            location = AoC_helpers.NextLocation(location, directions[last_direction])
            grid_char = AoC_helpers.Get2DLocation(grid, location)
            distance_travelled += 1
            if(grid_char == "#"):
                print("Ran into wall?", location)
                break
            if(grid_char in slopes):
                last_direction = slopes[grid_char]
                location = AoC_helpers.NextLocation(location, directions[last_direction])
                distance_travelled += 1
            # Figure out next move
            for direction in directions.keys():
                if(opposite_directions[last_direction] == direction):
                    continue
                next_location = AoC_helpers.NextLocation(location, directions[direction])
                if(not AoC_helpers.InGrid(grid_rows, grid_cols, next_location)):
                    continue
                grid_char = AoC_helpers.Get2DLocation(grid, next_location)
                if(grid_char == "#"):
                    continue
                if((direction, grid_char) in impossible_step):
                    continue
                next_directions.append(direction)
            # If no moves, or many moves, break and create a node
            if(len(next_directions) == 1):
                last_direction = next_directions[0]
            else:
                break
        # print("Found path from", start, "to", location)
        # print("With next directions:", next_directions)
        if(location not in intersections):
            intersections[location] = {
                "To": [],
                # "From": []
            }
        intersections[start]["To"].append((location, distance_travelled, path_id))
        # intersections[location]["From"].append((start, distance_travelled, path_id))
        if(not part1):
            # intersections[start]["From"].append((location, distance_travelled, path_id))
            intersections[location]["To"].append((start, distance_travelled, path_id))
            searched.add((location, opposite_directions[last_direction]))
        path_id += 1            
        if(len(next_directions) > 1):
            # Add other directions to queue
            for direction in next_directions:
                queue.append((location, direction))
    # for intersection in intersections.items():
    #     print(intersection)
    # Find longest path
    node_id = 0
    for node in intersections.keys():
        node_ids[node] = node_id
        node_id += 1
    # print(node_ids)
    visited = [False] * node_id
    visited[node_ids[entrance]] = True
    max_distance = dfs(entrance, end, tuple(visited))
    return max_distance


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
    