current_path = ["/"]
file_tree = { "/" : { } }
best = 1000000000
size = 0

def go_to_location():
    current_location = file_tree
    for directory in current_path:
        current_location = current_location[directory]
    return current_location

def get_size(location):
    if(type(location) == int):
        return location
    else:
        local_total = 0
        for key, value in location.items():
            local_total += get_size(value)
        return local_total

def get_best(location):
    # global best
    if(type(location) == int):
        return location
    else:
        local_total = 0
        for key, value in location.items():
            local_total += get_best(value)
        if(local_total > size - (70000000 - 30000000) and local_total < best):
            best = local_total
        return local_total

def main():
    global size
    file = open("input.txt", "r")
    for line in file:
        line = line.strip().split(" ")
        if (line[0] == "$") :
            if(line[1] == "cd"):
                if(line[2] == ".."):
                    current_path.pop()
                elif(line[2] == "/"):
                    current_path.clear()
                    current_path.append("/")
                else:
                    current_path.append(line[2])
            elif(line[1] == "ls"):
                continue
        else:
            if(line[0] == "dir"):
                go_to_location().update({line[1]: {} })
            else:
                go_to_location().update({line[1]: int(line[0])})
    size = get_size(file_tree)
    get_best(file_tree)
    print("best", best)


if __name__ == "__main__":
    main()