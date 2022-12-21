file = open("input.txt", "r")
score = 0

game_score = {
    "X": 0,
    "Y": 3,
    "Z": 6
}

shape_score = {
    "A X": 3,
    "B X": 1,
    "C X": 2,
    "A Y": 1,
    "B Y": 2,
    "C Y": 3,
    "A Z": 2,
    "B Z": 3,
    "C Z": 1
}

for line in file:
    line = line.strip()
    split_line = line.split()
    score += shape_score[line]
    score += game_score[split_line[1]]
print(score)