import sys
import pyperclip
sys.path.append('../')
import AoC_helpers
import copy

def printMap(pipes):
    for row in pipes:
        for square in row:
            if(square):
                print("0", end="")
            else:
                print(".", end="")
        print()

def run(filename: str, part2: bool):
    lines = [line.strip() for line in open(filename).readlines()]
    start = (-1,-1)
    rowCount = len(lines)
    colCount = len(lines[0])
    for row in range(rowCount):
        for col in range(colCount):
            if(lines[row][col] == "S"):
                start = (row, col)
    queue = [start]
    visited = {start: 0}
    previous = {start: (-1, -1)}
    directions = {
        "S": [(0, -1), (0, 1), (-1, 0), (1, 0)],
        "-": [(0, -1), (0, 1)],
        "|": [(-1, 0), (1, 0)],
        "7": [(0, -1), (1, 0)],
        "J": [(0, -1), (-1, 0)],
        "L": [(0, 1), (-1, 0)],
        "F": [(0, 1), (1, 0)],
        ".": [],
    }
    while len(queue) > 0:
        location = queue[0]
        queue = queue[1:]
        distance = visited[location]
        # print(location)
        for direction in directions[lines[location[0]][location[1]]]:
            newLocation = tuple(map(lambda i, j: i + j, location, direction))
            if(newLocation[0] < 0 or newLocation[1] < 0 or newLocation[0] >= rowCount or newLocation[1] >= colCount):
                continue
            if(newLocation in visited):
                continue
            if((-direction[0], -direction[1]) in directions[lines[newLocation[0]][newLocation[1]]]):
                visited[newLocation] = distance + 1
                queue.append(newLocation)
                previous[newLocation] = location
    if not part2:
        return max(visited.values())
    # Find relevant pipes
    end_distance = max(visited.values())
    end = (-1, -1)
    for location, distance in visited.items():
        if(distance == end_distance):
            end = location
    pipes = [end, start]
    backtracking = []
    for direction in directions[lines[end[0]][end[1]]]:
        nextLocation = tuple(map(lambda i, j: i + j, end, direction))
        backtracking.append(nextLocation)
    for location in backtracking:
        while(location != start):
            pipes.append(location)
            location = previous[location]
    # Generate bigger graph with pipes draw out
    bigPipes = []
    for row in range(rowCount * 3):
        bigPipes.append([False] * colCount * 3)
    for pipe in pipes:
        bigPipeLocation = (pipe[0] * 3 + 1, pipe[1] * 3 + 1)
        bigPipes[bigPipeLocation[0]][bigPipeLocation[1]] = True
        for direction in directions[lines[pipe[0]][pipe[1]]]:
            nextLocation = tuple(map(lambda i, j: i + j, bigPipeLocation, direction))
            bigPipes[nextLocation[0]][nextLocation[1]] = True
    # printMap(bigPipes)
    # Fill outside of the loop
    floodFill = [(0,0)]
    for row in range(len(bigPipes)):
        floodFill.append((row, 0))
        floodFill.append((row, len(bigPipes[0])-1))
    for col in range(len(bigPipes[0])):
        floodFill.append((0, col))
        floodFill.append((len(bigPipes)-1, col))
    while len(floodFill) > 0:
        location = floodFill[0]
        floodFill = floodFill[1:]
        if(location[0] < 0 or location[1] < 0 or location[0] >= len(bigPipes) or location[1] >= len(bigPipes[0])):
            continue
        if(bigPipes[location[0]][location[1]]):
            continue
        bigPipes[location[0]][location[1]] = True
        for direction in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            floodFill.append(tuple(map(lambda i, j: i + j, location, direction)))
    # printMap(bigPipes)
    # Count spaces that were not reached
    nestCount = 0
    for row in range(rowCount):
        for col in range(colCount):
            bigPipeLocation = (row * 3 + 1, col * 3 + 1)
            if not bigPipes[bigPipeLocation[0]][bigPipeLocation[1]]:
                nestCount += 1
    return nestCount

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

    part2 = (sys.argv[2] == '2')
    result = run(filename, part2)
    print(result)
    pyperclip.copy(str(result))
    