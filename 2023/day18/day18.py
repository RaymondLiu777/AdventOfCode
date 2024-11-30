import sys
import pyperclip
sys.path.append('../')
import AoC_helpers

def run(filename: str, part1: bool):
    border = []
    directions = {
        "U": (-1, 0),
        "D": (1, 0),
        "L": (0, -1),
        "R": (0, 1)
    }
    numToDirection = {
        "0": "R",
        "1": "D",
        "2": "L",
        "3": "U"
    }
    location = (0, 0)
    perimeter = 0
    for line in open(filename):
        direction, distance, color = ("", "", "")
        if(part1):
            direction, distance, color = AoC_helpers.parseLine(line, " ", " (", ")")
            distance = int(distance)
        else:
            direction, distance, color = AoC_helpers.parseLine(line, " ", " (#", ")")
            direction = numToDirection[color[5]]
            distance = int(color[0:5], 16)
        nextLocation = tuple(map(lambda i, j: i + j * distance, location, directions[direction]))
        border.append(nextLocation)
        perimeter += distance

    area = 0
    for idx in range(0, len(border) - 1):
        area += (border[idx - 1][0] + border[idx][0]) * (border[idx - 1][1] - border[idx][1])

    return int(area/2 + perimeter/2 + 1)


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
    