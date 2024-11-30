

movement = []
blocks = [
    [
        [True, True, True, True]
    ],
    [
        [False, True, False],
        [True, True, True],
        [False, True, False]
    ],
    [
        [True, True, True],
        [False, False, True],
        [False, False, True]
    ],
    [
        [True],
        [True],
        [True],
        [True]
    ],
    [
        [True, True],
        [True, True]
    ]
]

chamber = []
chamber_width = 7
increase = []

max_simulation_iterations = 10000
period_start_location = 1000
max_period_size = 5000

def print_chamber():
    for x in range(len(chamber)):
        for spot in chamber[-x - 1]:
            if(spot):
                print(u"\u2588", end="")
            else:
                print(u"\u25A1", end="")
        print()

def main():
    global movement
    file = open("day17/input.txt")
    movement = [*file.read()]
    top = 0
    block_index = 0
    movement_index = 0
    for x in range(max_simulation_iterations):
        block = blocks[block_index]
        #Increase chamber size
        while(len(chamber) < top + 3 + len(block)):
            chamber.append([False] * chamber_width)
        #Simulate blocks
        offset = [top + 3, 2]
        falling = True
        gas_move = True
        while(falling):
            next_move = [0, 0]
            #Gas
            if(gas_move):
                if(movement[movement_index] == ">"):
                    if(offset[1] + len(block[0]) < chamber_width):
                        next_move[1] += 1
                else:
                    if(offset[1] > 0):
                        next_move[1] -= 1
                movement_index = (movement_index + 1) % len(movement)
            else:
                next_move[0] -= 1
            #Check for collisions
            collision = False
            for block_y, row in enumerate(block):
                for block_x, b in enumerate(row):
                    if((block_y + offset[0] + next_move[0]) < 0):
                        collision = True
                    if b and chamber[block_y + offset[0] + next_move[0]][block_x + offset[1] + next_move[1]]:
                        collision = True
            if(collision):
                if(not gas_move):
                    falling = False
            else:
                offset[0] += next_move[0]
                offset[1] += next_move[1]
            gas_move = not gas_move
        for block_y, row in enumerate(block):
            for block_x, b in enumerate(row):
                if b:
                    chamber[block_y + offset[0]][block_x + offset[1]] = b
        old_top = top
        top = max(top, offset[0] + len(block))
        block_index = (block_index + 1) % len(blocks)
        increase.append(top - old_top)
    #Check for patterns 
    period = 0
    for x in range(1, max_period_size):
        pattern = True
        for y in range(x):
            if(increase[period_start_location + y] != increase[period_start_location + x + y]):
                pattern = False
                break
        if(pattern):
            period = x
            print("Period of pattern is", period)
            break
    if period == 0:
        print("Error search parameters not enough to find period")
        return
    # Height up to start
    total = 0
    for x in range(period_start_location):
        total += increase[x]
    period_increase = 0
    for x in range(period):
        period_increase += increase[period_start_location + x]
    num_blocks = 1000000000000
    num_blocks -= period_start_location
    total += (num_blocks // period) * period_increase
    for x in range(num_blocks % period):
        total += increase[period_start_location + x]
    print(total)

if __name__ == "__main__":
    main()