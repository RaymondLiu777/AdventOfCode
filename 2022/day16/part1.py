# Brute force dfs with minor optimizations

import re

from functools import lru_cache

regex = r"Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (.+)"

valves = {}
valve_to_index = {}
already_tried = []
max_time = 30

def check_already_searched(time, location, openned, pressure):
    for state in already_tried:
        if(location != state["location"]):
            continue
        if(openned != state["openned"]):
            continue
        if(time >= state["time"] and pressure <= state["pressure"]):
            return True
    return False

@lru_cache(maxsize=None)
def search_for_route(time, location, openned, pressure):
    if(check_already_searched(time, location, openned, pressure)):
        return 0
    else:
        already_tried.append({
            "location": location,
            "openned": openned,
            "time": time,
            "pressure": pressure
        })
    if(time >= max_time):
        return pressure
    max_pressure = 0
    valve = valves[location]
    if(valve["Flow Rate"] != 0 and not openned[valve_to_index[location]]):
        # Open valve
        new_openned = list(openned)
        new_openned[valve_to_index[location]] = True
        max_pressure = max(max_pressure, search_for_route(time + 1, location, tuple(new_openned), pressure + (max_time - time) * valve["Flow Rate"]))
    for next_location in valve["Tunnels"]:
        max_pressure = max(max_pressure, search_for_route(time + 1, next_location, openned, pressure))
    return max_pressure


def main():
    file = open("day16/input.txt")
    for line in file:
        result = re.search(regex, line.strip())
        valves[result.group(1)] = {
            "Flow Rate": int(result.group(2)),
            "Tunnels": result.group(3).split(", ")
        }
        if(int(result.group(2)) != 0):
            valve_to_index[result.group(1)] = len(valve_to_index)
    openned = (False, ) * len(valve_to_index)
    print(search_for_route(1, "AA", openned, 0))

if __name__ == "__main__":
    main()