import sys
import pyperclip

def part1(filename):
    lines = open(filename).readlines()
    times = list(map(int, lines[0].strip().split()[1:]))
    records = list(map(int, lines[1].strip().split()[1:]))
    total = 1
    print(times, records)
    for i in range(len(times)):
        minTime = 0
        for t in range(times[i]):
            if(t * (times[i] - t) > records[i]):
                minTime = t
                break
        total *= times[i] - (2 * minTime) + 1
        print(minTime, times[i] - (2 * minTime) + 1)
    return total



def part2(filename):
    #Use desmo calculator and quadratic equation solver :)
    pass



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

    result = ""
    if sys.argv[2] == '1':
        result = part1(filename)
    elif sys.argv[2] == '2':
        result = part2(filename)
    print(result)
    pyperclip.copy(result)
    