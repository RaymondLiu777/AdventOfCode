import sys
import pyperclip
sys.path.append('../')
# import AoC_helpers

def run(filename: str, part1: bool):
    if(part1):
        graphs = open(filename).read().split("\n\n")
        total = 0
        for graphLine in graphs:
            graph = [[char for char in line] for line in graphLine.split("\n")]
            row_count = len(graph)
            col_count = len(graph[0])
            row_sum = [0] * row_count
            col_sum = [0] * col_count
            for row, line in enumerate(graph):
                for col, location in enumerate(line):
                    if(location == "#"):
                        row_sum[row] += 1
                        col_sum[col] += 1
            for row in range(row_count - 1):
                mirror = True
                for i in range(min(row + 1, row_count - row - 1)):
                    if(row_sum[row + i + 1] != row_sum[row - i]):
                        mirror = False
                        break
                if(mirror == False):
                    continue
                for i in range(min(row + 1, row_count - row - 1)):
                    for j in range(col_count):
                        if(graph[row + i + 1][j] != graph[row - i][j]):
                            mirror = False
                            break
                    if(mirror == False):
                        break
                if(mirror):
                    total += (row + 1) * 100
            for col in range(col_count - 1):
                mirror = True
                for j in range(min(col + 1, col_count - col - 1)):
                    if(col_sum[col + j + 1] != col_sum[col - j]):
                        mirror = False
                        break
                if(mirror == False):
                    continue
                for j in range(min(col + 1, col_count - col - 1)):
                    for i in range(row_count):
                        if(graph[i][col + j + 1] != graph[i][col - j]):
                            mirror = False
                            break
                    if(mirror == False):
                        break
                if(mirror):
                    total += (col + 1)
        return total
    else:
        graphs = open(filename).read().split("\n\n")
        total = 0
        for graphLine in graphs:
            graph = [[char for char in line] for line in graphLine.split("\n")]
            row_count = len(graph)
            col_count = len(graph[0])
            row_sum = [0] * row_count
            col_sum = [0] * col_count
            for row, line in enumerate(graph):
                for col, location in enumerate(line):
                    if(location == "#"):
                        row_sum[row] += 1
                        col_sum[col] += 1
            for row in range(row_count - 1):
                mistakes = 0
                for i in range(min(row + 1, row_count - row - 1)):
                    if(row_sum[row + i + 1] == row_sum[row - i]):
                        continue
                    if(abs(row_sum[row + i + 1] - row_sum[row - i]) == 1):
                        mistakes += 1
                    else:
                        mistakes += 5
                        break
                if(mistakes != 1):
                    continue
                mistakes = 0
                for i in range(min(row + 1, row_count - row - 1)):
                    for j in range(col_count):
                        if(graph[row + i + 1][j] != graph[row - i][j]):
                            mistakes += 1
                if(mistakes == 1):
                    total += (row + 1) * 100
            for col in range(col_count - 1):
                mistakes = 0
                for j in range(min(col + 1, col_count - col - 1)):
                    if(col_sum[col + j + 1] == col_sum[col - j]):
                        continue
                    if(abs(col_sum[col + j + 1] - col_sum[col - j]) == 1):
                        mistakes += 1
                    else:
                        mistakes += 5
                        break
                if(mistakes != 1):
                    continue
                mistakes = 0
                for j in range(min(col + 1, col_count - col - 1)):
                    for i in range(row_count):
                        if(graph[i][col + j + 1] != graph[i][col - j]):
                            mistakes += 1
                if(mistakes == 1):
                    total += (col + 1)
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
    