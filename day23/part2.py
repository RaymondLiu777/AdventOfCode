import sys

elf_locations = set()

adjancent_tiles = [
    [-1, -1],
    [-1, 0],
    [-1, 1],
    [0, -1],
    [0, 1],
    [1, -1],
    [1, 0],
    [1, 1]
]

direction_order = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]

directions = {
    (-1, 0): [(-1, 0), (-1, -1), (-1, 1)],
    (1, 0): [(1, 0), (1, -1), (1, 1)],
    (0, -1): [(0, -1), (-1, -1), (1, -1)],
    (0, 1): [(0, 1), (-1, 1), (1, 1)],
}

def get_next_move(position):
    no_movement = True
    for offset in adjancent_tiles:
        if(tuple(map(sum, zip(position,offset))) in elf_locations):
            no_movement = False
    if no_movement:
        return position
    for direction in direction_order:
        valid_option = True
        for check in directions[direction]:
            if(tuple(map(sum, zip(position, check))) in elf_locations):
                valid_option = False
                break
        if valid_option:
            return tuple(map(sum, zip(position, direction)))
    return position

def need_to_move():
    for location in elf_locations:
        for offset in adjancent_tiles:
            if(tuple(map(sum, zip(location,offset))) in elf_locations):
                return True
    return False


def main():
    file = open("day23/input.txt")
    for row, line in enumerate(file):
        for col, char in enumerate(line):
            if(char == "#"):
                elf_locations.add((row, col))
    time = 0
    while(need_to_move()):
        next_step = {}
        for elf in elf_locations:
            next_location = get_next_move(elf)
            if(next_location not in next_step):
                next_step[next_location] = [elf]
            else:
                next_step[next_location].append(elf)
        elf_locations.clear()
        elf_locations.update(next_step.keys())
        for step, elves in next_step.items():
            if(len(elves) > 1):
                elf_locations.remove(step)
                elf_locations.update(elves)
        shift_direction = direction_order.pop(0)
        direction_order.append(shift_direction)
        time += 1
    print(time + 1)

if __name__ == "__main__":
    main()