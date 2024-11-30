monkeys = {}
parent_monkey = {}

def get_value_from_parent(monkey_name):
    parent = monkeys[parent_monkey[monkey_name]]
    if("value" in parent):
        return parent["value"]
    if(parent["name"] == "root"):
        value = 0
        if(parent["first"] == monkey_name):
            value = get_value(parent["second"])
        else:
            value = get_value(parent["first"])
        parent["value"] = value
        return value
    if(parent["first"] == monkey_name):
        second_value = get_value(parent["second"])
        parent_value = get_value_from_parent(parent["name"])
        operator = parent["operator"]
        if(operator == "+"):
            value = parent_value - second_value
        elif(operator == "-"):
            value = parent_value + second_value
        elif(operator == "*"):
            value = parent_value / second_value
        elif(operator == "/"):
            value = parent_value * second_value
        parent["value"] = value
        return parent["value"]
    else:
        first_value = get_value(parent["first"])
        parent_value = get_value_from_parent(parent["name"])
        operator = parent["operator"]
        if(operator == "+"):
            value = parent_value - first_value
        elif(operator == "-"):
            value = first_value - parent_value
        elif(operator == "*"):
            value = parent_value / first_value
        elif(operator == "/"):
            value = first_value / parent_value
        parent["value"] = value
        return parent["value"]


def get_value(monkey_name):
    if(monkey_name == "humn"):
        raise Exception()
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
            if(monkey_job[0] in parent_monkey or monkey_job[2] in parent_monkey):
                raise Exception("Not a tree structure")
            parent_monkey[monkey_job[0]] = monkey_name
            parent_monkey[monkey_job[2]] = monkey_name
        monkeys[monkey_name] = monkey
    print(get_value_from_parent("humn"))

if __name__ == "__main__":
    main()