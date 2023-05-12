class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [0 for _ in range(len(questions))]
        dp[-1] = questions[-1][0]
        
        for i in range(len(questions)-2,-1,-1):
            p,b = questions[i]
            dp[i] = dp[i+1]
            j = i+b+1
            if j < len(dp):
                dp[i] = max(dp[i], dp[j] + p)
            else:
                dp[i] = max(dp[i], p)
                
        return dp[0]