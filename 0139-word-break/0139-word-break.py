class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        d = set(wordDict)
        
        dp = [None for _ in range(len(s))]
        
        def dfs(i):
            if i >= len(s):
                return True
            if dp[i] != None:
                return dp[i]
            dp[i] = False
            
            ns = ''
            for j in range(i,len(s)):
                ns += s[j]
                if ns in d:
                    if dfs(j+1):
                        dp[i] = True
                        return True
            return False
                    
        return dfs(0)