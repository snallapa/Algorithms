# leetcode 442
nums = sorted(nums)
ans = []
for i in range(len(nums) - 1):
    if nums[i] == nums[i + 1]:
        ans.append(nums[i])
        i += 1
return ans
