import sys
import pyperclip
sys.path.append('../AoC_Helpers')
from InputParser import InputParser
# from Grid import Directions, Grid
# from TupleOps import TupleOps
# from Graph import Graph

def calculateChecksum(diskmap):
    checksum = 0
    for disk in diskmap:
        if disk["empty"]:
            continue
        # index_sum = sum(range(disk["location"], disk["location"] + disk["size"]))
        index_sum = (disk["location"] + (disk["size"]-1)/2) * disk["size"]
        checksum += index_sum * disk["id"]
        # print(disk["location"], disk["id"], disk["size"])
        # print("Checksum:", index_sum, disk["id"])
    return int(checksum)

def part1Compacting(diskmap):
    # Get empty block data
    empty_blocks=[]
    for disk in diskmap:
        if(disk["empty"]):
            empty_blocks.append(disk)
    # Get block at back and try to move forward
    extra_storage = []
    while len(empty_blocks) > 0:
        last_block = diskmap.pop()
        # print(last_block)
        if last_block["empty"]:
            empty_blocks.pop()
            continue
        empty_block = empty_blocks[0]
        # enough space
        if(last_block["size"] == empty_block["size"]):
            last_block["location"] = empty_block["location"]
            extra_storage.append(last_block)
            empty_blocks = empty_blocks[1:]
        # To much space
        elif(last_block["size"] < empty_block['size']):
            last_block["location"] = empty_block["location"]
            empty_block["location"] += last_block["size"]
            empty_block["size"] -= last_block["size"]
            extra_storage.append(last_block)
        # Not enough space
        else:
            empty_block["id"] = last_block["id"]
            empty_block["empty"] = False
            last_block["size"] -= empty_block["size"]
            # print("Added", last_block, empty_block)
            # print(diskmap, extra_storage)
            diskmap.append(last_block)
            empty_blocks = empty_blocks[1:]
    
    # Combine and filter
    final_diskmap = sorted([*extra_storage,*diskmap], key=lambda x: x["location"])
    final_diskmap = list(filter(lambda x: x["empty"]==False, final_diskmap))
    return final_diskmap

def part2Compacting(diskmap):
    filled_blocks = list(filter(lambda x: x["empty"] == False, diskmap))
    filled_blocks.reverse()
    empty_blocks = list(filter(lambda x: x["empty"] == True, diskmap))
    for disk in filled_blocks:
        for empty in empty_blocks:
            if(empty["location"] >= disk["location"]):
                break
            if(empty["size"] >= disk["size"]):
                disk["location"] = empty["location"]
                empty["location"] += disk["size"]
                empty["size"] -= disk["size"]
                break
    # Combine
    final_diskmap = sorted(diskmap, key=lambda x: x["location"])
    return final_diskmap

def run(filename: str, part1: bool):
    input = open(filename).read().strip()
    diskmap = []
    id = 0
    empty = False
    location = 0
    for space in input:
        diskmap.append({
            "location": location,
            "id": id if not empty else -1,
            "empty": empty,
            "size": int(space)
        })
        location += int(space)
        id += 1 if not empty else 0
        empty = not empty
    
    final_diskmap = part1Compacting(diskmap) if part1 else part2Compacting(diskmap)

    # print(final_diskmap)
    # for disk in final_diskmap:
    #     print(disk["location"], disk["id"], disk["size"])

    # for disk in final_diskmap:
    #     print(("." if disk["empty"] else str(disk["id"]))*disk["size"], end="")
    # print()

    return calculateChecksum(final_diskmap)


if __name__ == "__main__" :
    if len(sys.argv) < 3:
        print("Error, requires two command lines arguments: s/i 1/2")
        exit()
    if sys.argv[2] != '1' and sys.argv[2] != '2':
        print("Error invalid command line args:", sys.argv[1], sys.argv[2])
        exit()

    filename = ""
    if sys.argv[1] == 's':
        filename = "sample.txt"
    elif sys.argv[1] == 'i':
        filename = "input.txt"
    else:
        filename = sys.argv[1]

    part1 = (sys.argv[2] == '1')
    result = run(filename, part1)
    print(result)
    pyperclip.copy(str(result))
    