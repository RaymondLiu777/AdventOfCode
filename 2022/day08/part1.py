tree_map = []
rows = 0
cols = 0

def is_tree_visible(treeRow, treeCol):
    tree_size = tree_map[treeRow][treeCol]
    # Check row
    tree_row_before = False
    tree_row_after = False
    for row in range(rows):
        if(row < treeRow and tree_map[row][treeCol] >= tree_size):
            tree_row_before = True
        if(row > treeRow and tree_map[row][treeCol] >= tree_size):
            tree_row_after = True
    
    # Check col
    tree_col_before = False
    tree_col_after = False
    for col in range(cols):
        if(col < treeCol and tree_map[treeRow][col] >= tree_size):
            tree_col_before = True
        if(col > treeCol and tree_map[treeRow][col] >= tree_size):
            tree_col_after = True
    return not (tree_row_before and tree_row_after and tree_col_before and tree_col_after)

def main():
    file = open("day8/input.txt")
    for line in file:
        tree_map.append(list(line.strip()))
    global rows
    global cols
    rows = len(tree_map)
    cols = len(tree_map[0])
    # print(tree_map)
    total = 0
    for row in range(rows):
        for col in range(cols):
            if(is_tree_visible(row, col)):
                total += 1
    print(total)


if __name__ == "__main__":
    main()