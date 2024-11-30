import sys
import pyperclip
sys.path.append('../')
import AoC_helpers

def run(filename: str, part1: bool):
    star_map = [line.strip() for line in open(filename).readlines()]
    num_rows = len(star_map)
    num_cols = len(star_map[0])
    star_locations = []
    row_expansions = [True] * num_rows
    col_expansions = [True] * num_cols
    for row in range(num_rows):
        for col in range(num_cols):
            if star_map[row][col] == "#":
                star_locations.append((row,col))
                row_expansions[row] = False
                col_expansions[col] = False
    # print(row_expansions, col_expansions)
    # Generate offsets
    row_offset = []
    col_offset = []
    offset = 0
    expansion = 0
    if part1:
        expansion = 1
    else:
        expansion = 1000000 - 1
    for row in row_expansions:
        row_offset.append(offset)
        if(row):
            offset += expansion
    offset = 0
    for col in col_expansions:
        col_offset.append(offset)
        if(col):
            offset += expansion
    # print(row_offset, col_offset)
    # Check distances
    total = 0
    for i in range(len(star_locations)):
        for j in range(i + 1, len(star_locations)):
            star1 = star_locations[i]
            star2 = star_locations[j]
            diff = ((star1[0] + row_offset[star1[0]]) - (star2[0] + row_offset[star2[0]]), (star1[1] + col_offset[star1[1]]) - (star2[1] + col_offset[star2[1]]))
            total += abs(diff[0]) + abs(diff[1])
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
    