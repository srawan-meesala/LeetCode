from collections import defaultdict


def longestConsecutive(nums) -> int:
    n = defaultdict(int)
    high = 0
    for i in nums:
        n[i] = 1
    for i in range(len(nums)):
        k = 1
        if i-1 in n: 
            k += 1
        n[i] += n[i-1]
        high = max(n[i], high)
    for i in reversed(nums):
        n[i] += n[i-1]
        high = max(n[i], high)
    print(n)
    return high
nums = [100,4,200,1,3,2]
print(longestConsecutive(nums))