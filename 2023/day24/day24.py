import sys
import pyperclip
sys.path.append('../')
import AoC_helpers

def run(filename: str, part1: bool):
    boundaries = []
    if(sys.argv[1] == 's'):
        boundaries = [7, 27]
    else:
        boundaries = [200000000000000, 400000000000000]
    hail = []
    for line in open(filename):
        position, velocity = line.strip().split("@")
        position = tuple(map(int, position.split(",")))
        velocity = tuple(map(int, velocity.split(",")))
        hail.append((position, velocity))
    if part1:
        num_intersections = 0
        for i in range(len(hail)):
            for j in range(i + 1, len(hail)):
                # Calculate in slope-intercept form
                h1_pos, h1_vel = hail[i]
                h1_slope = h1_vel[1] / h1_vel[0]
                h1_intercept = h1_pos[1] - (h1_slope * h1_pos[0])
                h2_pos, h2_vel = hail[j]
                h2_slope = h2_vel[1] / h2_vel[0]
                h2_intercept = h2_pos[1] - (h2_slope * h2_pos[0])
                print(h1_pos, h1_vel, h2_pos, h2_vel)
                # Same slope = never intersects
                if(h1_slope == h2_slope):
                    print("Never intersects")
                    continue
                x_intersection = (h2_intercept - h1_intercept)/(h1_slope - h2_slope)
                y_intersection = h1_slope * x_intersection + h1_intercept
                # Check intersection is inside the boundary
                if(x_intersection < boundaries[0] or y_intersection < boundaries[0] or x_intersection > boundaries[1] or y_intersection > boundaries[1]):
                    print("Outside Boundary")
                    continue
                # Check time to see if when they hit intersection
                h1_time = (x_intersection - h1_pos[0])/h1_vel[0]
                h2_time = (x_intersection - h2_pos[0])/h2_vel[0]
                # If either time is negative, not possible
                if(h1_time < 0 or h2_time < 0):
                    print("Back in time miss")
                    continue
                print("Intersection:", x_intersection, y_intersection, "at", h1_time)
                num_intersections += 1
        return num_intersections
    else:
        h1_start, h1_vel = hail[0]
        h2_start, h2_vel = hail[1]
        h3_start, h3_vel = hail[2]
        for time1 in range(1, len(hail) + 2):
            for time2 in range(1, len(hail) + 2):
                for time3 in range(1, len(hail) + 2):
                    # Find positions that these times
                    h1_pos = tuple(map(lambda vel, start: time1 * vel + start, h1_vel, h1_start)) 
                    h2_pos = tuple(map(lambda vel, start: time2 * vel + start, h2_vel, h2_start)) 
                    h3_pos = tuple(map(lambda vel, start: time3 * vel + start, h3_vel, h3_start)) 
                    # Find line between these two points
                    h1_h2_difference = tuple(map(lambda x, y: x - y, h1_pos, h2_pos)) 
                    h1_h3_difference = tuple(map(lambda x, y: x - y, h1_pos, h3_pos)) 
                    # Normalize
                    max_h2 = max([abs(x) for x in h1_h2_difference])
                    h1_h2_difference = tuple(map(lambda x: x / max_h2, h1_h2_difference))
                    max_h3 = max([abs(x) for x in h1_h3_difference])
                    h1_h3_difference = tuple(map(lambda x: x / max_h3, h1_h3_difference))
                    # Invert signs if x is negative
                    if(h1_h2_difference[0] < 0):
                        h1_h2_difference = tuple(map(lambda x: -x, h1_h2_difference))
                    if(h1_h3_difference[0] < 0):
                        h1_h3_difference = tuple(map(lambda x: -x, h1_h3_difference))
                    # Check if they are the same
                    # if(h1_h2_difference == h1_h3_difference):
                    if(sum(map(lambda x, y: abs(x - y), h1_h2_difference, h1_h3_difference)) < 0.000001):
                        print(time1, time2, h1_pos, h2_pos)
                        sb_vel = tuple(map(lambda x, y: (x - y) / (time1 - time2), h1_pos, h2_pos)) 
                        # if(time1 < time2):
                        #     sb_vel = tuple(map(lambda x: -x, sb_vel))
                        start = tuple(map(lambda x, y: x - (y * time1), h1_pos, sb_vel))
                        print("Found:", start)
                        return start[0] + start[1] + start[2]
            print(time1)
        return None


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
    

# # z = zx_slope * x + zy_slope * y + intercept
# zx_slope = (h2_pos[2] - h1_pos[2]) / (h2_pos[0] - h1_pos[0])
# zy_slope = (h2_pos[2] - h1_pos[2]) / (h2_pos[1] - h1_pos[1])
# intercept = h1_pos[2] - (zx_slope * h1_pos[0] + zy_slope * h1_pos[1])
# # Check if third point falls on this line
# h3_calculated_z = zx_slope * h3_pos[0] + zy_slope * h3_pos[1] + intercept
# if(h3_calculated_z == h3_pos[2]):
#     print("Found solution")