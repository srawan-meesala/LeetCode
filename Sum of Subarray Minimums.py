arr = [11,81,94,43,3]
res = sum(arr)
n = len(arr)
MOD = (10**9) + 7
dp = [[float("inf") for _ in range(n)] for _ in range(2)]
dp[0] = arr
print(dp)
c1 = 0
c2 = 1
for i in range(n-1, 0, -1):
    c1, c2 = c2, c1
    for j in range(i):
        dp[c1][j] = min(dp[c2][j], dp[c2][j+1])
        res += dp[c1][j]
print('res', res)