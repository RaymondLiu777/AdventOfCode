import sys
import pyperclip
sys.path.append('../')
import AoC_helpers
import re

def run(filename: str, part1: bool):
    instructions = open(filename).readlines()
    regex_functions = "(mul\([0-9]{1,3},[0-9]{1,3}\))|(don't)|(do)"
    regex_mul = "mul\(([0-9]{1,3}),([0-9]{1,3})\)"
    total = 0
    on = True
    for instruction in instructions:
        muls = re.findall(regex_functions, instruction)
        for mul, dont, do in muls:
            if(dont == "don't"):
                on = False
            elif(do == "do"):
                on = True
            else:
                if on or part1:
                    nums = re.search(regex_mul, mul)
                    total += int(nums.group(1)) * int(nums.group(2))
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

    part1 = (sys.argv[2] == '1')
    result = run(filename, part1)
    print(result)
    pyperclip.copy(str(result))
    