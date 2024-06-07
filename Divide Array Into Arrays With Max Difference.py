nums, k = [15,13,12,13,12,14,12,2,3,13,12,14,14,13,5,12,12,2,13,2,2], 2
def solve(nums, k):
    nums.sort()
    print(nums)
    res = []
    for i in range(len(nums)//3):
        j = 3*i + 1
        print([nums[j-1], nums[j], nums[j+1]])
        if nums[j+1] - nums[j-1] > k:
            return []
        res.append([nums[j-1], nums[j], nums[j+1]])
    return res
print(solve(nums, k))