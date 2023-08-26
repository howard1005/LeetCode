class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: (x[1],x[0]))
        
        ofs = 1001
        dp = [[-1 for _ in range(2002)] for _ in range(len(pairs))]
        
        def dfs(i,j):
            if i == len(pairs):
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]
            dp[i][j] = 0
            
            a,b = pairs[i][0]+ofs,pairs[i][1]+ofs
            if a > j:
                dp[i][j] = max(dp[i][j],dfs(i+1,b)+1)
            dp[i][j] = max(dp[i][j],dfs(i+1,j))
            
            return dp[i][j]
        
        return dfs(0,0)