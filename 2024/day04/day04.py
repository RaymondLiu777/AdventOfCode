import sys
import pyperclip
sys.path.append('../')
from AoC_helpers import Grid, TupleOps, Directions

def checkForXmax1(crossword, start):
    XMAS_WORD = "XMAS"
    count = 0
    for direction in Directions.DIR.values():
        if(crossword.InGrid(start) and crossword.InGrid(tuple(map(lambda i, j: i + j * 3, start, direction)))):
            xmas = True
            for distance in range(4):
                if(crossword.Get(start, TupleOps.Multiply(direction, distance)) != XMAS_WORD[distance]):
                    xmas = False
            count += 1 if xmas else 0
    return count 

def checkForXmax2(crossword, start):
    if(crossword.Get(start) != "A"):
        return 0
    if(crossword.InGrid(TupleOps.Add(start, (-1, -1))) and crossword.InGrid(TupleOps.Add(start, (1, 1)))):
        tl = crossword.Get(start, (-1, -1))
        br = crossword.Get(start, (1, 1))
        tr = crossword.Get(start, (-1, 1))
        bl = crossword.Get(start, (1, -1))
        if((tl == "M" and br == "S") or (tl == "S" and br == "M")):
            if((tr == "M" and bl == "S") or (tr == "S" and bl == "M")):
                return 1
    return 0 

def run(filename: str, part1: bool):
    crossword = []
    for line in open(filename).readlines():
        crossword.append(line.strip())
    crossword = Grid(crossword)
    count = 0
    for row in range(crossword.rows):
        for col in range(crossword.cols):
            count += checkForXmax1(crossword, (row, col)) if part1 else checkForXmax2(crossword, (row, col))
    return count


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