tail_locations = set()
tail_location = [0, 0] # absolue position of tail
head = [0, 0] # relative position of head to tail
move_to_location = {
    "R": [1, 0],
    "L": [-1, 0],
    "U": [0, 1],
    "D": [0, -1]
}
movement = {
    #one direction
    str([2, 0]): [1, 0],
    str([-2, 0]): [-1, 0],
    str([0, 2]): [0, 1],
    str([0, -2]): [0, -1],
    #diagonal
    str([2, 1]): [1, 1],
    str([1, 2]): [1, 1],
    str([2, -1]): [1, -1],
    str([1, -2]): [1, -1],
    str([-2, 1]): [-1, 1],
    str([-1, 2]): [-1, 1],
    str([-2, -1]): [-1, -1],
    str([-1, -2]): [-1, -1],
}

def update_rope(direction):
    head[0] += move_to_location[direction][0]
    head[1] += move_to_location[direction][1]
    if(head[0] >= -1 and head[0] <= 1 and head[1] >= -1 and head[1] <= 1):
        return
    move = movement[str(head)]
    tail_location[0] += move[0]
    tail_location[1] += move[1]
    head[0] -= move[0]
    head[1] -= move[1]
    


def main():
    file = open("day9/input.txt")
    for line in file:
        split_line = line.strip().split()
        for x in range(int(split_line[1])):
            update_rope(split_line[0])
            tail_locations.add(str(tail_location))
    print(len(tail_locations))


if __name__ == "__main__":
    main()