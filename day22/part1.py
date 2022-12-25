import re
import math

board = []
path = []

def is_valid_square(position):
    if(position[0] < 0 or position[0] >= len(board)):
        return False
    elif(position[1] < 0 or position[1] >= len(board[position[0]])):
        return False
    elif(board[position[0]][position[1]] == " "):
        return False
    return True

def main():
    global path
    entire_file = open("day22/input.txt").read()
    map_string, path_string = entire_file.split("\n\n")
    for line in map_string.split("\n"):
        board.append([*line])
    path = re.findall(r"(\d+)([LR]?)", path_string)
    location = [0, 0]
    direction = 0
    for idx, spot in enumerate(board[0]):
        if(spot == "."):
            location[1] = idx
    for step in path:
        for x in range(int(step[0])):
            radian_direction = direction * (math.pi / 2)
            offset = [int(math.sin(radian_direction)), int(math.cos(radian_direction))]
            new_location = location
            new_location = list(map(lambda x, y: x + y, location, offset))
            if(not is_valid_square(new_location)):
                if(offset[0] != 0):
                    new_location[0] = (new_location[0]) % len(board)
                else:
                    new_location[1] = (new_location[1]) % len(board[new_location[0]])
            while(not is_valid_square(new_location)):
                if(offset[0] != 0):
                    new_location[0] = (new_location[0] + offset[0]) % len(board)
                else:
                    new_location[1] = (new_location[1] + offset[1]) % len(board[new_location[0]])
            if(board[new_location[0]][new_location[1]] != "#"):
                location = new_location
        if(step[1] == "R"):
            direction += 1
        elif(step[1] == "L"):
            direction -= 1
    direction_value = (direction % 4)
    print(1000*(location[0]+1) + 4 * (location[1]+1) + direction_value)

if __name__ == "__main__":
    main()