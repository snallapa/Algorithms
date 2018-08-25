#leetcode 34
nums = [5, 7,7,8,8,10,11]
target = 8
def binsearch():
    hi = len(nums) - 1
    lo = 0
    mid = int((hi - lo) / 2)
    while lo <= hi:
        if nums[mid] < target:
            lo = mid + 1
            mid = int((hi - lo) / 2) + lo
        elif nums[mid] > target:
            hi = mid - 1
            mid = int((hi - lo) / 2) + lo
        else:
            return mid
    return -1
index = binsearch()
if index == -1:
    print([index, index])
lo = index
hi = index
while True:
    if lo > 0 and nums[lo - 1] == target:
        lo -= 1
    elif hi < len(nums) and nums[hi + 1] == target:
        hi += 1
    else:
        break
print([lo, hi])
