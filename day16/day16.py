import sys
import pyperclip
sys.path.append('../')
import AoC_helpers

def run(filename: str, part1: bool):
    grid = [[char for char in line.strip()] for line in open(filename).readlines()]
    grid_rows = len(grid)
    grid_cols = len(grid[0])
    directions = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }
    direction_changes = {
        (".", "up"): ["up"],
        (".", "down"): ["down"],
        (".", "right"): ["right"],
        (".", "left"): ["left"],
        ("-", "up"): ["left", "right"],
        ("-", "down"): ["left", "right"],
        ("-", "left"): ["left"],
        ("-", "right"): ["right"],
        ("|", "left"): ["up", "down"],
        ("|", "right"): ["up", "down"],
        ("|", "up"): ["up"],
        ("|", "down"): ["down"],
        ("\\", "right"): ["down"],
        ("\\", "left"): ["up"],
        ("\\", "up"): ["left"],
        ("\\", "down"): ["right"],
        ("/", "right"): ["up"],
        ("/", "down"): ["left"],
        ("/", "up"): ["right"],
        ("/", "left"): ["down"],
    }
    start_options = [(0,-1,"right")]
    if not part1:
        start_options = []
        for row in range(grid_rows):
            start_options.append((row, -1, "right"))
            start_options.append((row, grid_cols, "left"))
        for col in range(grid_cols):
            start_options.append((-1, col, "down"))
            start_options.append((grid_rows, col, "up"))
    most_tiles = -1
    for start in start_options:
        queue = [start]
        visited = set()
        while len(queue) > 0:
            node = queue[0]
            queue = queue[1:]
            # print(node)
            if(node in visited):
                continue
            visited.add(node)
            next_location = tuple(map(lambda i, j: i + j, node[0:2], directions[node[2]]))
            if(next_location[0] >= 0 and next_location[1] >= 0 and next_location[0] < len(grid) and next_location[1] < len(grid[0])):
                for direction in direction_changes[(grid[next_location[0]][next_location[1]], node[2])]:
                    queue.append((next_location[0], next_location[1], direction))
        squares_lit = set()
        squares_lit.update([val[0:2] for val in visited])
        lit = len(squares_lit) - 1
        if(lit > most_tiles):
            most_tiles = lit
    return most_tiles


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
    