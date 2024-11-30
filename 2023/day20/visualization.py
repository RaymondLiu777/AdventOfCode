from pyvis.network import Network
net = Network(directed=True)

circuits = {}
for line in open("input.txt"):
    name, destinations = line.strip().split(" -> ")
    module = ""
    if("%" in name):
        module = "%"
        name = name[1:]
    if("&" in name):
        module = "&"
        name = name[1:]
    if(name == "broadcaster"):
        module = ""
    circuits[name] = {
        "type": module,
        "destinations": destinations.split(", "),
        "inputs": {},
        "ff_status": "off",
        "last_pulse": "",
    }
append_later = []
for circuit_name, circuit in circuits.items():
    for destination in circuit["destinations"]:
        if(destination not in circuits):
            append_later.append((destination, {
                "type": "-",
                "destinations": [],
                "inputs": {},
                "ff_status": "off",
            }))
        else:
            circuits[destination]["inputs"][circuit_name] = "low"
for key, value in append_later:
    circuits[key] = value
# Add nodes
labels = [value["type"] + key for key, value in circuits.items()]
print(labels)
net.add_nodes(list(circuits.keys()), label=labels)
# print(circuits)
# Add connections
for key, value in circuits.items():
    for destination in value["destinations"]:
        # print(key, destination)
        net.add_edge(key, destination)

# net.toggle_physics(False)
net.show("graph.html", notebook=False)