file = open("input.txt", "r")

lines = file.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip()
numLines = len(lines)
lineLength = len(lines[0])

total = 0
num = ""
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
                            if(lines[searchRow][searchCol] != "." and not lines[searchRow][searchCol].isnumeric()):
                                done = True
                                total += partNum
                                # print(partNum)
                        if(done):
                            break
                    if(done):
                        break
            num = ""

print(total)