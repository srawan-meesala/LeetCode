nums = [0, 1, 0]
k = 1
c = 0
res = 0
while c <= len(nums)-k:
    if nums[c] == 0:
        for i in range(k):
            nums[c+i] = 1 if nums[c+i] == 0 else 0
        print(nums)
        res += 1
    c += 1
print(res) if nums.count(0)==0 else print(-1)