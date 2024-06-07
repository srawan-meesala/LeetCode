matrix = [[-80,-13,22],[83,94,-5],[73,-48,61]]
n = len(matrix)

dp = [[float("inf") for _ in range(n)] for _ in range(n)]
dp[-1] = matrix[-1]
for i in range(n-2, -1, -1):
    for j in range(n):
        if j == 0 and j == n-1:
            dp[i][j] = dp[i+1][j] + matrix[i][j]
        else:
            if j == 0:
                dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + matrix[i][j]
            elif j == n-1:
                dp[i][j] = min(dp[i+1][j], dp[i+1][j-1]) + matrix[i][j]
            else:
                print(min(dp[i+1][j-1], dp[i+1][j], dp[i+1][j-1]))
                dp[i][j] = min(dp[i+1][j-1], dp[i+1][j], dp[i+1][j-1]) + matrix[i][j]
print(dp)