import numpy as np

tail_locations = set()
tail_location = [0, 0] # absolue position of tail
rope = np.full((9, 2), 0) # relative position of rope knot to next rope knot

move_to_location = {
    "R": [1, 0],
    "L": [-1, 0],
    "U": [0, 1],
    "D": [0, -1]
}
movement = {
    #one direction
    str(np.array([2, 0])): [1, 0],
    str(np.array([-2, 0])): [-1, 0],
    str(np.array([0, 2])): [0, 1],
    str(np.array([0, -2])): [0, -1],
    #diagonal
    str(np.array([2, 1])): [1, 1],
    str(np.array([1, 2])): [1, 1],
    str(np.array([2, -1])): [1, -1],
    str(np.array([1, -2])): [1, -1],
    str(np.array([-2, 1])): [-1, 1],
    str(np.array([-1, 2])): [-1, 1],
    str(np.array([-2, -1])): [-1, -1],
    str(np.array([-1, -2])): [-1, -1],
    #new options
    str(np.array([2, 2])): [1, 1],
    str(np.array([2, -2])): [1, -1],
    str(np.array([-2, 2])): [-1, 1],
    str(np.array([-2, -2])): [-1, -1],
}

def update_head(direction):
    rope[0][0] += move_to_location[direction][0]
    rope[0][1] += move_to_location[direction][1]
    update_knot(0, 1)
    
    
def update_knot(prevIndex, nextIndex):
    prev = rope[prevIndex]
    next = rope[nextIndex] if nextIndex < 9 else tail_location
    if(prev[0] >= -1 and prev[0] <= 1 and prev[1] >= -1 and prev[1] <= 1):
        return
    move = movement[str(prev)]
    next[0] += move[0]
    next[1] += move[1]
    prev[0] -= move[0]
    prev[1] -= move[1]
    if(nextIndex != len(rope)):
        update_knot(nextIndex, nextIndex + 1)
    else:
        tail_locations.add(str(tail_location))


def main():
    file = open("day9/input.txt")
    tail_locations.add(str(tail_location))
    for line in file:
        split_line = line.strip().split()
        for x in range(int(split_line[1])):
            update_head(split_line[0])
    print(len(tail_locations))

if __name__ == "__main__":
    main()