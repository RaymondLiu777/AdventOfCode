file = open("input.txt", "r")

total = 0
for line in file:
    first = -1
    last = -1
    for character in line:
        if character.isnumeric():
            if(first == -1):
                first = int(character)
            last = int(character)
    total += first * 10 + last

print(total)