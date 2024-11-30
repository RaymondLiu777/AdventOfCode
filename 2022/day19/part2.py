import re
from functools import lru_cache

construction_costs = []
max_resource_costs = []
max_time = 32

# Checks if the amount of resources gained in previous iteration is enough to built a robot this iteration
def enough_resources(robot_idx, num_resources, num_robots):
    just_enough = False
    can_build = True
    for idx, resource_cost in enumerate(construction_costs[robot_idx]):
        if(resource_cost == 0):
            continue
        resource = num_resources[idx]
        if(resource >= resource_cost and resource - num_robots[idx] < resource_cost):
            just_enough = True
        if(resource < resource_cost):
            can_build = False
    return just_enough and can_build

@lru_cache(maxsize=None)
def calculate_optimal_geodes(num_robots, num_resources, time):
    if(time >= max_time):
        return 0
    # Try to build a robot
    best = 0
    for robot in range(len(construction_costs)):
        if(robot != 3 and num_robots[robot] > max_resource_costs[robot]):
            continue
        # Run until enough resources
        new_time = time
        new_resources = tuple(num_resources)
        done_generating = False
        while(new_time < max_time and not done_generating):
            if(enough_resources(robot, new_resources, num_robots)):
                done_generating = True
            new_resources = tuple(map(lambda i, j: i + j, new_resources, num_robots))
            new_time +=1
        if(new_time >= max_time):
            continue
        new_resources = tuple(map(lambda i, j: i - j, new_resources, construction_costs[robot]))
        new_robots = num_robots
        generated_geodes = 0
        if(robot != 3):
            templist = list(num_robots)
            templist[robot] += 1
            new_robots = tuple(templist)
        elif(robot == 3):
            generated_geodes = max_time - new_time
        best = max(best, generated_geodes + calculate_optimal_geodes(new_robots, new_resources, new_time))
    return best

def main():
    global construction_costs
    global max_resource_costs
    file = open("day19/input.txt")
    totals = []
    for line in file:
        result = list(map(int, re.findall(r"\d+", line)))
        blueprint_id = result[0]
        construction_costs = [
            [result[1], 0, 0],
            [result[2], 0, 0],
            [result[3], result[4], 0],
            [result[5], 0, result[6]]
        ]
        max_resource_costs = [
            max(result[1], result[2], result[3], result[5]),
            result[4],
            result[6]
        ]
        num_robots = (1, 0, 0)
        num_resources = (0, 0, 0)
        num_geodes = calculate_optimal_geodes(num_robots, num_resources, 0)
        print(num_geodes)
        totals.append(num_geodes)
        calculate_optimal_geodes.cache_clear()
    print(totals)
    print(totals[0] * totals[1] * totals[2])


if __name__ == "__main__":
    main()