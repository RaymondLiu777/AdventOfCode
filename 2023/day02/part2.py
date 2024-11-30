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
    current = {
        "red": 0,
        "blue": 0,
        "green": 0
    }
    for round in game["rounds"]:
        if(round["red"] > current["red"]):
            current["red"] = round["red"]
        if(round["blue"] > current["blue"]):
            current["blue"] = round["blue"]
        if(round["green"] > current["green"]):
            current["green"] = round["green"]
    total += current["red"] * current["green"] * current["blue"]

# print(gameData)
print(total)


