import sys
import pyperclip
sys.path.append('../')
# import AoC_helpers

def run(filename: str, part1: bool):
    if(part1):
        graph = [[char for char in line.strip()] for line in open(filename).readlines()]
        num_rows = len(graph)
        num_cols = len(graph[0])
        for col in range(num_cols):
            solid = 0
            for row in range(num_rows):
                if(graph[row][col] == "#"):
                    solid = row + 1
                if(graph[row][col] == "O"):
                    if(row != solid):
                        graph[solid][col] = "O"
                        graph[row][col] = "."
                    solid += 1
        # for row in range(num_rows):
        #     for col in range(num_cols):
        #         print(graph[row][col], end="")
        #     print()
        total = 0
        for row in range(num_rows):
            for col in range(num_cols):
                if(graph[row][col] == "O"):
                    total += num_rows - row
        return total
    else:
        graph = [[char for char in line.strip()] for line in open(filename).readlines()]
        num_rows = len(graph)
        num_cols = len(graph[0])
        loads = []
        for i in range(1000):
            # North
            for col in range(num_cols):
                solid = 0
                for row in range(num_rows):
                    if(graph[row][col] == "#"):
                        solid = row + 1
                    if(graph[row][col] == "O"):
                        if(row != solid):
                            graph[solid][col] = "O"
                            graph[row][col] = "."
                        solid += 1
            # West 
            for row in range(num_rows):
                solid = 0
                for col in range(num_cols):
                    if(graph[row][col] == "#"):
                        solid = col + 1
                    if(graph[row][col] == "O"):
                        if(col != solid):
                            graph[row][solid] = "O"
                            graph[row][col] = "."
                        solid += 1
            # South
            for col in range(num_cols):
                solid = num_rows - 1
                for row in range(num_rows - 1, -1, -1):
                    if(graph[row][col] == "#"):
                        solid = row - 1
                    if(graph[row][col] == "O"):
                        if(row != solid):
                            graph[solid][col] = "O"
                            graph[row][col] = "."
                        solid -= 1
            # East 
            for row in range(num_rows):
                solid = num_cols - 1
                for col in range(num_cols - 1, -1, -1):
                    if(graph[row][col] == "#"):
                        solid = col - 1
                    if(graph[row][col] == "O"):
                        if(col != solid):
                            graph[row][solid] = "O"
                            graph[row][col] = "."
                        solid -= 1
            # for row in range(num_rows):
            #     for col in range(num_cols):
            #         print(graph[row][col], end="")
            #     print()
            # print()
            total = 0
            for row in range(num_rows):
                for col in range(num_cols):
                    if(graph[row][col] == "O"):
                        total += num_rows - row
            loads.append(total)
        # Loop detection
        start = 200
        for interval in range(5, 500):
            found = True
            for i in range(interval):
                if loads[start + i] != loads[start + interval + i]:
                    found = False
                    break
            if(found):
                break
        if not found:
            print("Can't find loop")
        # Calculate value
        offset = (1000000000 - start) % interval
        print(offset, interval)
        return loads[start + offset - 1]


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
    