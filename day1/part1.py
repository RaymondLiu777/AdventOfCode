file = open("input.txt", "r")
total = 0
max = 0
for line in file:
    if(line == "\n"):
        if(total > max):
            max = total
        total = 0
    else:
        total += int(line)
print(max)