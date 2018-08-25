#leetcode 11
height = [10,8,6,2,5,4,10,3,7]

i = 0
j = len(height) - 1
maxContainer = -1
while i < j:
    iLine = height[i]
    jLine = height[j]
    containerHeight = min(iLine, jLine)
    area = (j - i) * containerHeight
    if area > maxContainer:
        maxContainer = area
    if iLine <= jLine:
        i += 1
    else:
        j -= 1
print(maxContainer)
