file = open("input.txt", "r")

gameData = []
for line in file:
    split = line.split(":")
    gameNum = int(split[0].split()[1])
    rounds = split[1].strip().split(";")
    newGame = {
        "id": gameNum,
        "rounds":[],
    }
    for round in rounds:
        parts = round.split(",")
        newRound = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        for part in parts:
            split2 = part.split()
            amount = int(split2[0])
            color = split2[1].strip()
            newRound[color] = amount
        newGame["rounds"].append(newRound)
    gameData.append(newGame)

total = 0
for game in gameData:
    possible = True
    for round in game["rounds"]:
        if(round["red"] > 12 or round["green"] > 13 or round["blue"] > 14):
            possible = False
    if possible:
        total += game["id"]

# print(gameData)
print(total)


