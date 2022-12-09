current_path = ["/"]
file_tree = { "/" : { } }
total = 0

def go_to_location():
    global current_path
    global file_tree
    current_location = file_tree
    for directory in current_path:
        current_location = current_location[directory]
    return current_location

def find_files(location):
    global total
    if(type(location) == int):
        return location
    else:
        local_total = 0
        for key, value in location.items():
            local_total += find_files(value)
        if(local_total <= 100000):
            total += local_total
        return local_total

def main():
    file = open("day7/input.txt", "r")
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
    print(file_tree)
    find_files(file_tree)
    print("total", total)


if __name__ == "__main__":
    main()