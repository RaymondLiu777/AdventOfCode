import sys
import pyperclip
sys.path.append('../')
import AoC_helpers

def run(filename: str, part1: bool):
    input_workflows, input_parts = open(filename).read().split("\n\n")
    workflows = {}
    for workflow in input_workflows.split():
        name, rules_input = AoC_helpers.parseLine(workflow.strip(), "{", "}")
        rules = []
        for rule in rules_input.split(","):
            if(":" in rule):
                condition, destination = rule.split(":")
                category = condition[0]
                operator = condition[1]
                value = condition[2:]
                rules.append({
                    "category": category,
                    "operator": operator,
                    "value": int(value),
                    "destination": destination
                })
            else:
                rules.append({"destination": rule})
        workflows[name] = rules
        # print(name, rules)
    parts = []
    for part in input_parts.split():
        x, m, a, s = map(int, AoC_helpers.parseLine(part.strip(), "{x=", ",m=", ",a=", ",s=", "}"))
        parts.append({
            "x": x,
            "m": m,
            "a": a,
            "s": s
        })
    if(part1):
        valid_parts = []
        for part in parts:
            name = "in"
            while(True):
                workflow = workflows[name]
                for rule in workflow:
                    if("category" not in rule.keys()):
                        name = rule["destination"]
                        break
                    if(rule["operator"] == ">"):
                        if(part[rule["category"]] > rule["value"]):
                            name = rule["destination"]
                            break
                    elif(rule["operator"] == "<"):
                        if(part[rule["category"]] < rule["value"]):
                            name = rule["destination"]
                            break
                    else:
                        raise Exception(rule)
                if name == "A" or name == "R":
                    if name == "A":
                        valid_parts.append(part)
                    break
        total = sum([sum(part.values()) for part in valid_parts])
        return total
    else:
        queue = []
        queue.append(({
            "x": (1, 4001),
            "m": (1, 4001),
            "a": (1, 4001),
            "s": (1, 4001),
        }, "in"))
        valid_parts = []
        while len(queue) > 0:
            section, destination = queue[0]
            queue = queue[1:]
            if destination == "A" or destination == "R":
                if destination == "A":
                    valid_parts.append(section)
                continue
            workflow = workflows[destination]
            for rule in workflow:
                if("category" not in rule.keys()):
                    destination = rule["destination"]
                    queue.append((section, destination))
                    break
                # Figure out how to split parts of each section
                category_range = section[rule["category"]]
                # Range only on one side of rule
                if(category_range[0] >= rule["value"] or category_range[1] < rule["value"]):
                    continue
                else:
                    # Rule break range in half
                    new_range = [category_range[0], 0]
                    old_range = [0, category_range[1]] 
                    if(rule["operator"] == ">"):
                        new_range[1] = rule["value"] + 1
                        old_range[0] = rule["value"] + 1
                    elif(rule["operator"] == "<"):
                        new_range[1] = rule["value"]
                        old_range[0] = rule["value"]
                        new_range, old_range = old_range, new_range
                    else:
                        raise Exception(rule)
                    # move old range into new section
                    new_section = {
                        "x": section["x"],
                        "m": section["m"],
                        "a": section["a"],
                        "s": section["s"],
                    }
                    new_section[rule["category"]] = tuple(old_range)
                    queue.append((new_section, rule["destination"]))
                    # Keep new range
                    section[rule["category"]] = tuple(new_range)
        total = 0
        for part in valid_parts:
            num_parts = 1
            for cat in part.values():
                num_parts *= (cat[1] - cat[0])
            total += num_parts
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
    