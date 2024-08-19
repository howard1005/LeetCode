class Solution:
    def minSteps(self, n: int) -> int:
        # 최소 횟수 = [현재화면 숫자][clipboard]
        dp = [[inf for _ in range(n+1)] for _ in range(n+1)]

        for j in range(n+1):
            dp[-1][j] = 0

        for i in range(n,-1,-1):
            for j in range(n,-1,-1):
                if i+i < n+1:
                    dp[i][j] = min(dp[i][j],dp[i+i][i]+2)
                if i+j < n+1:
                    dp[i][j] = min(dp[i][j],dp[i+j][j]+1)

        return dp[1][0]

        