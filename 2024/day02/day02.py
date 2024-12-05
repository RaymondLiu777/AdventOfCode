import sys
import pyperclip
sys.path.append('../')

def checkValid(nums):
    increase = True if nums[0] < nums[1] else False
    for i in range(len(nums) - 1):
        if(increase and nums[i] > nums[i + 1]):
            return i
        elif not increase and nums[i] < nums[i + 1]:
            return i
        if(abs(nums[i] - nums[i+1]) > 3 or abs(nums[i] - nums[i+1]) < 1):
            return i
    return -1

def run(filename: str, part1: bool):
    count = 0
    damper_count = 0
    for line in open(filename).readlines():
        nums = list(map(int, line.strip().split()))
        problem_index = checkValid(nums)
        if problem_index == -1:
            count += 1
        else:
            nums_copy_0 = nums.copy()
            nums_copy_0.pop(problem_index - 1)
            nums_copy_1 = nums.copy()
            nums_copy_1.pop(problem_index)
            nums_copy_2 = nums.copy()
            nums_copy_2.pop(problem_index + 1)
            if checkValid(nums_copy_0) == -1 or checkValid(nums_copy_1) == -1 or checkValid(nums_copy_2) == -1:
                damper_count += 1
    return count if part1 else damper_count + count


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