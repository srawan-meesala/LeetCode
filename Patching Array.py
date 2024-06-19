def solve2(nums, n):
    curr = 0
    patches = 0
    for num in nums:
        while num > curr+1 and curr < n:
            patches += 1
            curr += curr+1
        if curr >= n: return patches
        curr += num
    while curr < n:
        patches += 1
        curr += curr+1
    return patches

nums = [1,2,2,6,34,38,41,44,47,47,56,59,62,73,77,83,87,89,94]
n = 20
print(solve2(nums, n))