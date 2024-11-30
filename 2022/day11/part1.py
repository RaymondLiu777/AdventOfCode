import re

regex1 = r"\s*Monkey (\d):\s*"
regex2 = r"Starting items: ([\d, ]*)\n"
regex3 = r"\s*Operation: new = old ([*+]) (\d+|old)\n"
regex4 = r"\s*Test: divisible by (\d+)\n"
regex5 = r"\s*If true: throw to monkey (\d+)\n"
regex6 = r"\s*If false: throw to monkey (\d+)"
monkey_regex = regex1 + regex2 + regex3 + regex4 + regex5 + regex6

monkeys = []
monkey_items = []

def main():
    global monkey_items
    file = open("day11/input.txt")
    monkey_file = file.read().strip().split("\n\n")
    for monkey_string in monkey_file:
        result = re.search(monkey_regex, monkey_string)
        monkeys.append({
            "Operation": result.group(3),
            "Operation Value": result.group(4),
            "Test": int(result.group(5)),
            "True": int(result.group(6)),
            "False": int(result.group(7)),
            "Inspections": 0
        })
        monkey_items.append(list(map(int, result.group(2).split(", "))))
    print(monkeys)
    print(monkey_items)
    for x in range(20):
        for i, stack in enumerate(monkey_items):
            monkey = monkeys[i]
            while len(stack) > 0:
                item = stack[0]
                operation_value = item if monkey["Operation Value"] == "old" else int(monkey["Operation Value"])
                if(monkey["Operation"] == "*"):
                    item *= operation_value
                elif(monkey["Operation"] == "+"):
                    item += operation_value
                else:
                    raise Exception("Fail to interpret operation")
                item = item // 3
                stack.pop(0)
                if(item % monkey["Test"] == 0):
                    monkey_items[monkey["True"]].append(item)
                else:
                    monkey_items[monkey["False"]].append(item)
                monkey["Inspections"] += 1
    print(monkey_items)
    totals = []
    for monkey in monkeys:
        totals.append(monkey["Inspections"])
    totals.sort(reverse=True)
    print(totals)
    print(totals[0] * totals[1])

if __name__ == "__main__":
    main()