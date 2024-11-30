
register_value = [1]
screen = []

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
    for x in range(len(register_value)):
        if(abs(register_value[x] - (x % 40)) <= 1):
            screen.append("#")
        else:
            screen.append(".")
    for x in range(6):
        for y in range(40):
            print(screen[x * 40 + y], end = "")
        print("")

if __name__ == "__main__":
    main()