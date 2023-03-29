class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        dp = [[0 for _ in range(len(satisfaction)+1)] for _ in range(len(satisfaction))]
        for j in range(len(satisfaction)+1):
            dp[-1][j] = max(0,j*satisfaction[-1])
        for i in range(len(satisfaction)-2,-1,-1):
            for j in range(len(satisfaction)):
                dp[i][j] = max(dp[i+1][j],satisfaction[i]*j+dp[i+1][j+1])
        return dp[0][1]