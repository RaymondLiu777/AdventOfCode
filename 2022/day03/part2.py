def get_value(overlap):
    for x in overlap:
        if(x >= "a" and x <= "z"):
            return ord(x) - ord("a") + 1
        elif(x >= "A" and x <= "Z"):
            return ord(x) - ord("A") + 27
    print(overlap)
    raise Exception("Failed value conversion")

def main():
    total = 0
    index = 0
    sets = [set(), set(), set()]
    file = open("day3/input.txt", "r")
    for line in file:
        line = line.strip()
        sets[index%3] = set(line)
        if(index % 3 == 2):
            total += get_value(sets[0].intersection(sets[1]).intersection(sets[2]))
        index += 1
    print(total)


if __name__ == "__main__":
    main()