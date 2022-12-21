line = open("input.txt", "r").readline()
letters = [*line[0:4]]
index = 0
for char in [*line]:
    letters[index%len(letters)] = char
    unique = True
    for x in range(len(letters)):
        for y in range(x + 1, len(letters)):
            if(letters[x] == letters[y]):
                unique = False
    if(unique == True):
        print(index + 1)
        quit()
    index += 1