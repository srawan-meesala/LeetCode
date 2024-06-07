nums = [1,2,3,5,6,7,8]

def solve(nums):
    n = len(nums)
    if n < 3:
        return 0
    new = [nums[i] - nums[i-1] for i in range(1, n)]
    i, p, count = 1, 0, 0
    while i < n-1:
        if new[i] == new[i-1]:
            p += 1
        else:
            if p >= 1:
                count += ((p * (p + 1)) // 2)
            p = 0
        i += 1
    if p >= 1:
        count += ((p * (p + 1)) // 2)
    return count

print(solve(nums))