class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ans = 0
        
        dp = {}
        
        def dfs(i,cum):
            nonlocal ans
            if i == len(nums):
                if cum == target:
                    return 1
                return 0
            
            if (i,cum) in dp:
                return dp[(i,cum)]
            dp[(i,cum)] = 0
            
            dp[(i,cum)] += dfs(i+1,cum+nums[i])
            dp[(i,cum)] += dfs(i+1,cum-nums[i])
            
            return dp[(i,cum)]
        
        ans = dfs(0,0)
        
        return ans