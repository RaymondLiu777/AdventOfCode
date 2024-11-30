file = open("input.txt", "r")

cards = []
for line in file:
    split = line.strip().split(":")
    cardNum = int(split[0].split()[1])
    numbers = split[1].split("|")
    winning = list(map(lambda x: int(x), numbers[0].split()))
    yourNums = list(map(lambda x: int(x), numbers[1].split()))

    # Calculate wins
    numMatches = 0
    for winningNum in winning:
        if winningNum in yourNums:
            numMatches += 1

    cards.append({
        "id": cardNum,
        "wins": winning,
        "yours": yourNums,
        "score": numMatches,
    })

numEach = [1] * len(cards)
for i in range(len(cards)):
    for j in range(cards[i]["score"]):
        if(i + j + 1 < len(numEach)):
            numEach[i + j + 1] += numEach[i]

print(sum(numEach))
