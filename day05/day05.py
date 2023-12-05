import sys
import pyperclip

def part1(filename):
    file = open(filename)
    lines = file.readlines()
    seeds = list(map(int, lines[0].split(":")[1].strip().split()))
    mappings = {}
    mapping = []
    conversion = ""
    for line in lines[2:]:
        if line.strip() == "":
            mappings[conversion] = mapping
            mapping = []
            continue
        elif "map" in line:
            conversion = line.strip().split()[0]
        else:
            mapping.append(tuple(map(int, line.split())))
    mappings[conversion] = mapping

    smallest_location = -1

    mapping_order = ["seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water", "water-to-light", "light-to-temperature", "temperature-to-humidity", "humidity-to-location"]
    for seed in seeds:
        location = seed
        for mapName in mapping_order:
            # found = False
            for conversion in mappings[mapName]:
                if(location >= conversion[1] and location < conversion[1] + conversion[2]):
                    location = conversion[0] + location - conversion[1]
                    # found = True
                    break
        if smallest_location == -1 or location < smallest_location:
            smallest_location = location
    return smallest_location

def part2(filename):
    file = open(filename)
    lines = file.readlines()
    seeds = list(map(int, lines[0].split(":")[1].strip().split()))
    mappings = {}
    mapping = []
    conversion = ""
    for line in lines[2:]:
        if line.strip() == "":
            mappings[conversion] = mapping
            mapping = []
            continue
        elif "map" in line:
            conversion = line.strip().split()[0]
        else:
            mapping.append(tuple(map(int, line.split())))
    mappings[conversion] = mapping

    smallest_location = -1

    mapping_order = ["seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water", "water-to-light", "light-to-temperature", "temperature-to-humidity", "humidity-to-location"]
    
    
    for i in range(0, len(seeds), 2):
        ranges = [(seeds[i], seeds[i+1])]
        # Go through each map
        for mapName in mapping_order:
            # print(mapName, ranges)
            next_ranges = []
            # Go through stored ranges
            for r in ranges:
                start = r[0]
                end = r[1]
                done = False
                # Convert ranges to new ranges
                while not done:
                    found = False
                    next_range_start = -1
                    for conversion in mappings[mapName]:
                        # Start of range is in a range
                        if(start >= conversion[1] and start < conversion[1] + conversion[2]):
                            found = True
                            newStart = conversion[0] + start - conversion[1]
                            newEnd = 0
                            if(end <= conversion[2]):
                                newEnd = end
                                done = True
                            else:
                                newEnd = conversion[2] - (start - conversion[1])
                                start = start + newEnd
                                end = end - newEnd
                            next_ranges.append((newStart, newEnd))
                            break
                        # Find next range where something starts
                        if(conversion[1] > start and (conversion[1] < next_range_start or next_range_start == -1)):
                            next_range_start = conversion[1]
                    # If we could not find a range that the start is in, this range does not change
                    if not found:
                        newStart = start
                        newEnd = 0
                        if(next_range_start < start):
                            newEnd = end
                            done = True
                        elif(start + end <= next_range_start):
                            newEnd = end
                            done = True
                        else:
                            newEnd = end - (next_range_start - start)
                            start = next_range_start
                        next_ranges.append((newStart, newEnd))
            ranges = next_ranges
        # Find smallest start value
        for r in ranges:
            if smallest_location == -1 or r[0] < smallest_location:
                smallest_location = r[0]
    return smallest_location



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
    