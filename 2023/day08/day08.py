import sys
import pyperclip
import numpy

def part1(filename):
    lines = open(filename).readlines()
    intructions = lines[0].strip()
    pathsInput = lines[2:]
    paths = {}
    for path in pathsInput:
        split = path.strip().split("=")
        location = split[0].strip()
        split2 = split[1].split(",")
        left = split2[0].replace("(", "").strip()
        right = split2[1].replace(")", "").strip()
        paths[location] = (left, right)
    done = False
    location = "AAA"
    distance = 0
    while not done:
        for direction in intructions:
            if(location == "ZZZ"):
                done = True
                break
            distance += 1
            if(direction == "L"):
                location = paths[location][0]
            elif(direction == "R"):
                location = paths[location][1]
            else:
                print("ERROR")
                exit()
    return distance

# Part 2 can be optimized with the knowledge at all cycles begin at 0 and are on a set loop
# But I wasn't sure about this and did some extra work instead to verify
def part2(filename):
    lines = open(filename).readlines()
    intructions = lines[0].strip()
    pathsInput = lines[2:]
    paths = {}
    for path in pathsInput:
        split = path.strip().split("=")
        location = split[0].strip()
        split2 = split[1].split(",")
        left = split2[0].replace("(", "").strip()
        right = split2[1].replace(")", "").strip()
        paths[location] = (left, right)
    locations = []
    # Find all locations that end in A
    for path in paths.keys():
        if(path[len(path) - 1] == "A"):
            locations.append(path)
    print(locations)
    cycles = []
    for location in locations:
        pattern = []
        # for i in range(pow(len(intructions),2)):
        for i in range(len(intructions) * 10000):
            # Check if all locations end in Z
            if(location[len(location) - 1] == "Z"):
                pattern.append(i)
            # Update all locations
            if(intructions[i % len(intructions)] == "L"):
                location = paths[location][0]
            elif(intructions[i % len(intructions)] == "R"):
                location = paths[location][1]
            else:
                print("ERROR")
                exit()
        # Pattern detection
        if(pattern[2] - pattern[1] == pattern[1]-pattern[0]):
            cycles.append(pattern[0])
            print(pattern[2]-pattern[1], pattern[0])
        else:
            print("couldn't detect pattern")
    return numpy.lcm.reduce(cycles)



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
    pyperclip.copy(str(result))
    