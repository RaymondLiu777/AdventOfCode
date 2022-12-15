queue = []
explored = set()
height_map = []

start = []
end = []

directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def main():
    #Parsing
    file = open("day12/input.txt")
    row = 0
    for line in file:
        height_map.append([])
        for col, char in enumerate(line.strip()):
            if(char == "S"):
                height_map[row].append(0)
            elif(char == "E"):
                start.append(row)
                start.append(col)
                height_map[row].append(ord("z") - ord("a"))
            else:
                height_map[row].append(ord(char) - ord("a"))
        row += 1
    #BFS
    queue.append({
        "location": [start[0], start[1]],
        "distance": 0
    })
    while(len(queue) > 0):
        item = queue.pop(0)
        location = item["location"]
        height = height_map[location[0]][location[1]]
        if str(location) in explored:
            continue
        if(height == 0):
            print(item["distance"])
            break
        for row,col in directions:
            new_location = [location[0] + row, location[1] + col]
            if(new_location[0] < 0 or new_location[0] >= len(height_map) or new_location[1] < 0 or new_location[1] >= len(height_map[0])):
                continue
            if(height_map[new_location[0]][new_location[1]] - height >= -1):
                queue.append({
                    "location": new_location,
                    "distance": item["distance"] + 1
                })
        explored.add(str(location))
    print("done")    


if __name__ == "__main__":
    main()