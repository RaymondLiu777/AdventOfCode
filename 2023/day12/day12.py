import sys
import pyperclip
sys.path.append('../')
# import AoC_helpers
import functools
import math

@functools.lru_cache
def backtrackingV3(grid: "tuple[str]", groups: "tuple[int]"):
    # End of string
    gridIdx = 0
    if(len(grid) == 0):
        if(len(groups) == 0):
            return 1
        else:
            return 0
    # No more groups
    if(len(groups) == 0):
        for char in grid:
            if(char == "#"):
                return 0
        return 1
    # Loop past any "."
    while gridIdx < len(grid) and grid[gridIdx] == ".":
        gridIdx += 1
    # Check if at end
    if(gridIdx == len(grid)):
        return backtrackingV3(grid[gridIdx:], groups)
    # Deal with ?
    total = 0
    if(grid[gridIdx] == "?"):
        total += backtrackingV3(grid[gridIdx + 1:], groups)
    # Deal with # or ? as #
    # Find next group of hashtags
    for i in range(groups[0]):
        if(gridIdx >= len(grid)):
            return total
        if(grid[gridIdx] == "."):
            return total
        gridIdx += 1
    # Check next value
    if(gridIdx == len(grid) or grid[gridIdx] == "."):
        total += backtrackingV3(grid[gridIdx:], groups[1:])
    elif(grid[gridIdx] == "?"):
        total += backtrackingV3(grid[gridIdx+1:], groups[1:])
    elif(grid[gridIdx] == "#"):
        return total
    return total

def run(filename: str, part1: bool):
    backtrackingV3.cache_clear()

    total = 0
    for line in open(filename):
        grid, nums = line.split()
        groups = [int(num) for num in nums.strip().split(",")]
        if(not part1):
            grid = ((grid + "?") * 5)[0:-1]
            groups = groups * 5
        gridInput = tuple([char for char in grid])
        total += backtrackingV3(gridInput, tuple(groups))

    return total

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
    

# Failed Attempts
def validatePuzzle(grid: str, groups: str):
    groupIdx = 0
    lastValue = "."
    numValues = 0
    for val in grid:
        if(val == "?"):
            return True
        if(val == "." and lastValue == "#"):
            if(groupIdx >= len(groups) or numValues != groups[groupIdx]):
                return False
            groupIdx += 1
        if(val == lastValue):
            numValues += 1
        else:
            numValues = 1
        lastValue = val
    if(lastValue == "#"):
        if(groupIdx >= len(groups) or numValues != groups[groupIdx]):
            return False
        groupIdx += 1
    return groupIdx == len(groups)



def backtracking(grid: str, groups: "list[int]", unknowns: "list[int]", idx: int):
    # print(grid)
    if(idx == len(unknowns)):
        return 1
    total = 0
    for val in ["#", "."]:
        newGrid = grid[0:unknowns[idx]] + val + grid[unknowns[idx]+1:]
        # print(newGrid, validatePuzzle(newGrid, groups))
        if(validatePuzzle(newGrid, groups)):
            total += backtracking(newGrid, groups, unknowns, idx + 1)
    return total

def groupUnknowns(unknowns: "list[int]"):
    start = unknowns[0]
    end = unknowns[0]
    unknownGroups = []
    for val in unknowns[1:]:
        if(val == end + 1):
            end = val
        else:
            unknownGroups.append((start, end + 1))
            start = val
            end = val
    return unknownGroups

# @functools.lru_cache
def calculatePossibilities(spaces: int, groups: "tuple[int]"):
    if(spaces < 0):
        return 0
    if(spaces == 0):
        return 1
    if(len(groups) == 0):
        return 1
    filledTiles = sum(groups) 
    neededSpace = filledTiles + len(groups) - 1
    if(neededSpace > spaces):
        return 0
    else:
        distributableSpaces = (spaces - filledTiles) - (len(groups) - 1)
        groups = len(groups) + 1
        return math.comb(distributableSpaces + groups - 1, distributableSpaces)



def backtrackingV2(grid: str, groups: "list[int]", gridIdx:int, groupIdx: int, partialSolutions: int):
    # End of grid
    if(gridIdx == len(grid)):
        if(groupIdx == len(groups)):
            return partialSolutions
        else:
            return 0
    # Loop past any "."
    while gridIdx < len(grid) and grid[gridIdx] == ".":
        gridIdx += 1
    # Check if at end
    if(gridIdx == len(grid)):
        return backtrackingV2(grid, groups, gridIdx, groupIdx, partialSolutions)
    # Must be at a # or ?
    if(grid[gridIdx] == "#"):
        # Find number hashtags
        numFilled = 0
        while gridIdx < len(grid) and grid[gridIdx] == "#":
            numFilled += 1
            gridIdx += 1
        # Chunk ends in .
        if(gridIdx == len(grid) or grid[gridIdx] == "."):
            if(numFilled == groups[groupIdx]):
                return backtrackingV2(grid, groups, gridIdx, groupIdx + 1, partialSolutions)
            else:
                return 0
        #Chunk must be finished because of "?"
        elif (grid[gridIdx] == "?"):
            # Find the number of ? marks
            numQuestionMarks = 0
            tempCounter = gridIdx
            while tempCounter < len(grid) and grid[tempCounter] == "?":
                numQuestionMarks += 1
                tempCounter += 1
            # Can't possibly fit group here
            if(numFilled > groups[groupIdx] or numFilled + numQuestionMarks < groups[groupIdx]):
                return 0
            # Can fit group here
            extraSpaceNeeded = groups[groupIdx] - numFilled + 1
            return backtrackingV2(grid, groups, gridIdx + extraSpaceNeeded, groupIdx + 1, partialSolutions)
        else:
            raise Exception("Error with", grid[gridIdx])
    # Counting for ?s
    elif(grid[gridIdx] == "?"):
        numQuestionMarks = 0
        tempCounter = gridIdx
        while tempCounter < len(grid) and grid[tempCounter] == "?":
            numQuestionMarks += 1
            tempCounter += 1
        total = 0
        numEndHashTags = 0
        while tempCounter < len(grid) and grid[tempCounter] == "#":
            numEndHashTags += 1
            tempCounter += 1
        # Generate options
        subGroup = []
        # Use no group (fill at with empty)
        if(numEndHashTags == 0):
            total += backtrackingV2(grid, groups, tempCounter, groupIdx, partialSolutions)
        for val in groups[groupIdx:]:
            subGroup.append(val)
            if(numEndHashTags > subGroup[-1]):
                continue
            if(numEndHashTags > 0): 
                if(len(subGroup) == 1 and numQuestionMarks - (subGroup[-1] - numEndHashTags + 1) == -1):
                    possibilities = 1
                else:
                    possibilities = calculatePossibilities(numQuestionMarks - (subGroup[-1] - numEndHashTags + 1), tuple(subGroup[0:len(subGroup) - 2]))
            else:
                possibilities = calculatePossibilities(numQuestionMarks, tuple(subGroup))
            if(possibilities == 0):
                continue
            total += backtrackingV2(grid, groups, tempCounter, groupIdx + len(subGroup), partialSolutions * possibilities)
        return total
    else:
        raise Exception("Error2 with", grid[gridIdx])
