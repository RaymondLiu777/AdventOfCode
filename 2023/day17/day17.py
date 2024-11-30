import sys
import pyperclip
sys.path.append('../')
import AoC_helpers
import heapq

def run(filename: str, part1: bool):
    heat_factor = 1
    grid = [[int(char) for char in line.strip()] for line in open(filename).readlines()]
    grid_rows = len(grid)
    grid_cols = len(grid[0])
    destination = (len(grid) - 1, len(grid[0]) - 1)
    directions = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }
    direction_changes = {
        "up": ["left", "right"],
        "down": ["left", "right"],
        "left": ["up", "down"],
        "right": ["up", "down"],
    }
    # distance + heat, distance from destination, heat, row, col, direction, blocks traveled in that direction
    open_set = [(grid_rows + grid_cols - 2, grid_rows + grid_cols - 2, 0, 0, 0, "right", 0)]
    # Closed set does not contain heat
    closed_set = set()
    while (len(open_set) > 0):
        # Find smallest heat value
        node = heapq.heappop(open_set)
        # print(node, end=" ")
        # Destination
        if(node[3:5] == destination):
            if not part1 and node[6] < 4:
                continue
            return node[2]
        if(node[3:] in closed_set):
            continue
        closed_set.add(node[3:])
        # Go forward
        next_location = tuple(map(lambda i, j: i + j, node[3:5], directions[node[5]]))
        condition = False
        if(part1):
            condition = node[6] < 3
        else:
            condition = node[6] < 10
        if( condition and next_location[0] >= 0 and next_location[1] >= 0 and next_location[0] < len(grid) and next_location[1] < len(grid[0])):
            next_heat = node[2] + grid[next_location[0]][next_location[1]]
            next_distance = grid_rows + grid_cols - next_location[0] - next_location[1] - 2
            next_distance *= heat_factor
            heapq.heappush(open_set, (next_heat + next_distance, next_distance, next_heat, next_location[0], next_location[1], node[5], node[6] + 1))
        # Turn
        if(part1 or node[6] > 3):
            for direction in direction_changes[node[5]]:
                next_location = tuple(map(lambda i, j: i + j, node[3:5], directions[direction]))
                if(next_location[0] >= 0 and next_location[1] >= 0 and next_location[0] < len(grid) and next_location[1] < len(grid[0])):
                    next_heat = node[2] + grid[next_location[0]][next_location[1]]
                    next_distance = grid_rows + grid_cols - next_location[0] - next_location[1] - 2
                    next_distance *= heat_factor
                    heapq.heappush(open_set, (next_heat + next_distance, next_distance, next_heat, next_location[0], next_location[1], direction, 1))
    return -1


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
    