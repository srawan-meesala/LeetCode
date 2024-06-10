def rob(nums) -> int:
    if len(nums) <= 3:
        return max(nums)
    dp1 = [0 for _ in range(len(nums))]
    dp2 = [0 for _ in range(len(nums))]
    dp1[-2], dp1[-3] = nums[-2], nums[-3]
    dp2[-1], dp2[-2] = nums[-1], nums[-2]
    dp1[-4] = nums[-4] + dp1[-2]
    dp2[-3] = nums[-3] + dp2[-1]
    for i in range(len(nums)-5, -1, -1):
        dp1[i] = nums[i] + max(dp1[i+2], dp1[i+3])
        print(dp1[i])
    for i in range(len(nums)-4, 0, -1):
        dp2[i] = nums[i] + max(dp2[i+2], dp2[i+3])
    print(dp1, dp2)
    return max(dp1[0], dp1[1], dp2[2], dp2[1])

nums = [1,2,3,4,5,1,2,3,4,5]
print(rob(nums))