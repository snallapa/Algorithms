grid = [[1,1,1,0],[0,1,1,0], [0,0,1,0], [1,1,1,1]]
def floodfill(index, target, replacement):
    if grid[index[0]][index[1]] == target:
        grid[index[0]][index[1]] = replacement
    else:
        return
    if index[0] > 0:
        floodfill((index[0] - 1, index[1]), target, replacement)
    if index[1] > 0:
        floodfill((index[0], index[1] - 1), target, replacement)
    if index[0] < len(grid) - 1:
        floodfill((index[0] + 1, index[1]), target, replacement)
    if index[1] < len(grid[0]) - 1:
        floodfill((index[0], index[1] + 1), target, replacement)
floodfill((0,0), 1, 2)
for i in range(len(grid)):
    for j in range(len(grid[0])):
        print(grid[i][j], end='')
    print()

