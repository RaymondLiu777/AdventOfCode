
def make_set(clist):
    s = set()
    for letter in list(clist):
        s.add(letter)
    return s

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
    file = open("day3/input.txt", "r")
    for line in file:
        line = line.strip()
        s1 = make_set(line[0:len(line)//2])
        s2 = make_set(line[len(line)//2:len(line)])
        total += get_value(s1.intersection(s2))
    print(total)


if __name__ == "__main__":
    main()