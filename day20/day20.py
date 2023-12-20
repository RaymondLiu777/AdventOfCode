import sys
import pyperclip
sys.path.append('../')
import AoC_helpers

def run(filename: str, part1: bool):
    circuits = {}
    for line in open(filename):
        name, destinations = line.strip().split(" -> ")
        module = ""
        if("%" in name):
            module = "ff"
            name = name[1:]
        if("&" in name):
            module = "cj"
            name = name[1:]
        if(name == "broadcaster"):
            module = "bc"
        circuits[name] = {
            "type": module,
            "destinations": destinations.split(", "),
            "inputs": {},
            "ff_status": "off",
            "last_pulse": "",
        }
    flip_flop_ids = []
    append_later = []
    for circuit_name, circuit in circuits.items():
        if(circuit["type"] == "ff"):
            flip_flop_ids.append(circuit_name)
        for destination in circuit["destinations"]:
            if(destination not in circuits):
                append_later.append((destination, {
                    "type": "end",
                    "destinations": [],
                    "inputs": {},
                    "ff_status": "off",
                }))
            else:
                circuits[destination]["inputs"][circuit_name] = "low"
    for key, value in append_later:
        circuits[key] = value
    # Loop button presses and save state
    low_pulses = 0
    high_pulses = 0
    for i in range(1000):
        queue = [("broadcaster", "low", "button")]
        while len(queue) > 0:
            # print(queue[0])
            circuit_name, pulse, source = queue[0]
            circuit = circuits[circuit_name]
            queue = queue[1:]
            next_pulse = ""
            if(pulse == "low"):
                low_pulses += 1
            else:
                high_pulses += 1
            if circuit["type"] == "ff":
                if(pulse == "low"):
                    if circuit["ff_status"] == "off":
                        circuit["ff_status"] = "on"
                        next_pulse = "high"
                    else:
                        circuit["ff_status"] = "off"
                        next_pulse = "low"
                else:
                    continue
            elif circuit["type"] == "cj":
                circuit["inputs"][source] = pulse
                if sum([val == "high" for val in circuit["inputs"].values()]) == len(circuit["inputs"]):
                    next_pulse = "low"
                else:
                    next_pulse = "high"
            elif circuit["type"] == "bc":
                next_pulse = pulse
            elif circuit["type"] == "end":
                pass
            else:
                raise Exception(circuit)
            for destination in circuit["destinations"]:
                queue.append((destination, next_pulse, circuit_name))
    print(low_pulses, high_pulses, low_pulses * high_pulses)
    return low_pulses * high_pulses

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
    