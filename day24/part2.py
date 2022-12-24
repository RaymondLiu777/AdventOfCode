import math
import heapq

blizzards = []
blizzard_timeline = []
board_size = (0, 0)
possible_moves = [
    (0, 0),
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
]

def get_pq_tuple(position, time, goal):
    h_value = abs(goal[0] - position[0]) + abs(goal[1] - position[1])
    f_value = h_value + time
    return (f_value, time, h_value, position)

def increase_blizzard_timeline():
    time = len(blizzard_timeline)
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
    if(position == (-1, 0) or position == (board_size[0], board_size[1] - 1)):
        return True
    if(position[0] < 0 or position[0] >= board_size[0] or position[1] < 0 or position[1] >= board_size[1]):
        return False
    return not blizzard_timeline[time][position[0]][position[1]]

def AStar(intial_time, intial_position, goal):
    #tuple is (f value, h value (mattahattan distance), g value (time), location)
    pq = []
    closed_set = set()
    step = get_pq_tuple(intial_position, intial_time, goal)
    heapq.heappush(pq, step) 
    closed_set.add(step)
    while (len(pq) > 0):
        top = heapq.heappop(pq)
        time = top[1]
        location = top[3]
        if(location == goal):
            return time
        for move in possible_moves:
            next_location = tuple(map(sum, zip(location, move)))
            if(valid_position(next_location, time + 1)):
                step = get_pq_tuple(next_location, time + 1, goal)
                if(step not in closed_set):
                    heapq.heappush(pq, step)
                    closed_set.add(step)

def main():
    global board_size
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
    intial_position = (-1, 0)
    trip1 = AStar(intial_time, intial_position, goal)
    trip2 = AStar(trip1, goal, intial_position)
    trip3 = AStar(trip2, intial_position, goal)
    print(trip1, trip2, trip3)

    


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