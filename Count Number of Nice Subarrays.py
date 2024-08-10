from collections import Counter
def solve(nums, k):
    nums[0] = nums[0]%2
    for i in range(1, len(nums)):
        if nums[i]%2==0:
            nums[i] = nums[i-1]
        else:
            nums[i] = 1 + nums[i-1]
    counter = dict(Counter(nums))
    if 0 in counter: counter[0] += 1
    else: counter[0] = 1
    res = 0
    print(nums)
    for i in nums:
        if i >= k:
            if i-k in counter:
                res += counter[i-k]
    return res

nums = [1,1,1,1,1]
k = 1
print(solve(nums, k))