import sys
import pyperclip
sys.path.append('../')
import AoC_helpers

def run(filename: str, part1: bool):
    if(part1):
        total = 0
        for step in open(filename).read().strip().split(","):
            hash = 0
            for char in step.strip():
                hash += ord(char)
                hash *= 17
                hash %= 256
            total += hash
        return total
    else:
        boxes = {}
        for i in range(256):
            boxes[i] = []
        for step in open(filename).read().strip().split(","):
            add = False
            key = ""
            value = ""
            if("=" in step):
                add = True
                key, value = step.split("=")
            else:
                key = step.split("-")[0]
            hash = 0
            for char in key:
                hash += ord(char)
                hash *= 17
                hash %= 256
            found = False
            for idx, box in enumerate(boxes[hash]):
                if(box[0] == key):
                    if(add):
                        boxes[hash][idx] = (key, value)
                    else:
                        boxes[hash].remove(box)
                    found = True
                    break
            if not found and add:
                boxes[hash].append((key, value))
        total = 0
        # print(boxes)
        for i in range(256):
            for idx, box in enumerate(boxes[i]):
                total += (i + 1) * (idx + 1) * int(box[1])
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
    