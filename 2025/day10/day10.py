import sys
import pyperclip
# import z3
from scipy.optimize import linprog
# import networkx as nx
sys.path.append('../AoC_Helpers')
sys.path.append('./2025/AoC_Helpers')
from InputParser import InputParser
# from Grid import Directions, Grid
# from TupleOps import TupleOps
# from Graph import Graph
from functools import lru_cache
# from collections import defaultdict

def get_state_lights(machine_size, buttons, pushed_buttons):
    machine = [False] * machine_size
    for idx, pushed in enumerate(pushed_buttons):
        if(pushed):
            for button in buttons[idx]:
                machine[button] = not machine[button]
    return tuple(machine)

def get_optimal_lights(goal, buttons, pushed_buttons, idx):
    # print(pushed_buttons, idx, get_state(len(goal), buttons, pushed_buttons))
    if(get_state_lights(len(goal), buttons, pushed_buttons) == goal):
        # return tuple(pushed_buttons)
        return sum(filter(lambda x: 1 if x == True else 0, pushed_buttons))
    if(idx >= len(pushed_buttons)):
        return len(goal) + 1
    opt1 = get_optimal_lights(goal, buttons, pushed_buttons, idx+1)
    pushed_buttons[idx] = True
    opt2 = get_optimal_lights(goal, buttons, pushed_buttons, idx+1)
    pushed_buttons[idx] = False
    return min(opt1, opt2)

# @lru_cache(maxsize=1000)
# def get_optimal_joltage(goal, button_set, idx):
#     # print(" " * idx, goal, idx)
#     if(sum(map(lambda x: 1 if x != 0 else 0, goal)) == 0):
#         # print(goal)
#         return 0
#     if(idx >= len(button_set)):
#         return -1
#     smallest_solution = -1
#     machine = list(goal)
#     presses = 0
#     while True:
#         solution = get_optimal_joltage(tuple(machine), button_set, idx + 1)
#         if(solution != -1):
#             solution += presses
#             if(smallest_solution == -1):
#                 smallest_solution = solution
#             if(solution < smallest_solution):
#                 smallest_solution = solution
#         incorrect = False
#         for button in button_set[idx]:
#             machine[button] -= 1
#             if(machine[button] < 0):
#                 incorrect = True
#                 break
#         presses += 1
#         if incorrect:
#             break
#     return smallest_solution

def get_optimal_joltage(goal, button_set):
    c = [1] * len(button_set)
    A = [[0 for x in range(len(button_set))] for y in range(len(goal))]
    b = list(goal)
    for idx, buttons in enumerate(button_set):
        for button in buttons:
            A[button][idx] = 1
    # print(A, b, c)
    result = linprog(c, A_eq=A, b_eq=b, integrality=3)
    # print(result)
    return int(sum(result.x)) if result.success else -1
    
        

def run(filename: str, part1: bool):
    data = InputParser(open(filename).read()).readLines().getData()
    machines = []
    for line in data:
        parts = line.split()
        machine = {}
        machine['goal'] = tuple(map(lambda x: x=="#", parts[0][1:-1]))
        machine['joltage'] = tuple(map(int, parts[-1][1:-1].split(",")))
        machine['buttons'] = []
        for button in parts[1:-1]:
            buttons = tuple(map(int, button[1:-1].split(",")))
            machine['buttons'].append(buttons)
        machines.append(machine)
    # print(machines)
    total = 0
    for machine in machines:
        if(part1):
            optimal = get_optimal_lights(machine['goal'], machine['buttons'], [False] * len(machine['buttons']), 0)
        else:
            optimal = get_optimal_joltage(machine['joltage'], tuple(machine['buttons']))
            if(optimal == -1):
                print("Error, no solution for ", machine)
        # print(optimal)
        total += optimal
    return total


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
    