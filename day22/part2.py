import re
import math
from enum import Enum

class Direction(Enum):
    Right = 0
    Down = 1
    Left = 2
    Up = 3

board = []
path = []
cube_side_length = 50
cube_sides = [
    [150, 0],
    [100, 0],
    [100, 50],
    [50, 50],
    [0, 50],
    [0, 100]
]
connections = {
    ((150, 49), Direction.Down, Direction.Right): ((149, 50), Direction.Right, Direction.Down), #F
    ((199, 0), Direction.Right, Direction.Down): ((0, 100), Direction.Right, Direction.Up), #J
    ((150,0), Direction.Down, Direction.Left): ((0, 50), Direction.Right, Direction.Up), #L
    ((149,0), Direction.Up, Direction.Left): ((0, 50), Direction.Down, Direction.Left), #K
    ((100, 0), Direction.Right, Direction.Up): ((50, 50), Direction.Down, Direction.Left), #G
    ((100, 99), Direction.Down, Direction.Right): ((49, 149), Direction.Up, Direction.Right), #I
    ((49, 100), Direction.Right, Direction.Down): ((50, 99), Direction.Down, Direction.Right) #H
}
portals = {}

def direction_to_offset(direction):
    radian_direction = direction * (math.pi / 2)
    offset = [int(math.sin(radian_direction)), int(math.cos(radian_direction))]
    return offset

def reverse_direction(direction):
    return (direction + 2) % 4

def generate_portals():
    for start, end in connections.items():
        direction_start = start[2].value
        direction_end = end[2].value
        offset_start = direction_to_offset(start[1].value)
        offset_end = direction_to_offset(end[1].value)
        for x in range(cube_side_length):
            start_location = tuple(map(lambda i,j: i + (j * x), start[0], offset_start))
            end_location = tuple(map(lambda i,j: i + (j * x), end[0], offset_end))
            portals[(start_location, direction_start)] = (end_location, reverse_direction(direction_end))
            portals[(end_location, direction_end)] = (start_location, reverse_direction(direction_start))

def get_next_location(location, direction):
    if((location, direction) in portals):
        return portals[(location, direction)]
    radian_direction = direction * (math.pi / 2)
    offset = [int(math.sin(radian_direction)), int(math.cos(radian_direction))]
    new_location = tuple(map(lambda x, y: x + y, location, offset))
    return new_location, direction

def main():
    global path
    entire_file = open("day22/input.txt").read()
    map_string, path_string = entire_file.split("\n\n")
    for line in map_string.split("\n"):
        board.append([*line])
    path = re.findall(r"(\d+)([LR]?)", path_string)
    generate_portals()
    location = (0, 50)
    direction = 0
    for step in path:
        for x in range(int(step[0])):
            new_location, new_direction = get_next_location(location, direction)
            if(board[new_location[0]][new_location[1]] == "#"):
                break
            location = new_location
            direction = new_direction
            board[location[0]][location[1]] = "A"
        if(step[1] == "R"):
            direction = (direction + 1) % 4
        elif(step[1] == "L"):
            direction = (direction - 1) % 4
    direction_value = (direction % 4)
    print(1000*(location[0]+1) + 4 * (location[1]+1) + direction_value)

if __name__ == "__main__":
    main()