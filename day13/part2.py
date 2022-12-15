
import json
import functools

def compare_lists(left, right, result):
    if(type(left) == int and type(right) == int):
        if(left != right):
            result.append(left < right)
            return True
        else:
            return False
    elif(type(left) == int and type(right) == list):
        newlist = [left]
        return compare_lists(newlist, right, result)
    elif(type(left) == list and type(right) == int):
        newlist = [right]
        return compare_lists(left, newlist, result)
    elif(type(left) == list and type(right) == list):
        min_len = min(len(left), len(right))
        for x in range(min_len):
            if(compare_lists(left[x], right[x], result)):
                return True
        if(len(left) == len(right)):
            return False
        else:
            result.append(len(left) < len(right))
            return True
    else:
        raise Exception("Unknown data type")

def list_cmp(left, right):
    solution = []
    compare_lists(left, right, solution)
    if(len(solution) == 0):
        return 0
    elif(solution[0] == True):
        return -1
    else:
        return 1

def main():
    file = open("day13/input.txt")
    packets = [[[2]], [[6]]]
    for pair in file.read().strip().split("\n\n"):
        pair = pair.split()
        packets.append(json.loads(pair[0]))
        packets.append(json.loads(pair[1]))
    sorted_packets = sorted(packets, key=functools.cmp_to_key(list_cmp))
    total = 1
    for idx, list in enumerate(sorted_packets):
        if(list == [[2]] or list == [[6]]):
            total *= idx + 1
    print(total)


if __name__ == "__main__":
    main()