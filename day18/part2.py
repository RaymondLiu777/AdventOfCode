
cubes = set()

max_values = [[100,0],[100,0],[100,0]]

adjacent = [
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1)
]

queue = []
searched = set()

def dfs():
    queue.append((max_values[0][0], max_values[1][0], max_values[2][0]))
    
    total = 0
    while len(queue) > 0:
        location = queue.pop()
        if location in searched:
            continue
        searched.add(location)
        if(location[0] < max_values[0][0] or location[0] > max_values[0][1]):
            continue
        if(location[1] < max_values[1][0] or location[1] > max_values[1][1]):
            continue
        if(location[2] < max_values[2][0] or location[2] > max_values[2][1]):
            continue
        for offset in adjacent:
            spot_to_check = (location[0] + offset[0], location[1] + offset[1], location[2] + offset[2])
            if spot_to_check in cubes:
                total +=1
            else:
                queue.append(spot_to_check)
    return total

def main():
    file = open("day18/input.txt")
    for line in file:
        split_line = line.strip().split(",")
        cube = tuple(map(int, split_line))
        max_values[0][0] = min(max_values[0][0], cube[0])
        max_values[0][1] = max(max_values[0][1], cube[0])
        max_values[1][0] = min(max_values[1][0], cube[1])
        max_values[1][1] = max(max_values[1][1], cube[1])
        max_values[2][0] = min(max_values[2][0], cube[2])
        max_values[2][1] = max(max_values[2][1], cube[2])
        cubes.add(cube)
    max_values[0][0] -= 1
    max_values[0][1] += 1
    max_values[1][0] -= 1
    max_values[1][1] += 1
    max_values[2][0] -= 1
    max_values[2][1] += 1
    print(dfs())



if __name__ == "__main__":
    main()