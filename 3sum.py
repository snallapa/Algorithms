#https://leetcode.com/problems/3sum/description/
nums = [-1, 0, 1, 2, -1, -4]
nums = sorted(nums)
numsDict = {}
for num in nums:
    numsDict[num] = numsDict.get(num, 0) + 1
length = len(nums)
uniqueTriplets = []
unique = {}

def checkPossible(a,b,c):
    unique = {}
    unique[a] = 1
    unique[b] = unique.get(b,0) + 1
    unique[c] = unique.get(c, 0) + 1
    for key, value in unique.items():
        if numsDict.get(key, 0) < value:
            return False
    return True
print(nums)
i = 0
j = len(nums) - 1
while nums[i] < 0:
    while nums[j] >= 0:
        a = nums[i]
        b = nums[j]
        c = -1 * (nums[i] + nums[j])
        triple = tuple(sorted([a,b,c]))
        if not unique.get(triple, False) and checkPossible(a,b,c):
            uniqueTriplets.append(triple)
            unique[triple] = True
        j = j - 1
    i = i + 1
    j = len(nums) - 1

print(uniqueTriplets)
