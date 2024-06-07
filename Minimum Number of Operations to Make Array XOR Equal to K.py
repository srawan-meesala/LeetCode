nums, k = [2,1,3,4], 1
xor = nums[0]
for i in range(1, len(nums)):
    xor = xor ^ nums[i]
res = bin(xor^k)[2:]
print(res.count('1'))