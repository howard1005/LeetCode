from math import gcd

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        ans = 0
        
        n = len(nums)//2
        
        dp = [-1] * (1<<len(nums))
        
        def dfs(i,st):
            if i == n:
                return 0
            
            if dp[st] != -1:
                return dp[st]
            dp[st] = 0
            
            for j in range(len(nums)):
                if (st>>j)&1:
                    continue
                for k in range(j+1,len(nums)):
                    if (st>>k)&1:
                        continue
                    g = gcd(nums[j],nums[k])
                    dfs(i+1,st|(1<<j)|(1<<k))
                    dp[st] = max(dp[st],g*(i+1) + dfs(i+1,st|(1<<j)|(1<<k)))
            
            return dp[st]
        
        ans = dfs(0,0)
        
        return ans