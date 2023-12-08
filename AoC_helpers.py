def parseLine(string: str, *arg):
    string = string.strip()
    result = []
    start = 0
    for split in arg:
        location = string.find(split, start)
        if(location != start):
            result.append(string[start:location])
        start = location + len(split)
    if(start != len(string)):
        result.append(string[start:])
    return result