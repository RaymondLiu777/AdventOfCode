import sys
import pyperclip
sys.path.append('../')

def run(filename: str, part1: bool):
    if part1:
        return part1(filename)
    else:
        return part2(filename)

def part1(filename: str):
    one = []
    two = []
    for line in open(filename).readlines():
        (list_one, list_two) = line.split()
        one.append(int(list_one))
        two.append(int(list_two))
    one.sort()
    two.sort()
    total = 0
    for i in range(len(one)):
        total += abs(one[i] - two[i])
    return total

def part2(filename: str):
    one = {}
    two = {}
    for line in open(filename).readlines():
        (list_one, list_two) = line.split()
        if(int(list_one) not in one):
            one[int(list_one)] = 0
        if(int(list_two) not in two):
            two[int(list_two)] = 0
        one[int(list_one)] += 1
        two[int(list_two)] += 1
    total = 0
    for num, count in one.items():
        if num in two:
            total += num * count * two[num]
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
    