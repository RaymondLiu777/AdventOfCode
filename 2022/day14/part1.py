

walls = set()
sand_locations = set()
lowest_position = 0
initial_sand_fall = (500,0)

def is_open(x, y):
    if (x,y) in sand_locations:
        return False
    for pointa, pointb in walls:
        if (x in range(min(pointa[0], pointb[0]), max(pointa[0], pointb[0]) + 1) and 
            y in range(min(pointa[1], pointb[1]), max(pointa[1], pointb[1]) + 1)):
            return False
    return True
    

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
    print(lowest_position)
    done = False
    count = 0
    while(not done):
        count += 1
        sand_location = list(initial_sand_fall)
        falling = True
        while(falling):
            if(sand_location[1] > lowest_position):
                done = True
                break
            if(is_open(sand_location[0], sand_location[1] + 1)):
                sand_location[1] += 1
            elif(is_open(sand_location[0] - 1, sand_location[1] + 1)):
                sand_location[0] -= 1
                sand_location[1] += 1
            elif(is_open(sand_location[0] + 1, sand_location[1] + 1)):
                sand_location[0] += 1
                sand_location[1] += 1
            else:
                falling = False
        sand_locations.add(tuple(sand_location))
    print(count - 1)

if __name__ == "__main__":
    main()