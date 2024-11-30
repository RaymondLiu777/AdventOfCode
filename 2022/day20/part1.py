
encrypted_file = []

def main():
    file = open("day20/input.txt")
    zero_value = (0, 0)
    for idx, line in enumerate(file):
        value = (int(line.strip()), idx)
        encrypted_file.append(value)
        if(value[0] == 0):
            zero_value = value
    current_idx = 0
    search_position = 0
    while(current_idx < len(encrypted_file)):
        # Find the number to move
        while(encrypted_file[search_position][1] != current_idx):
            search_position = (search_position + 1) % len(encrypted_file)
        # Where to move to
        new_location = (search_position + encrypted_file[search_position][0]) % (len(encrypted_file) - 1)
        value = encrypted_file.pop(search_position)
        encrypted_file.insert(new_location, value)
        current_idx += 1
        # for value in encrypted_file:
        #     print(value[0], end=", ")
        # print()
    zero_idx = encrypted_file.index(zero_value)
    total = 0
    for x in range(1,4):
        total += encrypted_file[(zero_idx + 1000*x) % len(encrypted_file)][0]
    print(total)


if __name__ == "__main__":
    main()