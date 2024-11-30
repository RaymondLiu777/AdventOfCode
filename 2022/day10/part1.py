
register_value = [1]
signals = [20, 60, 100, 140, 180, 220]

def main():
    file = open("day10/input.txt")
    for line in file:
        split_line = line.strip().split()
        if(split_line[0] == "noop"):
            register_value.append(register_value[len(register_value) - 1])
        elif(split_line[0] == "addx"):
            register_value.append(register_value[len(register_value) - 1])
            register_value.append(register_value[len(register_value) - 1] + int(split_line[1]))
        else:
            raise Exception("Fail to interpret command")
    # print(register_value)
    total = 0
    for x in signals:
        total += x * register_value[x - 1]
    print(total)        

if __name__ == "__main__":
    main()