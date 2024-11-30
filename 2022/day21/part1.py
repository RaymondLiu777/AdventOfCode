monkeys = {}

def get_value(monkey_name):
    monkey = monkeys[monkey_name]
    if("value" in monkey):
        return monkey["value"]
    else:
        first_monkey = get_value(monkey["first"])
        second_monkey = get_value(monkey["second"])
        operator = monkey["operator"]
        value = 0
        if(operator == "+"):
            value = first_monkey + second_monkey
        elif(operator == "-"):
            value = first_monkey - second_monkey
        elif(operator == "*"):
            value = first_monkey * second_monkey
        elif(operator == "/"):
            value = first_monkey / second_monkey
        else:
            raise Exception("Could not parse operator " + operator)
        monkey["value"] = value
        return monkey["value"]

def main():
    file = open("day21/input.txt")
    for line in file:
        split = line.strip().split(": ")
        monkey_name = split[0]
        monkey_job = split[1].split()
        monkey = {
            "name": monkey_name
        }
        if(len(monkey_job) == 1):
            monkey["value"] = int(monkey_job[0])
        else:
            monkey["first"] = monkey_job[0]
            monkey["operator"] = monkey_job[1]
            monkey["second"] = monkey_job[2]
        monkeys[monkey_name] = monkey
    print(get_value("root"))



if __name__ == "__main__":
    main()