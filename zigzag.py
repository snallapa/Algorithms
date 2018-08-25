s = "PAYPALISHIRING"
numRows = 4
if numRows == 1:
    print(s)
length = len(s)
grid = [["" for i in range(length)] for j in range(numRows)]
def printGrid():
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j], end='')
        print("")
inDiagonal = 0
inColumn = 0
currentColumn = 0
currentRow = 0
for i in range(length):
    if inDiagonal == numRows - 1:
        inColumn = 1
        inDiagonal = 0
        currentRow += 1
    if inColumn != numRows:
        grid[currentRow][currentColumn] = s[i]
        inColumn += 1
        currentRow += 0 if inColumn == numRows else 1        
    else:
        currentColumn += 1
        currentRow -= 1
        grid[currentRow][currentColumn] = s[i]
        inDiagonal += 1
ans = ""        
for i in range(len(grid)):
    for j in range(len(grid[0])):
        ans += grid[i][j]
print(ans)
