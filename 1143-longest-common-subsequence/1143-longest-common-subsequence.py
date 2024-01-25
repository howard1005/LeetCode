class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text2))] for _ in range(len(text1))]
        flag = 0
        for i in range(len(text2)):
            if text2[i] == text1[0]:
                flag = 1
            dp[0][i] = flag
        flag = 0
        for i in range(len(text1)):
            if text1[i] == text2[0]:
                flag = 1
            dp[i][0] = flag
        
        for i in range(1,len(text1)):
            for j in range(1,len(text2)):
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
                if text1[i] == text2[j]:
                    dp[i][j] = max(dp[i][j],dp[i-1][j-1]+1)
                   
        return dp[-1][-1]