import sys

walls = set()
sand_locations = set()
lowest_position = 0
initial_sand_fall = (500,0)

def is_open(position):
    if position in sand_locations:
        return False
    for pointa, pointb in walls:
        if (position[0] in range(min(pointa[0], pointb[0]), max(pointa[0], pointb[0]) + 1) and 
            position[1] in range(min(pointa[1], pointb[1]), max(pointa[1], pointb[1]) + 1)):
            return False
    return True
    
def bfs(position):
    if(not is_open(position)):
        return 0
    else:
        sand_locations.add(position)
        total = 1
        total += bfs((position[0], position[1] + 1))
        total += bfs((position[0] + 1, position[1] + 1))
        total += bfs((position[0] - 1, position[1] + 1))
        return total


def main():
    global lowest_position
    file = open("day14/input.txt")
    for line in file:
        positions = [s.split(",") for s in line.strip().split(" -> ")]
        for position in positions:
            x = int(position[0])
            y = int(position[1])
            position.clear()
            position.append(x)
            position.append(y)
            lowest_position = max(lowest_position, y)
        for i in range(len(positions) - 1):
            walls.add((tuple(positions[i]), tuple(positions[i+1])))
    walls.add(((-sys.maxsize - 1, lowest_position + 2), (sys.maxsize, lowest_position + 2)))
    print(bfs(initial_sand_fall))

if __name__ == "__main__":
    main()