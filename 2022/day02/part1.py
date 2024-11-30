file = open("input.txt", "r")
score = 0

shape_score = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

ties = ["A X", "B Y", "C Z"]
wins = ["A Y", "B Z", "C X"]
loses = ["A Z", "B X", "C Y"]

for line in file:
    line = line.strip()
    split_line = line.split()
    if(line in ties):
        score += 3
    elif(line in wins):
        score += 6
    score += shape_score[split_line[1]]
print(score)