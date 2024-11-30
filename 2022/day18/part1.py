
cubes = set()

adjacent = [
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1)
]

def main():
    file = open("day18/input.txt")
    for line in file:
        split_line = line.strip().split(",")
        cubes.add(tuple(map(int, split_line)))
    total = 0
    for cube in cubes:
        for offset in adjacent:
            spot_to_check = (cube[0] + offset[0], cube[1] + offset[1], cube[2] + offset[2])
            if spot_to_check not in cubes:
                total +=1
    print(total)



if __name__ == "__main__":
    main()