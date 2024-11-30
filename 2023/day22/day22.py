import sys
import pyperclip
sys.path.append('../')
import AoC_helpers
import heapq

def run(filename: str, part1: bool):
    bricks = []
    for line in open(filename):
        start, end = line.strip().split("~")
        start_location = tuple(map(int,start.split(",")))
        end_location = tuple(map(int,end.split(",")))
        direction = -1
        if(start_location[0] != end_location[0]):
            direction = 0
        if(start_location[1] != end_location[1]):
            direction = 1
        if(start_location[2] != end_location[2]):
            if(start_location[2] > end_location[2]):
                start_location, end_location = end_location, start_location
            direction = 2
        bricks.append((start_location, end_location, direction))
    bricks.sort(key=lambda brick: (brick[0][2], brick[1][2]))
    ground = {}
    supports = {} # Lower block -> Blocks ontop
    for idx, (start, end, direction) in enumerate(bricks):
        # Vertical bricks
        if(direction == 2 or direction == -1):
            if(start[0:2] not in ground):
                ground[start[0:2]] = (0, None)
            height, last_brick = ground[start[0:2]]
            ground[start[0:2]] = (height + (end[2] - start[2]) + 1, idx)
            if last_brick is not None:
                supports[last_brick].append(idx)
            supports[idx] = []
        # Other bricks
        else:
            ontop = set()
            curr_height = 0
            for axis in range(start[direction], end[direction] + 1):
                location = (axis, start[1]) if direction == 0 else (start[0], axis)
                if(location not in ground):
                    ground[location] = (0, None)
                height, last_brick = ground[location]
                if(curr_height == height):
                    ontop.add(last_brick)
                elif(height > curr_height):
                    ontop.clear()
                    ontop.add(last_brick)
                    curr_height = height
            for axis in range(start[direction], end[direction] + 1):
                location = (axis, start[1]) if direction == 0 else (start[0], axis)
                ground[location] = (curr_height + 1, idx)
            for support in ontop:
                if(support is not None):
                    supports[support].append(idx)
            supports[idx] = []
    # print(supports)
    # print(ground)
    # Calculate reverse supports
    reverse_supports = {} # Blocks ontop -> blocks below
    for idx, bricks in supports.items():
        reverse_supports[idx] = []
    for idx, bricks in supports.items():
        
        for brick in bricks:
            reverse_supports[brick].append(idx)
    # print(reverse_supports)
    # for foundation, bricks in supports.items():
    #     if(len(bricks) == 0):
    #         print(foundation)
    #     for brick in bricks:
    #         print(foundation, "->", brick)
    # Calculate which blocks can be removed
    if(part1):
        total = 0
        for idx, bricks in supports.items():
            can_be_removed = True
            for brick in bricks:
                contains_other_brick = False
                # print(brick, reverse_supports[brick])
                # Check to see if there are other bricks supporting that brick
                for support_brick in reverse_supports[brick]:
                    if(support_brick != idx):
                        contains_other_brick = True
                        break
                if(not contains_other_brick):
                    can_be_removed = False
                    break
            # print(idx, can_be_removed)
            if(can_be_removed):
                total += 1
                # print(idx)
        return total
    else:
        total = 0
        for key, value in supports.items():
            falling_blocks = set()
            queue = [key]
            while(len(queue) > 0):
                block = queue[0]
                queue = queue[1:]
                falling_blocks.add(block)
                for top_block in supports[block]:
                    supported_by_other_brick = False
                    for bottom_block in reverse_supports[top_block]:
                        if(bottom_block not in falling_blocks):
                            supported_by_other_brick = True
                            break
                    if(not supported_by_other_brick):
                        queue.append(top_block)
            total += len(falling_blocks) - 1
        return(total)




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
    
    # 467 Too high