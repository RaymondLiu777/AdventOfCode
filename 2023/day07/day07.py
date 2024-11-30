import sys
import pyperclip
from collections import Counter

def checkForTwoDoubles(handCounter):
    numTwos = 0
    for value in handCounter:
        if(value == 2):
            numTwos += 1
    return numTwos == 2

def part1(filename):
    hands = []
    file = open(filename)
    replace_values = [("A", "F"), ("K", "E"), ("Q","D"), ("J","C"), ("T", "B")]
    for line in file:
        hand, bid = line.strip().split()
        for value in replace_values:
            hand = hand.replace(value[0], value[1])
        counter = Counter(hand)
        typeValue = 0
        if 5 in counter.values():
            typeValue = 7
        elif 4 in counter.values():
            typeValue = 6
        elif 3 in counter.values() and 2 in counter.values():
            typeValue = 5
        elif 3 in counter.values():
            typeValue = 4
        elif checkForTwoDoubles(counter.values()):
            typeValue = 3
        elif 2 in counter.values():
            typeValue = 2
        else:
            typeValue = 1
        hands.append({
            "hand": hand,
            "value": typeValue,
            "bid": int(bid)
        })
    sortedHands = sorted(hands, key = lambda hand: (hand["value"], hand["hand"]))
    # print(sortedHands)
    total = 0
    for idx, hand in enumerate(sortedHands, 1):
        total += idx * hand["bid"]
    return total

def calculateType(handCounter):
    jokers = handCounter["1"]
    handCounter["1"] = 0
    most = max(handCounter.values())
    for key, value in handCounter.items():
        if value == most:
            handCounter[key] = 0
            break
    most += jokers
    if(most == 5):
        return 7
    elif(most == 4):
        return 6
    elif(most == 3):
        if 2 in handCounter.values():
            return 5
        else:
            return 4
    elif(most == 2):
        if 2 in handCounter.values():
            return 3
        else:
            return 2
    else:
        return 1
    
def part2(filename):
    hands = []
    file = open(filename)
    replace_values = [("A", "F"), ("K", "E"), ("Q","D"), ("J","1"), ("T", "B")]
    for line in file:
        hand, bid = line.strip().split()
        for value in replace_values:
            hand = hand.replace(value[0], value[1])
        counter = Counter(hand)
        typeValue = calculateType(counter)
        hands.append({
            "hand": hand,
            "value": typeValue,
            "bid": int(bid)
        })
    sortedHands = sorted(hands, key = lambda hand: (hand["value"], hand["hand"]))
    # print(sortedHands)
    total = 0
    for idx, hand in enumerate(sortedHands, 1):
        total += idx * hand["bid"]
    return total



if __name__ == "__main__" :
    if len(sys.argv) < 3:
        print("Error, requires two command lines arguments: s/i 1/2")
        exit()
    if (sys.argv[1] != 's' and sys.argv[1] != 'i') or (sys.argv[2] != '1' and sys.argv[2] != '2'):
        print("Error invalid command line args:", sys.argv[1], sys.argv[2])
        exit()

    filename = ""
    if sys.argv[1] == 's':
        filename = "sample.txt"
    elif sys.argv[1] == 'i':
        filename = "input.txt"

    result = ""
    if sys.argv[2] == '1':
        result = part1(filename)
    elif sys.argv[2] == '2':
        result = part2(filename)
    print(result)
    pyperclip.copy(result)
    