import sys
import pyperclip
sys.path.append('../AoC_Helpers')
from InputParser import InputParser
# from Grid import Directions, Grid
# from TupleOps import TupleOps
# from Graph import Graph
# from functools import cache
from collections import defaultdict

prune_value = 16777216

def hash(secret_num: int):
    step1 = (((secret_num * 64) % prune_value) ^ secret_num) % prune_value
    step2 = (((step1 // 32) % prune_value ) ^ step1) % prune_value
    step3 = (((step2 * 2048) % prune_value) ^ step2) % prune_value
    return step3

def run(filename: str, part1: bool):
    secret_nums = InputParser(open(filename).read()).readLines().getData()
    secret_nums = list(map(int, secret_nums))
    total = 0
    all_prices = []
    # Apply secret number calculation 2000 times
    for secret in secret_nums:
        monkey_prices = [secret % 10]
        for i in range(2000):
            secret = hash(secret)
            monkey_prices.append(secret % 10)
        all_prices.append(monkey_prices)
        # print(secret)
        total += secret
    if(part1):
        return total
    # Check all sequences
    all_sequences = defaultdict(int)
    for prices in all_prices:
        current_sequences = set()
        for i in range(len(prices) - 4):
            price = prices[i+4]
            changes = (prices[i+1] - prices[i], prices[i+2] - prices[i+1], prices[i+3] - prices[i+2], prices[i+4] - prices[i+3])
            if(changes not in current_sequences):
                all_sequences[changes] += price
            current_sequences.add(changes)
    max_bananas = -1
    for sequence, bananas in all_sequences.items():
        if(bananas > max_bananas):
            max_bananas = bananas
            max_sequence = sequence 
    print(max_sequence, max_bananas)
    return max_bananas
    



if __name__ == "__main__" :
    if len(sys.argv) < 3:
        print("Error, requires two command lines arguments: s/i 1/2")
        exit()
    if sys.argv[2] != '1' and sys.argv[2] != '2':
        print("Error invalid command line args:", sys.argv[1], sys.argv[2])
        exit()

    filename = ""
    if sys.argv[1] == 's':
        filename = "sample.txt"
    elif sys.argv[1] == 'i':
        filename = "input.txt"
    else:
        filename = sys.argv[1]

    part1 = (sys.argv[2] == '1')
    result = run(filename, part1)
    print(result)
    pyperclip.copy(str(result))
    