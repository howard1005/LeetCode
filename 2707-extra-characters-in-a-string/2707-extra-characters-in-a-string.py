class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dp = [-1 for _ in range(len(s))]
        d = set(dictionary)
        
        def dfs(i):
            if i >= len(s):
                return 0
            
            if dp[i] != -1:
                return dp[i]
            dp[i] = inf
            
            for j in range(i+1,len(s)+1):
                ss = s[i:j]
                if ss in d:
                    dp[i] = min(dp[i],dfs(j))
                else:
                    dp[i] = min(dp[i],dfs(j)+j-i)
            
            return dp[i]
        
        return dfs(0)
        
        