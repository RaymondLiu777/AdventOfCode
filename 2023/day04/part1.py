file = open("input.txt", "r")

cards = []
for line in file:
    split = line.strip().split(":")
    cardNum = int(split[0].split()[1])
    numbers = split[1].split("|")
    winning = list(map(lambda x: int(x), numbers[0].split()))
    yourNums = list(map(lambda x: int(x), numbers[1].split()))
    cards.append({
        "id": cardNum,
        "wins": winning,
        "yours": yourNums
    })

total = 0
for card in cards:
    numMatches = 0
    for winningNum in card["wins"]:
        if winningNum in card["yours"]:
            numMatches += 1
    if numMatches != 0:
        total += pow(2, numMatches - 1)

print(total)
