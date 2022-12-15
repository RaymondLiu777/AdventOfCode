import re

regex = r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)"

beacons = []
ranges = []
target_row = 2000000

def calculate_range(sensor_x, sensor_y, beacon_x, beacon_y):
    manhattan_distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
    row_distance = abs(sensor_y - target_row)
    space_within_row = manhattan_distance - row_distance
    if(space_within_row < 0):
        return
    range = [sensor_x - space_within_row, sensor_x + space_within_row]
    ranges.append(range)

def main():
    file = open("day15/input.txt")
    for line in file:
        result = re.search(regex, line.strip())
        beacon = [int(result.group(3)), int(result.group(4))]
        if not beacon in beacons:
            beacons.append(beacon)
        calculate_range(int(result.group(1)), int(result.group(2)), int(result.group(3)), int(result.group(4)))
    sorted_ranges = sorted(ranges, key=lambda x : x[0])
    print(sorted_ranges)
    consolidated_ranges = [sorted_ranges.pop(0)]
    while(len(sorted_ranges) > 0):
        range = sorted_ranges.pop(0)
        last_consolidated_range = consolidated_ranges[-1]
        if(last_consolidated_range[1] >= range[0]):
            consolidated_ranges.pop()
            consolidated_ranges.append([last_consolidated_range[0], max(last_consolidated_range[1],range[1])])
        else:
            consolidated_ranges.append(range)
    print(consolidated_ranges)
    total = 0
    relevant_beacons = list(filter(lambda beacon: beacon[1] == target_row, list(beacons)))
    print(relevant_beacons)
    for range in consolidated_ranges:
        total += range[1] - range[0] + 1
        for beacon in relevant_beacons:
            if(beacon[1] >= range[0] and beacon[1] <= range[1]):
                total -= 1
    print(total)

if __name__ == "__main__":
    main()