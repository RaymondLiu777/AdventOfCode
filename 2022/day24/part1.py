import math
import heapq

blizzards = []
blizzard_timeline = []
board_size = (0, 0)
intial_position = (-1, 0)
goal = (0, 0)
possible_moves = [
    (0, 0),
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
]

def get_pq_tuple(position, time):
    h_value = (goal[0] - position[0]) + (goal[1] - position[1])
    f_value = h_value + time
    return (f_value, time, h_value, position)

def increase_blizzard_timeline():
    time = len(blizzard_timeline)
    print(time)
    board = [[False for i in range(board_size[1])] for j in range(board_size[0])]
    for blizzard in blizzards:
        radian_direction = blizzard["direction"] * (math.pi / 2)
        offset = [int(math.sin(radian_direction)), int(math.cos(radian_direction))]
        location = list(map(lambda x,y,z: (x + y*time) % z, blizzard["position"], offset, board_size))
        board[location[0]][location[1]] = True
    blizzard_timeline.append(board)

def valid_position(position, time):
    while(time >= len(blizzard_timeline)):
        increase_blizzard_timeline()
    if(position == intial_position or position == goal):
        return True
    if(position[0] < 0 or position[0] >= board_size[0] or position[1] < 0 or position[1] >= board_size[1]):
        return False
    return not blizzard_timeline[time][position[0]][position[1]]

def main():
    global board_size
    global goal
    file = open("day24/input.txt").read().split("\n")
    # Parse input
    board_size = (len(file) - 2, len(file[0]) - 2)
    goal = (board_size[0], board_size[1] - 1)
    for row, line in enumerate(file):
        for col, char in enumerate(line):
            if(char == "#" or char == "."):
                continue
            blizzard = {
                "position": [row - 1, col - 1]
            }
            if(char == ">"):
                blizzard["direction"] = 0
            elif(char == "v"):
                blizzard["direction"] = 1
            elif(char == "<"):
                blizzard["direction"] = 2
            elif(char == "^"):
                blizzard["direction"] = 3
            blizzards.append(blizzard)
    intial_time = 0
    #tuple is (f value, h value (mattahattan distance), g value (time), location)
    pq = []
    closed_set = set()
    heapq.heappush(pq, get_pq_tuple(intial_position, intial_time)) 
    closed_set.add(get_pq_tuple(intial_position, intial_time))
    while (len(pq) > 0):
        top = heapq.heappop(pq)
        time = top[1]
        location = top[3]
        if(location == goal):
            print(time)
            break
        for move in possible_moves:
            next_location = tuple(map(sum, zip(location, move)))
            if(valid_position(next_location, time + 1)):
                if(get_pq_tuple(next_location, time + 1) not in closed_set):
                    heapq.heappush(pq, get_pq_tuple(next_location, time + 1))
                    closed_set.add(get_pq_tuple(next_location, time + 1))


def print_blizzard(timestamp):
    time = blizzard_timeline[timestamp]
    for row in time:
        for col in row:
            if(col):
                print("#", end="")
            else:
                print(".", end="")
        print()

if __name__ == "__main__":
    main()