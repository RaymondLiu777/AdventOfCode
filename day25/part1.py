

number_converter = {
    "2": 2,
    "1": 1,
    "0": 0,
    "-": -1,
    "=": -2
}

def main():
    file = open("day25/input.txt")
    total = [0] * 25
    for line in file:
        line = line.strip()
        carry = 0
        for x in range(len(line)):
            new_value = number_converter[line[len(line) - 1 - x]]
            total_position = len(total) - x - 1
            update_value = new_value + total[total_position] + carry
            if(update_value >= 3):
                update_value -= 5
                carry = 1
            elif(update_value <= -3):
                update_value += 5
                carry = -1
            else:
                carry = 0
            total[total_position] = update_value
        idx = len(total) - len(line) - 1
        while carry != 0:
            update_value = total[idx] + carry
            if(update_value >= 3):
                update_value -= 5
                carry = 1
            elif(update_value <= -3):
                update_value += 5
                carry = -1
            else:
                carry = 0
            total[idx] = update_value
            idx -= 1
        for value in total:
            if(value >= 0):
                print(value, end="")
            elif(value == -1):
                print("-", end="")
            elif(value == -2):
                print("=", end="")
            else:
                print("X")
        print()
        



if __name__ == "__main__":
    main()