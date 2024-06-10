def subarraysDivByK(nums, k: int) -> int:
    prefix, prefix_sum = {0: 1}, 0
    res = 0
    for i in range(len(nums)):
        prefix_sum += nums[i]
        prefix_sum %= k
        if prefix_sum in prefix:
            print(prefix_sum)
            res += prefix[prefix_sum]
            prefix[prefix_sum] += 1
        else:
            prefix[prefix_sum] = 1
    return res

nums = [4,5,0,-2,-3,1]
k = 5
print(subarraysDivByK(nums, k))

nums = [5]
k = 9
print(subarraysDivByK(nums, k))