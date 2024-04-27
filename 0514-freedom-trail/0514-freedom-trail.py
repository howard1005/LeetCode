class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        
        dp = [[inf for _ in range(len(ring))] for _ in range(len(key)+1)]
        
        for j in range(len(ring)):
            dp[-1][j] = 0
        
        def modRing(j):
            return (j+len(ring))%len(ring)

        
        for i in range(len(key)-1,-1,-1):
            jj = 0
            while jj < len(ring)*2:
                j = modRing(jj)
                
                if ring[j] == key[i]:
                    dp[i][j] = min(dp[i][j],dp[i+1][j]+1)
                else:
                    dp[i][j] = min(dp[i][j],dp[i][modRing(j+1)]+1,dp[i][modRing(j-1)]+1)
                
                jj += 1
                
            jj = len(ring)*2-1
            while jj >= 0:
                j = modRing(jj)
                
                if ring[j] == key[i]:
                    dp[i][j] = min(dp[i][j],dp[i+1][j]+1)
                else:
                    dp[i][j] = min(dp[i][j],dp[i][modRing(j+1)]+1,dp[i][modRing(j-1)]+1)
                
                jj -= 1
            

        return dp[0][0]