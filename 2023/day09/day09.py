import sys
import pyperclip
sys.path.append('../')
import AoC_helpers

def extrapolate(seq: "list[int]"):
    allZero = True
    for val in seq:
        if val != 0:
            allZero = False
    if(allZero):
        return 0
    diffs = []
    for i in range(len(seq) - 1):
        diffs.append(seq[i+1] - seq[i])
    return seq[len(seq) - 1] + extrapolate(diffs)

def back_extrapolate(seq: "list[int]"):
    allZero = True
    for val in seq:
        if val != 0:
            allZero = False
    if(allZero):
        return 0
    diffs = []
    for i in range(len(seq) - 1):
        diffs.append(seq[i+1] - seq[i])
    return seq[0] - back_extrapolate(diffs)

def run(filename: str, part2: bool):
    total = 0
    for line in open(filename):
        if(part2):
            total += back_extrapolate(list(map(int, line.strip().split())))
        else:
            total += extrapolate(list(map(int, line.strip().split())))
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

    part2 = (sys.argv[2] == '2')
    result = run(filename, part2)
    print(result)
    pyperclip.copy(str(result))
    