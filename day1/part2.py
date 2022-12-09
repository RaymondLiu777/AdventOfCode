file = open("input.txt", "r")
total = 0
totals = []
for line in file:
    if(line == "\n"):
        totals.append(total)
        total = 0
    else:
        total += int(line)
totals.sort(reverse = True)
print(totals[0] + totals[1] + totals[2])