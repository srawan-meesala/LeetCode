class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        t = s[::-1]
        n = len(s)
        dp = [[0 for _ in range(n+1)]for _ in range(n+1)]
        s = ' '+s
        t = ' '+t
        for i in range(1,n+1):
            for j in range(1,n+1):
                if s[i]==t[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]