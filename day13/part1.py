
import json


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


def main():
    file = open("day13/input.txt")
    index = 1
    total = 0
    for pair in file.read().strip().split("\n\n"):
        pair = pair.split()
        left = json.loads(pair[0])
        right = json.loads(pair[1])
        solution = []
        compare_lists(left, right, solution)
        # print(left, right, solution)
        if(len(solution) == 0 or len(solution) > 1):
            raise Exception("Error")
        elif(solution[0] == True):
            total += index
        index += 1
    print(total)

if __name__ == "__main__":
    main()