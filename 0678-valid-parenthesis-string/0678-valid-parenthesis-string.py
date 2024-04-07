class Solution:
    def checkValidString(self, s: str) -> bool:
        
        dp = [[False for _ in range(len(s)+1)] for _ in range(len(s)+1)]
        
        dp[-1][0] = True
        
        for i in range(len(s)-1,-1,-1):
            for j in range(len(s)+1):
                c = s[i]
                if c == '(':
                    if j < len(s):
                        dp[i][j] |= dp[i+1][j+1]
                elif c == ')':
                    if j > 0:
                        dp[i][j] |= dp[i+1][j-1]
                elif c == '*':
                    dp[i][j] |= dp[i+1][j]
                    if j < len(s):
                        dp[i][j] |= dp[i+1][j+1]
                    if j > 0:
                        dp[i][j] |= dp[i+1][j-1]
        
        return dp[0][0]
            
            
                