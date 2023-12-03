file = open("input.txt", "r")

lines = file.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip()
numLines = len(lines)
lineLength = len(lines[0])

total = 0
num = ""
gears = {}
for row, line in enumerate(lines):
    for col, char in enumerate(line):
        if char.isnumeric():
            num += char
        if col + 1 >= len(line) or not line[col + 1].isnumeric():
            if(num != ""):
                partNum = int(num)
                # Search for symbol
                startRow = row - 1
                startCol = col - len(num)
                done = False
                for i in range(3):
                    for j in range(len(num) + 2):
                        searchRow = startRow + i
                        searchCol = startCol + j
                        if(searchRow >= 0 and searchRow < numLines and searchCol >= 0 and searchCol < lineLength):
                            if lines[searchRow][searchCol] == "*":
                                done = True
                                location = (searchRow, searchCol)
                                if location not in gears:
                                    gears[location] = []
                                gears[location].append(partNum)
                                # print(partNum)
                        if(done):
                            break
                    if(done):
                        break
            num = ""

for key, value in gears.items():
    if(len(value) == 2) :
        total += value[0] * value[1]

print(total)