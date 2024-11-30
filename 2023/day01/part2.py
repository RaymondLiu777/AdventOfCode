file = open("input.txt", "r")

replaceDict = [("one", "one1one"), ("two", "two2two"), ("three", "three3three"), ("four", "four4four"), ("five", "five5five"), 
               ("six", "six6six"), ("seven", "seven7seven"), ("eight", "eight8eight"), ("nine", "nine9nine")]
total = 0
for line in file:
    for word, number in replaceDict:
        line = line.replace(word, number)
    first = -1
    last = -1
    for character in line:
        if character.isnumeric():
            if(first == -1):
                first = int(character)
            last = int(character)
    total += first * 10 + last
print(total)