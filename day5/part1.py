import re

stacks = [
    [],
    ["D", "L", "V", "T", "M", "H", "F"],
    ["H", "Q", "G", "J", "C", "T", "N", "P"],
    ["R", "S", "D", "M", "P", "H"],
    ["L", "B", "V", "F"],
    ["N", "H", "G", "L", "Q"],
    ["W", "B", "D", "G", "R", "M", "P"],
    ["G", "M", "N", "R", "C", "H", "L", "Q"],
    ["C", "L", "W"],
    ["R", "D", "L", "Q", "J", "Z", "M", "T"]
]

regex = "move (\d+) from (\d+) to (\d+)"

def main():
    file = open("day5/input.txt").read()
    for line in file.split("\n\n")[1].split("\n"):
        result = re.search(regex, line.strip())
        stack = []
        for x in range(int(result.group(1))):
            box = stacks[int(result.group(2))].pop()
            stack.append(box)
        for item in stack:
            stacks[int(result.group(3))].append(item)
    print(stacks)
    for stack in stacks[1:]:
        print(stack[len(stack) - 1], end="")

if __name__ == "__main__":
    main()