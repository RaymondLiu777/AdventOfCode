import re
from functools import lru_cache

construction_costs = []
max_time = 24

# Checks for enough resources
def can_build_robot(robot_idx, num_resources):
    for idx, resource_cost in enumerate(construction_costs[robot_idx]):
        if(num_resources[idx] < resource_cost):
            return False
    return True

# Checks if the amount of resources gained in previous iteration is enough to built a robot this iteration
def just_enough_resources(robot_idx, num_resources, num_robots):
    just_enough = False
    for idx, resource_cost in enumerate(construction_costs[robot_idx]):
        if(resource_cost == 0):
            continue
        resource = num_resources[idx]
        if(resource >= resource_cost and resource - num_robots[idx] < resource_cost):
            just_enough = True
    return just_enough

@lru_cache(maxsize=None)
def calculate_optimal_geodes(num_robots, num_resources, time):
    if(time >= max_time):
        return 0
    # Try to build a robot
    best = 0
    for robot in range(len(construction_costs)):
        if(can_build_robot(robot, num_resources) and just_enough_resources(robot, num_resources, num_robots)):
            new_resources = tuple(map(lambda i, j, k: i - j + k, num_resources, construction_costs[robot], num_robots[0:3]))
            templist = list(num_robots)
            templist[robot] += 1
            new_robots = tuple(templist)
            best = max(best, num_robots[3] + calculate_optimal_geodes(new_robots, new_resources, time + 1))
    # Don't do anything
    new_resources = tuple(map(lambda i, j: i + j, num_resources, num_robots[0:3]))
    best = max(best, num_robots[3] + calculate_optimal_geodes(num_robots, new_resources, time + 1))
    return best

def main():
    global construction_costs
    file = open("day19/input.txt")
    total = 0
    for line in file:
        result = list(map(int, re.findall(r"\d+", line)))
        blueprint_id = result[0]
        construction_costs = [
            [result[1], 0, 0],
            [result[2], 0, 0],
            [result[3], result[4], 0],
            [result[5], 0, result[6]]
        ]
        num_robots = (1, 0, 0, 0)
        num_resources = (0, 0, 0)
        num_geodes = calculate_optimal_geodes(num_robots, num_resources, 0)
        print(num_geodes)
        total += num_geodes * blueprint_id
        calculate_optimal_geodes.cache_clear()
    print(total)


if __name__ == "__main__":
    main()