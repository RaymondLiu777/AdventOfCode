import sys
import pyperclip
sys.path.append('../')
import AoC_helpers
import numpy

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
    circuit_info = {}
    important_circuits = ["br", "rz", "lf", "fk"]
    for circuit in important_circuits:
        circuit_info[circuit] = []
    append_later = []
    for circuit_name, circuit in circuits.items():
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
    i = 0
    limit = 1000 if part1 else 5000
    while(i < limit):
        i += 1
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
            if(circuit_name in important_circuits and next_pulse == "high"):
                circuit_info[circuit_name] = i
            for destination in circuit["destinations"]:
                queue.append((destination, next_pulse, circuit_name))
    if(part1):
        return low_pulses * high_pulses
    else:
        # Find cycles and calculate lcm
        return numpy.lcm.reduce(list(circuit_info.values()))

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

# Failed optimization attempt
def generateState(circuits, flip_flop_ids, conjunction_ids):
    state = []
    # print(flip_flop_ids, conjunction_ids, circuits)
    for ff in flip_flop_ids.keys():
        state.append(circuits[ff]["ff_status"] == "on")
    for cj in conjunction_ids.keys():
        inputs = []
        for input in circuits[cj]["inputs"].values():
            inputs.append(input == "high")
        state.append(tuple(inputs))
    return tuple(state)

def calculateChanges(start_state, end_state, num_ff, num_cj):
    state = []
    for i in range(num_ff):
        state.append(start_state[i] != end_state[i])
    for i in range(num_ff, num_ff + num_cj):
        inputs = []
        for j in range(len(start_state[i])):
            inputs.append(start_state[i][j] != end_state[i][j])
        state.append(tuple(inputs))
    return tuple(state)

def part2_Attempt1(filename: str, part1: bool):
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
    flip_flop_ids = {}
    conjunction_ids = {}
    append_later = []
    for circuit_name, circuit in circuits.items():
        if(circuit["type"] == "ff"):
            flip_flop_ids[circuit_name] = len(flip_flop_ids)
        if(circuit["type"] == "cj"):
            conjunction_ids[circuit_name] = len(conjunction_ids)
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
    i = 0
    done = False
    states = []
    num_ff = len(flip_flop_ids)
    num_cj = len(conjunction_ids)
    # Store state of circuit
    start_state = generateState(circuits, flip_flop_ids, conjunction_ids)
    while(not done):
        # print("Start state: ", start_state)
        touches = [False] * (num_ff + num_cj)
        skipped = False
        i += 1
        for state in states:
            skip_state = True
            for idx, value in enumerate(state["touches"]):
                if(value):
                    # ff state
                    if(state["start"][idx] != start_state[idx]):
                        skip_state = False
                        break
            if(skip_state):
                # Apply updates and continue
                for key, value in flip_flop_ids.items():
                    if(state["changes"][value] == True):
                        circuits[key]["ff_status"] = "off" if circuits[key]["ff_status"] == "on" else "on"
                for key, value in conjunction_ids.items():
                    for idx, (input, pulse) in enumerate(circuits[key]["inputs"].items()):
                        if(state["changes"][value + num_ff][idx]):
                            circuits[key]["inputs"][input] = "high" if pulse == "low" else "low"
                skipped = True
                break
        if(skipped):
            start_state = generateState(circuits, flip_flop_ids, conjunction_ids)
            print("skipped")
            continue
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
                touches[flip_flop_ids[circuit_name]] = True
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
                touches[conjunction_ids[circuit_name] + len(flip_flop_ids)] = True
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
                if(destination == "rx" and next_pulse == "low"):
                    done = True
        # Generate End State
        end_state = generateState(circuits, flip_flop_ids, conjunction_ids)
        changes = calculateChanges(start_state, end_state, num_ff, num_cj)
        states.append({
            "start": start_state,
            "changes": changes,
            "touches": touches
        })
        # print(start_state, "\n", end_state, "\n", changes, "\n", touches, "\n")
        print(i)
        start_state = end_state
    return i