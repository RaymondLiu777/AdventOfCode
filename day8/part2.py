tree_map = []
rows = 0
cols = 0
directions = [[0 , 1], [1, 0], [0, -1], [-1, 0]]

def tree_scenic_score(treeRow, treeCol):
    tree_size = tree_map[treeRow][treeCol]
    score = 1
    for direction in directions:
        index = 1
        while True:
            row = treeRow + direction[0] * index
            col = treeCol + direction[1] * index
            if(row < 0 or col < 0 or row >= rows or col >= cols):
                index -= 1
                break
            if(tree_map[row][col] >= tree_size):
                break
            index += 1
        score *= index 
    # print(score)
    return score

def main():
    file = open("day8/input.txt")
    for line in file:
        tree_map.append(list(line.strip()))
    global rows
    global cols
    rows = len(tree_map)
    cols = len(tree_map[0])
    # print(tree_map)
    best_score = 0
    for row in range(rows):
        for col in range(cols):
            score = tree_scenic_score(row, col)
            if(score > best_score):
                best_score = score
    print(best_score)

if __name__ == "__main__":
    main()