# Brute force dfs search with optimized graph (only look at nodes with working valves)
# search elephant and person paths together

import re

from functools import lru_cache

regex = r"Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (.+)"

valves = {}
valve_to_index = {"AA": 0}
simple_valve_graph = {}
important = set()
max_time = 26

def bfs(start):
    queue = []
    explored = set()
    queue.append({
        "valve": start,
        "distance": 0
    })
    while(len(queue) > 0):
        location = queue.pop(0)
        valve_name = location["valve"]
        valve_distance = location["distance"]
        valve = valves[valve_name]
        if valve_name in explored:
            continue
        if valve["Flow Rate"] > 0 and valve_name != start:
            simple_valve_graph[(start,valve_name)] = valve_distance
        for tunnel in valve["Tunnels"]:
            queue.append({
                "valve": tunnel,
                "distance": valve_distance + 1
            })
        explored.add(valve_name)

@lru_cache(maxsize=None)
def search_for_route(h_time, e_time, h_location, e_location, visited, pressure, visits):
    if(visits >= len(important)):
        return pressure
    max_pressure = pressure
    for valve_name in important:
        if(visited[valve_to_index[valve_name]]):
            continue
        new_visited = list(visited)
        new_visited[valve_to_index[valve_name]] = True
        #Move Human
        new_time = h_time + simple_valve_graph[(h_location, valve_name)] + 1
        new_pressure = pressure + (max_time - new_time) * valves[valve_name]["Flow Rate"]
        if(new_time < max_time):
            max_pressure = max(max_pressure, 
                search_for_route(new_time, e_time,
                    valve_name, e_location,
                    tuple(new_visited), 
                    new_pressure, 
                    visits + 1))
        #Move Elephant
        new_time = e_time + simple_valve_graph[(e_location, valve_name)] + 1
        new_pressure = pressure + (max_time - new_time) * valves[valve_name]["Flow Rate"]
        if(new_time < max_time):
            max_pressure = max(max_pressure, 
                search_for_route(h_time, new_time, 
                    h_location, valve_name, 
                    tuple(new_visited), 
                    new_pressure, 
                    visits + 1))
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
            important.add(result.group(1))
            valve_to_index[result.group(1)] = len(valve_to_index)

    #generate better graph
    bfs("AA")
    for valve in important:
        bfs(valve)
    #Search graph
    visited = (False, ) * len(valve_to_index)
    print(search_for_route(0, 0, "AA", "AA", visited, 0, 0))

if __name__ == "__main__":
    main()