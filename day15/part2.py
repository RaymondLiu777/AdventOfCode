import re

regex = r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)"

sensor_beacons = []
beacons = []
size = 4000000

def calculate_range(sensor_x, sensor_y, beacon_x, beacon_y, target_row, ranges):
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
        sensor_beacons.append([int(result.group(1)), int(result.group(2)), int(result.group(3)), int(result.group(4))])
    for x in range(size):
        ranges = []
        for sensor_beacon in sensor_beacons:
            calculate_range(sensor_beacon[0], sensor_beacon[1], sensor_beacon[2], sensor_beacon[3], x, ranges)
        sorted_ranges = sorted(ranges, key=lambda x : x[0])
        consolidated_ranges = [sorted_ranges.pop(0)]
        while(len(sorted_ranges) > 0):
            range0 = sorted_ranges.pop(0)
            last_consolidated_range = consolidated_ranges[-1]
            if(last_consolidated_range[1] >= range0[0] - 1):
                consolidated_ranges.pop()
                consolidated_ranges.append([last_consolidated_range[0], max(last_consolidated_range[1],range0[1])])
            else:
                consolidated_ranges.append(range0)
        in_row = True
        for range0 in consolidated_ranges:
            if range0[0] <= 0 and range0[1] >= size:
                in_row = False
                break
        if(in_row):
            print("In row y =", x, consolidated_ranges)
            print("If there are only 2 ranges, then solution is", ((consolidated_ranges[0][1] + 1) * size) + x)
            break

if __name__ == "__main__":
    main()