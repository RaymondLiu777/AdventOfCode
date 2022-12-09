import re

def completely_overlap(min1, max1, min2, max2):
    if min1 >= min2 and max1 <= max2:
        return True
    if min2 >= min1 and max2 <= max1:
        return True
    return False

def main():
    file = open("day4/input.txt")
    total = 0
    for line in file:
        values = list(map(int, line.strip().replace("-", ",").split(",")))
        if(completely_overlap(values[0], values[1], values[2], values[3])):
            total += 1
    print(total)



if __name__ == "__main__":
    main()